import tkinter
import tkinter as tk
import customtkinter
from tkinter import messagebox
import math
import os
from Virtual_Keyboard import VirtualKeyboard
from Virtual_Keyboard_Number import VirtualKeyboardNumber

import XFace_Database_Function

class Screen6(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        self.step_frame = customtkinter.CTkFrame(self, width=int(self.main_app.width/600*600), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=0)
        self.step_frame.place(relx=0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(self, command= lambda: self.back_screen(), width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        #--------------------------------------------
        #                   Canvas
        #--------------------------------------------

        # Create Canvas
        canvas = customtkinter.CTkCanvas(
            self.step_frame,
            width = int(self.main_app.width/600*600),
            height = int(self.main_app.height/500*150),
            bg = "#e6e6e6",
            highlightthickness = 0,
            bd = 0
        )
        canvas.place(relx=0, rely=0.24)

        # Add Line
        canvas.create_line(125, 45, 810, 45, width=2)

        # Add Circle 1 Border
        canvas.create_aa_circle(125, 45, 38, math.pi/2, fill="#288fc8")
        # Add Circle 1
        canvas.create_aa_circle(125, 45, 35, math.pi/2, fill="#d9d9d9")
        # Add Text 1
        canvas.create_text(125, 45, text="1", fill="black", font=('Arial 25'))
        # Add Text "Username/Password/"
        canvas.create_text(125, 95, text="Username/Password/", fill="black", font=('Arial 10'))
        # Add Text "Department"
        canvas.create_text(125, 107, text="Department", fill="black", font=('Arial 10'))

        # Add Circle 2
        canvas.create_aa_circle(485, 45, 35, math.pi/2, fill="#d9d9d9")
        # Add Text 2
        canvas.create_text(485, 45, text="2", fill="black", font=('Arial 25'))
        # Add Text "Face Registration"
        canvas.create_text(485, 95, text="Face Registration", fill="black", font=('Arial 10'))

        # Add Circle 3
        canvas.create_aa_circle(845, 45, 35, math.pi/2, fill="#d9d9d9")
        # Add Text 3
        canvas.create_text(845, 45, text="3", fill="black", font=('Arial 25'))
        # Add Text "Completed"
        canvas.create_text(845, 95, text="Completed", fill="black", font=('Arial 10'))

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        vcmd50 = (self.register(self.main_app.limit_char50), '%P')
        vcmd6 = (self.register(self.main_app.limit_char6), '%P')

        # Add Frame Name Frame
        self.name_frame = customtkinter.CTkFrame(self, width=int(self.main_app.width/600*600), height=int(self.main_app.height/500*350), fg_color="#e6e6e6", corner_radius=0)
        self.name_frame.place(relx=0,rely=0.3)

        # Add Text "Username"
        username_label = customtkinter.CTkLabel(master=self.name_frame, text="User Name", font=("Arial", 20), text_color="black")
        username_label.place(relx=0.15, rely=0.057)

        # Add Text Box for Name                     
        self.username_entrybox = customtkinter.CTkEntry(master=self.name_frame, width=int(self.main_app.width/600*440) , height=int(self.main_app.height/500*40), text_color="black", font=("Arial", 20), validate="key", validatecommand=vcmd50)
        self.username_entrybox.place(relx=0.133, rely=0.157)

        # Add Text "Password"
        password_label = customtkinter.CTkLabel(master=self.name_frame, text="Password", font=("Arial", 20), text_color="black")
        password_label.place(relx=0.15, rely=0.286)

        # Add Text Box for Password
        self.password_entrybox= customtkinter.CTkEntry(master=self.name_frame, width=int(self.main_app.width/600*200) , height=int(self.main_app.height/500*40), text_color="black", font=("Arial", 20), validate="key", validatecommand=vcmd6)
        self.password_entrybox.place(relx=0.133, rely=0.386)

        # Add Text "Administrator"
        administrator_label = customtkinter.CTkLabel(master=self.name_frame, text="Administrator", font=("Arial", 20), text_color="black")
        administrator_label.place(relx=0.54, rely=0.286)

        def checkbox_event():
            print("checkbox toggled, current value:", check_var.get())

        check_var = tkinter.StringVar(value="on")

        self.administrator_checkbox = customtkinter.CTkCheckBox(
            master=self.name_frame,
            text="",
            width=int(self.main_app.width/600*40),
            height=int(self.main_app.height/500*40), 
            checkbox_width=int(self.main_app.width/600*40), 
            checkbox_height=int(self.main_app.height/500*40),  
            command=checkbox_event,
            variable=check_var, 
            onvalue="O", 
            offvalue="X",
            border_color="white",
            bg_color="white",
            fg_color="white",
            corner_radius=10,
            checkmark_color="black",
            hover_color="white",
        )

        self.administrator_checkbox.place(relx=0.558, rely=0.386)

        # Add Text "Department"
        department_label = customtkinter.CTkLabel(master=self.name_frame, text="Department", font=("Arial", 20), text_color="black")
        department_label.place(relx=0.15, rely=0.514)

        # Add ComboBox for Department
        self.department_entrybox = customtkinter.CTkEntry(master=self.name_frame, width=int(self.main_app.width/600*440) , height=int(self.main_app.height/500*40), text_color="black", font=("Arial", 20))
        self.department_entrybox.place(relx=0.133, rely=0.614)
        self.department_button = customtkinter.CTkButton(master=self.name_frame, text="▼", command=self.show_department_menus, text_color="black", font=("Arial",20), fg_color="white", width=int(self.main_app.width/600*40), height=int(self.main_app.height/500*40), cursor="hand2")
        self.department_button.place(relx=0.808, rely=0.614)

        # Add Button "Next"
        btn_next = customtkinter.CTkButton(master=self.name_frame, width=int(self.main_app.width/600*80), command= lambda: self.next_screen(7), text="Next", font=("Arial", 20), text_color="black", corner_radius=10, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
        btn_next.place(relx=0.733, rely=0.8)

        # Create the virtual keyboard
        self.message_frame1 = None
        # Initialize department Frame with Listbox and Scrollbar
        self.department_frame = tk.Frame(self, bg="#424242")
        self.department_listbox = tk.Listbox(self.department_frame, font=("Arial", 15), width=int(self.main_app.width/600*37), height=3)
        department_names = XFace_Database_Function.fetch_departmentname()
        for department in department_names:
            self.department_listbox.insert("end", department)
        self.department_listbox.bind("<Double-Button-1>", self.select_department)
        self.department_scrollbar = tk.Scrollbar(self.department_frame, orient="vertical", command=self.department_listbox.yview)
        self.department_listbox.config(yscrollcommand=self.department_scrollbar.set)

    #VirtualKeyboard Settings
    def entry_keyboard(self):
        self.keyboard_general = VirtualKeyboard(self)  
        self.keyboard_number = VirtualKeyboardNumber(self)

        self.keyboard_is_visible = False
        self.current_keyboard = None
        self.current_entry = None 

        self.bind_all("<Button-1>", self.global_click)

    def global_click(self, event):
        x, y = event.x_root, event.y_root

        kx, ky, kw, kh = self.keyboard_general.winfo_rootx(), self.keyboard_general.winfo_rooty(), self.keyboard_general.winfo_width(), self.keyboard_general.winfo_height()
        if kx <= x <= kx + kw and ky <= y <= ky + kh:
            return  
        
        kx, ky, kw, kh = self.keyboard_number.winfo_rootx(), self.keyboard_number.winfo_rooty(), self.keyboard_number.winfo_width(), self.keyboard_number.winfo_height()
        if kx <= x <= kx + kw and ky <= y <= ky + kh:
            return

        entry_clicked = None
        keyboard_to_use = None

        entries = {
            self.username_entrybox: self.keyboard_general,
            self.password_entrybox: self.keyboard_number
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
    
    # Value initialization
    def clear_entry_boxes_and_checkbox(self):
        self.username_entrybox.delete(0, tk.END)
        self.password_entrybox.delete(0, tk.END)
        self.department_entrybox.delete(0, tk.END)
        self.administrator_checkbox.deselect()

    # Check input values and set values and remove keybord settings and screen transitons
    def next_screen(self, index):
        username = self.username_entrybox.get()
        password = self.password_entrybox.get()
        department = self.department_entrybox.get()
        if username == "" or password == "" or department == "":
            self.message_frame1 = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*490), height=int(self.main_app.height/500*300), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame1.place(relx=0.13, rely=0.33)
            error_label = customtkinter.CTkLabel(master=self.message_frame1, text="Has not been entered!", font=("Arial", 20), text_color="black")
            error_label.place(relx=0.38, rely=0.3)
            btn_ok = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.message_frame1.destroy(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.42, rely=0.7)
        elif len(password) < 6:
            self.message_frame1 = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*490), height=int(self.main_app.height/500*300), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame1.place(relx=0.13, rely=0.33)
            error_label = customtkinter.CTkLabel(master=self.message_frame1, text="Password less then 6 digits!", font=("Arial", 20), text_color="black")
            error_label.place(relx=0.38, rely=0.3)
            btn_ok = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.message_frame1.destroy(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.42, rely=0.7)
        else:
            self.main_app.set_username(self.username_entrybox.get())
            self.main_app.set_password(self.password_entrybox.get())
            self.main_app.set_department(self.department_entrybox.get())
            self.main_app.set_administrator(self.administrator_checkbox.get())
            self.unbind_all("<Button-1>")
            self.main_app.show_next_screen(index)

    # Deletion of "photoget_register.png"files and frame and remove keybord settings and screen transitions 
    def back_screen(self):
        current_directory = os.getcwd()
        target_path = 'photoget_register/photoget_register.png'
        target_file_path = os.path.join(current_directory, target_path)
        if os.path.exists(target_file_path):
            os.remove(target_file_path)
        if self.message_frame1:
            self.message_frame1.destroy()
        self.unbind_all("<Button-1>")    
        loginuseradminflag = self.main_app.get_loginuseradminflag()
        
        if loginuseradminflag:
            self.main_app.show_next_screen(4)
        else:
            self.main_app.show_next_screen(5)

    # Enter the value selected in the list
    def select_department(self, event):
        selected_department = self.department_listbox.get(tk.ACTIVE)
        self.department_entrybox.delete(0, tk.END)
        self.department_entrybox.insert(0, selected_department)
        self.show_department_menus()

    # Showing and Hiding Lists
    def show_department_menus(self):
        if not self.department_frame.winfo_ismapped():
            self.department_listbox.delete(0, 'end')
            department_names = XFace_Database_Function.fetch_departmentname()
            for department in department_names:
                self.department_listbox.insert("end", department)
            self.department_frame.place(relx=0.133, rely=0.81)
            self.department_listbox.pack(side="left")
            self.department_scrollbar.pack(side="right", fill="y")
        else:
            self.department_frame.place_forget()