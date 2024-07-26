import tkinter as tk
import customtkinter
import math
import os
from PIL import Image, ImageTk
import CameraRspiPicam
import cv2
import numpy as np

class Screen21(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

        # Initialize retake_button and accept_button
        self.retake_button = None
        self.accept_button = None

        # Initial value
        self.after_id = None
        self.flag = True

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        self.step_frame = customtkinter.CTkFrame(self, width=self.main_app.width, height=self.main_app.height, fg_color="#e6e6e6", corner_radius=0)
        self.step_frame.pack()

        # Create Canvas
        self.canvas = customtkinter.CTkCanvas(
                    self.step_frame,
                    width = self.main_app.width,
                    height = self.main_app.height,
                    bg = "#e6e6e6",
                    highlightthickness = 0,
                    bd = 0
                )
        self.canvas.place(relx=0, rely=0)

        self.canvas.create_aa_circle(50, 300, 30, math.pi/2, fill="black")
        self.canvas.create_aa_circle(50, 300, 29, math.pi/2, fill="white")
        self.canvas.create_aa_circle(50, 300, 25, math.pi/2, fill="black")
        camera_shoot = self.canvas.create_aa_circle(50, 300, 24, math.pi/2, fill="white")

        self.canvas.tag_bind(camera_shoot, "<Button-1>", self.camera_shoot_click_event)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=self.step_frame, command=lambda: self.next_screen(14), width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        self.photo_shoot_canvas = tk.Canvas(master=self.step_frame, width=640, height=480)
        self.photo_shoot_canvas.place(relx=0.3, rely=0.1)
 
    # Start the video process
    def photo_update_start(self):
        width, height = 640, 480
        try:
            self.video_process = CameraRspiPicam.capture_video()
            self.frame_size = width * height * 3 // 2  # YUV420p frame size
            self.update()
        except Exception as e:
            print(e)
    
    # Start of after process
    def update(self):
        ret, frame = self.get_frame()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.photo_shoot_canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.after_id = self.photo_shoot_canvas.after(15, self.update)
        print("edit after:", self.after_id)

    # Camera image
    def get_frame(self):
        width, height = 640, 480
        raw_frame = self.video_process.stdout.read(self.frame_size)
        if not raw_frame:
            return (False, None)
        # Convert raw YUV420p data to a numpy array
        yuv = np.frombuffer(raw_frame, dtype=np.uint8).reshape((height + height // 2, width))
        # Convert YUV to RGB
        frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB_I420)
        return (True, frame)
    
    # Cancel after process and stop the video process and deleting button and set flag and screen transitons
    def next_screen(self, index):
        # Cancel after process
        if self.after_id:
            self.photo_shoot_canvas.after_cancel(self.after_id)
        # Stop the video process
        if hasattr(self, 'video_process') and self.video_process:
            self.video_process.terminate()
            self.video_process = None
        # Deleting button
        if self.retake_button:
            self.retake_button.destroy()
        if self.accept_button:
            self.accept_button.destroy()
        # Set flag
        self.flag = True
        # Screen transitons
        self.main_app.show_next_screen(index)

    # Camera shutter release
    def camera_shoot_click_event(self, event):
        if self.flag:
            self.camera_shoot_click()
            self.flag = False

    # Cancel after process and stop the video process and creating Retake and OK buttons
    def camera_shoot_click(self):
        ret, frame = self.get_frame()
        # Cancel after process
        if self.after_id:
            self.photo_shoot_canvas.after_cancel(self.after_id)
        # Stop the video process
        if hasattr(self, 'video_process') and self.video_process:
            self.video_process.terminate()
            self.video_process = None 
        if ret:
            photo_shoot_confirm_path = self.main_app.photo_get("edit")
            cv2.imwrite(photo_shoot_confirm_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            # Create two additional buttons
            self.retake_button = customtkinter.CTkButton(master=self.step_frame, text="Retake", command=lambda: self.retake_click(), font=("Arial", 20), text_color="black", width=int(self.main_app.width/600*120), height=int(self.main_app.height/500*60), fg_color="#D9D9D9", bg_color="#ffffff", corner_radius=10, cursor="hand2")
            self.retake_button.place(relx=0.2167, rely=0.85)  
            self.accept_button = customtkinter.CTkButton(master=self.step_frame, command=lambda: self.next_screen(14), text="OK", font=("Arial", 20), text_color="black", width=int(self.main_app.width/600*120), height=int(self.main_app.height/500*60), fg_color="#D9D9D9", bg_color="#ffffff", corner_radius=10, cursor="hand2")
            self.accept_button.place(relx=0.7833, rely=0.85)

    # Retaking of images
    def retake_click(self):
        self.photo_shoot_canvas.delete("all")
        self.photo_update_start()
        self.flag = True
        if self.retake_button:
            self.retake_button.destroy()
        if self.accept_button:
            self.accept_button.destroy()
