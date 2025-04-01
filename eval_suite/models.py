from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model_and_tokenizer(name="gpt2", device="cuda" if torch.cuda.is_available() else "cpu"):
    tokenizer = AutoTokenizer.from_pretrained(name)
    model = AutoModelForCausalLM.from_pretrained(name).to(device)
    model.eval()
    return model, tokenizer