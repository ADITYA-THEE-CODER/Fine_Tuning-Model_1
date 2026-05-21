# Step 1: Install required libraries
!pip install transformers datasets -q

# Step 2: Import tokenizer loader
from transformers import AutoTokenizer

# Step 3: Choose the model
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Step 4: Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Step 5: Test tokenizer
print(tokenizer("Hello AI"))

# Step 6: Import model loader
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(model_name)
