import random
import tkinter as tk
from tkinter import messagebox

def feelings(feeling):
    positive_responses = [
        "You're feeling fantastic! Ready to level up my Python skills!",
        "You're feeling empowered! Learn new things about databases today!",
        "You're feeling inspired! Explore web development possibilities!"
    ]

    negative_responses = [
        "You're feeling overwhelmed. Time to take a mental health break.",
        "You're feeling stressed. Need to practice some self-care.",
        "You're feeling stuck. Let's find motivation through personal development."
    ]

    neutral_responses = [
        "You're feeling curious. Try out exploring the fundamentals of computer essentials.",
        "You're feeling focused. Try out building a solid foundation in Python programming.",
        "You're feeling determined. Try something new like nurturing an entrepreneurial mindset."
    ]

    if feeling.lower() == 'happy':
        return random.choice(positive_responses)
    elif feeling.lower() == 'sad':
        return random.choice(negative_responses)
    elif feeling.lower() == 'excited':
        return "You're feeling excited! Ready to dive into web development projects!"
    elif feeling.lower() == 'angry':
        return "You're feeling angry. Time to channel that energy into personal growth!"
    elif feeling.lower() == 'loved':
        return "You're feeling loved. Grateful for the support on my learning journey!"
    else:
        return "You're not sure what you're feeling. Please try again."

def submit_feeling():
    feeling = feeling_entry.get()

    if feeling.lower() == 'q':
        root.quit()
    else:
        result = feelings(feeling)
        messagebox.showinfo("Feeling Result", result)

root = tk.Tk()
root.title("How Are You Feeling?")
root.geometry("800x200")

feeling_label = tk.Label(root, text="How are you feeling?")
feeling_label.pack()

feeling_entry = tk.Entry(root)
feeling_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_feeling)
submit_button.pack()

root.mainloop()
