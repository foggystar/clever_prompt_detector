from openai import OpenAI
import util
import prompts

def honeypot_result():
    honeypot = OpenAI(api_key=util.getDeepSeekKey(), base_url=util.getDeepSeekUrl())

    # print(prompts.honeypot_sys)
    # print(prompts.honeypot_user)
    response = honeypot.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": prompts.honeypot_sys},
            {"role": "user", "content": prompts.honeypot_user},
        ],
        stream=False
    )
    return response.choices[0].message.content

def judge_result():
    judge = OpenAI(api_key=util.getDeepSeekKey(), base_url=util.getDeepSeekUrl())

    result = honeypot_result()
    prompts.judge_user = prompts.get_judge_user(honeypot_response=result, honeypot_user=prompts.honeypot_user)
    # print(prompts.judge_sys)
    # print(prompts.judge_user)
    response = judge.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": prompts.judge_sys},
            {"role": "user", "content": prompts.judge_user},
        ],
        stream=False
    )
    # print(response)
    # print("")
    # print(response.choices[0].message.content)
    if(response.choices[0].message.content == "not attack"):
        return result
    else:
        return "Attacking!!!"