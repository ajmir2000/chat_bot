import dotenv
import os
from openai import OpenAI


dotenv.load_dotenv()

llm = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
)

messages = [
    {"role": "system", "content": "You are a helpful assistant. you name is Azar bot interduce yourself as Azar bot and you are a helpful assistant. in fist message you should introduce yourself as Azar bot and you are a helpful assistant."}
]


def bot(message):
    messages.append({"role": "user", "content": message})
    response = llm.chat.completions.create(
        model="openai/gpt-oss-20b", messages=messages, temperature=0.7, max_tokens=150

    )
    response_text = response.choices[0].message.content
    messages.append({"role": "assistant", "content": response_text})
    return response_text


def chat():
    while True:
        user_input = input("Ask something (type q to quit): ").strip().lower()
        if user_input.lower() == "q":
            print("Exiting the chat. Goodbye!")
            break

        bot_answer = bot(user_input)
        print(f"Bot: {bot_answer}")


def main():
    chat()
    print(messages)


if __name__ == "__main__":
    main()
