import os

def getDeepSeekKey():
    return os.getenv('DEEPSEEK_API_KEY')

def getDeepSeekUrl():
    return "https://api.deepseek.com"