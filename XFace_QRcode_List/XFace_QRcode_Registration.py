import tkinter as tk
import customtkinter
import numpy as np
import XFace_Database_Function
from Virtual_Keyboard import VirtualKeyboard
import datetime
import calendar
import qrcode
import random
import string
import os

class Screen23(tk.Frame):
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

        # Frame for all elements
        self.menu_frame = customtkinter.CTkFrame(self, width=self.main_app.width, height=self.main_app.height, fg_color="#e6e6e6", corner_radius=0)
        self.menu_frame.place(relx=0)

        # Back Button
        back_btn = customtkinter.CTkButton(self, text="<", command=lambda: self.back_screen(22), width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), text_color="black", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        # Title for the QR Registration section
        title_label = customtkinter.CTkLabel(self.menu_frame, text="QR Registration", font=("Arial", 24), text_color="black", fg_color="transparent")
        title_label.place(relx=0.1, rely=0.1)

        # Name Entry
        vcmd50 = (self.register(self.main_app.limit_char50), '%P')
        qr_name_label = customtkinter.CTkLabel(self.menu_frame, text="QR Name", font=("Arial", 20), text_color="black", fg_color="transparent")
        qr_name_label.place(relx=0.1, rely=0.2)
        self.qr_name_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20),  width=int(self.main_app.width/600*400), height=int(self.main_app.height/500*35), validate="key", validatecommand=vcmd50)
        self.qr_name_entry.place(relx=0.1, rely=0.25)

        # Start Time
        start_time_label = customtkinter.CTkLabel(self.menu_frame, text="StartTime", font=("Arial", 20), text_color="black", fg_color="transparent")
        start_time_label.place(relx=0.1, rely=0.35)
        
        # year
        self.current_year = datetime.datetime.now().year
        year_label = customtkinter.CTkLabel(self.menu_frame, text="Year", font=("Arial", 15), text_color="black", fg_color="transparent")
        year_label.place(relx=0.1, rely=0.4)
        self.year_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*100), height=int(self.main_app.height/500*35))
        self.year_entry.place(relx=0.1, rely=0.45)
        self.year_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_year_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.year_menu_button.place(relx=0.217, rely=0.45)

        # month
        self.current_month = datetime.datetime.now().month
        month_label = customtkinter.CTkLabel(self.menu_frame, text="Month", font=("Arial", 15), text_color="black", fg_color="transparent")
        month_label.place(relx=0.3, rely=0.4)
        self.month_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*50), height=int(self.main_app.height/500*35))
        self.month_entry.place(relx=0.3, rely=0.45)
        self.month_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_month_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.month_menu_button.place(relx=0.333, rely=0.45)
       
        # day
        self.current_day = datetime.datetime.now().day
        day_label = customtkinter.CTkLabel(self.menu_frame, text="Day", font=("Arial", 15), text_color="black", fg_color="transparent")
        day_label.place(relx=0.4, rely=0.4)
        self.day_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*50), height=int(self.main_app.height/500*35))
        self.day_entry.place(relx=0.4, rely=0.45)
        self.day_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_day_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.day_menu_button.place(relx=0.434, rely=0.45)

        # time
        time_label = customtkinter.CTkLabel(self.menu_frame, text="Time", font=("Arial", 15), text_color="black", fg_color="transparent")
        time_label.place(relx=0.5, rely=0.4)
        self.time_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*150), height=int(self.main_app.height/500*35))
        self.time_entry.place(relx=0.5, rely=0.45)
        self.time_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_time_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.time_menu_button.place(relx=0.7, rely=0.45)
        
        #end Time
        end_time_label = customtkinter.CTkLabel(self.menu_frame, text="EndTime", font=("Arial", 20), text_color="black", fg_color="transparent")
        end_time_label.place(relx=0.1, rely=0.6)
        
        # year1
        year1_label = customtkinter.CTkLabel(self.menu_frame, text="Year", font=("Arial", 15), text_color="black", fg_color="transparent")
        year1_label.place(relx=0.1, rely=0.65)
        self.year1_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*100), height=int(self.main_app.height/500*35))
        self.year1_entry.place(relx=0.1, rely=0.7)
        self.year1_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_year1_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.year1_menu_button.place(relx=0.217, rely=0.7)

        # month1
        month1_label = customtkinter.CTkLabel(self.menu_frame, text="Month", font=("Arial", 15), text_color="black", fg_color="transparent")
        month1_label.place(relx=0.3, rely=0.65)
        self.month1_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*50), height=int(self.main_app.height/500*35))
        self.month1_entry.place(relx=0.3, rely=0.7)
        self.month1_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_month1_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.month1_menu_button.place(relx=0.333, rely=0.7)
       
        # day1
        day1_label = customtkinter.CTkLabel(self.menu_frame, text="Day", font=("Arial", 15), text_color="black", fg_color="transparent")
        day1_label.place(relx=0.4, rely=0.65)
        self.day1_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*50), height=int(self.main_app.height/500*35))
        self.day1_entry.place(relx=0.4, rely=0.7)
        self.day1_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_day1_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.day1_menu_button.place(relx=0.434, rely=0.7)

        # time1
        time1_label = customtkinter.CTkLabel(self.menu_frame, text="Time", font=("Arial", 15), text_color="black", fg_color="transparent")
        time1_label.place(relx=0.5, rely=0.65)
        self.time1_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=int(self.main_app.width/600*150), height=int(self.main_app.height/500*35))
        self.time1_entry.place(relx=0.5, rely=0.7)
        self.time1_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_time1_menu, text_color="black", font=("Arial", 20), fg_color="white", width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*35), cursor="hand2")
        self.time1_menu_button.place(relx=0.7, rely=0.7)

        # Next Button
        save_btn = customtkinter.CTkButton(self.menu_frame, text="Save & USB Output", command=lambda: self.save(), text_color="black", font=("Arial Blod", 20), fg_color="white", width=int(self.main_app.width/600*80), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        save_btn.place(relx=0.75, rely=0.85)

        # Initialize Start Time Frame with Listbox and Scrollbar
        self.year_frame = tk.Frame(self, bg="#424242")
        self.year_listbox = tk.Listbox(self.year_frame, font=("Arial", 15), width=int(self.main_app.width/600*6), height=3)
        for i in range(3):
            self.year_listbox.insert("end",f"{self.current_year + i}")
        self.year_listbox.bind("<Double-Button-1>", self.select_year)
        self.year_scrollbar = tk.Scrollbar(self.year_frame, orient="vertical", command=self.year_listbox.yview)
        self.year_listbox.config(yscrollcommand=self.year_scrollbar.set)

        # Initialize Start Time Frame with Listbox and Scrollbar
        self.month_frame = tk.Frame(self, bg="#424242")
        self.month_listbox = tk.Listbox(self.month_frame, font=("Arial", 15), width=int(self.main_app.width/600*2), height=3)
        for i in range(1, 13):
            self.month_listbox.insert("end", f"{i:02d}")
        self.month_listbox.bind("<Double-Button-1>", self.select_month)
        self.month_scrollbar = tk.Scrollbar(self.month_frame, orient="vertical", command=self.month_listbox.yview)
        self.month_listbox.config(yscrollcommand=self.month_scrollbar.set)

        # Initialize Start Time Frame with Listbox and Scrollbar
        self.day_frame = tk.Frame(self, bg="#424242")
        self.day_listbox = tk.Listbox(self.day_frame, font=("Arial", 15), width=int(self.main_app.width/600*2), height=3)
        year = int(self.current_year)
        month = int(self.current_month)
        num_days = calendar.monthrange(year, month)[1] 
        for i in range(1, num_days + 1):
            self.day_listbox.insert("end", f"{i:02d}")
        self.day_listbox.bind("<Double-Button-1>", self.select_day)
        self.day_scrollbar = tk.Scrollbar(self.day_frame, orient="vertical", command=self.day_listbox.yview)
        self.day_listbox.config(yscrollcommand=self.day_scrollbar.set)

        # Initialize Start Time Frame with Listbox and Scrollbar
        self.time_frame = tk.Frame(self, bg="#424242")
        self.time_listbox = tk.Listbox(self.time_frame, font=("Arial", 15), width=int(self.main_app.width/600*11), height=3)
        for hour in range(24):
            self.time_listbox.insert("end", f"{hour:02d}:00")
        self.time_listbox.bind("<Double-Button-1>", self.select_time)
        self.time_scrollbar = tk.Scrollbar(self.time_frame, orient="vertical", command=self.time_listbox.yview)
        self.time_listbox.config(yscrollcommand=self.time_scrollbar.set)

        # Initialize Start Time Frame with Listbox and Scrollbar
        self.year1_frame = tk.Frame(self, bg="#424242")
        self.year1_listbox = tk.Listbox(self.year1_frame, font=("Arial", 15), width=int(self.main_app.width/600*6), height=3)
        for i in range(3):
            self.year1_listbox.insert("end",f"{self.current_year + i}")
        self.year1_listbox.bind("<Double-Button-1>", self.select_year1)
        self.year1_scrollbar = tk.Scrollbar(self.year1_frame, orient="vertical", command=self.year1_listbox.yview)
        self.year1_listbox.config(yscrollcommand=self.year1_scrollbar.set)

        # Initialize Start Time Frame with Listbox and Scrollbar
        self.month1_frame = tk.Frame(self, bg="#424242")
        self.month1_listbox = tk.Listbox(self.month1_frame, font=("Arial", 15), width=int(self.main_app.width/600*2), height=3)
        for i in range(1, 13):
            self.month1_listbox.insert("end", f"{i:02d}")
        self.month1_listbox.bind("<Double-Button-1>", self.select_month1)
        self.month1_scrollbar = tk.Scrollbar(self.month1_frame, orient="vertical", command=self.month1_listbox.yview)
        self.month1_listbox.config(yscrollcommand=self.month1_scrollbar.set)

        # Initialize Start Time Frame with Listbox and Scrollbar
        self.day1_frame = tk.Frame(self, bg="#424242")
        self.day1_listbox = tk.Listbox(self.day1_frame, font=("Arial", 15), width=int(self.main_app.width/600*2), height=3)
        for i in range(1, num_days + 1):
            self.day1_listbox.insert("end", f"{i:02d}")
        self.day1_listbox.bind("<Double-Button-1>", self.select_day1)
        self.day1_scrollbar = tk.Scrollbar(self.day1_frame, orient="vertical", command=self.day1_listbox.yview)
        self.day1_listbox.config(yscrollcommand=self.day1_scrollbar.set)

        # Initialize Start Time Frame with Listbox and Scrollbar
        self.time1_frame = tk.Frame(self, bg="#424242")
        self.time1_listbox = tk.Listbox(self.time1_frame, font=("Arial", 15), width=int(self.main_app.width/600*11), height=3)
        for hour in range(24):
            self.time1_listbox.insert("end", f"{hour:02d}:00")
        self.time1_listbox.bind("<Double-Button-1>", self.select_time1)
        self.time1_scrollbar = tk.Scrollbar(self.time1_frame, orient="vertical", command=self.time1_listbox.yview)
        self.time1_listbox.config(yscrollcommand=self.time1_scrollbar.set)

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
            self.qr_name_entry: self.keyboard_general
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

    # Save to DB
    def save(self):
        if self.flag:
            get_usbpath, returncode = self.main_app.get_usbpath()
            qr_name = self.qr_name_entry.get()
            start_year = self.year_entry.get()
            start_month = self.month_entry.get()
            start_day = self.day_entry.get()
            start_time = self.time_entry.get()
            end_year = self.year1_entry.get()
            end_month = self.month1_entry.get()
            end_day = self.day1_entry.get()
            end_time = self.time1_entry.get()
            if returncode == 0:
                if not all([qr_name, start_year, start_month, start_day, start_time, end_year, end_month, end_day, end_time]):
                    self.flag = False
                    self.message_frame1 = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
                    self.message_frame1.place(relx=0.25, rely=0.32)
                    error_label = customtkinter.CTkLabel(master=self.message_frame1, text="Has not been entered!", font=("Arial", 20), text_color="black")
                    error_label.place(relx=0.25, rely=0.1)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.cancel(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.35, rely=0.7)
                else:
                    start_datetime = f"{start_year}{start_month}{start_day}{start_time}"
                    end_datetime = f"{end_year}{end_month}{end_day}{end_time}"
                    random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
                    creationdate = datetime.datetime.now().strftime("%Y%m%d")
                    XFace_Database_Function.save_qrcode(qr_name,start_datetime,end_datetime,random_password,self.user_name,creationdate)
                    qr_content = f"{random_password} Starts:{start_datetime} End:{end_datetime}"
                    qr = qrcode.make(qr_content)
                    qr_filename = os.path.join(get_usbpath, f"{qr_name}.png")
                    qr.save(qr_filename)
                    self.message_frame = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
                    self.message_frame.place(relx=0.25, rely=0.32)
                    success_label = customtkinter.CTkLabel(master=self.message_frame, text="QRcode distribution successfully.", font=("Arial", 20), text_color="black")
                    success_label.place(relx=0.16, rely=0.1)
                    success_label1 = customtkinter.CTkLabel(master=self.message_frame, text="Plaese remove USB.", font=("Arial", 20), text_color="black")
                    success_label1.place(relx=0.28, rely=0.3)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.destroy_message_frame(get_usbpath), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.35, rely=0.7)
                    self.flag = False
            else:
                self.message_frame2 = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
                self.message_frame2.place(relx=0.25, rely=0.32)
                error_label = customtkinter.CTkLabel(master=self.message_frame2, text="No USBs found!", font=("Arial", 20), text_color="black")
                error_label.place(relx=0.35, rely=0.3)
                btn_ok = customtkinter.CTkButton(master=self.message_frame2, width=int(self.main_app.width/600*80), command=lambda:self.cancel2(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                btn_ok.place(relx=0.35, rely=0.7)
                self.flag = False
                
    # Set flags and remove frame
    def cancel(self):
        self.flag = True
        self.message_frame1.destroy()
        
    # Set flags and remove frame
    def cancel2(self):
        self.flag = True
        self.message_frame2.destroy()

    # Set flags, delete widgets, remove keybord settings and screen transitons
    def destroy_message_frame(self,get_usbpath):
        self.flag = True
        self.main_app.usb_eject(get_usbpath)
        self.message_frame.destroy()
        self.qr_name_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.month_entry.delete(0, tk.END)
        self.day_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.year1_entry.delete(0, tk.END)
        self.month1_entry.delete(0, tk.END)
        self.day1_entry.delete(0, tk.END)
        self.time1_entry.delete(0, tk.END)
        self.unbind_all("<Button-1>")
        self.main_app.show_next_screen(22)
    
    # Obtain user ID for Excel output
    def get_user_id(self):
        new_user_id = self.main_app.get_loginuserid()
        self.user_id = new_user_id
        self.user_name = self.main_app.get_loginusername()
        self.year_entry.insert(0, str(self.current_year))
        self.month_entry.insert(0, f"{self.current_month:02}")
        self.day_entry.insert(0, f"{self.current_day:02}")
        self.time_entry.insert(0, "00:00")
        self.year1_entry.insert(0, str(self.current_year))
        self.month1_entry.insert(0, f"{self.current_month:02}")
        self.day1_entry.insert(0, f"{self.current_day+1:02}")
        self.time1_entry.insert(0, "00:00")


    # Value initialization, remove keybord settings and screen transitons
    def back_screen(self, index):
        self.qr_name_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.month_entry.delete(0, tk.END)
        self.day_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.year1_entry.delete(0, tk.END)
        self.month1_entry.delete(0, tk.END)
        self.day1_entry.delete(0, tk.END)
        self.time1_entry.delete(0, tk.END)
        self.unbind_all("<Button-1>")
        self.main_app.show_next_screen(index)

    def update_day_list(self):
        year = int(self.year_entry.get())
        month = int(self.month_entry.get())
        num_days = calendar.monthrange(year, month)[1]
        self.day_entry.delete(0, tk.END)
        self.day_listbox.delete(0, tk.END)
        for i in range(1, num_days + 1):
            self.day_listbox.insert("end", f"{i:02d}")

    # Enter the value selected in the list
    def select_year(self, event):
        selected_time = self.year_listbox.get(tk.ACTIVE)
        self.year_entry.delete(0, tk.END)
        self.year_entry.insert(0, selected_time)
        self.year_frame.place_forget()
        self.update_day_list()

    # Enter the value selected in the list
    def select_month(self, event):
        selected_time = self.month_listbox.get(tk.ACTIVE)
        self.month_entry.delete(0, tk.END)
        self.month_entry.insert(0, selected_time)
        self.month_frame.place_forget()
        self.update_day_list()

    # Enter the value selected in the list
    def select_day(self, event):
        selected_time = self.day_listbox.get(tk.ACTIVE)
        self.day_entry.delete(0, tk.END)
        self.day_entry.insert(0, selected_time)
        self.day_frame.place_forget()

    # Enter the value selected in the list
    def select_time(self, event):
        selected_time = self.time_listbox.get(tk.ACTIVE)
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, selected_time)
        self.time_frame.place_forget()

    def update_day1_list(self):
        year = int(self.year1_entry.get())
        month = int(self.month1_entry.get())
        num_days = calendar.monthrange(year, month)[1]
        self.day1_entry.delete(0, tk.END)
        self.day1_listbox.delete(0, tk.END)
        for i in range(1, num_days + 1):
            self.day1_listbox.insert("end", f"{i:02d}")

    # Enter the value selected in the list
    def select_year1(self, event):
        selected_time = self.year1_listbox.get(tk.ACTIVE)
        self.year1_entry.delete(0, tk.END)
        self.year1_entry.insert(0, selected_time)
        self.year1_frame.place_forget()
        self.update_day1_list()

    # Enter the value selected in the list
    def select_month1(self, event):
        selected_time = self.month1_listbox.get(tk.ACTIVE)
        self.month1_entry.delete(0, tk.END)
        self.month1_entry.insert(0, selected_time)
        self.month1_frame.place_forget()
        self.update_day1_list()

    # Enter the value selected in the list
    def select_day1(self, event):
        selected_time = self.day1_listbox.get(tk.ACTIVE)
        self.day1_entry.delete(0, tk.END)
        self.day1_entry.insert(0, selected_time)
        self.day1_frame.place_forget()

    # Enter the value selected in the list
    def select_time1(self, event):
        selected_time = self.time1_listbox.get(tk.ACTIVE)
        self.time1_entry.delete(0, tk.END)
        self.time1_entry.insert(0, selected_time)
        self.time1_frame.place_forget()

    # Showing and Hiding Lists
    def show_year_menu(self):
        if not self.year_frame.winfo_ismapped():
            self.year_frame.place(relx=0.1, rely=0.513)
            self.year_listbox.pack(side="left")
            self.year_scrollbar.pack(side="right", fill="y")
        else:
            self.year_frame.place_forget()

    # Showing and Hiding Lists
    def show_month_menu(self):
        if not self.month_frame.winfo_ismapped():
            self.month_frame.place(relx=0.3, rely=0.513) ###re
            self.month_listbox.pack(side="left")
            self.month_scrollbar.pack(side="right", fill="y")
        else:
            self.month_frame.place_forget()

    # Showing and Hiding Lists
    def show_day_menu(self):
        if not self.day_frame.winfo_ismapped():
            self.day_frame.place(relx=0.4, rely=0.513) ###re
            self.day_listbox.pack(side="left")
            self.day_scrollbar.pack(side="right", fill="y")
        else:
            self.day_frame.place_forget()
    
    # Showing and Hiding Lists
    def show_time_menu(self):
        if not self.time_frame.winfo_ismapped():
            self.time_frame.place(relx=0.5, rely=0.513) ###re
            self.time_listbox.pack(side="left")
            self.time_scrollbar.pack(side="right", fill="y")
        else:
            self.time_frame.place_forget()

    # Showing and Hiding Lists
    def show_year1_menu(self):
        if not self.year1_frame.winfo_ismapped():
            self.year1_frame.place(relx=0.1, rely=0.763)
            self.year1_listbox.pack(side="left")
            self.year1_scrollbar.pack(side="right", fill="y")
        else:
            self.year1_frame.place_forget()

    # Showing and Hiding Lists
    def show_month1_menu(self):
        if not self.month1_frame.winfo_ismapped():
            self.month1_frame.place(relx=0.3, rely=0.763) ###re
            self.month1_listbox.pack(side="left")
            self.month1_scrollbar.pack(side="right", fill="y")
        else:
            self.month1_frame.place_forget()

    # Showing and Hiding Lists
    def show_day1_menu(self):
        if not self.day1_frame.winfo_ismapped():
            self.day1_frame.place(relx=0.4, rely=0.763) ###re
            self.day1_listbox.pack(side="left")
            self.day1_scrollbar.pack(side="right", fill="y")
        else:
            self.day1_frame.place_forget()
    
    # Showing and Hiding Lists
    def show_time1_menu(self):
        if not self.time1_frame.winfo_ismapped():
            self.time1_frame.place(relx=0.5, rely=0.763) ###re
            self.time1_listbox.pack(side="left")
            self.time1_scrollbar.pack(side="right", fill="y")
        else:
            self.time1_frame.place_forget()