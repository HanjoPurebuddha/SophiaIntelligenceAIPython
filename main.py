import openai, threading, tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

class SophiaAI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sophia AI")
        self.geometry('900x700')
        self.outputs, self.running, self.params, self.model_var, self.instance_var, self.waiting_label, self.prompt = {'default': []}, False, {'t': 0.7, 'p': 0.9, 'm': 4096, 'f': 0, 'pres': 0}, tk.StringVar(), tk.StringVar(value='default'), tk.Label(self, text=""), ""
        self.init_widgets()

    def init_widgets(self):
        [w.pack(pady=5) for w in [tk.Button(self, text="Enter/Upload Prompt", command=self.load_prompt), tk.Text(self, height=10), tk.OptionMenu(self, self.model_var, *([m['id'] for m in openai.Model.list()['data']])), tk.OptionMenu(self, self.instance_var, *list(self.outputs.keys()), 'New', command=self.switch_instance), tk.Button(self, text="Regenerate & Run", command=self.regenerate_and_run)]]

    def switch_instance(self, value):
        self.instance_var.set(value)
        self.outputs[self.instance_var.get()] = self.outputs.get(self.instance_var.get(), [])

    def load_prompt(self):
        with open(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")], initialfile="the_sophia_prompt.txt"), "r") as file:
            self.prompt = file.read().strip()

    def regenerate_and_run(self):
        with open("iterated_interface.py", "w") as file:
            file.write(openai.Completion.create(prompt=self.prompt, max_tokens=1000).choices[0].text)
            import iterated_interface

if __name__ == "__main__":
    SophiaAI().mainloop()
