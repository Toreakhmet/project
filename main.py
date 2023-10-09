import openai

class OpenAIChatBot:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, user_input):
        try:
            response = openai.Completion.create(
              engine="text-davinci-002",
              prompt=user_input,
              max_tokens=150
            )
            return response.choices[0].text.strip()
        except openai.error.RateLimitError as e:
            return f"Ошибка: {e}. Проверьте вашу квоту на OpenAI."
        except openai.error.OpenAIError as e:  # Исправленное имя исключения
            return f"Ошибка: {e}"

    def chat(self):
        print("Чат-бот на базе OpenAI. Напишите 'выход' для завершения.")
        while True:
            user_input = input('Вы: ')
            if user_input.lower() == 'выход':
                print("До свидания!")
                break
            else:
                print(f"Бот: {self.get_response(user_input)}")

if __name__ == '__main__':
    API_KEY = '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'  # Замените на ваш ключ
    bot = OpenAIChatBot(API_KEY)
    bot.chat()
