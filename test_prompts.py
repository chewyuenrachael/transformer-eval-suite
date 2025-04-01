from eval_suite.prompts import get_prompt

example = get_prompt("summarization", 1, "The mitochondria is the powerhouse of the cell.")
print(example)