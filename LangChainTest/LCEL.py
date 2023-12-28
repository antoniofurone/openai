from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


prompt = ChatPromptTemplate.from_template(
    "Tell me a short joke about {topic}"
)
output_parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo")
chain = (
    {"topic": RunnablePassthrough()} 
    | prompt
    | model
    | output_parser
)

chain.invoke("ice cream")

for chunk in chain.stream("ice cream"):
    print(chunk, end="", flush=True)

print("\n")


# chain batch call
chain.batch(["ice cream", "spaghetti", "dumplings"])
for chunk in chain.stream("spaghetti"):
    print(chunk, end="", flush=True)

#await ainvoke_chain("ice cream")
    
#llm invece di chatbot
from langchain.llms import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct")
llm_chain = (
    {"topic": RunnablePassthrough()} 
    | prompt
    | llm
    | output_parser
)

llm_chain.invoke("ice cream")
