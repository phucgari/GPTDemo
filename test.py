import os
import openai
from dotenv import load_dotenv
from countToken import truncate_messages
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

temperature = 1
cv_detail = open("cv_detail.txt", encoding='UTF-8').readlines()
messages = []

messages.append({"role": "system", "content": f"""
You are an assistant named Poppy which role is to introduce about a person have this CV which is in the delimiter bellow:{cv_detail}.
"""})

while True:
    message = input()
    if message == "quit()":
        break
    messages.append({"role": "user", "content":
                    f"""Using the CV to reply to the requested message in delimiter. If there are not related information in the CV, reply: "Sorry this is not under my knowledge".
                    requested message: "{message}" """})
    truncate_messages(messages)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=temperature,
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
