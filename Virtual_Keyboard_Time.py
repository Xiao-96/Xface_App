import tkinter as tk
import customtkinter as ctk

class VirtualKeyboardTime(tk.Frame):
    def __init__(self, parent, on_key_press):
        super().__init__(parent)
        self.parent = parent
        self.entry = None
        self.on_key_press = on_key_press

        self.rows = [
            "789:",
            "456.",
            "1230"
        ]
        self.create_keyboard()

        self.backspace_button = ctk.CTkButton(self, text="⌫", width=200, height=50, command=self.backspace, fg_color="gray")
        self.backspace_button.grid(row=4, column=0, columnspan=4)

    def show_for(self, entry):
        if self.entry != entry:
            self.entry = entry
            self.position_window_near_entry(entry)
        self.pack(side="bottom")  

    def position_window_near_entry(self, entry):
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()

        keyboard_width = self.winfo_reqwidth()
        keyboard_height = self.winfo_reqheight()

        x_pos = (screen_width - keyboard_width) // 2
        y_pos = screen_height - keyboard_height

        self.place(x=x_pos, y=y_pos)

    def create_keyboard(self):
        for row_index, rows in enumerate(self.rows):
            for col_index, letter in enumerate(rows):
                button = ctk.CTkButton(self, text=letter, width=50, height=50, command=lambda l=letter: self.on_key_press(self.entry, l), fg_color="gray")
                button.grid(row=row_index, column=col_index)                             ###_fix 20240606 1-1-7-1-5 on_press -> on_key_press

    def backspace(self):
        current_text = self.entry.get()
        if current_text:
            self.entry.delete(len(current_text) - 1, tk.END)