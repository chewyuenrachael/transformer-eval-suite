# 🧠 Transformer Evaluation Suite

A developer-facing benchmarking and visualization toolkit to evaluate 🤗 Hugging Face transformer models using prompt variants and core NLP metrics.

[🚀 **Live Demo**](https://transformer-eval-suite.streamlit.app/)  
_Explore the app live in your browser — compare models, prompts, and metrics interactively._

Designed to support:
- ✅ Open-ended experimentation with transformer architectures
- ✅ Prompt engineering research and deployment validation
- ✅ LLM product teams and startups making model decisions
- ✅ Meaningful, reproducible, and explainable comparisons
---

## 🔍 What It Does

This suite lets you:

- Choose **any transformer model** on Hugging Face (e.g., `gpt2`, `EleutherAI/gpt-neo-125M`)
- Benchmark it across different **prompt formulations** for a given task (e.g., summarization)
- Generate outputs and evaluate them using:
  - **BLEU**: n-gram precision
  - **ROUGE-1 / ROUGE-L**: n-gram recall and longest common subsequence
  - **Cosine Similarity**: sentence embeddings using `sentence-transformers`
- Export all results to **CSV**
- Visualize results using **Plotly** or an **interactive Streamlit dashboard**

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 🔁 Model Comparison | Run multiple models in parallel and benchmark them side-by-side |
| ✍️ Prompt Variants | Inject prompt templates (e.g. `TL;DR:`, `Can you summarize...`) |
| 🧪 Evaluation Metrics | BLEU, ROUGE-1, ROUGE-L, Cosine Similarity |
| 📊 Visual Tools | CLI output, CSV exports, interactive Plotly + Streamlit visualizations |
| 🌐 Streamlit Dashboard | Explore results visually and compare models across prompts |

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

> Optional (but recommended for Plotly export):  
```bash
pip install -U kaleido
```

---

## 🔧 Running the Evaluation

Run evaluation across any number of models with this command:

```bash
python cli.py --models gpt2 EleutherAI/gpt-neo-125M --task summarization
```

This will:
- Inject 3 prompt variants for each model
- Generate and decode outputs
- Evaluate each output using BLEU, ROUGE, and cosine similarity
- Save results to `results/summarization-comparison/`

---

## 📁 Output Directory Structure

```
results/
├── summarization-comparison/
│   ├── gpt2.json
│   ├── EleutherAI_gpt-neo-125M.json
│   ├── all_results.json
│   ├── all_results.csv
│   ├── BLEU_bar_chart.png
```

---

## 📊 Visualizing the Results

### Option 1: Plotly chart via CLI

```bash
python plot_results.py --metric BLEU --save
```

Or open interactively in the browser:

```bash
python plot_results.py --metric ROUGE-L --show
```

### Option 2: Streamlit Dashboard

```bash
streamlit run dashboard.py
```

Visit `http://localhost:8501` to interactively explore model vs. prompt comparisons.

---

## ✨ Live Demo

👉 [Try the Streamlit App](https://your-streamlit-url.streamlit.app/)  
_Compare model performance across prompt styles and metrics in your browser._

---

## 📊 Example Summary Table

| Model | Prompt | BLEU | ROUGE-1 | ROUGE-L | Cosine |
|-------|--------|------|----------|----------|--------|
| gpt2 | TL;DR: | 0.21 | 0.33 | 0.28 | 0.88 |
| EleutherAI/gpt-neo-125M | TL;DR: | 0.18 | 0.31 | 0.26 | 0.85 |

---

## 🧠 Prompt Templates Used

The toolkit tests each model on a task using multiple styles of prompts:

- `Summarize the following text:`
- `Can you provide a summary of:`
- `TL;DR:`

This allows you to measure **prompt sensitivity** across models and see how small wording changes affect output quality.

---

## 🧑‍💻 Technologies Used

- 🤗 Hugging Face Transformers + Datasets
- `torch`, `scikit-learn`, `nltk`, `sentence-transformers`
- `plotly`, `matplotlib`, `pandas`, `seaborn`
- `streamlit` for the interactive UI
- `click` for CLI argument parsing

---

## ✅ Use Cases

- 🔬 Model comparison for academic research
- 🛠️ Prompt engineering + experimentation
- 💼 Startups evaluating summarization or Q&A systems
- 📊 Internal model observability and monitoring

---

## 📌 To-Do

- [ ] Add support for Q&A and classification tasks
- [ ] Expand metric support (e.g., METEOR, BERTScore)
- [ ] Add GPT-style evaluation (helpfulness/harmlessness)
- [ ] Model fine-tuning integration
- [ ] OpenAI / Claude API support

---

## 📄 License

MIT License

---

## 👩‍💻 Author

**Rachael Chew**  
Building at the intersection of AI systems, developer tools, and cognition.  
GitHub: [@chewyuenrachael](https://github.com/chewyuenrachael)

---

## 🙌 Contributing

Pull requests are welcome!  
Open an issue to suggest new features, evaluation methods, or tasks.
