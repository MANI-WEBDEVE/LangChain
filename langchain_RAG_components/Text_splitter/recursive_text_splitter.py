from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
My name is Muhammad Inam and i and self learner . i start the Agentic AI enginnering. to change the entire world and build physical robots to every things is autonomus

18 Auguest 2024 i start m juorny to learn IT but i have no idea i can start i first learn web beacuse its fundamental for every things

"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=0
)


result=splitter.split_text(text)

print(result)