"""
# Reference：
# https://towardsdatascience.com/beginners-guide-to-the-gpt-3-model-2daad7fc335a
# https://www.twilio.com/blog/ultimate-guide-openai-gpt-3-language-model"""
import os
from typing import Text, List, Union, Dict
import openai
import langchain
from constants import GPT_3DOT5_TURBO
from utils.enviroments import set_gpt_env


def get_response_from_completion(prompt: Text, temperateture=0.7, model=GPT_3DOT5_TURBO, engine=None) -> Text:
    completion = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=1024,
        stop=None,
        temperateture=temperateture
    )
    response = completion.choices[0].text
    return response


def get_chat_completion(prompt: Union[Text, List[Dict]], model=GPT_3DOT5_TURBO):
    if isinstance(prompt, str):
        messages = [{"role": "user", "content": prompt}]
    else:
        messages = prompt
    response = openai.ChatCompletion.create(
        url='https://api.openai.com/v1/chat/completions',
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


if __name__ == "__main__":
    set_gpt_env(use_openai=True)
    response = get_chat_completion("what about hangzhou?")
    print(f"response={response}")
