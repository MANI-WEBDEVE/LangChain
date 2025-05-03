from langchain_text_splitters import RecursiveCharacterTextSplitter , Language

text = """
class Markdown:
    count = 0

    def __init__(self, name):
        self.name=name
        Markdown.count += 1
    
    def showCount(self):
        print(self.count)

        
obj1=Markdown("iname)
obj1=Markdown("tahir)
"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, # and change the onlu language name 
    chunk_size=100,
    chunk_overlap=0
)


result=splitter.split_text(text)

print(result)