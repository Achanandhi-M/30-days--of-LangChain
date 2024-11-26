from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=ChatCohere()

prompt=ChatPromptTemplate.from_messages([
    ("system", "You are a world class badminton player"),
    ("user","{input}")
])

output_parser=StrOutputParser()

chain=prompt | llm | output_parser

user_Input=input("What can I help with?:")

result=chain.invoke({user_Input})

print(result)