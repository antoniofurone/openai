# propmpt, model, output parser
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
prompt_value=prompt.invoke({"topic": "ice cream"})
print("Messages=",prompt_value.to_messages)

model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

print(chain.invoke({"topic": "ice cream"}))

from langchain.llms import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct")
message=llm.invoke(prompt_value)
print(output_parser.invoke(message))