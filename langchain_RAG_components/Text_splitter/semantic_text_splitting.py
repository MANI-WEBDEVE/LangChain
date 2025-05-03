from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_vertexai.embeddings import VertexAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

splitter=SemanticChunker(
    GoogleGenerativeAIEmbeddings(model="models/embedding-001"), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Embed a single query
query_vector = embeddings.embed_query("Hello world!")
print(len(query_vector))  # Show first 5 dimensions


text = """
My name is Muhammad Inam and i and self learner . i start the Agentic AI enginnering. to change the entire world and build physical robots to every things is autonomus

18 Auguest 2024 i start m juorny to learn IT but i have no idea i can start i first learn web beacuse its fundamental for every things

"""


result=splitter.create_documents([text])

print(result)