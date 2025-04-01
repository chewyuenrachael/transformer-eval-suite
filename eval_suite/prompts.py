PROMPT_VARIANTS = {
    "summarization": [
        "Summarize the following text:\n{input}",
        "Can you provide a summary of:\n{input}",
        "TL;DR:\n{input}"
    ],
    "qa": [
        "Question: {input}\nAnswer:",
        "Based on the following, answer the question:\n{input}",
        "Q: {input}\nA:"
    ]
}

def get_prompt(task_type, version, input_text):
    """Returns the filled-in prompt for a given task and version index."""
    return PROMPT_VARIANTS[task_type][version].format(input=input_text)