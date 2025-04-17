# models/openai_wrapper.py

import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenAIModel:
    def __init__(self, model_name="gpt-4o", temperature=0.7, max_tokens=512):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self, prompt: str) -> dict:
        start_time = time.time()
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        end_time = time.time()

        return {
            "output": response.choices[0].message.content.strip(),
            "tokens_used": response.usage.total_tokens,
            "latency": end_time - start_time
        }
