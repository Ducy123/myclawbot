from __future__ import annotations
import os, hashlib
from pathlib import Path
from openai import OpenAI
import chromadb
from common import load_settings, collect_files, chunk_text, collection_for_path


def main():
    settings = load_settings()
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise SystemExit('OPENAI_API_KEY_MISSING')
    client = OpenAI(api_key=api_key)
    chroma = chromadb.PersistentClient(path=settings['chroma_path'])

    files = collect_files()
    total_chunks = 0
    for file in files:
        text = file.read_text(errors='ignore')
        chunks = chunk_text(
            text,
            settings['chunk']['target_chars'],
            settings['chunk']['overlap_chars'],
            settings['chunk']['min_chars'],
        )
        if not chunks:
            continue
        cname = collection_for_path(file, settings)
        col = chroma.get_or_create_collection(cname)
        docs, ids, metas = [], [], []
        for i, chunk in enumerate(chunks):
            hid = hashlib.sha1(f'{file}:{i}:{chunk}'.encode()).hexdigest()
            ids.append(hid)
            docs.append(chunk)
            metas.append({'path': str(file), 'chunk_index': i})
        embeds = client.embeddings.create(model=settings['embedding_model'], input=docs)
        vectors = [d.embedding for d in embeds.data]
        existing = set(col.get(ids=ids).get('ids', []))
        add_docs=[]; add_ids=[]; add_meta=[]; add_vec=[]
        for _id, d, m, v in zip(ids, docs, metas, vectors):
            if _id in existing:
                continue
            add_ids.append(_id); add_docs.append(d); add_meta.append(m); add_vec.append(v)
        if add_ids:
            col.add(ids=add_ids, documents=add_docs, metadatas=add_meta, embeddings=add_vec)
            total_chunks += len(add_ids)
            print(f'Indexed {len(add_ids)} chunks -> {cname} from {file}')
    print(f'DONE total_new_chunks={total_chunks}')

if __name__ == '__main__':
    main()
