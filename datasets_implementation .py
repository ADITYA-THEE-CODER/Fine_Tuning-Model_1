formatted_data = []
data = [
    {
        "instruction": "Create exam notes from the PDF",
        "input": "Chess is a two-player strategy board game played on an 8x8 grid with 64 squares.",
        "output": "Chess: A two-player strategy board game played on an 8x8 grid with 64 squares."
    },

    {
        "instruction": "Create exam notes from the PDF",
        "input": "Football is a family of team sports where two teams compete to advance a ball into the opposing team's goal or end zone.",
        "output": "Football: A team sport where two teams compete to advance a ball into the opposing team's goal."
    }
]

for item in data:
    text = f"""
### Instruction:
{item['instruction']}

### Input:
{item['input']}

### Response:
{item['output']}
"""
    
    formatted_data.append(text)

print(formatted_data[0])
