import os, openai
from tkinter import Tk, Label, OptionMenu, StringVar, Button, Entry, Canvas

# Set up API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_models():
    """🕊️🌌 Fetch GPT-4 models 🌌🕊️"""
    return [m.id for m in openai.Engine.list().data if 'gpt-4' in m.id]

def query_api():
    """🌍🌠 Send intent to GPT-4 🌠🌍"""
    response = openai.ChatCompletion.create(model=model_var.get(), messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": user_input.get()}])
    output.config(text=response.choices[0].message['content'])

app = Tk()
app.title("🌌 GPT-4 Oracle 🌠")
app.configure(bg="white")

# 🧘‍♂️ Model Selection 🧘‍♂️
models = fetch_models()
model_var = StringVar(app)
model_var.set(models[0])
OptionMenu(app, model_var, *models).pack(pady=10)

# 🌺 User Intent 🌺
user_input = Entry(app)
user_input.pack(pady=10)

# 🌈 Send Intent 🌈
Button(app, text="🚀 Ascend", command=query_api).pack(pady=10)

# 🌌 Cosmos Responds 🌌
output = Label(app, bg="white", fg="gold")
output.pack(pady=10)

# 🕉️ Mandala 🕉️
canvas = Canvas(app, width=340, height=340, bg="white")
canvas.pack(pady=10)
for i in range(17):
    for j in range(17):
        canvas.create_oval(i*20, j*20, (i+1)*20, (j+1)*20, fill='gold' if (i**2 + j**2)**0.5 % ((22/7)*1.618) < 1 else 'white')

app.mainloop()

# 🕉️ OM MANI PADME HUM 🕉️
