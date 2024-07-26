import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
import XFace_Database_Function

class Screen2(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

        # Initial value
        self.afterid = None
        self.starttime_flag = True
        self.endtime_flag = True

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        self.step_frame = customtkinter.CTkFrame(self, width=self.main_app.width, height=self.main_app.height, fg_color="#e6e6e6", corner_radius=0)
        self.step_frame.pack()

        # Add Square
        self.error_square = customtkinter.CTkFrame(master=self.step_frame, width=int(self.main_app.width/600*500), height=int(self.main_app.height/500*400), fg_color="white", corner_radius=20, border_color="white", border_width=1)
        self.error_square.place(relx=0.08, rely=0.1)

        # Add "Hello," label
        hello_label = customtkinter.CTkLabel(master=self.step_frame, text="Hello,", font=("Arial", 30), text_color="black", bg_color="white")
        hello_label.place(relx=0.38,rely=0.38)

        # Add Username label
        self.username_txt_label = customtkinter.CTkLabel(master=self.step_frame, text="", font=("Arial", 30), text_color="black", bg_color="white", justify="center")
        self.username_txt_label.place(relx=0.47,rely=0.38)

        # Add Button "Attendance"
        btn_attendance = customtkinter.CTkButton(master=self.step_frame, width=int(self.main_app.width/600*120), command= lambda: self.attendance_starttime(), text="Attendance", font=("Arial", 25), text_color="black", corner_radius=10, fg_color="#d9d9d9", bg_color="white", border_width=0, hover_color="gray", cursor="hand2")
        btn_attendance.place(relx=0.133,rely=0.64)

        # Add Button "Clocking out"
        btn_clocking_out = customtkinter.CTkButton(master=self.step_frame, width=int(self.main_app.width/600*120), command= lambda: self.attendance_endtime(), text="Clocking out", font=("Arial", 25), text_color="black", corner_radius=10, fg_color="#d9d9d9", bg_color="white", border_width=0, hover_color="gray", cursor="hand2")
        btn_clocking_out.place(relx=0.4,rely=0.64)

        # Add Button "Menu"
        btn_menu = customtkinter.CTkButton(master=self.step_frame, width=int(self.main_app.width/600*120), command= lambda: self.next_screen(), text="Menu", font=("Arial", 25), text_color="black", corner_radius=10, fg_color="#d9d9d9", bg_color="white", border_width=0, hover_color="gray", cursor="hand2")
        btn_menu.place(relx=0.68,rely=0.64)

        # Add Description label
        description_label = customtkinter.CTkLabel(master=self.step_frame, text="If there is no operation, the system automatically logs out after 10 seconds.", font=("Arial", 20), text_color="black", bg_color="white")
        description_label.place(relx=0.15,rely=0.8)

    # 10-second count and screen transition
    def timecountup(self):
        if self.timecount < 10:
            self.timecount += 1
            self.afterid = self.after(1000,self.timecountup)
            print("success after:", self.afterid)
        else:
            self.back_screen()

    # New line in login user name
    def wrap_text(self, text, max_length):  
        lines = []
        for i in range(0, len(text), max_length):
            lines.append(text[i:i+max_length])
        return "\n".join(lines)

    # Obtaining a login user name and ID
    def get_username(self):
        self.user_id = self.main_app.get_loginuserid()
        self.username_txt = self.main_app.get_loginusername()
        wrapped_text = self.wrap_text(self.username_txt, 25)
        self.username_txt_label.configure(text=wrapped_text) 
    
    # Reset time counts
    def get_timecount(self):
        self.timecount = 0

    # Save attendance time to DB
    def attendance_starttime(self):
        if self.starttime_flag:
            self.starttime_flag = False
            XFace_Database_Function.save_work_start_time(self.user_id)
            XFace_Database_Function.save_enteringtime(self.user_id)
            self.back_screen()

    # Save leaving time to DB
    def attendance_endtime(self):
        if self.endtime_flag:
            self.endtime_flag = False
            XFace_Database_Function.save_work_end_time(self.user_id)
            self.back_screen()

    # Cancel after process and stop face recognition process and screen transitons
    def next_screen(self):
        self.after_cancel(self.afterid)
        self.main_app.facerecognition_stop()
        
        loginuseradminflag = self.main_app.get_loginuseradminflag()
        
        if loginuseradminflag:
            self.main_app.show_next_screen(4)
        else:
            self.main_app.show_next_screen(5)

    # Screen transitons
    def back_screen(self):
        if self.afterid:
            self.after_cancel(self.afterid)
        self.main_app.show_next_screen(1)

    # Set flag
    def set_time_flag(self):
        self.starttime_flag = True
        self.endtime_flag = True