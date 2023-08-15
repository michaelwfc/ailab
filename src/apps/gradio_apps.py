"""build simple apps with gradio"""
import os
import io
from IPython.display import Image, display, HTML
from PIL import Image
import base64
from dotenv import load_dotenv, find_dotenv
import requests
import json
from transformers import pipeline

_ = load_dotenv(find_dotenv())  # read local .env file
hf_api_key = os.environ['HF_API_KEY']


get_completion = pipeline(
    "summarization", model="shleifer/distilbart-cnn-12-6")


def summarize(input):
    output = get_completion(input)
    return output[0]['summary_text']
