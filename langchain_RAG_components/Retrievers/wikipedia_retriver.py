from langchain_community.retrievers import WikipediaRetriever

retriever=WikipediaRetriever( top_k_results=2)

docs=retriever.invoke("who is Jinnah")

for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")  # truncate for display

