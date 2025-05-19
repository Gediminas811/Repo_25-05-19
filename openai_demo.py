import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("SECRET")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)   

while True:
    user_input = input("What is your question? ")
    
    response = client.chat.completions.create(messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. Always reply in Lithuanian language.",
        },
        {
            "role": "user",
            "content": user_input
        }
    ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )
       
    print(response.choices[0].message.content)
