import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
from PIL import Image

class Screen7(tk.Frame):
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
        self.step_frame.pack()

        # Add "<" Button
        back_btn = customtkinter.CTkButton(self, width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), command= lambda: self.next_screen(6), text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        # Initial value
        self.screen_flag = True

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

        # Add Circle 3
        canvas.create_aa_circle(845, 45, 35, math.pi/2, fill="#d9d9d9")
        # Add Text 3
        canvas.create_text(845, 45, text="3", fill="black", font=('Arial 25'))
        # Add Text "Completed"
        canvas.create_text(845, 95, text="Completed", fill="black", font=('Arial 10'))

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        # Add Frame Image Frame
        self.image_frame = customtkinter.CTkFrame(self, width=int(self.main_app.width/600*600), height=int(self.main_app.height/500*350), fg_color="#e6e6e6", corner_radius=0)
        self.image_frame.pack()

        # Add Description Text 1
        txt1 = "Register the facial information to be used for authentication.\nSelect one of the methods and complete the registration."
        name_label = customtkinter.CTkLabel(master=self.image_frame, text=txt1, font=("Arial", 15), text_color="black", justify="center")
        name_label.place(relx=0.32,rely=0.114)

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        cam_path = os.path.join(images_folder, "camera.png")
        img_path = os.path.join(images_folder, "image.png")

        # Add Image
        self.cam_image = tk.PhotoImage(file=cam_path)
        self.img_image = tk.PhotoImage(file=img_path)

        # Camera Button
        cam_btn = tk.Button(self.image_frame, command= lambda: self.next_screen(10), image=self.cam_image, borderwidth=0, width=int(self.main_app.width/600*150), height=int(self.main_app.height/500*140), cursor="hand2")
        cam_btn.place(relx=0.1667, rely=0.257)

        # Camera Text    
        cam_label = customtkinter.CTkLabel(master=self.image_frame, text="Register with Camera", font=("Arial", 15), text_color="black", justify="center")
        cam_label.place(relx=0.223, rely=0.686)

        # Image Button
        img_btn = tk.Button(self.image_frame, command= lambda: self.next_screen(12), image=self.img_image, borderwidth=0, width=int(self.main_app.width/600*150), height=int(self.main_app.height/500*140), cursor="hand2")
        img_btn.place(relx=0.583, rely=0.257)

        # Image Text
        cam_label = customtkinter.CTkLabel(master=self.image_frame, text="Register with Photo", font=("Arial", 15), text_color="black", justify="center")
        cam_label.place(relx=0.65, rely=0.686)

    # Screen transitons
    def next_screen(self, index):
        if self.screen_flag:
            self.screen_flag = False
            self.main_app.show_next_screen(index)
    
    # Set screen_flag
    def set_screen_flag(self):
        self.screen_flag = True