# 🧠 Transformer Evaluation Suite

A developer-friendly toolkit to **compare, benchmark, and visualize the performance** of different transformer models on tasks like summarization and question answering.

Built to support:
- Research validation
- Prompt sensitivity analysis
- LLM product evaluation
- Startups working with internal knowledge graphs or unstructured data

---

## 🚀 Features

- 🤗 Evaluate multiple HuggingFace transformer models (e.g., `gpt2`, `EleutherAI/gpt-neo-125M`)
- 📊 Benchmark performance across prompt variants
- 🧪 Calculate metrics: BLEU, ROUGE, Cosine Similarity
- 📁 Export results to CSV
- 📈 Visualize performance using interactive Plotly charts
- 🌐 Streamlit dashboard for live exploration

---

## 📦 Installation

Clone and set up the virtual environment:

```bash
git clone git@github.com:chewyuenrachael/transformer-eval-suite.git
cd transformer-eval-suite

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

---

## 🔧 Usage

### Run evaluation for multiple models

```bash
python cli.py --models gpt2 EleutherAI/gpt-neo-125M --task summarization
```

This will:
- Generate outputs using several prompt styles
- Measure latency and token count
- Compute BLEU, ROUGE, cosine similarity
- Save results in `results/` directory

---

## 📁 Output Structure

```
results/
├── summarization-comparison/
│   ├── gpt2.json
│   ├── EleutherAI_gpt-neo-125M.json
│   ├── all_results.json
│   ├── all_results.csv
│   └── BLEU_bar_chart.png
```

---

## 📊 Visualizations

### Run metric visualizer:

```bash
python plot_results.py --metric BLEU --save
```

Or to open interactive browser view:

```bash
python plot_results.py --metric ROUGE-L --show
```

### Example:

| Model | Prompt | BLEU | ROUGE-1 | ROUGE-L |
|-------|--------|------|----------|----------|
| gpt2 | 0 | 0.21 | 0.33 | 0.28 |
| EleutherAI/gpt-neo-125M | 0 | 0.19 | 0.31 | 0.26 |

---

## 🌐 Live Dashboard

Start the Streamlit UI:

```bash
streamlit run dashboard.py
```

> Visit `http://localhost:8501` in your browser to explore metrics interactively!

---

## 🔍 Evaluation Metrics

| Metric | Description |
|--------|-------------|
| **BLEU** | Measures n-gram overlap between generated output and input |
| **ROUGE** | Measures recall-based overlap (n-gram + longest common subsequence) |
| **Cosine Similarity** | Measures semantic similarity between embeddings |

---

## ✨ Use Cases

- Researchers evaluating model generalization
- Startups analyzing how models perform on internal documents
- Product teams building LLM-powered summarization / Q&A systems
- Prompt engineers comparing phrasing sensitivity

---

## 🧑‍💻 Technologies

- 🤗 HuggingFace Transformers
- `torch`, `datasets`, `nltk`, `scikit-learn`
- `plotly`, `pandas`, `click`
- `streamlit` for the live dashboard

---

## 📌 To-Do

- [ ] Add support for arbitrary input texts
- [ ] Add support for long-context models (e.g. Mistral, GPT-J)
- [ ] Integrate OpenAI API evaluation
- [ ] Model fine-tuning hooks
- [ ] Expand prompt library

---

## 🧠 Author

**Rachael Chew** – *Building at the intersection of AI systems and developer tooling.*

GitHub: [@chewyuenrachael](https://github.com/chewyuenrachael)

---

## 🌟 Contributing

Pull requests welcome! Open an issue first to discuss what you’d like to add or improve.

---

## 📄 License

MIT License

---

## 📸 Preview

![BLEU comparison](results/summarization-comparison/BLEU_bar_chart.png)
