import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date
import os

TASKS_FILE = "tasks.txt"
DATE_FORMAT = "%Y-%m-%d"


def create_demo_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            f.write("Сдать лабу | 2026-05-20\n")
            f.write("Скоро экзамен | 2026-05-27\n")
            f.write("Навестить бабушку | 2026-06-15\n")
            f.write("Сходить в кино | 2026-07-01\n")
            f.write("Новый год | 2027-01-01\n")


def load_tasks():
    tasks = []
    if not os.path.exists(TASKS_FILE):
        return tasks

    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "|" not in line:
                continue

            title, date_str = [x.strip() for x in line.split("|", 1)]

            try:
                task_date = datetime.strptime(date_str, DATE_FORMAT).date()
                tasks.append((title, task_date))
            except ValueError:
                continue

    return tasks


def get_task_text(task_title, task_date):
    today = date.today()
    delta = (task_date - today).days

    if delta < 0:
        return f"Прошло {-delta} дн. от {task_title}", "overdue"
    elif delta == 0:
        return f"Прямо сейчас: {task_title}", "today"
    else:
        return f"Осталось {delta} дн. до {task_title}", "future"


def refresh_tasks():
    text.config(state="normal")
    text.delete("1.0", tk.END)

    tasks = sorted(load_tasks(), key=lambda x: x[1])

    text.insert(tk.END, "Мои текущие задачи\n\n", "title")

    if not tasks:
        text.insert(tk.END, "Задач пока нет\n", "future")
    else:
        for task_title, task_date in tasks:
            line, tag = get_task_text(task_title, task_date)
            text.insert(tk.END, line + "\n", tag)

    text.config(state="disabled")


def add_task():
    title = entry_title.get().strip()
    date_str = entry_date.get().strip()

    if not title or not date_str:
        messagebox.showwarning("Ошибка", "Заполни название и дату.")
        return

    try:
        datetime.strptime(date_str, DATE_FORMAT)
    except ValueError:
        messagebox.showerror("Ошибка", "Дата должна быть в формате ГГГГ-ММ-ДД.")
        return

    with open(TASKS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{title} | {date_str}\n")

    entry_title.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    refresh_tasks()


create_demo_file()

root = tk.Tk()
root.title("Что мне делать, как мне жить?")
root.geometry("760x520")
root.configure(bg="black")

top_frame = tk.Frame(root, bg="black")
top_frame.pack(pady=10)

label_title = tk.Label(
    top_frame,
    text="Мои текущие задачи",
    font=("Times New Roman", 26, "bold"),
    fg="yellow",
    bg="black"
)
label_title.pack()

text = tk.Text(
    root,
    width=55,
    height=14,
    bg="black",
    fg="white",
    insertbackground="white",
    font=("Arial", 16),
    bd=0,
    highlightthickness=0
)
text.pack(padx=20, pady=10)

text.tag_config("title", foreground="yellow", justify="center", font=("Times New Roman", 24, "bold"))
text.tag_config("overdue", foreground="red")
text.tag_config("today", foreground="orange")
text.tag_config("future", foreground="lightgray")

bottom_frame = tk.Frame(root, bg="black")
bottom_frame.pack(pady=10)

tk.Label(bottom_frame, text="Задача:", fg="white", bg="black", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
entry_title = tk.Entry(bottom_frame, width=25, font=("Arial", 12))
entry_title.grid(row=0, column=1, padx=5, pady=5)

tk.Label(bottom_frame, text="Дата (ГГГГ-ММ-ДД):", fg="white", bg="black", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
entry_date = tk.Entry(bottom_frame, width=25, font=("Arial", 12))
entry_date.grid(row=1, column=1, padx=5, pady=5)

btn_add = tk.Button(
    bottom_frame,
    text="Добавить",
    command=add_task,
    font=("Arial", 12, "bold"),
    bg="yellow",
    fg="black",
    width=15
)
btn_add.grid(row=2, column=0, columnspan=2, pady=10)

refresh_tasks()
root.mainloop()