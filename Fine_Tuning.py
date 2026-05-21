# peft : Parameter Efficient Fine Tuning
# trl : Transformer Reinforcement Learning

# Step 1: Install required libraries
!pip install transformers datasets peft trl accelerate -q

# Step 2: Import tokenizer and model loader
from transformers import AutoTokenizer, AutoModelForCausalLM

# Step 3: Import LoRA config
from peft import LoraConfig

# Step 4: Choose model
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Step 5: Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Step 6: Load model
model = AutoModelForCausalLM.from_pretrained(model_name)

# Step 7: Create prompt
prompt = "User: What is machine learning?\nAssistant:"

# Step 8: Convert prompt into tensors
inputs = tokenizer(
    prompt,
    return_tensors="pt"
)

# Step 9: Generate output
outputs = model.generate(
    **inputs,
    max_new_tokens=50
)

# Step 10: Decode generated tokens
response = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

# Step 11: Print response
print(response)

# Step 12: Create LoRA configuration
config = LoraConfig(
    r=8,
)
