from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage


llm=ChatCohere()

message = [HumanMessage(content="Who won the 2024 IPL Trophy?")]

print(llm.invoke(message).content)