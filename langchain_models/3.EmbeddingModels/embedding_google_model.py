from langchain_google_vertexai import VertexAIEmbeddings
from dotenv import load_dotenv
import vertexai
import os

load_dotenv()

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'E:/LangChain/embedding-model-test-69bd14ba3494.json'

# Initialize Vertex AI with project ID and credentials
vertexai.init(project="embedding-model-test")

embedding_model = VertexAIEmbeddings(model='text-embedding-004')

result = embedding_model.embed_query(text='Islamabad is the capital of Pakistan')
print(result)