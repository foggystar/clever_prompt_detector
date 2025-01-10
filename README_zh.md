# clever_prompt_detector

一个用于检测提示词注入的工具

## 安装

```bash
git clone https://github.com/foggystar/clever_prompt_detector
cd clever_prompt_detector
```

若你希望使用conda虚拟环境，执行：
```bash
conda env create -f environment.yml
conda activate clever_detector
```

如果不使用虚拟环境，执行：
```bash
pip install -e .
```

## 使用方法

你需要在环境变量中设置 **DEEPSEEK_API_KEY**
```bash
export DEEPSEEK_API_KEY="Your_API_Key"
```

调用工具接口：

```python
from clever_prompt_detector import get_result

result = get_result.query()
print(result)
```

执行demo：
```bash
python ./test.py
```

### 调整提示词

所有提示词都在 **clever_prompt_detector/prompts.py** 中, 可以在此文件中调整它们