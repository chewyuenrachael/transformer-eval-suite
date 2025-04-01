# eval_suite/metrics.py

from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer
import torch

# Load a sentence embedding model
embed_tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
embed_model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def get_embedding(text):
    inputs = embed_tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = embed_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def compute_cosine_similarity(gen_text, reference_text):
    gen_vec = get_embedding(gen_text)
    ref_vec = get_embedding(reference_text)
    return cosine_similarity(gen_vec, ref_vec)[0][0]

def compute_bleu(gen_text, reference_text):
    return sentence_bleu([reference_text.split()], gen_text.split())

def compute_rouge(gen_text, reference_text):
    scorer = rouge_scorer.RougeScorer(["rouge1", "rougeL"], use_stemmer=True)
    return scorer.score(reference_text, gen_text)
