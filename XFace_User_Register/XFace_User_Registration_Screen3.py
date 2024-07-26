import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox

import XFace_Database_Function

class Screen9(tk.Frame):
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

        # Add Frame Step Frame
        self.step_frame = customtkinter.CTkFrame(self, width=int(self.main_app.width/600*600), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=0)
        self.step_frame.pack()

        # Add "<" Button
        back_btn = customtkinter.CTkButton(self, width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), command= lambda: self.next_screen(), text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
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

        # Add Circle 2 Border
        canvas.create_aa_circle(485, 45, 38, math.pi/2, fill="#288fc8")
        # Add Circle 2
        canvas.create_aa_circle(485, 45, 35, math.pi/2, fill="#d9d9d9")
        # Add Text 2
        canvas.create_text(485, 45, text="2", fill="black", font=('Arial 25'))
        # Add Text "Face Registration"
        canvas.create_text(485, 95, text="Face Registration", fill="black", font=('Arial 10'))

        # Add Circle 3 Border
        canvas.create_aa_circle(845, 45, 38, math.pi/2, fill="#288fc8")
        # Add Circle 3
        canvas.create_aa_circle(845, 45, 35, math.pi/2, fill="#d9d9d9")
        # Add Text 3
        canvas.create_text(845, 45, text="3", fill="black", font=('Arial 25'))
        # Add Text "Completed"
        canvas.create_text(845, 95, text="Completed", fill="black", font=('Arial 10'))

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        # Add Frame Step Frame 2
        self.step_frame2 = customtkinter.CTkFrame(self, width=int(self.main_app.width/600*600), height=int(self.main_app.height/500*400), fg_color="#e6e6e6", corner_radius=0)
        self.step_frame2.pack()

        # Create canvas
        canvas2 = customtkinter.CTkCanvas(
            self.step_frame2,
            width = int(self.main_app.width/600*600),
            height = int(self.main_app.height/500*400),
            bg = "#e6e6e6",
            highlightthickness = 0,
            bd = 0
        )
        canvas2.place(relx=0.05, rely=0.24)

        # Add Text "description1"
        description1_label = customtkinter.CTkLabel(master=self.step_frame2, text="Register a user with the following information.", font=("Arial", 15), text_color="black")
        description1_label.place(relx=0.35, rely=0.04)

        # Add Text "description2"
        description2_label = customtkinter.CTkLabel(master=self.step_frame2, text="If you are satisfied, press Save.", font=("Arial", 15), text_color="black")
        description2_label.place(relx=0.38, rely=0.1)

        # Add Text "Name"     
        name_label = customtkinter.CTkLabel(master=self.step_frame2, text="Name:", font=("Arial Bold", 22), text_color="black")
        name_label.place(relx=0.05, rely=0.2125)

        # Add Name Line
        canvas2.create_line(50, 16, 600, 16, width=1)

        # Add Name Label                                   
        self.username_txt_label = customtkinter.CTkLabel(master=self.step_frame2, width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*15), text="", font=("Arial", 15), text_color="black", justify="center")
        self.username_txt_label.place(relx=0.195, rely=0.2125)

        # Add Text "User ID"
        userid_label = customtkinter.CTkLabel(master=self.step_frame2, text="User ID:", font=("Arial Bold", 22), text_color="black")
        userid_label.place(relx=0.05, rely=0.325)

        # Add User ID Line
        canvas2.create_line(50, 63, 600, 63, width=1)

        # Add Userid Label                                    
        self.userid_txt_label = customtkinter.CTkLabel(master=self.step_frame2, text="", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*15), font=("Arial", 15), text_color="black", justify="center")
        self.userid_txt_label.place(relx=0.217, rely=0.325)

        # Add Text "Password"
        password_label = customtkinter.CTkLabel(master=self.step_frame2, text="Password:", font=("Arial Bold", 22), text_color="black")
        password_label.place(relx=0.05, rely=0.4375)
        # Add Pssword Line
        canvas2.create_line(50, 112, 600, 112, width=1)

        # Add Password Label                                      
        self.password_txt_label = customtkinter.CTkLabel(master=self.step_frame2, width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*15), text="", font=("Arial", 15), text_color="black", justify="center")
        self.password_txt_label.place(relx=0.2717, rely=0.4375)

        # Add Text "Department"
        department_label = customtkinter.CTkLabel(master=self.step_frame2, text="Department:", font=("Arial Bold", 22), text_color="black")
        department_label.place(relx=0.05, rely=0.55)

        # Add Department Line
        canvas2.create_line(50, 159, 600, 159, width=1)

        # Add department Label
        self.department_txt_label = customtkinter.CTkLabel(master=self.step_frame2, width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*15), text="", font=("Arial", 15), text_color="black", justify="center")
        self.department_txt_label.place(relx=0.3083, rely=0.55)

        # Add Text "Administrator"
        adminstrator_label = customtkinter.CTkLabel(master=self.step_frame2, text="Administrator:", font=("Arial Bold", 22), text_color="black")
        adminstrator_label.place(relx=0.05, rely=0.675)

        # Add Administrator Line
        canvas2.create_line(50, 210, 600, 210, width=1)

        # Add Administrator Label
        self.administrator_check_label = customtkinter.CTkLabel(master=self.step_frame2, width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*15), text="", font=("Arial", 15), text_color="black", justify="center")
        self.administrator_check_label.place(relx=0.3533, rely=0.675)

        # Add Button "Save"
        btn_save = customtkinter.CTkButton(master=self.step_frame2, command=lambda: self.save(), width=int(self.main_app.width/600*80), text="Save", font=("Arial", 20), text_color="black", corner_radius=10, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
        btn_save.place(relx=0.75, rely=0.725)

    # Save encoding data to pickle file and input values to DB
    def save(self):
        if self.flag:
            username = self.username_txt_label.cget('text')
            password = self.password_txt_label.cget('text')
            department = self.department_txt_label.cget('text')
            admin_text = self.administrator_check_label.cget('text')
            userid = self.userid_txt
            if admin_text == 'True':
                is_admin = 1
            elif admin_text == 'False': 
                is_admin = 0
            check_encodings_flag = self.main_app.check_encodings_main("register")
            if check_encodings_flag:
                face_photo = self.main_app.get_registerfacephoto(userid,username,is_admin,"register")
                XFace_Database_Function.insert_userinfo(username, password, department, is_admin, face_photo)
                self.message_frame = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
                self.message_frame.place(relx=0.25, rely=0.33)
                success_label = customtkinter.CTkLabel(master=self.message_frame, text="Updated successfully.", font=("Arial", 20), text_color="black")
                success_label.place(relx=0.25, rely=0.3)
                btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.destroy_message_frame(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                btn_ok.place(relx=0.34, rely=0.7)
                self.flag = False 
            else:
                self.message_frame = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
                self.message_frame.place(relx=0.25, rely=0.33)
                success_label = customtkinter.CTkLabel(master=self.message_frame, text="Not get encodedata. Please again", font=("Arial", 20), text_color="black")
                success_label.place(relx=0.17, rely=0.3)
                btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.destroy_message_frame_noencoding(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                btn_ok.place(relx=0.34, rely=0.7)
                self.flag = False 

    # Set flag and Deletion of "photoget_register.png"files and frame and screen transitions 
    def destroy_message_frame(self):
        self.flag = True
        self.message_frame.destroy()
        current_directory = os.getcwd()
        target_path = 'photoget_register/photoget_register.png'
        target_file_path = os.path.join(current_directory, target_path)
        if os.path.exists(target_file_path):
            os.remove(target_file_path)

        loginuseradminflag = self.main_app.get_loginuseradminflag()
        
        if loginuseradminflag:
            self.main_app.show_next_screen(4)
        else:
            self.main_app.show_next_screen(5)

    # Screen transitions 
    def next_screen(self):
        if self.flag:
            self.main_app.show_next_screen(7)
    
    # Setb flag and Deletion frame
    def destroy_message_frame_noencoding(self):
        self.flag = True
        self.message_frame.destroy()

    # Retrieve the entered value
    def get_username(self): 
        self.username_txt = self.main_app.get_username()
        self.username_txt_label.configure(text=self.username_txt)

    def get_password(self):
        self.password_txt = self.main_app.get_password()
        self.password_txt_label.configure(text=self.password_txt)

    def get_department(self):
        self.department_txt = self.main_app.get_department()
        self.department_txt_label.configure(text=self.department_txt)

    def get_userid(self):
        self.userid_txt = XFace_Database_Function.fetch_next_user_id()
        self.userid_txt_label.configure(text=self.userid_txt)

    def get_administrator(self):
        self.administrator_check_txt = self.main_app.get_administrator()
        if self.administrator_check_txt == 'O':
            self.administrator_check = 'True'
        elif self.administrator_check_txt == 'X':
            self.administrator_check = 'False'
        self.administrator_check_label.configure(text=self.administrator_check)

    # Display acquired images on screen
    def get_facephoto(self):
        profile_path = self.main_app.get_photopath("register")
        profile_image = Image.open(profile_path)
        profile_image = profile_image.resize((150, 150), Image.Resampling.LANCZOS)
        profile_photo = ImageTk.PhotoImage(profile_image)
        self.profile_label = tk.Label(self.step_frame2, image=profile_photo, bg="#e6e6e6")
        self.profile_label.image = profile_photo
        self.profile_label.place(relx=0.743, rely=0.275)
