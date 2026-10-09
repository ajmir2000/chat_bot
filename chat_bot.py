import dotenv
import os
from openai import OpenAI


dotenv.load_dotenv()

llm = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
)


def bot(message):
    response = llm.chat.completions.create(
        model="openai/gpt-oss-20b", messages=[{"role": "user", "content": message}]

    )

    return response.choices[0].message.content


def main():
    user_input = input("Ask something: ")
    bot_answer = bot(user_input)
    print(f"Bot: {bot_answer}")


if __name__ == "__main__":
    main()
