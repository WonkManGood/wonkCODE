# Use a pipeline as a high-level helper

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("PowerInfer/SmallThinker-3B-Preview")
model = AutoModelForCausalLM.from_pretrained("PowerInfer/SmallThinker-3B-Preview")

from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="PowerInfer/SmallThinker-3B-Preview")
pipe(messages)