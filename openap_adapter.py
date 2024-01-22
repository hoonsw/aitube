# プロンプトの送信・メッセージの受信を行うクラス


import openai
import dotenv
import os

# APIキーの設定
dotenv.load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


class OpenAIAdaptor:
    def __init__(self):
        # character_promptはキャラクターの設定
        with open("aituber/character_prompt.txt", "r", encoding="utf-8") as f:
            self.character_prompt = f.read()

        pass

    def create_message(self, role, message):
        return {
            "role": role,
            "content": message
        }

    def create_chat(self, question):
        system_message = self.create_message("system", self.character_prompt)
        user_message = self.create_message("user", question)
        messages = [system_message, user_message]
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,)

        return res["choices"][0]["message"]["content"]


if __name__ == "__main__":
    adapter = OpenAIAdaptor()
    response_text = adapter.create_chat("こんにちは なんか面白い話して")
    print(response_text)
