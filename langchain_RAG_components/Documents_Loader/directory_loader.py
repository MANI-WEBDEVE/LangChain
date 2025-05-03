from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader

loader=DirectoryLoader(
    path="./document_folder",
    glob="*.pdf",
    loader_cls=PyMuPDFLoader
)


############# docs=loader.load # this method consume you memory to use lazy load is peformance optimize 

docs=loader.lazy_load()

print(type(docs))

print([x for x in docs])