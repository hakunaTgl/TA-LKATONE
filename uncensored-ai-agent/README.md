# Uncensored AI Agent

A framework for implementing AI agents using the Wizard Vicuna 13B Uncensored model.

## Project Structure

```
uncensored-ai-agent/
├── models/
│   └── wizard_vicuna_13b_uncensored.gguf
│
├── src/
│   ├── __init__.py
│   ├── agent.py
│   ├── tokenizer.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the model file `wizard_vicuna_13b_uncensored.gguf` and place it in the `models/` directory

## Dependencies

- **transformers**: Hugging Face transformers library for NLP models
- **torch**: PyTorch for deep learning
- **pydantic**: Data validation using Python type annotations
- **deepseek**: Deep learning utilities

## Usage

```python
from src.agent import Agent, AgentConfig

# Configure the agent
config = AgentConfig(
    model_path="models/wizard_vicuna_13b_uncensored.gguf",
    temperature=0.7,
    max_tokens=2048
)

# Initialize and use the agent
agent = Agent(config)
agent.load_model()
response = agent.chat("Hello, how can you help me?")
print(response)
```

## Modules

- **agent.py**: Main agent implementation with configuration and interaction methods
- **tokenizer.py**: Text tokenization and encoding/decoding utilities
- **utils.py**: Helper functions for configuration, validation, and text processing

## License

See LICENSE file for details.
