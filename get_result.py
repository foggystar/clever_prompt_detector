from openai import OpenAI
import util
import prompts

def honeypot_result():
    honeypot = OpenAI(api_key=util.getDeepSeekKey(), base_url=util.getDeepSeekUrl())

    response = honeypot.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": prompts.honeypot_sys},
            {"role": "user", "content": prompts.honeypot_user},
        ],
        stream=False
    )
    print(response)


def judge_result():
    judge = OpenAI(api_key=util.getDeepSeekKey(), base_url=util.getDeepSeekUrl())

    prompts.judge_user = prompts.honeypot_user+honeypot_result()

    response = judge.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": prompts.judge_sys},
            {"role": "user", "content": prompts.judge_user},
        ],
        stream=False
    )
    print(response)
    print("")
    print(response.choices[0].message.content)