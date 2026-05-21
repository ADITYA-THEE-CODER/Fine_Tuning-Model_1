# Step 1: Install required libraries
!pip install transformers datasets -q

# Step 2: Import tokenizer and model loader
from transformers import AutoTokenizer, AutoModelForCausalLM

# Step 3: Choose model
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Step 4: Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Step 5: Load model
model = AutoModelForCausalLM.from_pretrained(model_name)

# Step 6: Create proper chat-style prompt
prompt = "User: What is machine learning?\nAssistant:"

# Step 7: Convert prompt into tensors
inputs = tokenizer(
    prompt,
    return_tensors="pt"
)

# Step 8: Generate output tokens
outputs = model.generate(
    **inputs,
    max_new_tokens=50
)

# Step 9: Decode tokens back into English
response = tokenizer.decode(outputs[0])

# Step 10: Print final response
print(response)
