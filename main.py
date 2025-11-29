from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv(override=True)



llm = ChatOpenAI(model="gpt-5-mini", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    result = agent.invoke({"messages": HumanMessage(content="search for top 3 demanded AI jobs in software engineering in bay area on linkedin and list their detsils")})
    print(result)

if __name__ == "__main__":
    main()
