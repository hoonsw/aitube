import openai

# api設定
key = "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"
openai.api_key = key

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
res = openai.Completion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)

# 結果の表示
print(res)
