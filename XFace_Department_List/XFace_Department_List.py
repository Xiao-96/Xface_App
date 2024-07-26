import tkinter as tk
from tkinter import messagebox
import customtkinter
import os
import XFace_Database_Function
from PIL import Image

class Screen15(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

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

        # create Button
        create_btn = customtkinter.CTkButton(master=self.name_frame,  command= lambda: self.create_screen(16), text="Create", text_color="black", hover_color="gray", font=("Arial", 20), border_width=0, width=int(self.main_app.width/600*200), height=int(self.main_app.height/500*30), fg_color="white", corner_radius=10, cursor="hand2")
        create_btn.place(relx=0.2, rely=0.05)

        # Add School Name Label
        department_label = customtkinter.CTkLabel(master=self.name_frame, text="Department", text_color="black", font=("Arial", 20), fg_color="transparent")
        department_label.place(relx=0.2, rely=0.12)

        #Add Entrybox for Department
        self.department_entrybox = customtkinter.CTkEntry(master=self.name_frame, width=int(self.main_app.width/600*200), height=int(self.main_app.height/500*30), text_color="black", font=("Arial", 15))
        self.department_entrybox.place(relx=0.2, rely=0.17)
        self.department_button = customtkinter.CTkButton(master=self.name_frame, text="▼", command=self.show_department_menus, text_color="black", font=("Arial",15), fg_color="white", width=int(self.main_app.width/600*35), height=int(self.main_app.height/500*30), cursor="hand2")
        self.department_button.place(relx=0.78, rely=0.17)        

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        search_path = os.path.join(images_folder, "search.png")

        # Add Image
        search_pil_image = Image.open(search_path)
        search_image = customtkinter.CTkImage(search_pil_image)

        # Search Button
        self.search_btn = customtkinter.CTkButton(master=self.name_frame, command=self.search, image=search_image, text="Search", text_color="black", hover_color="gray", font=("Arial", 20), border_width=0, width=int(self.main_app.width/600*110), height=int(self.main_app.height/500*30), fg_color="white", cursor="hand2")
        self.search_btn.place(relx=0.51, rely=0.27)

        # Initialize department Frame with Listbox and Scrollbar
        self.department_frame = tk.Frame(self, bg="#424242")
        self.department_listbox = tk.Listbox(self.department_frame, font=("Arial", 15), width=int(self.main_app.width/600*15), height=3)
        self.department_listbox.insert("end", "All")
        department_names = XFace_Database_Function.fetch_departmentname()
        for department in department_names:
            self.department_listbox.insert("end", department)
        self.department_listbox.bind("<Double-Button-1>", self.select_department)
        self.department_scrollbar = tk.Scrollbar(self.department_frame, orient="vertical", command=self.department_listbox.yview)
        self.department_listbox.config(yscrollcommand=self.department_scrollbar.set)

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        self.info_frame = customtkinter.CTkScrollableFrame(master=self, width=int(self.main_app.width/600*298), height=int(self.main_app.height/500*500), fg_color="#d9d9d9", corner_radius=0)
        self.info_frame.place(relx=0.481)

        self.department_details = XFace_Database_Function.fetch_departmentname() 
        self.build_department_frames(self.department_details)

    # Reset frame
    def build_department_frames(self, departments):
        self.clear_department_frames()
        if len(departments) == 1:
            self.add_department_frame(self.info_frame, departments, 1)
        else:
            for index, department in enumerate(departments):
                self.add_department_frame(self.info_frame, department, index)

    # Deleting frames
    def clear_department_frames(self):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

    # Retrieve department to display from DB and create frames
    def search(self):
        departmentname = self.department_entrybox.get()
        if departmentname == '' or departmentname == 'All':
            departments = XFace_Database_Function.fetch_departmentname()
        else:
            departments = XFace_Database_Function.fetch_departmentname_by_departmentname(departmentname)
        self.build_department_frames(departments)

    # Create frames
    def add_department_frame(self, parent_frame, department_name, tag):
        department_frame = customtkinter.CTkFrame(master=parent_frame, width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*70), fg_color="white", corner_radius=10, border_width=0, border_color="#5cb6f8")
        department_frame.bind('<Button-1>', lambda event: self.toggle_border(department_frame))
        department_frame.tag = tag
        department_frame.pack(padx=10, pady=5)

        canvas = customtkinter.CTkCanvas(
            department_frame,
            width=int(self.main_app.width/600*7),
            height=int(self.main_app.height/500*65),
            bg="#fce467",  # Example background color
            highlightthickness=0,
            bd=0
        )
        canvas.bind('<Button-1>', lambda event: self.toggle_border(department_frame))
        canvas.place(x=15, y=2)

        name_label = customtkinter.CTkLabel(master=department_frame, text=department_name, text_color="black", font=("Arial", 20), fg_color="transparent")
        name_label.bind('<Button-1>', lambda event: self.toggle_border(department_frame))
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
            if hasattr(self, 'detail_frame') and self.detail_frame.winfo_exists():
                self.detail_frame.destroy()

            detail_frame = customtkinter.CTkFrame(master=self.name_frame, width=int(self.main_app.width/600*260), height=int(self.main_app.height/500*310), fg_color="white", corner_radius=10, border_width=0)
            detail_frame.place(relx=0.05, rely=0.36)
            name = kwargs.get('b', "")
            
            departmentname_detail_label = customtkinter.CTkLabel(master=detail_frame, justify="center", width=int(self.main_app.width/600*260), text=name, text_color="black", font=("Arial", 25), fg_color="transparent")
            departmentname_detail_label.place(relx=0, rely=0.6)

            edit_btn = customtkinter.CTkButton(master=detail_frame, command=lambda: self.next_screen(name, 17), text="Edit", text_color="black", hover_color="grey", font=("Arial", 20), border_width=0, width=int(self.main_app.width/600*90), height=int(self.main_app.height/500*30), fg_color="#d9d9d9", cursor="hand2")
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

    # Delete data from DB
    def delete_data(self,name):
        if isinstance(name, list):
            name = name[0]
        XFace_Database_Function.delete_department(name)
        self.flag = True
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
        departments = XFace_Database_Function.fetch_departmentname() 
        self.build_department_frames(departments)
    
    # Get the value of the department to be edited and value initialization and screen transitons
    def next_screen(self, name, index):
        if isinstance(name, list):
            name = name[0]
        department_info = XFace_Database_Function.fetch_department(name)
        self.main_app.set_department_name(department_info[0])
        self.main_app.set_start_time(department_info[1])
        self.main_app.set_end_time(department_info[2])
        self.main_app.set_rest_time(department_info[3])
        self.main_app.set_over_time(department_info[4])
        self.department_entrybox.delete(0, tk.END)
        self.toggle_detail_frame(0)
        self.main_app.show_next_screen(index)
        
    # Value initialization and screen transitons
    def create_screen(self, index):
        self.department_entrybox.delete(0, tk.END)
        self.toggle_detail_frame(0)
        self.main_app.show_next_screen(index)

    # Value initialization and screen transitons
    def back_screen(self):
        self.department_entrybox.delete(0, tk.END)
        self.toggle_detail_frame(0)
        loginuseradminflag = self.main_app.get_loginuseradminflag()
        
        if loginuseradminflag:
            self.main_app.show_next_screen(4)
        else:
            self.main_app.show_next_screen(5)

    # Enter the value selected in the list
    def select_department(self, event):
        self.selected_department = self.department_listbox.get(tk.ACTIVE)
        self.department_entrybox.delete(0, tk.END)
        self.department_entrybox.insert(0, self.selected_department)
        self.show_department_menus()

    # Showing and Hiding Lists
    def show_department_menus(self):
        if not self.department_frame.winfo_ismapped():
            self.department_listbox.delete(0, 'end')
            department_names = XFace_Database_Function.fetch_departmentname()
            self.department_listbox.insert("end", "All")
            for department in department_names:
                self.department_listbox.insert("end", department)
            self.department_frame.place(relx=0.098, rely=0.23)
            self.department_listbox.pack(side="left")
            self.department_scrollbar.pack(side="right", fill="y")
        else:
            self.department_frame.place_forget()