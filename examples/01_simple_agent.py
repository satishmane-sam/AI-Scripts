import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def simple_chat(message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("🤖 Simple AI Agent")
    print("=" * 50)
    user_input = input("\nYou: ")
    response = simple_chat(user_input)
    print(f"\nAgent: {response}")

