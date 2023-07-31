```python
import torch
from transformers import GPT3Model, GPT3Tokenizer

class DonaldJrAdventureModel:
    def __init__(self):
        self.tokenizer = GPT3Tokenizer.from_pretrained('gpt3')
        self.model = GPT3Model.from_pretrained('gpt3')
        self.model.load_state_dict(torch.load('trained_models/gpt3_model.pt'))

    def generate_simulation(self, adventure_type):
        input_ids = self.tokenizer.encode(adventure_type, return_tensors='pt')
        output = self.model.generate(input_ids, max_length=500, temperature=0.7)
        simulation_result = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return simulation_result
```