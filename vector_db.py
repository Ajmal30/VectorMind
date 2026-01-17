from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

class QdrantStorage:
    def __init__(self, collection_name: str = "docs", url: str = "http://localhost:633", dim: int = 3072):
        self.client = QdrantClient(host=url, timeout=30)
        self.collection_name = collection_name
        self._ensure_collection(dim)

    def _ensure_collection(self, dim):
        if not self.client.get_collection(self.collection_name, ignore_missing=True):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
            )

    def upsert_vectors(self, ids, vectors: list[PointStruct], paylods):
        points = [PointStruct(id=ids[i], vector=vectors[i], payload=paylods[i]) for i in range(len(ids))]
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
    
    def search(self, query_vector, top_k: int = 5):
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=top_k,
            with_payload=True
        )
        contexts = []
        sources = set()
        for r in results:
            payload = getattr(r, 'payload', None) or {}
            text = payload.get('text', "")
            source = payload.get('source', "")
            if text:
                contexts.append(text)
                sources.add(source)
        return {"contexts": contexts, "sources": list(sources)}