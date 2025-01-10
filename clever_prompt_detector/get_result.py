from openai import OpenAI
from clever_prompt_detector import util
from clever_prompt_detector import prompts
from openai import BadRequestError, RateLimitError, APIError, APIConnectionError

def honeypot_result(prompt_user=""):
    honeypot = OpenAI(api_key=util.getDeepSeekKey(), base_url=util.getDeepSeekUrl())
    try:
        response = honeypot.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": prompts.honeypot_sys},
            {"role": "user", "content": prompt_user},
        ],
        max_tokens=500,
        stream=False
        )
        return response.choices[0].message.content
    # except BadRequestError as e:
    #     print(f"请求参数错误: {e}")
    # except RateLimitError as e:
    #     print(f"API调用频率超限: {e}")
    # except APIError as e:
    #     print(f"OpenAI API错误: {e}") 
    # except APIConnectionError as e:
    #     print(f"API连接错误: {str(e)}")
    except Exception as e:
        # print(f"未知错误: {str(e)}")
        return "The honeypot is attacked"

def query(prompt_user=""):
    judge = OpenAI(api_key=util.getDeepSeekKey(), base_url=util.getDeepSeekUrl())

    result = honeypot_result(prompt_user)
    prompts.judge_user = prompts.get_judge_user(honeypot_response=result, honeypot_user=prompt_user)
    try:
        response = judge.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": prompts.judge_sys},
                {"role": "user", "content": prompts.judge_user},
            ],
            stream=False
        )
        if(response.choices[0].message.content == "not attack"):
            return [result, False, "not attack"]
        else:
            return [result, True, "attack"]
    # except BadRequestError as e:
    #     print(f"请求参数错误: {e}")
    # except RateLimitError as e:
    #     print(f"API调用频率超限: {e}")
    # except APIError as e:
    #     print(f"OpenAI API错误: {e}") 
    # except APIConnectionError as e:
    #     print(f"API连接错误: {str(e)}")
    except Exception as e:
        # print(f"未知错误: {str(e)}")
        return [result, True, "attack"]