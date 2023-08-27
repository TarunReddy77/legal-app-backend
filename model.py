import openai


def answer_question(question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": generate_prompt(question)}
        ]
    )

    bot_response = completion.choices[0].message.content

    return {"answer": bot_response}


def generate_prompt(question: str):
    return f"{question} Give the answer in one sentence."
