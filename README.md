# clever_prompt_detector

A tool to detect prompt injection attacks using AI.

## Installation

```bash
git clone https://github.com/foggystar/clever_prompt_detector
cd clever_prompt_detector
```

if you are using a virtual environment by conda, you can use the commands
```bash
conda create -n clever_detector python=3.9
conda activate clever_detector
conda install openai
```

else, you can use
```bash
pip install -e .
```

## Usage

You need to first set your **DEEPSEEK_API_KEY** in your environment
```bash
export DEEPSEEK_API_KEY={Your_API_Key}
```

Then you can try this project by:

```python
from clever_prompt_detector import get_result

result = get_result.judge_result()
print(result)
```

You can also run **clever_prompt_detector/test.py** to see the demo

### Adjust the prompts

All the prompts are init in **clever_prompt_detector/prompts.py** , you can adjust them there