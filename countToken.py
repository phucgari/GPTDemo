import os
import tiktoken
from dotenv import load_dotenv
load_dotenv()

model_name=os.getenv("MODEL_NAME")

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def num_tokens_from_messages(messages)->int:
    sum=0
    for message in messages:
        sum+=num_tokens_from_string(message["content"],model_name)
    print(sum)
    return sum

def truncate_messages(messages):
    while(num_tokens_from_messages(messages)>=4000):
        messages.pop(1)
