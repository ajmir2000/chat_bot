import dotenv
import os
from openai import OpenAI


dotenv.load_dotenv()

llm = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
)


def bot(message):
    llm.chat.completions.create(
        model="meta-llama/llama-prompt-guard-2-22m",

    )
    answer = "hello"
    return answer


def main():
    user_input = input("AAsk something: ")
    bot_answer = bot(user_input)
    print(f"Bot: {bot_answer}")


if __name__ == "__main__":
    main()
