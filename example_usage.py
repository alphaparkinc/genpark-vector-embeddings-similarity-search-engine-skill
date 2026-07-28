from client import VectorSearchEngineClient

def main():
    client = VectorSearchEngineClient()
    res = client.search_vectors(query_vec=[0.1, 0.2, 0.3])
    print(f"Result for top_k_indices: {res['top_k_indices']}")

if __name__ == "__main__":
    main()
