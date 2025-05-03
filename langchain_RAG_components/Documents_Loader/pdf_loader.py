from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("./ML.pdf")

docs=loader.load()

print(len(docs))

print(docs[0])

print("page content = ",docs[20].page_content)

print("metadata =",docs[0].metadata)