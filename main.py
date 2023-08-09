import openai, tkinter as tk
from tkinter import filedialog

class SophiaAI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sophia AI")
        self.geometry('1000x800')
        self.instances = {'default': []}
        self.current_instance = 'default'
        self.prompt = "Welcome to Sophia AI! Upload or write your prompt."
        self.gpt4_models = [m['id'] for m in openai.Model.list()['data'] if 'gpt-4' in m['id']]
        self.selected_model = tk.StringVar(value=self.gpt4_models[0]) # Default to the first GPT-4 model
        self.init_widgets()

    def init_widgets(self):
        tk.Label(self, text="Best GPT-4 model selected by default.").pack(pady=5)
        tk.OptionMenu(self, self.selected_model, *self.gpt4_models).pack(pady=5)
        tk.Button(self, text="Enter/Upload Prompt", command=self.load_prompt).pack(pady=5)
        self.prompt_display = tk.Label(self, text=self.prompt, wraplength=900, font=("Arial", 12))
        self.prompt_display.pack(pady=5)
        self.generate_button = tk.Button(self, text="Generate Response", command=self.generate_response)
        self.generate_button.pack(pady=5)
        self.chat_window = tk.Text(self, height=15, wrap=tk.WORD, font=("Courier New", 12))
        self.chat_window.pack(pady=5)
        self.user_input = tk.Entry(self, width=50)
        self.user_input.pack(pady=5)
        tk.Button(self, text="Talk to Sophia", command=self.talk_to_sophia).pack(pady=5)

    def load_prompt(self):
        with open(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")], initialfile="the_sophia_prompt.txt"), "r") as file:
            self.prompt = file.read().strip()
            self.prompt_display.config(text=self.prompt)

    def generate_response(self):
        self.generate_button.config(state=tk.DISABLED, text="Generating...")
        self.after(100, self.background_generate_response)

    def background_generate_response(self):
        # Using OpenAI's ChatCompletion API
        response = openai.ChatCompletion.create(
            model=self.selected_model.get(),
            messages=[{"role": "system", "content": self.prompt}] + self.instances[self.current_instance]
        )
        self.instances[self.current_instance].append({"role": "assistant", "content": response.choices[0].message['content']})
        self.chat_window.insert(tk.END, "Sophia: " + response.choices[0].message['content'] + '\n')
        self.chat_window.see(tk.END)  # Scroll to the end
        self.generate_button.config(state=tk.NORMAL, text="Generate Response")

    def talk_to_sophia(self):
        user_message = self.user_input.get()
        self.chat_window.insert(tk.END, "You: " + user_message + '\n')
        self.instances[self.current_instance].append({"role": "user", "content": user_message})
        self.user_input.delete(0, tk.END)
        self.generate_response()  # Automatically generate response

if __name__ == "__main__":
    SophiaAI().mainloop()
