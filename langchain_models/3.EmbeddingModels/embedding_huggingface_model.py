from langchain_huggingface import HuggingFaceEmbeddings
import os


os.environ['HF_HOME']="E:/huggingface_embeddign_model"

embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text="Hi, I am a student and I am learning AI"
docs=[
    'hello Guys I am AI engineer',
    'I`m currently learning AI stuff',
    'I`m from PAKISTAN'
]
embedding_single_vector=embedding_model.embed_query(text) # for single text
embedding_multi_vector=embedding_model.embed_documents(docs) # for multiple text

print(embedding_multi_vector)
