import random
from pathlib import Path

BASE_DIR = Path(__file__).parent
DRAWINGS_DIR = BASE_DIR / "hangman_drawings"
WORDS_FILE = BASE_DIR / "words.txt"


def load_words():
    with WORDS_FILE.open("r", encoding="utf-8") as file:
        return [line.strip().lower() for line in file if line.strip()]


def load_drawing(mistakes):
    drawing_file = DRAWINGS_DIR / f"gallows_{mistakes}.txt"
    with drawing_file.open("r", encoding="utf-8") as file:
        return file.read()


def show_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def start():
    words = load_words()
    word = random.choice(words)
    guessed_letters = set()
    mistakes = 0
    max_mistakes = 6

    print("Игра «Виселица на поле чудес». Угадайте слово по буквам.")

    while mistakes < max_mistakes and not all(letter in guessed_letters for letter in word):
        print(load_drawing(mistakes))
        print(show_word(word, guessed_letters))
        letter = input("Введите одну букву: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Введите одну букву.")
        elif letter in guessed_letters:
            print("Вы уже называли эту букву.")
        else:
            guessed_letters.add(letter)
            if letter not in word:
                mistakes += 1
                print("Такой буквы нет.")
            else:
                print("Есть такая буква!")

    print(load_drawing(mistakes))
    if all(letter in guessed_letters for letter in word):
        print("Вы угадали слово:", word)
    else:
        print("Попытки закончились. Загаданное слово:", word)
