import os
from typing import List, Dict
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from datetime import datetime
import json

class CompleteAIAgent:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key required")
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=self.api_key)
        self.tools = self._create_tools()
        self.memory: List[Dict] = []
        self.agent_executor = self._create_agent()
    
    def _create_tools(self) -> List[Tool]:
        def calculate(expr: str) -> str:
            try:
                return str(eval(expr))
            except:
                return "Error in calculation"
        def get_time() -> str:
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        def get_memory() -> str:
            if not self.memory:
                return "No previous conversations."
            return json.dumps(self.memory[-5:], indent=2)
        return [
            Tool(name="calculator", description="Calculate math expressions", func=calculate),
            Tool(name="get_time", description="Get current time", func=get_time),
            Tool(name="get_memory", description="Get conversation history", func=get_memory)
        ]
    
    def _create_agent(self) -> AgentExecutor:
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful AI assistant with access to tools.
            You can perform calculations, get time, and remember conversations.
            Always be helpful and explain your actions."""),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        agent = create_openai_tools_agent(self.llm, self.tools, prompt)
        return AgentExecutor(agent=agent, tools=self.tools, verbose=False)
    
    def chat(self, message: str) -> str:
        try:
            result = self.agent_executor.invoke({"input": message})
            response = result["output"]
            self.memory.append({
                "user": message,
                "agent": response,
                "timestamp": datetime.now().isoformat()
            })
            return response
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    print("🤖 Complete AI Agent")
    print("=" * 50)
    print("\nType 'quit' to exit\n")
    try:
        agent = CompleteAIAgent()
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye! 👋")
                break
            if not user_input:
                continue
            response = agent.chat(user_input)
            print(f"Agent: {response}\n")
    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()

