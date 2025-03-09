from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# create a chat template

chat_template=ChatPromptTemplate(
    [
        ('system', "your are my shopco chat support manager"),
        MessagesPlaceholder(variable_name="messages_history"),
        ('user', "{input}"),
    ]
)
messages_history=[]
# load a chat messages history
with open("messages-history.txt", 'r') as f:
    messages_history.extend(f.readlines())

# create  prompts
print("chat_message_history ", messages_history)
prompts=chat_template.invoke({'messages_history':messages_history, 'input':'please tell me my order successfully cencel'})

print("prompts messages ", prompts)