import openai
import dotenv
import os

# APIキーの設定
dotenv.load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

# メッセージ作成
messages = [{
    "role": "system",
    "content": "こんにちは、私はAIチューバーです。あなたのお悩みを解決します。"
},
    {
    "role": "user",
    "content": "こんにちは、AIチューバーさん。私は、AIチューバーさんについて知りたいです。"
}
]

# APiの呼び出し
res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)

# 結果の表示
print(res)