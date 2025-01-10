# clever_prompt_detector

A tool to detect prompt injection attacks using AI.

## Installation

```bash
git clone https://github.com/foggystar/clever_prompt_detector
cd clever_prompt_detector
```

if you are using a virtual environment by conda, you can use the commands
```bash
conda env create -f environment.yml
conda activate clever_detector
```

else, if you don't use a virtual environment, 
```bash
pip install -e .
```

## Usage

You need to first set your **DEEPSEEK_API_KEY** in your environment
```bash
export DEEPSEEK_API_KEY="Your_API_Key"
```

Then you can try this project by:

```python
from clever_prompt_detector import get_result

result = get_result.query()
print(result)
```

See the demo:
```bash
python ./test.py
```

### Adjust the prompts

All the prompts are init in **clever_prompt_detector/prompts.py** , you can adjust them there