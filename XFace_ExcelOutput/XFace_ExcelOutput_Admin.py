import tkinter as tk
from tkinter import messagebox
import customtkinter
import numpy as np
from XFace_ExcelOutput.XFace_ExcelOutput_Function import AttendanceRecord
from XFace_ExcelOutput.XFace_ExcelOutput_Function import EmployeeInfo
from Virtual_Keyboard import VirtualKeyboard
from Virtual_Keyboard_Number import VirtualKeyboardNumber
employeeinfo = EmployeeInfo()
attendancerecord = AttendanceRecord()

class Screen19(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

        # Initial value of flag
        self.flag = True
        self.info_flag = True
        self.user_flag = True
        self.list_flag = True

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Frame for all elements
        self.menu_frame = customtkinter.CTkFrame(self, width=self.main_app.width, height=self.main_app.height, fg_color="#e6e6e6", corner_radius=0)
        self.menu_frame.place(relx=0)

        # Back Button
        back_btn = customtkinter.CTkButton(self, text="<", command=lambda: self.back_screen(4), width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), text_color="black", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        # Title for the Excel Output section
        title_label = customtkinter.CTkLabel(self.menu_frame, text="Excel Output", font=("Arial", 24), text_color="black", fg_color="transparent")
        title_label.place(relx=0.1, rely=0.1)

        vcmd50 = (self.register(self.main_app.limit_char50), '%P')
        vcmd6 = (self.register(self.main_app.limit_char6), '%P')

        # User Name Entry
        user_name_label = customtkinter.CTkLabel(self.menu_frame, text="User Name", font=("Arial", 20), text_color="black", fg_color="transparent")
        user_name_label.place(relx=0.07, rely=0.2)
        self.user_name_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20),  width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*35), validate="key", validatecommand=vcmd50)
        self.user_name_entry.place(relx=0.07, rely=0.25)

        # Yearmonth Entry
        yearmonth_label = customtkinter.CTkLabel(self.menu_frame, text="YearMonth", font=("Arial", 20), text_color="black", fg_color="transparent")
        yearmonth_label.place(relx=0.6, rely=0.2)
        self.yearmonth_entry = customtkinter.CTkEntry(self.menu_frame, placeholder_text="YYYYMM", font=("Arial", 20), width=int(self.main_app.width/600*150), height=int(self.main_app.height/500*35), validate="key", validatecommand=vcmd6)
        self.yearmonth_entry.place(relx=0.6, rely=0.25)

        # User ID Entry
        user_id_label = customtkinter.CTkLabel(self.menu_frame, text="User ID", font=("Arial", 20), text_color="black", fg_color="transparent")
        user_id_label.place(relx=0.07, rely=0.35)
        self.user_id_entry = customtkinter.CTkEntry(self.menu_frame, placeholder_text="000000", font=("Arial", 20), width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*35), validate="key", validatecommand=vcmd6)
        self.user_id_entry.place(relx=0.07, rely=0.4)

        # UserInfo list Button
        userinfo_btn = customtkinter.CTkButton(self.menu_frame, text="UserInfo List", command=lambda:self.ExcelOutput(self.yearmonth_entry.get()), text_color="black", font=("Arial Bold", 15), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        userinfo_btn.place(relx=0.07, rely=0.6)

        # AttendanceRecord User Button
        AttendanceRecord_user_btn = customtkinter.CTkButton(self.menu_frame, text="AttendanceRecord User", command=lambda:self.ExcelOutput_user(self.user_id_entry.get(), self.user_name_entry.get(), self.yearmonth_entry.get()), text_color="black", font=("Arial Bold", 15), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        AttendanceRecord_user_btn.place(relx=0.07, rely=0.75)

        # AttendanceRecord List Button
        AttendanceRecord_list_btn = customtkinter.CTkButton(self.menu_frame, text="AttendanceRecord List", command=lambda:self.ExcelOutput_list(self.yearmonth_entry.get()), text_color="black", font=("Arial Bold", 15), fg_color="white", width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*50), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        AttendanceRecord_list_btn.place(relx=0.52, rely=0.75)

    #VirtualKeyboard Settings
    def entry_keyboard(self):
        self.keyboard_general = VirtualKeyboard(self)  
        self.keyboard_number = VirtualKeyboardNumber(self)
        
        self.keyboard_is_visible = False
        self.current_keyboard = None
        self.current_entry = None 

        self.bind_all("<Button-1>", self.global_click)

    def global_click(self, event):
        x, y = event.x_root, event.y_root

        kx, ky, kw, kh = self.keyboard_general.winfo_rootx(), self.keyboard_general.winfo_rooty(), self.keyboard_general.winfo_width(), self.keyboard_general.winfo_height()
        if kx <= x <= kx + kw and ky <= y <= ky + kh:
            return 
        
        kx, ky, kw, kh = self.keyboard_number.winfo_rootx(), self.keyboard_number.winfo_rooty(), self.keyboard_number.winfo_width(), self.keyboard_number.winfo_height()
        if kx <= x <= kx + kw and ky <= y <= ky + kh:
            return 

        entry_clicked = None
        keyboard_to_use = None

        entries = {
            self.user_name_entry: self.keyboard_general,
            self.yearmonth_entry: self.keyboard_number,
            self.user_id_entry: self.keyboard_number
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

    # Value initialization, remove keybord settings and screen transitons
    def back_screen(self, index):
        if self.flag:
            self.user_name_entry.delete(0, tk.END)
            self.yearmonth_entry.delete(0, tk.END)
            self.user_id_entry.delete(0, tk.END)
            self.unbind_all("<Button-1>")
            self.main_app.show_next_screen(index)
    
    # Creation of Excel output confirmation frame
    def ExcelOutput(self,yearmonth):
        if self.flag:
            get_usbpath, returncode = self.main_app.get_usbpath()
            self.message_frame_ExcelOutput = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*500), height=int(self.main_app.height/500*250), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame_ExcelOutput.place(relx=0.1, rely=0.25)
            if returncode == 0:  
                if yearmonth == "":
                    error_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput, text="Yearmonth has not been entered!", font=("Arial", 20), text_color="black")
                    error_label.place(relx=0.32, rely=0.3)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput, width=int(self.main_app.width/600*80), command=lambda:self.cancel_message_frame_ExcelOutput(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.4, rely=0.7)
                else:
                    ask_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput, text="Output user information?", font=("Arial", 20), text_color="black")
                    ask_label.place(relx=0.37, rely=0.3)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput, width=int(self.main_app.width/600*80), command=lambda:self.employeeinfo_ExcelOutput(yearmonth,get_usbpath), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.75, rely=0.7)
                    btn_Cancel = customtkinter.CTkButton(master=self.message_frame_ExcelOutput, width=int(self.main_app.width/600*80), command=lambda:self.cancel_message_frame_ExcelOutput(), text="Cancel", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_Cancel.place(relx=0.12, rely=0.7)
            else:
                error_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput, text="No USBs found!", font=("Arial", 20), text_color="black")
                error_label.place(relx=0.4, rely=0.3)
                btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput, width=int(self.main_app.width/600*80), command=lambda:self.cancel_message_frame_ExcelOutput(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                btn_ok.place(relx=0.4, rely=0.7)

            self.flag = False
    
    # Set flags and remove frame
    def cancel_message_frame_ExcelOutput(self):
        self.flag = True
        self.message_frame_ExcelOutput.destroy()

    # Employee information Excel Output
    def employeeinfo_ExcelOutput(self,yearmonth,get_usbpath):
        if self.info_flag:
            self.info_flag = False
            employeeinfo.ExcelOutput(yearmonth,get_usbpath)
            self.message_frame_ExcelOutput1 = customtkinter.CTkFrame(master=self.message_frame_ExcelOutput,width=int(self.main_app.width/600*410), height=int(self.main_app.height/500*170), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame_ExcelOutput1.place(relx=0.1, rely=0.15)
            ask_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput1, text="Remove USB?", font=("Arial", 20), text_color="black")
            ask_label.place(relx=0.4, rely=0.3)
            btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput1, width=int(self.main_app.width/600*80), command=lambda:self.employeeinfo_ExcelOutput_success(get_usbpath), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.65, rely=0.75)
            btn_Cancel = customtkinter.CTkButton(master=self.message_frame_ExcelOutput1, width=int(self.main_app.width/600*80), command=lambda:self.destory_message_frame_ExcelOutput1(), text="Cancel", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_Cancel.place(relx=0.1, rely=0.75)
    
    # Removing aUSB memory device, set flags and remove frame
    def employeeinfo_ExcelOutput_success(self,get_usbpath):
        self.main_app.usb_eject(get_usbpath)
        self.message_frame_ExcelOutput.destroy()
        self.flag = True
        self.info_flag = True
    
    # Set flags and remove frame
    def destory_message_frame_ExcelOutput1(self):
        self.info_flag = True
        self.message_frame_ExcelOutput1.destroy()

    # Creation of Excel output confirmation frame
    def ExcelOutput_user(self,userid,username,yearmonth):
        if self.flag:
            get_usbpath, returncode = self.main_app.get_usbpath()
            self.message_frame_ExcelOutput_user = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*500), height=int(self.main_app.height/500*250), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame_ExcelOutput_user.place(relx=0.1, rely=0.25)
            if returncode == 0:
                if userid == "" or username == "" or yearmonth == "":
                    error_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput_user, text="Has not been entered!", font=("Arial", 20), text_color="black")
                    error_label.place(relx=0.36, rely=0.3)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_user, width=int(self.main_app.width/600*80), command=lambda:self.cancel_message_frame_ExcelOutput_user(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.4, rely=0.7)
                else:
                    ask_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput_user, text=f"Do you want to output {username} attendance information for {yearmonth}", font=("Arial", 20), text_color="black")
                    ask_label.place(relx=0.17, rely=0.35)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_user, width=int(self.main_app.width/600*80), command=lambda:self.attendancerecord_ExcelOutput_user(userid,username,yearmonth,get_usbpath), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.75, rely=0.7)
                    btn_Cancel = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_user, width=int(self.main_app.width/600*80), command=lambda:self.cancel_message_frame_ExcelOutput_user(), text="Cancel", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_Cancel.place(relx=0.12, rely=0.7)
            else:
                error_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput_user, text="No USBs found!", font=("Arial", 20), text_color="black")
                error_label.place(relx=0.4, rely=0.3)
                btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_user, width=int(self.main_app.width/600*80), command=lambda:self.cancel_message_frame_ExcelOutput_user(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                btn_ok.place(relx=0.4, rely=0.7)
            self.flag = False

    # Set flags and remove frame
    def cancel_message_frame_ExcelOutput_user(self):
        self.flag = True
        self.message_frame_ExcelOutput_user.destroy()

    # Excel output of attendance information for one user
    def attendancerecord_ExcelOutput_user(self,userid,username,yearmonth,get_usbpath):
        if self.user_flag:
            self.user_flag = False
            attendancerecord.ExcelOutput_user(userid,username,yearmonth,get_usbpath)
            self.message_frame_ExcelOutput_user1 = customtkinter.CTkFrame(master=self.message_frame_ExcelOutput_user,width=int(self.main_app.width/600*410), height=int(self.main_app.height/500*170), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame_ExcelOutput_user1.place(relx=0.1, rely=0.15)
            ask_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput_user1, text="Remove USB?", font=("Arial", 20), text_color="black")
            ask_label.place(relx=0.4, rely=0.3)
            btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_user1, width=int(self.main_app.width/600*80), command=lambda:self.attendancerecord_ExcelOutput_user_success(get_usbpath), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.65, rely=0.75)
            btn_Cancel = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_user1, width=int(self.main_app.width/600*80), command=lambda:self.destroy_message_frame_ExcelOutput_user1(), text="Cancel", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_Cancel.place(relx=0.1, rely=0.75)

    # Removing a USB memory device, set flags and remove frame
    def attendancerecord_ExcelOutput_user_success(self,get_usbpath):
        self.main_app.usb_eject(get_usbpath)
        self.message_frame_ExcelOutput_user.destroy()
        self.flag = True
        self.user_flag = True

    # Set flags and remove frame
    def destroy_message_frame_ExcelOutput_user1(self):
        self.user_flag = True
        self.message_frame_ExcelOutput_user1.destroy()
                
    # Creation of Excel output confirmation frame
    def ExcelOutput_list(self,yearmonth):
        if self.flag:
            get_usbpath, returncode = self.main_app.get_usbpath()
            self.message_frame_ExcelOutput_list = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*500), height=int(self.main_app.height/500*250), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame_ExcelOutput_list.place(relx=0.1, rely=0.25)
            if returncode == 0:
                if yearmonth == "":
                    error_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput_list, text="Yearmonth has not been entered!", font=("Arial", 20), text_color="black")
                    error_label.place(relx=0.32, rely=0.3)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_list, width=int(self.main_app.width/600*80), command=lambda:self.cancel_message_frame_ExcelOutput_list(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.4, rely=0.7)
                else:
                    ask_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput_list, text=f"Do you want to output alluser attendance information for {yearmonth}", font=("Arial", 20), text_color="black")
                    ask_label.place(relx=0.17, rely=0.35)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_list, width=int(self.main_app.width/600*80), command=lambda:self.attendancerecord_ExcelOutput_list(yearmonth,get_usbpath), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.75, rely=0.7)
                    btn_Cancel = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_list, width=int(self.main_app.width/600*80), command=lambda:self.cancel_message_frame_ExcelOutput_list(), text="Cancel", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_Cancel.place(relx=0.12, rely=0.7)

            else:
                error_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput_list, text="No USBs found!", font=("Arial", 20), text_color="black")
                error_label.place(relx=0.4, rely=0.3)
                btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_list, width=int(self.main_app.width/600*80), command=lambda:self.cancel_message_frame_ExcelOutput_list(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                btn_ok.place(relx=0.4, rely=0.7)
            
            self.flag = False
    
    # Set flags and remove frame
    def cancel_message_frame_ExcelOutput_list(self):
        self.flag = True
        self.message_frame_ExcelOutput_list.destroy()

    # Excel output of attendance information for all users
    def attendancerecord_ExcelOutput_list(self,yearmonth,get_usbpath):
        if self.list_flag:
            self.list_flag = False
            attendancerecord.ExcelOutput_list(yearmonth,get_usbpath)
            self.message_frame_ExcelOutput_list1 = customtkinter.CTkFrame(master=self.message_frame_ExcelOutput_list,width=int(self.main_app.width/600*410), height=int(self.main_app.height/500*170), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame_ExcelOutput_list1.place(relx=0.1, rely=0.15)
            ask_label = customtkinter.CTkLabel(master=self.message_frame_ExcelOutput_list1, text="Remove USB?", font=("Arial", 20), text_color="black")
            ask_label.place(relx=0.4, rely=0.3)
            btn_ok = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_list1, width=int(self.main_app.width/600*80), command=lambda:self.attendancerecord_ExcelOutput_list_success(get_usbpath), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.65, rely=0.75)
            btn_Cancel = customtkinter.CTkButton(master=self.message_frame_ExcelOutput_list1, width=int(self.main_app.width/600*80), command=lambda:self.destroy_message_frame_ExcelOutput_list1(), text="Cancel", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_Cancel.place(relx=0.1, rely=0.75)

    # Removing aUSB memory device, set flags and remove frame
    def attendancerecord_ExcelOutput_list_success(self,get_usbpath):
            self.main_app.usb_eject(get_usbpath)
            self.message_frame_ExcelOutput_list.destroy()
            self.flag = True
            self.list_flag = True

    # Set flags and remove frame
    def destroy_message_frame_ExcelOutput_list1(self):
        self.list_flag = True
        self.message_frame_ExcelOutput_list1.destroy()