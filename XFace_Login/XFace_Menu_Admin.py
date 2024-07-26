import tkinter as tk
from tkinter import messagebox
import customtkinter
from datetime import datetime
import subprocess
from PIL import Image, ImageTk
from Virtual_Keyboard import VirtualKeyboard

class Screen4(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

        # Get the current date and format it
        self.current_date = datetime.now().strftime("%Y / %m / %d")
        
        # Initial value
        self.flag = True
        self.wifi_flag = True
        self.wifi_frame_flag = True

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

        # Add User Register Button
        user_register_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(6), text="User Registration", text_color="black", font=("Arial Bold", 20), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        user_register_btn.place(relx=0.07, rely=0.3)

        # Add Department Master Button
        department_master_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(15), text="Department Master", text_color="black", font=("Arial Bold", 20), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        department_master_btn.place(relx=0.52, rely=0.3)

        # Add Edit user Information Button
        edit_user_information_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(13), text="Edit user Information", text_color="black", font=("Arial Bold", 20), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_user_information_btn.place(relx=0.07, rely=0.45)

        # Add Edit Attendance Record Button
        edit_attendance_record_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(18), text="Edit Attendance Record", text_color="black", font=("Arial Bold", 20), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_attendance_record_btn.place(relx=0.52, rely=0.45)

        # Add Excel Output Button
        edit_excel_output_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(19), text="Excel Output", text_color="black", font=("Arial Bold", 20), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_excel_output_btn.place(relx=0.07, rely=0.6)

        # Add Wifi Setting Information Button
        edit_wifi_setting_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.open_wifi_settings(), text="Wifi Setting", text_color="black", font=("Arial Bold", 20), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_wifi_setting_btn.place(relx=0.3, rely=0.75)

        # Add QRcode Button
        qrcode_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(22), text="QR Code", text_color="black", font=("Arial Bold", 20), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        qrcode_btn.place(relx=0.52, rely=0.6)

        power_icon_pil = Image.open('XFace_Login/images/power.png')
        power_icon_pil_resized = power_icon_pil.resize((50, 50))
        self.power_icon = ImageTk.PhotoImage(power_icon_pil_resized)

        # Add Power off Button
        power_off_btn = tk.Button(self.menu_frame, image=self.power_icon, command= lambda: self.power_off(), bg="white", width=int(self.main_app.width/600*50), height=int(self.main_app.height/500*50), borderwidth=0, cursor="hand2")
        power_off_btn.place(relx=0.85, rely=0.85)

    # Create frame for Wifi connection
    def open_wifi_settings(self):
        if self.wifi_frame_flag:
            self.wifi_frame_flag = False
            self.wifi_frame = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*550), height=int(self.main_app.height/500*250), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.wifi_frame.place(relx=0.06, rely=0.25)

            # Add
            ssid_label = customtkinter.CTkLabel(master=self.wifi_frame, text="SSID", font=("Arial", 20), text_color="black")
            ssid_label.place(relx=0.15, rely=0.1)
            self.ssid = customtkinter.CTkEntry(master=self.wifi_frame,  width=int(self.main_app.width/600*350), height=int(self.main_app.height/500*25), font=("Arial", 20), text_color="black")
            self.ssid.place(relx=0.15, rely=0.2)

            password_label = customtkinter.CTkLabel(master=self.wifi_frame, text="Password", font=("Arial", 20), text_color="black")
            password_label.place(relx=0.15, rely=0.4)
            self.password = customtkinter.CTkEntry(master=self.wifi_frame,  width=int(self.main_app.width/600*350), height=int(self.main_app.height/500*25), font=("Arial", 20), text_color="black")
            self.password.place(relx=0.15, rely=0.5)

            # Add Button "connect"
            btn_connect = customtkinter.CTkButton(master=self.wifi_frame, width=int(self.main_app.width/600*80), command=lambda: self.connect_wifi(), text="Connect", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_connect.place(relx=0.7, rely=0.75)

            # Add Button "Cancel"
            btn_Cancel = customtkinter.CTkButton(master=self.wifi_frame, width=int(self.main_app.width/600*80), command=self.destroy_wifi_frame, text="Cancel", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_Cancel.place(relx=0.1, rely=0.75)

            self.entry_keyboard()

    # Wifi connection with entered SSID and password
    def connect_wifi(self):
        if self.wifi_flag:
            self.wifi_flag = False
            ssid, password = self.ssid.get(),self.password.get()
            self.message_frame = customtkinter.CTkFrame(master=self.wifi_frame,width=int(self.main_app.width/600*500), height=int(self.main_app.height/500*210), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame.place(relx=0.06, rely=0.1)
            if ssid == "" or password == "":
                error_label = customtkinter.CTkLabel(master=self.message_frame, text="Has not been entered!", font=("Arial", 20), text_color="black")
                error_label.place(relx=0.37, rely=0.25)
                btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.message_frame.destroy(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                btn_ok.place(relx=0.42, rely=0.7)
                self.wifi_flag = True
            else:
                try:
                    subprocess.run(['sudo', 'nmcli', 'dev', 'wifi', 'connect', ssid, 'password', password], check=True)
                    success_label = customtkinter.CTkLabel(master=self.message_frame, text="Connecting this WIFI successfully!", font=("Arial", 20), text_color="black")
                    success_label.place(relx=0.37, rely=0.25)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.destroy_wifi_frame(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.42, rely=0.7)
                except subprocess.CalledProcessError:
                    error_label = customtkinter.CTkLabel(master=self.message_frame, text="Error connecting to WiFi network!", font=("Arial", 20), text_color="black")
                    error_label.place(relx=0.37, rely=0.25)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.destroy_message_frame(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.42, rely=0.7)
                    

    # Deleting frame and set flag and remove keybord settings
    def destroy_wifi_frame(self):
        if self.current_keyboard:
            self.current_keyboard.pack_forget()  
        self.wifi_frame.destroy()
        self.wifi_flag = True
        self.wifi_frame_flag = True
        self.unbind_all("<Button-1>")

    # Deleting frame and set flag
    def destroy_message_frame(self):
        self.message_frame.destroy()
        self.wifi_flag = True
    
    # Creation of shutdown confirmation frame
    def power_off(self):
        if self.flag:
            self.message_frame1 = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*550), height=int(self.main_app.height/500*250), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame1.place(relx=0.06, rely=0.25)

            ask_label = customtkinter.CTkLabel(master=self.message_frame1, text="Are you sure you want to shut down the app?", font=("Arial", 20), text_color="black")
            ask_label.place(relx=0.25, rely=0.35)

            # Add Button "ok"
            btn_ok = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.shutdown_now(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.7, rely=0.75)

            # Add Button "Cancel"
            btn_Cancel = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.cancel(), text="Cancel", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_Cancel.place(relx=0.1, rely=0.75)
            
            self.flag = False
            
    # Set flags and remove frame
    def cancel(self):
        self.flag = True
        self.message_frame1.destroy()

    # Shutdown
    def shutdown_now(self):
        self.flag = True
        self.main_app.root.destroy()
        #subprocess.call(['sudo', 'shutdown', 'now'])

    # Re-retrieve date and update label values
    def set_currentdate(self):
        self.current_date = datetime.now().strftime("%Y / %m / %d")
        self.datetxt_label.configure(text=self.current_date)

    # Screen transitons
    def next_screen(self, index):
        self.main_app.show_next_screen(index)

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
            self.ssid: self.keyboard_general,
            self.password: self.keyboard_general
        }
        
        for entry, keyboard in entries.items():
            try:
                ex, ey, ew, eh = entry.winfo_rootx(), entry.winfo_rooty(), entry.winfo_width(), entry.winfo_height()
            except tk.TclError:
                return
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