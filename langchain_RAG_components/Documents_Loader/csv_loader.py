from langchain_community.document_loaders import CSVLoader

loader=CSVLoader("./sample.csv")

docs=loader.load()

print([x.page_content for x in docs])
print([x.metadata for x in docs])