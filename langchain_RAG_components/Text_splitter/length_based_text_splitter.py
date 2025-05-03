from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Update this path to the absolute path where your PDF is located
loader = PyPDFLoader("ML-43.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
    separator=""  
)


text = """
Artificial intelligence has revolutionized the way we interact with technology, enabling machines to perform tasks that once required human intelligence. From natural language processing to computer vision, AI systems are now capable of understanding and responding to complex inputs with remarkable accuracy. This transformation has not only enhanced productivity across industries but also opened up new possibilities for innovation and problem-solving. As AI continues to evolve, it is reshaping the boundaries of what machines can achieve, fostering a future where automation and intelligence work hand in hand.

However, the rapid advancement of AI also raises important ethical and societal questions. Issues such as data privacy, algorithmic bias, and the potential displacement of jobs demand careful consideration and proactive measures. It is crucial for researchers, policymakers, and industry leaders to collaborate in creating frameworks that ensure AI is developed and deployed responsibly. By addressing these challenges, we can harness the full potential of AI while minimizing its risks, paving the way for a more equitable and sustainable technological future.
"""

result = splitter.split_text(text)

result_1=splitter.split_documents(docs)

print(result_1)
