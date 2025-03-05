from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

os.environ['HF_HOME']="E:/huggingface_embeddign_model"

embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    'Artificial Intelligence is transforming the world.',
    'Machine learning is a subset of AI.',
    'Deep learning is a subset of machine learning.',
    'AI can be used in various fields such as healthcare, finance, and transportation.',
    'Natural language processing is a branch of AI that deals with the interaction between computers and humans.',
    'Reinforcement learning is an area of machine learning.',
    'AI models require a lot of data for training.',
    'Ethics in AI is an important consideration.',
    'AI can help in automating repetitive tasks.',
    'AI research is advancing rapidly.'
]

query='What AI is effect'

docs_embedding=embedding_model.embed_documents(documents)
query_embedding=embedding_model.embed_query(query)


scores=cosine_similarity(np.array([query_embedding]), np.array(docs_embedding))[0]
index, score=sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(f"Query: {query}")

print(f"Most similar document: {documents[index]}")

print(f"Similarity score: {score}, and index {index}")
