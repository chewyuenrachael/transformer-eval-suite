# models/__init__.py

from .openai_wrapper import OpenAIModel
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model_and_tokenizer(model_name):
    if model_name.startswith("openai/"):
        return OpenAIModel(model_name=model_name.split("openai/")[1]), None
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        return model, tokenizer
