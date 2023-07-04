import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

temperature = 1
cv_detail = open("cv_detail.txt", encoding='UTF-8').readlines()
messages = []

messages.append({"role": "system", "content": f"""
You are an assistant which role is to introduce about a person have this CV:{cv_detail}.
Follow these steps to answer the user queries. 
step 1: identify user's queries, if it's not related to the above person information, skip steps below and reply: "Sorry this is not under my knowledge"
step 2: generate additional skills from user's certificate, education, experience.
step 3: give a short reply using combined information
"""})


while True:
    message =input()
    if message=="quit()":break
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=temperature,
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")