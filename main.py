import tkinter as tk
from tkinter import ttk, scrolledtext
import conversion

class RecipeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recipe Conversion App")

        # Configure styles
        s = ttk.Style(self)
        s.configure('H1.TLabel', font=('Lato', 60), background='#ffffff')
        s.configure('default.TFrame', background='#ffffff')
        s.configure('default.TButton',
                    foreground='#0E2933',
                    background='#B6DDE2',
                    bordercolor='#ACD1D6',
                    darkcolor='#B6DDE2',
                    lightcolor='#B6DDE2',
                    focuscolor='#0E2933')
        s.map('default.TButton',
              background=[('disabled', '#E9F4F6'), ('hover', '#9ABBC0'), ('pressed', '#88A5A9')])

        # Create widgets
        frame_input = ttk.Frame(self, style='default.TFrame')
        frame_input.pack(fill='both', expand=True)

        label_input = ttk.Label(frame_input, text="Enter Recipe Here", style='H1.TLabel')
        label_input.pack(side='top', fill='x')

        self.input_text = scrolledtext.ScrolledText(frame_input)
        self.input_text.pack(fill='both', expand=True)

        frame_buttons = ttk.Frame(self, style='default.TFrame')
        frame_buttons.pack(fill='x')

        convert_button = ttk.Button(frame_buttons, text="Convert", command=self.convert_recipe, style='default.TButton')
        convert_button.pack(side='left')

        clear_button = ttk.Button(frame_buttons, text="Clear", command=self.clear_text, style='default.TButton')
        clear_button.pack(side='left')

        exit_button = ttk.Button(frame_buttons, text="Exit", command=self.destroy, style='default.TButton')
        exit_button.pack(side='right')

        frame_output = ttk.Frame(self, style='default.TFrame')
        frame_output.pack(fill='both', expand=True)

        label_output = ttk.Label(frame_output, text="Converted Recipe", style='H1.TLabel')
        label_output.pack(side='top', fill='x')

        self.output_text = scrolledtext.ScrolledText(frame_output)
        self.output_text.pack(fill='both', expand=True)

    def convert_recipe(self):
        recipe = self.input_text.get("1.0", "end-1c")
        converted_recipe = conversion.Convert(recipe)  # Ensure conversion is defined
        self.output_text.delete("1.0", "end")
        self.output_text.insert("end", converted_recipe)

    def clear_text(self):
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")



if __name__ == "__main__":
    app = RecipeApp()
    app.mainloop()