import tkinter as tk
import time
import random
import os

start_time = None
sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Practice makes perfect, and perfect practice makes progress.",
    "Typing is a skill that improves with consistency and time.",
    "Speed comes with accuracy. Focus on being accurate first.",
    "Stay calm and type with confidence.",
    "Learning to type faster helps improve productivity and communication.",
    "In a world driven by technology, typing is one of the most essential skills.",
    "Python is a powerful and beginner-friendly programming language used around the world.",
    "The art of writing has evolved from pen and paper to keyboards and screens.",
    "Good posture, correct finger placement, and regular breaks can improve your typing experience.",
    "Computers have become a crucial part of our daily lives. Whether for work, study, or entertainment, typing efficiently helps us save time and energy.",
    "Successful typing involves muscle memory, focus, and a relaxed posture. The more you practice, the better your brain and fingers will coordinate.",
    "Touch typing means you no longer need to look at your keyboard. It may take effort at first, but it pays off in speed and accuracy over time.",
    "Typing games and tests are a fun way to build up your typing speed. They help develop muscle memory while keeping you engaged and motivated.",
    "Even though voice assistants are common today, the ability to type clearly and quickly remains a fundamental skill for digital communication."
]


sample_text=sample_texts[random.randint(0,len(sample_texts)-1)]

def load_high_scores():
    if not os.path.exists('highscores.txt'):
        with open('highscores.txt','w') as f:
            f.write("0")
    with open('highscores.txt','r') as f:
        return float(f.read().strip())




def start_timer(event):
    global start_time
    if start_time is None:
        start_time = time.time()

def count_wpm():
    global start_time, sample_text
    end_time = time.time()
    typed_text=input.get("1.0",tk.END).strip()
    num_words=len(typed_text.split())
    time_taken = end_time - start_time
    wpm=(num_words/time_taken)*60
    current_high = load_high_scores()
    if wpm > current_high:
        with open("highscores.txt", "w") as file:
            file.write(str(wpm))
    current_high = load_high_scores()

    text=f"Your Typing speed is {wpm:.2f}WPM and the HIGHScore is {current_high:.2f}WPM"

    tk.Label(screen, text=text, wraplength=500, font=("Helvetica", 14)).pack()



    start_time = None





screen=tk.Tk()
screen.title("Typing Speed Test")
screen.geometry("600x400")

tk.Label(screen, text=sample_text, wraplength=500, font=("Helvetica", 14)).pack()

input=tk.Text(screen, height=5, width=50)
input.pack()
input.bind("<KeyPress>", start_timer)

submit_button = tk.Button(screen, text="Submit", command=count_wpm)
submit_button.pack(pady=10)

tk.mainloop()
