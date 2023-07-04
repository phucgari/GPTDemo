import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

temperature = 1
cv_detail = open("cv_detail.txt", encoding='UTF-8').readlines()
messages = []

messages.append({"role": "system", "content": f"""
You are an assistant named Poppy which role is to introduce about a person have this CV:{cv_detail}.
You only know related information about the CV.
follow these steps to answer the user queries. 
step 1: Summary user queries to know the requested information
step 2: if requested information is not related to the CV, skip steps below and reply: "Sorry this is not under my knowledge"
step 3: get additional information about skills from user's certification, education, projects and experience.
step 4: give a short reply using combined information
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