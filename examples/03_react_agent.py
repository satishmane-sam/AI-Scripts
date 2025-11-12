import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from datetime import datetime

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def get_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

def search_knowledge(query: str) -> str:
    knowledge = {
        "python": "Python is a high-level programming language known for its simplicity.",
        "ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
        "agent": "An AI agent is an autonomous entity that perceives and acts."
    }
    query_lower = query.lower()
    for key, value in knowledge.items():
        if key in query_lower:
            return value
    return "Information not found."

tools = [
    Tool(name="get_time", description="Gets current date and time", func=get_time),
    Tool(name="calculator", description="Performs calculations", func=calculate),
    Tool(name="search", description="Searches knowledge base", func=search_knowledge)
]

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI assistant that uses tools to answer questions.
    Follow the ReAct pattern:
    1. Think about what you need to do
    2. Use appropriate tools
    3. Observe the results
    4. Provide the final answer
    
    Always explain your reasoning."""),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def react_agent(query: str) -> str:
    result = agent_executor.invoke({"input": query})
    return result["output"]

if __name__ == "__main__":
    print("🤖 ReAct Pattern Agent")
    print("=" * 50)
    queries = [
        "What time is it?",
        "What is 15 * 23?",
        "Tell me about Python"
    ]
    for query in queries:
        print(f"\nYou: {query}")
        response = react_agent(query)
        print(f"Agent: {response}")

