# eval_suite/runner.py

import torch
import time
from models import load_model_and_tokenizer
from eval_suite.prompts import get_prompt
from eval_suite.metrics import compute_cosine_similarity, compute_bleu, compute_rouge
from models.openai_wrapper import OpenAIModel
from datasets import load_dataset

def load_medical_dataset():
    dataset = load_dataset("FreedomIntelligence/medical-o1-reasoning-SFT", "en")
    return dataset["train"]

def run_eval(model_name, prompts, task_type, dataset):
    model, tokenizer = load_model_and_tokenizer(model_name)
    results = []

    for i in range(min(len(dataset), len(prompts))):
        input_text = dataset[i]['Question']
        prompt = get_prompt(task_type, i, input_text)

        # === Generation ===
        if isinstance(model, OpenAIModel):
            result = model.generate(prompt)
            output = result["output"]
            latency = result["latency"]
            tokens_used = result["tokens_used"]
        else:
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
            start = time.time()
            with torch.no_grad():
                output_tensor = model.generate(**inputs, max_new_tokens=50)
            end = time.time()
            output = tokenizer.decode(output_tensor[0], skip_special_tokens=True)
            latency = end - start
            tokens_used = output_tensor.shape[1]

        # === Evaluation ===
        expected_output = dataset[i]['Response']

        bleu = compute_bleu(expected_output, output)
        rouge = compute_rouge(expected_output, output)
        cosine = compute_cosine_similarity(expected_output, output)

        # === Result Object ===
        results.append({
            "prompt_variant": i,
            "input": prompt,
            "output": output,
            "latency": float(latency),
            "num_tokens": int(tokens_used),
            "cosine_similarity": float(cosine),
            "bleu": float(bleu),
            "rouge": rouge,
            "model_type": "openai" if isinstance(model, OpenAIModel) else "huggingface"
        })

    return results
