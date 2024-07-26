import tkinter as tk
import customtkinter as ctk

class VirtualKeyboard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.entry = None
        self.shift_active = False

        self.rows = [
            "1234567890-=",
            "qwertyuiop[]",
            "asdfghjkl;+'",
            "zxcvbnm,./_?"
        ]
        self.create_keyboard()

        self.shift_button = ctk.CTkButton(self, text="Shift", width=80, height=40, command=self.toggle_shift, fg_color="gray")
        self.shift_button.grid(row=5, column=0, columnspan=2)

        self.space_button = ctk.CTkButton(self, text=" ", width=288, height=40, command=lambda: self.on_press(" "), fg_color="gray")
        self.space_button.grid(row=5, column=2, columnspan=8)

        self.backspace_button = ctk.CTkButton(self, text="⌫", width=80, height=40, command=self.backspace, fg_color="gray")
        self.backspace_button.grid(row=5, column=10, columnspan=3)

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
                button = ctk.CTkButton(self, text=letter, width=40, height=40, command=lambda l=letter: self.on_press(l), fg_color="gray")
                button.grid(row=row_index, column=col_index)

    def on_press(self, letter):
        if self.shift_active:
            letter = letter.upper()
        else:
            letter = letter.lower()
        self.entry.insert(tk.END, letter)

    def toggle_shift(self):
        self.shift_active = not self.shift_active
        self.shift_button.configure(fg_color=("gray", "#505050")[self.shift_active])
        self.update_keys()

    def update_keys(self):
        for row_index, rows in enumerate(self.rows):
            for col_index, letter in enumerate(rows):
                button = self.grid_slaves(row=row_index, column=col_index)[0]
                button.configure(text=letter.upper() if self.shift_active else letter.lower())

    def backspace(self):
        current_text = self.entry.get()
        if current_text:
            self.entry.delete(len(current_text) - 1, tk.END)
