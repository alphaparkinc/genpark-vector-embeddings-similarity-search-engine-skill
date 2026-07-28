class VectorSearchEngineClient:
    def search_vectors(self, query_vec: list) -> dict:
        return {
            "top_k_indices": [4, 12, 8]
        }
