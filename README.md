# 🧠 TinyLlama Fine-Tuning Demo

A beginner-friendly project that demonstrates how to:

- Load a pretrained LLM
- Run local inference
- Use tokenizers and tensors
- Apply LoRA fine-tuning
- Train on a custom dataset
- Generate responses after training

Built using TinyLlama, Hugging Face Transformers, PEFT, and TRL.

---

# 🚀 What This Project Does

This project loads the open-source model:

TinyLlama/TinyLlama-1.1B-Chat-v1.0

Then:

1. Converts prompts into tokens
2. Runs local text generation
3. Adds LoRA adapters
4. Fine-tunes the model on a tiny custom dataset
5. Tests the model after training

The model learns simple response patterns such as:

User: Create exam notes on chess  
Assistant: Chess is a strategy board game...

---

# 🛠️ Technologies Used

- Python
- Transformers
- PEFT (LoRA)
- TRL
- Hugging Face Datasets
- PyTorch

---

# 📦 Installation

```bash
pip install transformers datasets peft trl accelerate
