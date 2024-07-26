import tkinter as tk
import customtkinter
import math
import os
from PIL import Image, ImageTk
from customtkinter import CTkImage
import XFace_Database_Function
from io import BytesIO
from Virtual_Keyboard import VirtualKeyboard
from tkinter import messagebox

class Screen13(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)
        self.portrait_image = None

        # Toggle Confirm
        self.confirm = 0
        
        # Initial value of flag
        self.flag = True
        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Name Frame
        self.name_frame = customtkinter.CTkFrame(master=self, width=int(self.main_app.width/600*290), height=int(self.main_app.height/500*500), fg_color="#e6e6e6", corner_radius=0)
        self.name_frame.place(relx=0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(self, command= lambda: self.back_screen(), width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        # Add Name Label
        name_label = customtkinter.CTkLabel(master=self.name_frame, text="User Name", text_color="black", font=("Arial", 20), fg_color="transparent")
        name_label.place(relx=0.2, rely=0.01)

        # Add Text Entry for Username                                                                                                                                                                          
        vcmd50 = (self.register(self.main_app.limit_char50), '%P')
        self.username_entrybox = customtkinter.CTkEntry(master=self.name_frame, width=int(self.main_app.width/600*200) , height=int(self.main_app.height/500*30), text_color="black", font=("Arial", 15), validate="key", validatecommand=vcmd50)
        self.username_entrybox.place(relx=0.2, rely=0.06)
        # Add School Name Label
        department_label = customtkinter.CTkLabel(master=self.name_frame, text="Department", text_color="black", font=("Arial", 20), fg_color="transparent")
        department_label.place(relx=0.2, rely=0.12)

        # Add ComboBox for Department
        self.department_entrybox = customtkinter.CTkEntry(master=self.name_frame, width=int(self.main_app.width/600*200), height=int(self.main_app.height/500*30), text_color="black", font=("Arial", 15))
        self.department_entrybox.place(relx=0.2, rely=0.17)
        self.department_button = customtkinter.CTkButton(master=self.name_frame, text="▼", command=self.show_department_menus, text_color="black", font=("Arial",15), fg_color="white", width=int(self.main_app.width/600*35), height=int(self.main_app.height/500*30), cursor="hand2")
        self.department_button.place(relx=0.78, rely=0.17)

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        search_path = os.path.join(images_folder, "search.png")

        # Add Image
        # Load search image using PIL and then create CTkImage
        pil_image = Image.open(search_path)
        search_image = CTkImage(pil_image)

        # Search Button
        self.search_btn = customtkinter.CTkButton(master=self.name_frame, command=self.search, image=search_image, text="Search", text_color="black", font=("Arial", 20), border_width=0, width=int(self.main_app.width/600*110), height=30, fg_color="white", hover_color="gray", cursor="hand2")
        self.search_btn.place(relx=0.51, rely=0.27)

        # Initialize department Frame with Listbox and Scrollbar
        self.department_frame = tk.Frame(self, bg="#424242")
        self.department_listbox = tk.Listbox(self.department_frame, font=("Arial", 15), width=int(self.main_app.width/600*15), height=3)
        self.department_listbox.insert("end", "All")
        department_names = XFace_Database_Function.fetch_departmentname_all()
        for department in department_names:
            self.department_listbox.insert("end", department)
        self.department_listbox.bind("<Double-Button-1>", self.select_department)
        self.department_scrollbar = tk.Scrollbar(self.department_frame, orient="vertical", command=self.department_listbox.yview)
        self.department_listbox.config(yscrollcommand=self.department_scrollbar.set)

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        # Add Info Frame
        self.info_frame = customtkinter.CTkScrollableFrame(master=self, width=int(self.main_app.width/600*298), height=int(self.main_app.height/500*500), fg_color="#d9d9d9", corner_radius=0)
        self.info_frame.place(relx=0.481)

        self.user_details = XFace_Database_Function.fetch_usernames() 
        self.build_user_frames(self.user_details)

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
            self.username_entrybox: self.keyboard_general
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

    # Reset frame
    def build_user_frames(self, users):
        self.clear_user_frames()
        for index, user in enumerate(users):
            self.add_user_frame(self.info_frame, user, index)

    # Deleting frames
    def clear_user_frames(self):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

    # Retrieve users to display from DB and create frames
    def search(self):
        departmentname = self.department_entrybox.get()
        username = self.username_entrybox.get()
        if username == '':
            if departmentname == '' or departmentname == 'All':  
                users = XFace_Database_Function.fetch_usernames()
            else:
                users = XFace_Database_Function.fetch_usernames_by_departmentname(departmentname)
        else:
            if departmentname == '' or departmentname == 'All':  
                users = XFace_Database_Function.fetch_username_by_username(username)
            else:
                users = XFace_Database_Function.fetch_usernames_by_departmentname_username(departmentname,username)
        
        self.build_user_frames(users)

    # Create frames
    def add_user_frame(self, parent_frame, user_name, tag):
        user_frame = customtkinter.CTkFrame(master=parent_frame, width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*70), fg_color="white", corner_radius=10, border_width=0, border_color="#5cb6f8")
        user_frame.bind('<Button-1>', lambda event: self.toggle_border(user_frame))
        user_frame.tag = tag
        user_frame.pack(padx=10, pady=5)

        canvas = customtkinter.CTkCanvas(
            user_frame,
            width=int(self.main_app.width/600*7),
            height=int(self.main_app.height/500*65),
            bg="#fce467",  # Example background color
            highlightthickness=0,
            bd=0
        )
        canvas.bind('<Button-1>', lambda event: self.toggle_border(user_frame))
        canvas.place(x=15, y=2)

        name_label = customtkinter.CTkLabel(master=user_frame, text=user_name, text_color="black", font=("Arial", 20), fg_color="transparent")
        name_label.bind('<Button-1>', lambda event: self.toggle_border(user_frame))
        name_label.place(x=50, y=10)

    # Toggle setting
    def toggle_border(self, frame):
        if frame._border_width == 0:
            for child in frame.master.winfo_children():
                if isinstance(child, customtkinter.CTkFrame):
                    child.configure(border_width=0)
            frame.configure(border_width=2)
            color = frame.winfo_children()[0].cget("bg")
            name = frame.winfo_children()[1].cget("text")
            index = frame.tag
            self.toggle_detail_frame(1, a=color, b=name, c=index)
        else:
            frame.configure(border_width=0)
            self.toggle_detail_frame(0)

    def toggle_detail_frame(self, toggle, *args, **kwargs):
        if toggle == 1:
            index = kwargs['c']
            if hasattr(self, 'detail_frame') and self.detail_frame.winfo_exists():
                self.detail_frame.destroy()

            detail_frame = customtkinter.CTkFrame(master=self.name_frame, width=int(self.main_app.width/600*260), height=int(self.main_app.height/500*310), fg_color="white", corner_radius=10, border_width=0)
            detail_frame.place(relx=0.05, rely=0.36)
            border_color = kwargs.get('a', "white")
            name = kwargs.get('b', "")
            photo_data = XFace_Database_Function.fetch_facephoto_by_userid(name)

            if photo_data and photo_data[0]:
                portrait_image = Image.open(BytesIO(photo_data[0]))
                resized_image = portrait_image.resize((200,200), Image.Resampling.LANCZOS)
                self.portrait_image = ImageTk.PhotoImage(resized_image)
            else:
                not_found_image = Image.open('XFace_User_List/images/loading.png')  
                resized_image = not_found_image.resize((120,120), Image.Resampling.LANCZOS)
                self.portrait_image = ImageTk.PhotoImage(resized_image)
            
            canvas_detail = customtkinter.CTkCanvas(detail_frame, width=int(self.main_app.width/600*175), height=int(self.main_app.height/500*175), bg="white", highlightthickness=0, bd=0)
            canvas_detail.create_aa_circle(150, 89, 86, math.pi/2, fill=border_color)
            canvas_detail.create_image(150, 87, image=self.portrait_image, anchor=tk.CENTER)
            canvas_detail.place(relx=0.16, rely=0.01)

            username_detail_label = customtkinter.CTkLabel(master=detail_frame, justify="center", width=int(self.main_app.width/600*260), text=name, text_color="black", font=("Arial", 25), fg_color="transparent")
            username_detail_label.place(relx=0, rely=0.6)

            edit_btn = customtkinter.CTkButton(master=detail_frame, command=lambda: self.next_screen(name, 14), text="Edit", text_color="black", hover_color="grey", font=("Arial", 20), border_width=0, width=int(self.main_app.width/600*90), height=int(self.main_app.height/500*30), fg_color="#d9d9d9", cursor="hand2")
            edit_btn.place(relx=0.1, rely=0.85)

            delete_btn = customtkinter.CTkButton(master=detail_frame, command=lambda: self.confirm_delete(name), text="Delete", text_color="black", hover_color="grey", font=("Arial", 20), border_width=0, width=int(self.main_app.width/600*90), height=int(self.main_app.height/500*30), fg_color="#d9d9d9", cursor="hand2")
            delete_btn.place(relx=0.55, rely=0.85)

            self.detail_frame = detail_frame
        else:
            if hasattr(self, 'detail_frame') and self.detail_frame.winfo_exists():
                self.detail_frame.destroy()

    # Creating a deletion confirmation frame
    def confirm_delete(self, name):
        if self.flag:
            self.message_frame1 = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*510), height=int(self.main_app.height/500*250), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame1.place(relx=0.1, rely=0.25)

            ask_label = customtkinter.CTkLabel(master=self.message_frame1, text="Are you sure you want to Delete this data?", font=("Arial", 20), text_color="black")
            ask_label.place(relx=0.25, rely=0.35)

            # Add Button "ok"
            btn_ok = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.delete_data(name), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.7, rely=0.75)

            # Add Button "Cancel"
            btn_Cancel = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.cancel(), text="Cancel", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_Cancel.place(relx=0.1, rely=0.75)
            
            self.flag = False

    # Set flags and remove frame
    def cancel(self):
        self.flag = True
        self.message_frame1.destroy()

    # Delete data from pickle files and DB 
    def delete_data(self,name):
        if isinstance(name, list):
            name = name[0]
        XFace_Database_Function.delete_user_by_userid(name)
        self.flag = True
        self.main_app.deletepickle_main_app(name)
        self.message_frame = customtkinter.CTkFrame(master=self.message_frame1,width=int(self.main_app.width/600*450), height=int(self.main_app.height/500*200), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
        self.message_frame.place(relx=0.07, rely=0.15)
        success_label = customtkinter.CTkLabel(master=self.message_frame, text="This data has been deleted successfully.", font=("Arial", 20), text_color="black")
        success_label.place(relx=0.3, rely=0.3)
        btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.delete_success(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
        btn_ok.place(relx=0.42, rely=0.7)
    
    # Re-create frame
    def delete_success(self):
        self.message_frame1.destroy()
        self.toggle_detail_frame(0)
        users= XFace_Database_Function.fetch_usernames()
        self.build_user_frames(users)

    # Get the value of the user to be edited and value initialization and screen transitons
    def next_screen(self, name, index):
        self.unbind_all("<Button-1>")
        self.username_entrybox.delete(0, tk.END)
        self.department_entrybox.delete(0, tk.END)
        self.toggle_detail_frame(0)
        list = XFace_Database_Function.fetch_userinfo_departmentname_by_userid(name)
        user_name, password, department_name=list[0]

        self.main_app.set_edit_user_id(name)
        self.main_app.set_edit_user_name(user_name)
        self.main_app.set_edit_current_password(password)
        self.main_app.set_edit_department_name(department_name)
        self.main_app.show_next_screen(index)
        
    # Value initialization and screen transitons
    def back_screen(self):
        self.username_entrybox.delete(0, tk.END)
        self.department_entrybox.delete(0, tk.END)
        self.unbind_all("<Button-1>")
        self.toggle_detail_frame(0)
        self.main_app.show_next_screen(4)

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
            department_names = XFace_Database_Function.fetch_departmentname_all()
            self.department_listbox.insert("end", "All")
            for department in department_names:
                self.department_listbox.insert("end", department)
            self.department_frame.place(relx=0.098, rely=0.23)
            self.department_listbox.pack(side="left")
            self.department_scrollbar.pack(side="right", fill="y")
        else:
            self.department_frame.place_forget()
