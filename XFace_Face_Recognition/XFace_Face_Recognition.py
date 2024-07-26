import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import cv2
import datetime
import time
import numpy as np
import CameraRspiPicam
import XFace_Database_Function
import os
from threading import Timer

class Screen1(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

        # Initial value
        self.update_counter = 0
        self.save_interval = 10  # Save every 10 updates
        self.after_id = None
        self.after_flag = True
        self.screen_flag = True

        # Get CameraLog path
        cameralogpath = self.main_app.get_cameralogpath()
        self.cap_path = f"{cameralogpath}/cap.png"
        self.detector = cv2.QRCodeDetector()
        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        self.step_frame = customtkinter.CTkFrame(self, width=self.main_app.width, height=self.main_app.height, fg_color="#e6e6e6", corner_radius=0)
        self.step_frame.pack()

        # Add Camera Display Label
        self.photo_label = tk.Label(master=self.step_frame, width=640, height=480)
        self.photo_label.place(relx=0.3,rely=0.1)

        # Add Button "pass"
        btn_pass = customtkinter.CTkButton(master=self.step_frame, width=int(self.main_app.width/600*80), command= lambda: self.next_screen(3), text="Pass", font=("Arial", 20), text_color="black", corner_radius=10, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
        btn_pass.place(relx=0.02, rely=0.9)

    # Set flag and screen transitons
    def next_screen(self, index):
        self.reset_screen()
        time.sleep(1)
        self.after_flag = True
        self.screen_flag = True
        self.main_app.show_next_screen(index)

    # Cancel after process and stop the video process and black out cap.png
    def reset_screen(self):
        # Cancel after process
        if self.after_id:
            self.after_flag = False
            #print(self.after_id)
            self.after_cancel(self.after_id)
            #print("after_cancel",self.after_id)
        # Stop the video process
        if hasattr(self, 'video_process') and self.video_process:
            self.video_process.terminate()
            self.video_process = None
        # Black out cap.png
        width, height = 640, 480
        blank_image = np.zeros((height, width, 3), dtype=np.uint8)
        cv2.imwrite(self.cap_path, blank_image)

    # Start the video process 
    def photo_update_start(self):
        if self.screen_flag:
            self.screen_flag = False
            width, height = 640, 480
            try:
                self.video_process = CameraRspiPicam.capture_video()
                self.frame_size = width * height * 3 // 2  # YUV420p frame size
                self.update()
            except Exception as e:
                print(e)
        #self.main_app.schedule_hdmi_control()

    # Start of after process
    def update(self):
        if self.after_flag:
            ret, frame = self.get_frame()
            if ret:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.photo_label.configure(image=self.photo)
                self.update_counter += 1
                if self.update_counter >= self.save_interval:
                    cv2.imwrite(self.cap_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                    self.update_counter = 0
                    img = cv2.imread(self.cap_path)  ###QRcode scan 20240717_xiao
                    data, _, _ = self.detector.detectAndDecode(img)
                    if data:
                        current_time = datetime.datetime.now()
                        password = data[:50]
                        start_time_str = data.split("Starts:")[1].split(" ")[0]
                        end_time_str = data.split("End:")[1]
                        start_time = datetime.datetime.strptime(start_time_str, "%Y%m%d%H:%M")
                        end_time = datetime.datetime.strptime(end_time_str, "%Y%m%d%H:%M")
                        result = XFace_Database_Function.check_password_in_qrcode(password)

                        if result is not None and start_time <= current_time <= end_time:
                            print("1:QRcode scanning success")
                        else:
                            print("0:QRcode is invalid")
                    else:
                        print("0:No QRcodes were scanned")
            #print("after_check")
            #if self.after_id:
                #print("after_id:",self.after_id)
            self.after_id = self.after(50, self.update)

    # Camera image
    def get_frame(self):
        width, height = 640, 480
        if self.video_process is None or self.video_process.stdout is None:
            return (False, None)
        raw_frame = self.video_process.stdout.read(self.frame_size)
        if not raw_frame:
            return (False, None)
        # Convert raw YUV420p data to a numpy array
        yuv = np.frombuffer(raw_frame, dtype=np.uint8).reshape((height + height // 2, width))
        # Convert YUV to RGB
        frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB_I420)
        return (True, frame)
