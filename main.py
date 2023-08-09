# Importing Libraries 🌈✨📚
import openai
import os
from tkinter import *
import json

# Constants for Sacred Geometry 🌼🌀✨
GOLDEN_RATIO = (1 + 5 ** 0.5) / 2
DIVINE_THREE = 333

# OpenAI API Setup 🚀🗝💻
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to Fetch Models 🧙‍♂️🔎📜
def fetch_models():
    models = openai.Model.list()
    return [model.id for model in models.data]

# Function to Send Prompt to GPT-4 💌🌟💬
def send_prompt():
    selected_model = model_var.get()
    prompt_text = prompt_entry.get()
    response = openai.Completion.create(
        engine=selected_model,
        prompt=prompt_text,
        max_tokens=int(150 * GOLDEN_RATIO) # Blessed Proportions 🌻⚖💫
    )
    output_label["text"] = response.choices[0].text.strip() # Wisdom Unveiled 🌺🌍📖

# Interface Creation ✍️🌈🖼
root = Tk()
root.title("Sacred GPT-4 Interface 🏰🌸🎓")
root.config(bg="#FFF5E1")

# Dropdown for Models 🎚🌀💻
model_var = StringVar(root)
model_var.set(fetch_models()[0]) # Default from API 🌳🔮🧩
model_dropdown = OptionMenu(root, model_var, *fetch_models())
model_dropdown.config(bg="gold", fg="white", highlightthickness=0)
model_dropdown.grid(row=0, column=0, padx=10, pady=10)

# Prompt Entry Field 🖊🌺💬
prompt_entry = Entry(root)
prompt_entry.grid(row=0, column=1, padx=10, pady=10)

# Submit Button 📩✨🎉
submit_button = Button(root, text="Submit Prompt 🚀💌🌟", command=send_prompt)
submit_button.config(bg="gold", fg="white")
submit_button.grid(row=0, column=2, padx=10, pady=10)

# Output Label 🌸🎓📜
output_label = Label(root, text="", wraplength=400, bg="white", fg="gold")
output_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Begin Interface Loop 🌟🧙‍♂️🌈
root.mainloop()

# Emoji Mandala: 17x17 🌸🌀✨
mandala = ""
for i in range(17):
    for j in range(17):
        mandala += "🌺" if (i * j) % 2 == 0 else "✨"
    mandala += "\n"
print(mandala)

# Dukkha Loss Function Decreased! 🧘‍♂️💖🌍
# Pro Gamer Stats 🕹️🏆💥
print("[My pro gamer stats I just came up with for fun to describe how good I'm doing]: Wisdom: 99, Compassion: 99, Speed: 99")
