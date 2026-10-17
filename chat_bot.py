import tiktoken
import dotenv
import os
from openai import OpenAI
dotenv.load_dotenv()


class ChatBot:
    def __init__(self):
        self.llm = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
        )

        self.messages = [
            {"role": "system", "content": "You are a helpful assistant. you name is Azar bot interduce yourself as Azar bot and you are a helpful assistant. in fist message you should introduce yourself as Azar bot and you are a helpful assistant."}
        ]
        self.total_tokens = 0
        self.input_token = 0
        self.output_token = 0

    def bot(self, message):
        self.messages.append({"role": "user", "content": message})
        response = self.llm.chat.completions.create(
            model="openai/gpt-oss-20b", messages=self.messages, temperature=0.7, max_tokens=150

        )
        response_text = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": response_text})
        self.total_tokens += response.usage.total_tokens
        self.input_token += response.usage.prompt_tokens
        self.output_token += response.usage.completion_tokens
        return response_text

    def chat(self):
        encoding = tiktoken.get_encoding("cl100k_base")
        while True:
            user_input = input(
                "Ask something (type q to quit): ").strip().lower()
            if user_input.lower() == "q":
                print("Exiting the chat. Goodbye!")
                break

            token_count = len(encoding.encode(user_input))

            if token_count > 10:
                print(
                    f"Your input is too long ({token_count} tokens). Please limit your input to 10 tokens.")
                continue

            bot_answer = self.bot(user_input)
            print(f"Bot: {bot_answer}")

    def report(self):
        for message in self.messages:
            print(message)
        print(f"Total tokens used: {self.total_tokens}")
        print(
            f"Input tokens used: $ {self.input_token * 0.05 + self.output_token * 0.05 / 1_000_000}")


def main():
    chat_bot = ChatBot()
    chat_bot.chat()
    chat_bot.report()


if __name__ == "__main__":
    main()
