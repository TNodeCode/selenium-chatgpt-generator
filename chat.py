import os
import openai
from extract import extract_code

openai.api_key = os.getenv("OPENAPI_SECRET")


class Models:
    GPT4 = "gpt-4"                   # 8k tokens
    GPT4_32k = "gpt-4-32k"           # 32k tokens
    GPT35 = "gpt-3.5-turbo"          # 4k tokens
    GPT35_16k = "gpt-3.5-turbo-16k"  # 16k tokens


def chat_with_chatgpt(prompt, model=Models.GPT35):
    messages = [{"role": "system", "content":
                 "You are a intelligent assistant."}]
    messages.append(
        {"role": "user", "content": prompt},
    )
    chat = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )

    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply, messages


def let_chatgpt_generate_code(prompt, model=Models.GPT35):
    reply, messages = chat_with_chatgpt(prompt, model=model)
    return extract_code(reply)
