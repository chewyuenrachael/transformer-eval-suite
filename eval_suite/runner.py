# eval_suite/runner.py

import torch
import time
from eval_suite.models import load_model_and_tokenizer
from eval_suite.prompts import get_prompt
from eval_suite.metrics import compute_cosine_similarity, compute_bleu, compute_rouge

def run_eval(model_name, prompts, task_type):
    model, tokenizer = load_model_and_tokenizer(model_name)
    results = []

    # You can customize this reference for your own evaluation task
    reference = "The theory of relativity is a theory by Einstein explaining how time and space are linked for objects moving at a consistent speed."

    for i, _ in enumerate(prompts):
        input_text = "Explain the theory of relativity."  # You can swap this out later
        prompt = get_prompt(task_type, i, input_text)
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        start = time.time()
        with torch.no_grad():
            output = model.generate(**inputs, max_new_tokens=50)
        end = time.time()

        generated = tokenizer.decode(output[0], skip_special_tokens=True)
        latency = end - start

        # 🧪 Evaluation metrics
        cos_sim = compute_cosine_similarity(generated, reference)
        bleu = compute_bleu(generated, reference)
        rouge = compute_rouge(generated, reference)

        results.append({
            "prompt_variant": i,
            "input": prompt,
            "output": generated,
            "latency": float(latency),
            "num_tokens": int(output.shape[1]),
            "cosine_similarity": float(cos_sim),
            "bleu": float(bleu),
            "rouge": {
                "rouge1": float(rouge["rouge1"].fmeasure),
                "rougeL": float(rouge["rougeL"].fmeasure)
            }
        })


    return results
