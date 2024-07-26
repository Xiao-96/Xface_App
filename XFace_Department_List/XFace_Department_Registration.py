import tkinter as tk
import customtkinter
from tkinter import messagebox
import numpy as np
from XFace_textfile import Department_Registration_textdir
import XFace_Database_Function
from Virtual_Keyboard import VirtualKeyboard

class Screen16(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

        
        # Initial value of flag
        self.flag = True

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Frame for all elements
        self.menu_frame = customtkinter.CTkFrame(self, width=self.main_app.width, height=self.main_app.height, fg_color="#e6e6e6", corner_radius=0)
        self.menu_frame.place(relx=0)

        # Back Button
        back_btn = customtkinter.CTkButton(self, text="<", command=lambda: self.back_screen(15), width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), text_color="black", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        # Title for the Department Registration section
        title_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[1], font=("Arial", 24), text_color="black", fg_color="transparent")
        title_label.place(relx=0.1, rely=0.1)

        # Department Name Entry
        vcmd50 = (self.register(self.main_app.limit_char50), '%P')
        department_name_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[2], font=("Arial", 20), text_color="black", fg_color="transparent")
        department_name_label.place(relx=0.1, rely=0.2)
        self.department_name_entry = customtkinter.CTkEntry(self.menu_frame, placeholder_text="IT", font=("Arial", 20),  width=int(self.main_app.width/600*400), height=int(self.main_app.height/500*35), validate="key", validatecommand=vcmd50)
        self.department_name_entry.place(relx=0.1, rely=0.25)

        # Starting Work Time Entry
        starting_time_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[3], font=("Arial", 20), text_color="black", fg_color="transparent")
        starting_time_label.place(relx=0.1, rely=0.35)
        self.start_time_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*150), height=int(self.main_app.height/500*35))
        self.start_time_entry.insert(0, "09:00")
        self.start_time_entry.place(relx=0.1, rely=0.4)
        self.start_time_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_start_time_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.start_time_menu_button.place(relx=0.3, rely=0.4)

        # Ending Work Time Entry
        ending_time_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[4], font=("Arial", 20), text_color="black", fg_color="transparent")
        ending_time_label.place(relx=0.5, rely=0.35)
        self.end_time_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*150), height=int(self.main_app.height/500*35))
        self.end_time_entry.insert(0, "18:00")
        self.end_time_entry.place(relx=0.5, rely=0.4)
        self.end_time_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_end_time_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.end_time_menu_button.place(relx=0.7, rely=0.4)

        # Rest Time Entry
        rest_time_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[5], font=("Arial", 20), text_color="black", fg_color="transparent")
        rest_time_label.place(relx=0.1, rely=0.6)
        self.rest_time_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*150), height=int(self.main_app.height/500*35))
        self.rest_time_entry.insert(0, "1.00")
        self.rest_time_entry.place(relx=0.1, rely=0.65)
        self.rest_time_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_rest_time_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.rest_time_menu_button.place(relx=0.3, rely=0.65)

        # Over Time Entry
        over_time_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[6], font=("Arial", 20), text_color="black", fg_color="transparent")
        over_time_label.place(relx=0.5, rely=0.6)
        self.over_time_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*150), height=int(self.main_app.height/500*35))
        self.over_time_entry.insert(0, "0")
        self.over_time_entry.place(relx=0.5, rely=0.65)
        self.over_time_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_over_time_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.over_time_menu_button.place(relx=0.7, rely=0.65)

        # Next Button
        save_btn = customtkinter.CTkButton(self.menu_frame, text=Department_Registration_textdir[10], command=lambda: self.save(), text_color="black", font=("Arial Blod", 20), fg_color="white", width=int(self.main_app.width/600*80), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        save_btn.place(relx=0.75, rely=0.85)

        # Initialize Start Time Frame with Listbox and Scrollbar
        self.start_time_frame = tk.Frame(self, bg="#424242")
        self.start_time_listbox = tk.Listbox(self.start_time_frame, font=("Arial", 15), width=int(self.main_app.width/600*11), height=10)
        for hour in range(24):
            for minute in (0, 30):
                self.start_time_listbox.insert("end", f"{hour:02d}:{minute:02d}")
        self.start_time_listbox.bind("<Double-Button-1>", self.select_start_time)
        self.start_time_scrollbar = tk.Scrollbar(self.start_time_frame, orient="vertical", command=self.start_time_listbox.yview)
        self.start_time_listbox.config(yscrollcommand=self.start_time_scrollbar.set)

        # Initialize End Time Frame with Listbox and Scrollbar
        self.end_time_frame = tk.Frame(self, bg="#424242")
        self.end_time_listbox = tk.Listbox(self.end_time_frame, font=("Arial", 15), width=int(self.main_app.width/600*11), height=10)
        for hour in range(24):
            for minute in (0, 30):
                self.end_time_listbox.insert("end", f"{hour:02d}:{minute:02d}")
        self.end_time_listbox.bind("<Double-Button-1>", self.select_end_time)
        self.end_time_scrollbar = tk.Scrollbar(self.end_time_frame, orient="vertical", command=self.end_time_listbox.yview)
        self.end_time_listbox.config(yscrollcommand=self.end_time_scrollbar.set)

        # Initialize Rest Time Frame with Listbox and Scrollbar
        self.rest_time_frame = tk.Frame(self, bg="#424242")
        self.rest_time_listbox = tk.Listbox(self.rest_time_frame, font=("Arial", 15), width=int(self.main_app.width/600*11), height=10)
        for i in np.arange(0.5, 5.25, 0.25):
            self.rest_time_listbox.insert("end", f"{i:.02f}")
        self.rest_time_listbox.bind("<Double-Button-1>", self.select_rest_time)
        self.rest_time_scrollbar = tk.Scrollbar(self.rest_time_frame, orient="vertical", command=self.rest_time_listbox.yview)
        self.rest_time_listbox.config(yscrollcommand=self.rest_time_scrollbar.set)

        # Initialize Over Time Frame with Listbox and Scrollbar
        self.over_time_frame = tk.Frame(self, bg="#424242")
        self.over_time_listbox = tk.Listbox(self.over_time_frame, font=("Arial", 15), width=int(self.main_app.width/600*11), height=10)
        for i in np.arange(0, 310, 10):
            self.over_time_listbox.insert("end", f"{i}")
        self.over_time_listbox.bind("<Double-Button-1>", self.select_over_time)
        self.over_time_scrollbar = tk.Scrollbar(self.over_time_frame, orient="vertical", command=self.over_time_listbox.yview)
        self.over_time_listbox.config(yscrollcommand=self.over_time_scrollbar.set)

    #VirtualKeyboard Settings
    def entry_keyboard(self):
        self.keyboard_general = VirtualKeyboard(self)  

        self.keyboard_is_visible = False
        self.current_keyboard = None
        self.current_entry = None 

        self.bind_all("<Button-1>", self.global_click)

    def global_click(self, event):
        x, y = event.x_root, event.y_root

        kx, ky, kw, kh = self.keyboard_general.winfo_rootx(), self.keyboard_general.winfo_rooty(), self.keyboard_general.winfo_width(), self.keyboard_general.winfo_height()
        if kx <= x <= kx + kw and ky <= y <= ky + kh:
            return  

        entry_clicked = None
        keyboard_to_use = None

        entries = {
            self.department_name_entry: self.keyboard_general
        }

        for entry, keyboard in entries.items():
            ex, ey, ew, eh = entry.winfo_rootx(), entry.winfo_rooty(), entry.winfo_width(), entry.winfo_height()
            if ex <= x <= ex + ew and ey <= y <= ey + eh:
                entry_clicked = entry
                keyboard_to_use = keyboard
                break

        if entry_clicked:
            if entry_clicked != self.current_entry:
                self.current_entry = entry_clicked
                if self.current_keyboard:
                    self.current_keyboard.pack_forget()   
                keyboard_to_use.show_for(entry_clicked)  
                self.current_keyboard = keyboard_to_use
                self.keyboard_is_visible = True
        else:
            if self.keyboard_is_visible:
                self.current_keyboard.pack_forget() 
                self.keyboard_is_visible = False
                self.current_entry = None
                self.current_keyboard = None

    # Save to DB
    def save(self):
        if self.flag:
            department_name = self.department_name_entry.get()
            start_time = self.start_time_entry.get()
            end_time = self.end_time_entry.get()
            rest_time = self.rest_time_entry.get()
            over_time = self.over_time_entry.get()
            if not department_name.strip():
                self.flag = False
                self.message_frame1 = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
                self.message_frame1.place(relx=0.25, rely=0.32)
                error_label = customtkinter.CTkLabel(master=self.message_frame1, text="Has not been entered!", font=("Arial", 20), text_color="black")
                error_label.place(relx=0.25, rely=0.1)
                btn_ok = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.cancel(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                btn_ok.place(relx=0.35, rely=0.7)
                return
            
            flag = XFace_Database_Function.insert_department(department_name, start_time, end_time, rest_time, over_time)

            self.message_frame = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame.place(relx=0.25, rely=0.32)
            if flag:
                success_label = customtkinter.CTkLabel(master=self.message_frame, text="Department registration successfully.", font=("Arial", 20), text_color="black")
                success_label.place(relx=0.15, rely=0.1)
            else:
                error_label = customtkinter.CTkLabel(master=self.message_frame, text="Creation of up to 100 departments.", font=("Arial", 20), text_color="black")
                error_label.place(relx=0.15, rely=0.1)
            btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.destroy_message_frame(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.35, rely=0.7)

            self.flag = False
    
    # Set flags and remove frame
    def cancel(self):
        self.flag = True
        self.message_frame1.destroy()
        
    # Set flags, delete widgets, remove keybord settings and screen transitons
    def destroy_message_frame(self):
        self.flag = True
        self.message_frame.destroy()
        self.unbind_all("<Button-1>")
        loginuseradminflag = self.main_app.get_loginuseradminflag()
        
        if loginuseradminflag:
            self.main_app.show_next_screen(4)
        else:
            self.main_app.show_next_screen(5)

    # Value initialization, remove keybord settings and screen transitons
    def back_screen(self, index):
        self.department_name_entry.delete(0, tk.END)
        self.unbind_all("<Button-1>")
        self.main_app.show_next_screen(index)

    # Enter the value selected in the list
    def select_start_time(self, event):
        selected_time = self.start_time_listbox.get(tk.ACTIVE)
        self.start_time_entry.delete(0, tk.END)
        self.start_time_entry.insert(0, selected_time)
        self.start_time_frame.place_forget()

    def select_end_time(self, event):
        selected_time = self.end_time_listbox.get(tk.ACTIVE)
        self.end_time_entry.delete(0, tk.END)
        self.end_time_entry.insert(0, selected_time)
        self.end_time_frame.place_forget()

    def select_rest_time(self, event):
        selected_time = self.rest_time_listbox.get(tk.ACTIVE)
        self.rest_time_entry.delete(0, tk.END)
        self.rest_time_entry.insert(0, selected_time)
        self.rest_time_frame.place_forget()

    def select_over_time(self, event):
        selected_time = self.over_time_listbox.get(tk.ACTIVE)
        self.over_time_entry.delete(0, tk.END)
        self.over_time_entry.insert(0, selected_time)
        self.over_time_frame.place_forget()

    # Showing and Hiding Lists
    def show_start_time_menu(self):
        if not self.start_time_frame.winfo_ismapped():
            self.start_time_frame.place(relx=0.1, rely=0.465)
            self.start_time_listbox.pack(side="left")
            self.start_time_scrollbar.pack(side="right", fill="y")
        else:
            self.start_time_frame.place_forget()

    def show_end_time_menu(self):
        if not self.end_time_frame.winfo_ismapped():
            self.end_time_frame.place(relx=0.5, rely=0.465)
            self.end_time_listbox.pack(side="left")
            self.end_time_scrollbar.pack(side="right", fill="y")
        else:
            self.end_time_frame.place_forget()

    def show_rest_time_menu(self):
        if not self.rest_time_frame.winfo_ismapped():
            self.rest_time_frame.place(relx=0.1, rely=0.23)
            self.rest_time_listbox.pack(side="left")
            self.rest_time_scrollbar.pack(side="right", fill="y")
        else:
            self.rest_time_frame.place_forget()

    def show_over_time_menu(self):
        if not self.over_time_frame.winfo_ismapped():
            self.over_time_frame.place(relx=0.5, rely=0.23)
            self.over_time_listbox.pack(side="left")
            self.over_time_scrollbar.pack(side="right", fill="y")
        else:
            self.over_time_frame.place_forget()