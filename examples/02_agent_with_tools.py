import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def calculate(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

calculator_tool = Tool(
    name="calculator",
    description="Performs mathematical calculations. Input should be a valid Python expression.",
    func=calculate
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to a calculator tool."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_openai_tools_agent(llm, [calculator_tool], prompt)
agent_executor = AgentExecutor(agent=agent, tools=[calculator_tool], verbose=True)

def chat_with_tools(message: str) -> str:
    result = agent_executor.invoke({"input": message})
    return result["output"]

if __name__ == "__main__":
    print("🤖 AI Agent with Tools")
    print("=" * 50)
    test_queries = [
        "What is 25 * 4?",
        "Calculate 100 divided by 5",
        "What is 2 to the power of 8?"
    ]
    for query in test_queries:
        print(f"\nYou: {query}")
        response = chat_with_tools(query)
        print(f"Agent: {response}")

