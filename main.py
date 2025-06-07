import random

random_num = random.randint(1, 100)
max_attempts = 10
attempt = 0  # Лічильник спроб

print("Вітаємо у грі 'Вгадай число'!")
print("Комп'ютер загадав число від 1 до 100.")
print(f"У вас є {max_attempts} спроб, щоб його вгадати.")

while attempt < max_attempts:
    print(f"\nСпроба {attempt + 1} з {max_attempts}")

    try:
        user_guess = int(input("Введіть ваше число: "))
    except ValueError:
        print("Будь ласка, введіть правильне число!")
        continue  # Пропускаємо зменшення лічильника спроб

    attempt += 1  # Збільшуємо лічильник спроб лише при коректному введенні

    if user_guess == random_num:
        print(f"Вітаємо! Ви вгадали число {random_num} за {attempt} спроб!")
        break
    elif user_guess < random_num:
        print("Занадто маленьке")
    else:
        print("Занадто велике")
else:
    print(f"\nГра закінчена! Загадане число було: {random_num}")
    print("Спробуйте ще раз!")