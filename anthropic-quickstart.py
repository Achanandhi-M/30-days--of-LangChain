from langchain_anthropic import ChatAnthropic

llm=ChatAnthropic(model='claude-3-sonnet-20240229',temperature=0.2,max_tokens=1024)

llm.invoke("who won the 2024 IPL Trophy?")


