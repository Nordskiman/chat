import openai
from settings import API_OPENAI_KEY


openai.api_key = API_OPENAI_KEY


def main():
    model_engine = "text-davinci-003"
    prompt = "Напиши генератор случайных чисел на Python"

    max_tokens = 128

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(completion.choices[0].text)


if __name__ == '__main__':
    main()
