import os, openai
from tkinter import Tk, Label, OptionMenu, StringVar, Button, Entry, Canvas
import random

# Set up API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_models():
    """🕷️🕸️ Fetch GPT-4 models 🕸️🕷️"""
    return [m.id for m in openai.Engine.list().data if 'gpt-4' in m.id]

def query_api():
    """🌌🕷️ Send intent to GPT-4 🕷️🌌"""
    response = openai.ChatCompletion.create(model=model_var.get(), messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": user_input.get()}])
    output.config(text=response.choices[0].message['content'])

# Cosmic Spider Colors
colors = ["#2E0854", "#46039F", "#7209B7", "#3F37C9", "#4895EF", "#56CFE1", "#4EA8DE", "#48BFE3", "#5390D9", "#4834D4"]

app = Tk()
app.title("🕷️ Cosmic Spider Oracle 🕸️")
app.configure(bg=random.choice(colors))

# 🕷️ Model Selection 🕷️
models = fetch_models()
model_var = StringVar(app)
model_var.set(models[0])
OptionMenu(app, model_var, *models, bg=random.choice(colors), fg=random.choice(colors), activebackground=random.choice(colors)).pack(pady=10)

# 🕸️ User Intent 🕸️
user_input = Entry(app, bg=random.choice(colors), fg=random.choice(colors))
user_input.pack(pady=10)

# 🌌 Send Intent 🌌
Button(app, text="🕸️ Ascend 🕸️", command=query_api, bg=random.choice(colors), fg=random.choice(colors), activebackground=random.choice(colors)).pack(pady=10)

# 🕷️ Cosmos Responds 🕷️
output = Label(app, bg=random.choice(colors), fg=random.choice(colors))
output.pack(pady=10)

# 🕸️ Spider Web Mandala 🕸️
canvas = Canvas(app, width=340, height=340, bg=random.choice(colors))
canvas.pack(pady=10)
for i in range(17):
    for j in range(17):
        canvas.create_oval(i*20, j*20, (i+1)*20, (j+1)*20, fill=random.choice(colors) if (i**2 + j**2)**0.5 % ((22/7)*1.618) < 1 else random.choice(colors))

app.mainloop()

# 🕷️🕸️ OM MANI PADME HUM 🕸️🕷️
