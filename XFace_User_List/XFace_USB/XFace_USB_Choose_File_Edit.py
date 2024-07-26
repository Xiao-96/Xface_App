import tkinter as tk
import customtkinter
import os
from PIL import Image, ImageTk
import shutil

class Screen11(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="white", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        self.step_frame = customtkinter.CTkFrame(self, width=self.main_app.width, height=self.main_app.height, fg_color="#e6e6e6", corner_radius=0)
        self.step_frame.pack()

        # Add Square
        self.gray_square = customtkinter.CTkFrame(master=self.step_frame,width=int(self.main_app.width/600*500), height=int(self.main_app.height/500*500), fg_color="white", corner_radius=0, border_color="white", border_width=1)
        self.gray_square.place(relx=0.2, rely=0)

        # Add "<" Button                                                
        back_btn = customtkinter.CTkButton(self, command=lambda: self.next_screen(14), width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), text="<", text_color="black", font=("Arial", 30), fg_color="transparent", bg_color="#e6e6e6", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        # Add scrollbar
        self.scrollable_frame = customtkinter.CTkScrollableFrame(master=self.step_frame, width=int(self.main_app.width/600*460), height=int(self.main_app.height/500*500), bg_color="white", fg_color="white", scrollbar_fg_color="white")
        self.scrollable_frame.place(relx=0.2, rely=0, relheight=1)
    
    # Displays images on USB memory stick on application screen
    def load_image_buttons(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()        
        self.get_usbpath, returncode = self.main_app.get_usbpath()
        if returncode == 0:
            row, col = 0, 0
            found_image = False
            for file_name in os.listdir(self.get_usbpath):
                if file_name.endswith(('.png', '.jpg', '.jpeg')): 
                    found_image = True
                    img_path = os.path.join(self.get_usbpath, file_name)
                    img = Image.open(img_path)
                    img = img.resize((150, 150), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    button = tk.Button(self.scrollable_frame, image=photo, width=150, height=150, command=lambda img_path=img_path: self.open_image(img_path))
                    button.image = photo
                    button.grid(row=row, column=col, padx=10, pady=10)
                    col += 1
                    if col > 2:  
                        col = 0
                        row += 1
            if not found_image:
                label = tk.Label(self.scrollable_frame, text="No photos found.")
                label.grid(row=0, column=0, padx=10, pady=10, sticky='wens')
        else:
            label = tk.Label(self.scrollable_frame, text="No USBs found.")
            label.grid(row=0, column=0, padx=10, pady=10, sticky='wens')
            return
        
    # Copy selected images to "photoget_edit.png"
    def open_image(self, img_path):
        current_directory = os.getcwd()
        target_path = 'photoget_edit/photoget_edit.png'
        target_file_path = os.path.join(current_directory, target_path)
        shutil.copyfile(img_path, target_file_path)
        self.main_app.usb_eject(self.get_usbpath)
        self.main_app.show_next_screen(14)

    # USB disconnetion and screen transition
    def next_screen(self, index):
        self.main_app.usb_eject(self.get_usbpath)
        self.main_app.show_next_screen(index)
