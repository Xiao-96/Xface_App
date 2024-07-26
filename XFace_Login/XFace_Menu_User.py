import tkinter as tk
import customtkinter
from datetime import datetime
import XFace_Database_Function

class Screen5(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

        # Get the current date and format it
        self.current_date = datetime.now().strftime("%Y / %m / %d")

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Menu Frame
        self.menu_frame = customtkinter.CTkFrame(self, width=self.main_app.width, height=self.main_app.height, fg_color="#424242", corner_radius=0)
        self.menu_frame.place(relx=0)

        # Add Date Label
        self.datetxt_label = customtkinter.CTkLabel(master=self.menu_frame, text=self.current_date, font=("Arial", 22), text_color="white")
        self.datetxt_label.place(relx=0.1, rely=0.035)

        # Add Logout Button
        logout_btn =customtkinter.CTkButton(master=self.menu_frame, text="Logout", command= lambda: self.next_screen(1), text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*90), height=int(self.main_app.height/500*40), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        logout_btn.place(relx=0.83, rely=0.03)

        # Add Edit Attendance Record Button
        edit_attendance_record_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(18), text="Edit Attendance Record", text_color="black", font=("Arial Bold", 20), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_attendance_record_btn.place(relx=0.52, rely=0.3)

        # Add Edit user Information Button
        edit_user_information_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(14), text="Edit user Information", text_color="black", font=("Arial Bold", 20), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_user_information_btn.place(relx=0.07, rely=0.3)

        # Add Excel Output Button
        edit_excel_output_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(20), text="Excel Output", text_color="black", font=("Arial Bold", 20), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_excel_output_btn.place(relx=0.07, rely=0.45)

    # Re-retrieve date and update label values
    def set_currentdate(self):
        self.current_date = datetime.now().strftime("%Y / %m / %d")
        self.datetxt_label.configure(text=self.current_date)
    
    # Screen transitons and set the value of Edit User Information
    def next_screen(self, index):
        userid = self.main_app.get_loginuserid()
        list = XFace_Database_Function.fetch_userinfo_departmentname_by_userid(userid)
        user_name, password, department_name=list[0]

        self.main_app.set_edit_user_id(userid)
        self.main_app.set_edit_user_name(user_name)
        self.main_app.set_edit_current_password(password)
        self.main_app.set_edit_department_name(department_name)
        self.main_app.show_next_screen(index)
