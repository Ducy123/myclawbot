from __future__ import annotations
import os, sys
from openai import OpenAI
import chromadb
from common import load_settings


def main():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: query.py <query>')
    q = ' '.join(sys.argv[1:])
    settings = load_settings()
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise SystemExit('OPENAI_API_KEY_MISSING')
    client = OpenAI(api_key=api_key)
    chroma = chromadb.PersistentClient(path=settings['chroma_path'])
    emb = client.embeddings.create(model=settings['embedding_model'], input=[q]).data[0].embedding
    for name in settings['collections'].values():
        col = chroma.get_or_create_collection(name)
        res = col.query(query_embeddings=[emb], n_results=3)
        print(f'=== {name} ===')
        for doc, meta, dist in zip(res.get('documents', [[]])[0], res.get('metadatas', [[]])[0], res.get('distances', [[]])[0]):
            print(meta.get('path'), 'dist=', dist)
            print(doc[:500].replace('\n', ' '))
            print('---')

if __name__ == '__main__':
    main()
