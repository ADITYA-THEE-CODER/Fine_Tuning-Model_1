# Step 1: Install required libraries
!pip install transformers datasets peft trl accelerate -q


# Step 2: Import tokenizer and model loader
from transformers import AutoTokenizer, AutoModelForCausalLM

# Step 3: Import LoRA tools
from peft import LoraConfig, get_peft_model

# Step 4: Import Dataset object
from datasets import Dataset


# Step 5: Choose the model
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


# Step 6: Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)


# Step 7: Load model
model = AutoModelForCausalLM.from_pretrained(model_name)


# Step 8: Create chat-style prompt
prompt = "User: What is machine learning?\nAssistant:"


# Step 9: Convert prompt into tensors
inputs = tokenizer(
    prompt,
    return_tensors="pt"
)


# Step 10: Generate output tokens
outputs = model.generate(
    **inputs,
    max_new_tokens=50
)


# Step 11: Decode tokens back into English
response = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)


# Step 12: Print model response
print(response)


# Step 13: Create LoRA configuration
config = LoraConfig(
    r=8,
)


# Step 14: Attach LoRA adapters to model
model = get_peft_model(model, config)


# Step 15: Create tiny training dataset
data = [
    {
        "text": "User: Create exam notes on chess\nAssistant: Chess is a strategy board game played on an 8x8 board."
    },

    {
        "text": "User: Create exam notes on football\nAssistant: Football is a team sport where players try to score goals."
    }
]


# Step 16: Convert list into Dataset object
dataset = Dataset.from_list(data)

from trl import SFTTrainer

from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=1,
    num_train_epochs=1,
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    args=training_args,
)
