# clever_prompt_detector

A tool to detect prompt injection attacks using AI.

## Installation

```bash
git clone https://github.com/yourusername/clever_prompt_detector
cd clever_prompt_detector
pip install -e .
```

## Usage
```python
from clever_prompt_detector import get_result

result = get_result.judge_result()
print(result)
```

You can also run **clever_prompt_detector/test.py** to see the demo

### Adjust the prompts

All the prompts are init in **clever_prompt_detector/prompts.py** , you can adjust them there