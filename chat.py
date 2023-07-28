import os
import openai
from extract import extract_code

openai.api_key = os.getenv("OPENAPI_SECRET")


def chat_with_chatgpt(prompt):
    messages = [{"role": "system", "content":
                 "You are a intelligent assistant."}]
    messages.append(
        {"role": "user", "content": prompt},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply, messages


def let_chatgpt_generate_code(prompt):
    reply, messages = chat_with_chatgpt(prompt)
    return extract_code(reply)
