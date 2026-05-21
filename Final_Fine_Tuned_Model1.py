# =========================================
# STEP 1: Install Required Libraries
# =========================================

!pip install transformers datasets peft trl accelerate -q


# =========================================
# STEP 2: Import Libraries
# =========================================

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments
)

from peft import (
    LoraConfig,
    get_peft_model
)

from datasets import Dataset

from trl import SFTTrainer


# =========================================
# STEP 3: Choose Model
# =========================================

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


# =========================================
# STEP 4: Load Tokenizer
# =========================================

tokenizer = AutoTokenizer.from_pretrained(model_name)


# =========================================
# STEP 5: Load Model
# =========================================

model = AutoModelForCausalLM.from_pretrained(model_name)


# =========================================
# STEP 6: Test Model BEFORE Fine-Tuning
# =========================================

prompt = "User: What is machine learning?\nAssistant:"

inputs = tokenizer(
    prompt,
    return_tensors="pt"
)

outputs = model.generate(
    **inputs,
    max_new_tokens=50
)

response = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print("===== BEFORE FINE-TUNING =====")
print(response)


# =========================================
# STEP 7: Create LoRA Configuration
# =========================================

config = LoraConfig(
    r=8,
)


# =========================================
# STEP 8: Attach LoRA Adapters
# =========================================

model = get_peft_model(model, config)


# =========================================
# STEP 9: Create Tiny Training Dataset
# =========================================

data = [
    {
        "text": "User: Create exam notes on chess\nAssistant: Chess is a strategy board game played on an 8x8 board."
    },

    {
        "text": "User: Create exam notes on football\nAssistant: Football is a team sport where players try to score goals."
    }
]


# =========================================
# STEP 10: Convert Into Dataset Object
# =========================================

dataset = Dataset.from_list(data)


# =========================================
# STEP 11: Training Settings
# =========================================

training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=1,
    num_train_epochs=1,
)


# =========================================
# STEP 12: Create Trainer
# =========================================

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    args=training_args,
)


# =========================================
# STEP 13: Start Fine-Tuning
# =========================================

trainer.train()


# =========================================
# STEP 14: Test Model AFTER Fine-Tuning
# =========================================

prompt = "User: Create exam notes on chess\nAssistant:"

inputs = tokenizer(
    prompt,
    return_tensors="pt"
)

outputs = model.generate(
    **inputs,
    max_new_tokens=50
)

response = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print("\n===== AFTER FINE-TUNING =====")
print(response)
