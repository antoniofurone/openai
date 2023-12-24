from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a chatbot for support operation on Sparkle's Bigdata platform"},
    {"role": "user", "content": "Coud you describe Sparkle Bigdata platform ?"}
  ]
)

print(completion.choices[0].message)
print("-----")
completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0613",
  messages=[
    {"role": "system", "content": "You are a chatbot for support operation on Sparkle's Bigdata platform"},
    {"role": "user", "content": "Coud you describe Sparkle Bigdata platform ?"}
  ]
)

