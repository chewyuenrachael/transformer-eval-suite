from eval_suite.runner import run_eval
from eval_suite.prompts import PROMPT_VARIANTS

results = run_eval("gpt2", PROMPT_VARIANTS["summarization"], "summarization")
for r in results:
    print(f"\nPrompt Variant {r['prompt_variant']} ({r['latency']:.2f}s):\n{r['output']}\n")
