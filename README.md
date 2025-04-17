# 🧠 Transformer Evaluation Suite

A developer-facing benchmarking and visualization toolkit to evaluate 🤗 Hugging Face and OpenAI transformer models using prompt variants and core NLP metrics.

[🚀 **Live Demo**](https://transformer-eval-suite.streamlit.app/)  
_Explore the app live in your browser — compare models, prompts, and metrics interactively._

---

## 🧭 What’s New

✅ **OpenAI API Integration**  
Use models like `gpt-4o`, `gpt-4`, and `gpt-3.5-turbo` with your API key via `.env`.

✅ **Hugging Face Dataset Integration**  
Now supports datasets from 🤗 `datasets` like `FreedomIntelligence/medical-o1-reasoning-SFT` to evaluate on real-world, medically grounded questions.

✅ **Evaluation Filtering**  
Run evaluation only on shorter examples using `--filter-short` or modify filtering logic in `cli.py`.

---

## 🔍 What It Does

This suite lets you:

- Choose **any transformer model** from Hugging Face **or OpenAI**
- Benchmark them across different **prompt formulations** for a given task (e.g., summarization)
- Load **domain-specific datasets** for evaluation (e.g., medical reasoning)
- Evaluate generated outputs using:
  - **BLEU**: n-gram precision
  - **ROUGE-1 / ROUGE-L**: recall and LCS overlap
  - **Cosine Similarity**: using `sentence-transformers`
- Export to **CSV** for reporting
- Visualize results using **Plotly** or a **Streamlit dashboard**

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/transformer-eval-suite.git
cd transformer-eval-suite

# Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

> For Hugging Face dataset access:  
```bash
huggingface-cli login
```

> For OpenAI model access:  
```bash
echo "OPENAI_API_KEY=your-key-here" > .env
```

---

## 🔧 Running Evaluations

### ✅ Hugging Face models
```bash
python cli.py --models gpt2 EleutherAI/gpt-neo-125M --task summarization
```

### ✅ OpenAI models
```bash
python cli.py --models openai/gpt-4o --task summarization
```

> This will:
- Pull real medical reasoning prompts from Hugging Face
- Run 3 prompt variants per example
- Evaluate outputs with BLEU, ROUGE, and Cosine Similarity
- Save results to `results/summarization-comparison/`

---

## 🧪 Evaluation Metrics

| Metric | Description |
|--------|-------------|
| BLEU | Precision of n-grams |
| ROUGE-1 | Overlap of unigrams |
| ROUGE-L | Longest common subsequence |
| Cosine | Semantic similarity via `sentence-transformers` |

---

## 📁 Output Structure

```
results/
├── summarization-comparison/
│   ├── openai_gpt-4o.json
│   ├── all_results.json
│   ├── results.csv
```

---

## 🩺 Built-in Dataset (Optional)

This project currently loads:

📚 `FreedomIntelligence/medical-o1-reasoning-SFT`  
A high-quality dataset for advanced medical reasoning (~25k examples).  
To modify, edit this section in `cli.py` or `runner.py`:

```python
dataset = load_dataset("FreedomIntelligence/medical-o1-reasoning-SFT", "en")["train"]
dataset = dataset.filter(lambda x: len(x["Question"]) < 500 and len(x["Response"]) < 800)
```

---

## 📊 Visualization Options

### 📈 CLI Charts
```bash
python plot_results.py --metric BLEU --show
```

### 🌐 Streamlit Dashboard
```bash
streamlit run dashboard.py
```

Then open `http://localhost:8501`

---

## ✨ Sample Evaluation Table

| Model         | Prompt | Cosine Sim | BLEU  | ROUGE-1 | ROUGE-L |
|---------------|--------|------------|-------|----------|----------|
| openai/gpt-4o | 0      | 0.815      | 0.148 | 0.493    | 0.313    |
| openai/gpt-4o | 1      | 0.884      | 0.200 | 0.630    | 0.396    |
| openai/gpt-4o | 2      | 0.904      | 0.117 | 0.535    | 0.323    |

---

## 🧠 Prompt Templates

The suite tests each model on prompt styles like:

- `Summarize the following text:`
- `Can you provide a summary of:`
- `TL;DR:`

This reveals **prompt sensitivity** and helps optimize instruction design.

---

## ✅ Use Cases

- 🔬 Research into LLM capabilities and prompt sensitivity
- 🛠️ Developer tools for prompt + model comparison
- 🧪 QA + summarization pipelines
- 🧭 OpenAI API-based evaluation harness

---

## 📌 To-Do

- [ ] Expand metrics (BERTScore, METEOR)
- [ ] Add classification / QA tasks
- [ ] Integrate with Claude / Anthropic API
- [ ] Save prompt-output pairs for ablation
- [ ] Add more domain-specific datasets

---

## 📄 License

MIT License

---

## 👩‍💻 Author

**Rachael Chew**  
AI systems | Developer tooling | Medical cognition  
GitHub: [@chewyuenrachael](https://github.com/chewyuenrachael)

---

## 🙌 Contributing

Pull requests welcome!  
Want to add datasets, metrics, or visualization tools? Let’s build together.