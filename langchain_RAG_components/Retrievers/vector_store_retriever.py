from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain.schema import Document

load_dotenv()

docs = [
    Document(page_content="Albert Einstein was a theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics. His work is also known for its influence on the philosophy of science.", metadata={"source": "biography"}),
    Document(page_content="Einstein was born in Ulm, in the Kingdom of Württemberg in the German Empire, on March 14, 1879. He had one sister, Maja, who was two years younger than him.", metadata={"source": "early_life"}),
    Document(page_content="Einstein married Mileva Marić in 1903, and they had two sons, Hans Albert and Eduard. The couple later divorced in 1919.", metadata={"source": "family"}),
    Document(page_content="In 1919, Einstein married Elsa Löwenthal, who was his first cousin maternally and second cousin paternally. Elsa had two daughters from her previous marriage.", metadata={"source": "marriage"}),
    Document(page_content="Einstein's contributions to science include the famous equation E=mc^2, which describes the relationship between mass and energy, and his work on the photoelectric effect, for which he won the Nobel Prize in Physics in 1921.", metadata={"source": "scientific_contributions"}),
]

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

vectorstore = FAISS.from_documents(docs, embeddings)

retriever=vectorstore.as_retriever(search_kwargs={"k": 2}, search_type="mmr", lambda_mult=0.5)

results = retriever.get_relevant_documents("What are Einstein's contributions to science?")
for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")  # truncate for display
    print(f"Metadata:\n{doc.metadata}...")  # truncate for display