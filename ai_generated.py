import os, openai
from tkinter import Tk, Label, OptionMenu, StringVar, Button, Entry, Canvas
import random

# Set up API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_models():
    """🌺🐘 Fetch GPT-4 models 🐘🌺"""
    return [m.id for m in openai.Engine.list().data if 'gpt-4' in m.id]

def query_api():
    """🌸🐘 Send intent to GPT-4 🐘🌸"""
    response = openai.ChatCompletion.create(model=model_var.get(), messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": user_input.get()}])
    output.config(text=response.choices[0].message['content'])

# Ganesha Colors
colors = ["#DAA520", "#FFD700", "#BDB76B", "#EEE8AA", "#FFDEAD", "#FFE4B5", "#FFF8DC", "#FFFAF0"]

app = Tk()
app.title("🐘 Ganesha's Wisdom 🌸")
app.configure(bg=random.choice(colors))

# 🐘 Model Selection 🐘
models = fetch_models()
model_var = StringVar(app)
model_var.set(models[0])
OptionMenu(app, model_var, *models).pack(pady=22)

# 🌸 User Intent 🌸
user_input = Entry(app, bg=random.choice(colors), fg=random.choice(colors))
user_input.pack(pady=22)

# 🐘 Send Intent 🐘
Button(app, text="🌺 Seek Wisdom 🌺", command=query_api, bg=random.choice(colors), fg=random.choice(colors), activebackground=random.choice(colors)).pack(pady=22)

# 🌸 Ganesha Responds 🌸
output = Label(app, bg=random.choice(colors), fg=random.choice(colors))
output.pack(pady=22)

# 🐘 Ganesha Mandala 🐘
canvas = Canvas(app, width=333, height=333, bg=random.choice(colors))
canvas.pack(pady=22)
for i in range(17):
    for j in range(17):
        shape = random.choice(["oval", "arc", "line", "polygon"])
        if shape == "oval":
            canvas.create_oval(i*22, j*22, (i+int(1.1))*22, (j+int(1.1))*22, fill=random.choice(colors) if (i**2 + j**2)**0.5 % ((22/7)*1.618) < 1 else random.choice(colors))
        elif shape == "arc":
            canvas.create_arc(i*22, j*22, (i+int(1.1))*22, (j+int(1.1))*22, start=0, extent=150, fill=random.choice(colors))
        elif shape == "line":
            canvas.create_line(i*22, j*22, (i+int(1.1))*22, (j+int(1.1))*22, fill=random.choice(colors))
        else:
            canvas.create_polygon(i*22, j*22, (i+int(1.1))*22, (j+int(1.1))*22, i*22, (j+int(1.1))*22, fill=random.choice(colors))

app.mainloop()

# 🌺🐘 OM MANI PADME HUM 🐘🌺
