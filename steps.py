# Step 1: Install required libraries
!pip install transformers datasets -q

# Step 2: Import tokenizer loader
from transformers import AutoTokenizer

# Step 3: Choose model
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Step 4: Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Step 5: Test tokenizer
print(tokenizer("Hello AI"))

# Step 6: Import model loader
from transformers import AutoModelForCausalLM

# Step 7: Load the actual AI model
model = AutoModelForCausalLM.from_pretrained(model_name)

# Step 8: Convert text into tensors
inputs = tokenizer(
    "What is machine learning?",
    return_tensors="pt"
)

# Step 9: Generate output tokens
outputs = model.generate(
    **inputs,
    max_new_tokens=30
)
