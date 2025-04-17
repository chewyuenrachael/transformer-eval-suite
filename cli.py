# cli.py
import csv
from tabulate import tabulate
import click
from eval_suite.runner import run_eval
from eval_suite.prompts import PROMPT_VARIANTS
import json
from pathlib import Path
from datasets import load_dataset

@click.command()
@click.option('--models', multiple=True, required=True, help='List of HuggingFace model names')
@click.option('--task', default="summarization", help='Task type (summarization/qa)')
def main(models, task):
    prompts = PROMPT_VARIANTS[task]
    dataset = load_dataset("FreedomIntelligence/medical-o1-reasoning-SFT", "en")["train"].select(range(100))

    # Filter for cleaner, shorter samples
    dataset = dataset.filter(lambda x: len(x["Question"]) < 500 and len(x["Response"]) < 800)

    all_results = []

    output_dir = Path(f"results/{task}-comparison")
    output_dir.mkdir(parents=True, exist_ok=True)

    for model in models:
        print(f"\n🧠 Evaluating model: {model}")
        results = run_eval(model, prompts, task, dataset)

        all_results.append({
            "model": model,
            "results": results
        })

        # Save individual model results
        with open(output_dir / f"{model.replace('/', '_')}.json", "w") as f:
            json.dump(results, f, indent=2)

    # Save combined results
    with open(output_dir / "all_results.json", "w") as f:
        json.dump(all_results, f, indent=2)

    # Save CSV summary
    csv_path = output_dir / "results.csv"
    with open(csv_path, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # ✅ Updated header row
        writer.writerow([
            "Model", "Prompt", "Latency", "Num Tokens",
            "Cosine Sim", "BLEU", "ROUGE-1", "ROUGE-L", "Output"
        ])

        for model_block in all_results:
            model = model_block["model"]
            for entry in model_block["results"]:
                writer.writerow([
                    model,
                    entry["prompt_variant"],
                    round(entry["latency"], 4),
                    entry["num_tokens"],
                    round(entry["cosine_similarity"], 4),
                    round(entry["bleu"], 4),
                    round(entry["rouge"]["rouge1"].fmeasure, 4),
                    round(entry["rouge"]["rougeL"].fmeasure, 4),
                    entry["output"].strip().replace("\n", " ")[:200]  # Add this!
                ])


    print(f"📦 CSV summary saved to: {csv_path}")

    print(f"\n✅ All evaluations complete. Results saved to: {output_dir}")

    print(f"\n🧪 Evaluation Summary (Task: {task})")
    table_data = []
    for model_block in all_results:
        model = model_block["model"]
        for entry in model_block["results"]:
            table_data.append([
                model,
                entry["prompt_variant"],
                round(entry["cosine_similarity"], 3),
                round(entry["bleu"], 3),
                round(entry["rouge"]["rouge1"].fmeasure, 3),
                round(entry["rouge"]["rougeL"].fmeasure, 3)
            ])

    headers = ["Model", "Prompt", "Cosine Sim", "BLEU", "ROUGE-1", "ROUGE-L"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))



if __name__ == '__main__':
    main()
