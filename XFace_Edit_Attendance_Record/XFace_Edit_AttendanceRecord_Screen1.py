import tkinter as tk
from tkinter import messagebox
import customtkinter
import os
from XFace_Database_Function import fetch_user_attendance1, update_user_attendance
import datetime
import calendar
from Virtual_Keyboard import VirtualKeyboard
from Virtual_Keyboard_Time import VirtualKeyboardTime

class Screen18(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)
        
        # Initial value
        self.yearmonth = ""
        self.entries = []
        self.user_id = ""
        self.flag = True
        self.save_flag = True
        self.screen_flag = True
        
        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------
        self.vcmd5 = (self.register(self.main_app.limit_char5), '%P')
        self.vcmd50 = (self.register(self.main_app.limit_char50), '%P')
        # Frame for all elements
        self.menu_frame = customtkinter.CTkFrame(self, width=self.main_app.width, height=self.main_app.height, fg_color="#e6e6e6", corner_radius=0)
        self.menu_frame.place(relx=0, rely=0)

        # Back Button
        back_btn = customtkinter.CTkButton(self, text="<", command=lambda: self.back_screen(), width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), text_color="black", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        # Title for the Department Registration section
        title_label = customtkinter.CTkLabel(self.menu_frame, text="Edit attendance record", font=("Arial", 24), text_color="black", fg_color="transparent")
        title_label.place(relx=0.1, rely=0.1)

        # Search Button
        save_btn = customtkinter.CTkButton(self.menu_frame, text="Save", command=self.save_changes, text_color="black", font=("Arial Blod", 20), fg_color="white", width=int(self.main_app.width/600*50), height=int(self.main_app.height/500*20), corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        save_btn.place(relx=0.85, rely=0.1)

        # Add Year Entry and Button
        self.current_year = datetime.datetime.now().year
        self.year_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), justify="center", width=int(self.main_app.width/600*100), height=int(self.main_app.height/500*35))
        self.year_entry.insert(0, str(self.current_year))
        self.year_entry.place(relx=0.45, rely=0.1)
        self.year_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_year_menus, text_color="black", font=("Arial",20), fg_color="white", width=int(self.main_app.width/600*35), height=int(self.main_app.height/500*35), cursor="hand2")
        self.year_button.place(relx=0.61, rely=0.1)

        # Add Month Entry and Button
        self.current_month = datetime.datetime.now().month
        self.month_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), justify="center", width=int(self.main_app.width/600*50), height=int(self.main_app.height/500*35))
        self.month_entry.insert(0, f"{self.current_month:02}")
        self.month_entry.place(relx=0.69, rely=0.1)
        self.month_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_month_menus, text_color="black", font=("Arial",20), fg_color="white", width=int(self.main_app.width/600*35), height=int(self.main_app.height/500*35), cursor="hand2")
        self.month_button.place(relx=0.76, rely=0.1)

        # Initialize Year Frame with Listbox and Scrollbar
        self.year_frame = tk.Frame(self, bg="#424242")
        self.year_listbox = tk.Listbox(self.year_frame, font=("Arial", 15), width=int(self.main_app.width/600*8), height=5)
        for i in range(10):
            self.year_listbox.insert("end",f"{self.current_year - i}")
        self.year_listbox.bind("<Double-Button-1>", self.select_year)
        self.year_scrollbar = tk.Scrollbar(self.year_frame, orient="vertical", command=self.year_listbox.yview)
        self.year_listbox.config(yscrollcommand=self.year_scrollbar.set)

        # Initialize Month Frame with Listbox and Scrollbar
        self.month_frame = tk.Frame(self, bg="#424242")
        self.month_listbox = tk.Listbox(self.month_frame, font=("Arial", 15), width=int(self.main_app.width/600*4), height=5)
        for i in range(1, 13):
            self.month_listbox.insert("end", f"{i:02d}")
        self.month_listbox.bind("<Double-Button-1>", self.select_month)
        self.month_scrollbar = tk.Scrollbar(self.month_frame, orient="vertical", command=self.month_listbox.yview)
        self.month_listbox.config(yscrollcommand=self.month_scrollbar.set)
        
        # Canvas and Scrollbar for attendance records
        self.canvas = customtkinter.CTkCanvas(self.menu_frame, bg="#e6e6e6", highlightthickness=0)
        self.scrollbar = customtkinter.CTkScrollbar(self.menu_frame, orientation="vertical", command=self.canvas.yview)

        num_entries = 32
        entry_height = 40
        padding = 10
        total_height = num_entries * (entry_height + padding)
        # Ensure the scrollable frame can expand as needed
        self.scrollable_frame = tk.Frame(self.canvas, bg="#e6e6e6", height=total_height)

        # Create window inside canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor=tk.NW)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Place canvas and scrollbar
        self.canvas.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.47)
        self.scrollbar.place(relx=0.95, rely=0.2, relwidth=0.03, relheight=0.47)

        self.init_headers()
        self.add_entries(num_entries)
        year = self.year_entry.get().strip()
        month = self.month_entry.get().strip()
        if year and month:
            self.yearmonth = year + month

    # Creating entries
    def add_entries(self, num_entries):
        for i in range(1, num_entries):
            label = tk.Label(self.scrollable_frame, bg="#e6e6e6", height=2)
            label.grid(row=i, column=0, padx=10)

    # Table Header Creation
    def init_headers(self):
        self.headers = []  
        headers = ["Date", "Clock In", "Clock Out", "WorkTime", "Memo"]
        headers_widths = [int(self.main_app.width/600*40), int(self.main_app.width/600*60), int(self.main_app.width/600*60), int(self.main_app.width/600*50), int(self.main_app.width/600*240)]
        for col, header in enumerate(headers):
            label = customtkinter.CTkLabel(self.scrollable_frame, text=header, font=("Arial", 15), text_color="black", fg_color="transparent", width=headers_widths[col])
            label.grid(row=0, column=col, padx=10, pady=10, sticky="w")
            self.headers.append(label)  

    # Update yearmonth
    def update_yearmonth(self):
        year = self.year_entry.get().strip()
        month = self.month_entry.get().strip()
        if year and month:
            self.yearmonth = year + month
            self.load_data()

    # Obtain the user ID of the user whose attendance is to be displayed 
    def get_user_id(self):
        new_user_id = self.main_app.get_loginuserid()
        self.user_id = new_user_id
        self.entry_keyboard()
        self.load_data()

    # Scrollbar settings
    def update_scrollregion(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # Create an entry with attendance information obtained from DB as initial value
    def update_entries(self, year, month):
        self.clear_entries()  

        year = int(year)  
        month = int(month)
        num_days = calendar.monthrange(year, month)[1]  
        dates = {} 
        self.entries_time = {}
        for day in range(1, num_days + 1):
            day_key = f"{day:02}"
            dates[day_key] = [day_key, None, None, None, None]

        attendance_data = fetch_user_attendance1(self.user_id, f"{year}{month:02}")
        if attendance_data:
            for data in attendance_data:
                date_key = f"{data[0]:02}"
                if date_key in dates:
                    existing_list = dates[date_key]
                    for index in range(1, len(data)):
                        existing_list[index] = data[index]

        for i, date in enumerate(sorted(dates.keys(), key=int), start=1):  
            data = dates[date]
            row_entries = []
            for j in range(5): 
                entry_width = [int(self.main_app.width/600*40), int(self.main_app.width/600*60), int(self.main_app.width/600*60), int(self.main_app.width/600*50), int(self.main_app.width/600*240)][j]
                keyboard = self.keyboard_time if j < 4 else self.keyboard_general
                if j == 0:
                    widget = customtkinter.CTkLabel(self.scrollable_frame, text=date, font=("Arial", 12), width=entry_width, text_color="black", fg_color="transparent")
                    widget.grid(row=i, column=j, padx=10, pady=5, sticky="w")
                    row_entries.append((widget, None))
                else:
                    widget = customtkinter.CTkEntry(self.scrollable_frame, font=("Arial", 12), width=entry_width, validate="key", validatecommand=self.vcmd50 if j == 4 else self.vcmd5)
                    if data[j] is not None:
                        widget.insert(0, str(data[j])) 
                    widget.grid(row=i, column=j, padx=10, pady=5)
                    self.entries_time[widget] = j
                    row_entries.append((widget, keyboard))
            self.entries.append(row_entries)

        self.update_scrollregion()

    # Delete entry
    def clear_entries(self):
        for row_entries in self.entries:
            for widget, keyboard in row_entries:
                widget.destroy()
        self.entries = []

    # # Update yearmonth
    def load_data(self):
        self.update_entries(self.year_entry.get(), self.month_entry.get())
        
    #VirtualKeyboard Settings
    def entry_keyboard(self):
        self.keyboard_general = VirtualKeyboard(self)  
        self.keyboard_time = VirtualKeyboardTime(self, self.process_key_press)
        
        self.keyboard_is_visible = False
        self.current_keyboard = None
        self.current_entry = None 

        self.bind_all("<Button-1>", self.global_click)

    def global_click(self, event):
        x, y = event.x_root, event.y_root

        kx, ky, kw, kh = self.keyboard_general.winfo_rootx(), self.keyboard_general.winfo_rooty(), self.keyboard_general.winfo_width(), self.keyboard_general.winfo_height()
        if kx <= x <= kx + kw and ky <= y <= ky + kh:
            return 
        
        kx, ky, kw, kh = self.keyboard_time.winfo_rootx(), self.keyboard_time.winfo_rooty(), self.keyboard_time.winfo_width(), self.keyboard_time.winfo_height()
        if kx <= x <= kx + kw and ky <= y <= ky + kh:
            return 

        entry_clicked = None
        keyboard_to_use = None

        for row_entries in self.entries:
            for widget, keyboard in row_entries:
                if widget:
                    ex, ey, ew, eh = widget.winfo_rootx(), widget.winfo_rooty(), widget.winfo_width(), widget.winfo_height()
                    if ex <= x <= ex + ew and ey <= y <= ey + eh:
                        entry_clicked = widget
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

    def auto_insert_colon(self, widget):
        content = widget.get()
        if len(content) == 2 and ':' not in content:
            content += ':'
            widget.delete(0, 'end')
            widget.insert(0, content)

    def process_key_press(self, entry, char):
        entry.insert(tk.END, char)
        if self.entries_time.get(entry) in (1, 2):
            self.auto_insert_colon(entry)

    
    # Value initialization, remove keybord settings and screen transitons
    def back_screen(self):
        if self.screen_flag: 
            self.year_entry.delete(0, tk.END)
            self.year_entry.insert(0, str(self.current_year))
            self.month_entry.delete(0, tk.END)
            self.month_entry.insert(0, f"{self.current_month:02}")
            self.unbind_all("<Button-1>")
            loginuseradminflag = self.main_app.get_loginuseradminflag()
            
            if loginuseradminflag:
                self.main_app.show_next_screen(4)
            else:
                self.main_app.show_next_screen(5)

    # Creating a save confirmation frame
    def save_changes(self):
        if self.flag:
            self.message_frame1 = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*500), height=int(self.main_app.height/500*250), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame1.place(relx=0.1, rely=0.25)

            ask_label = customtkinter.CTkLabel(master=self.message_frame1, text="Are you sure you want to Save these changes?", font=("Arial", 20), text_color="black")
            ask_label.place(relx=0.25, rely=0.35)

            # Add Button "ok"
            btn_ok = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.save_data(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.7, rely=0.75)

            # Add Button "Cancel"
            btn_Cancel = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.cancel(), text="Cancel", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_Cancel.place(relx=0.1, rely=0.75)
            self.flag = False
            self.screen_flag = False
        
    # Set flags and remove frame
    def cancel(self):
        self.flag = True
        self.screen_flag = True
        self.message_frame1.destroy()

    # Save to DB
    def save_data(self):
        if self.save_flag:
            self.save_flag = False
            for row_entries in self.entries:
                date = row_entries[0][0].cget('text') 
                clock_in = row_entries[1][0].get()    
                clock_out = row_entries[2][0].get()   
                work_time = row_entries[3][0].get()   
                memo = row_entries[4][0].get()         
                update_user_attendance(self.user_id, self.yearmonth, date, clock_in, clock_out, work_time, memo)
            self.message_frame = customtkinter.CTkFrame(master=self.message_frame1,width=int(self.main_app.width/600*450), height=int(self.main_app.height/500*200), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame.place(relx=0.07, rely=0.15)
            success_label = customtkinter.CTkLabel(master=self.message_frame, text="These changes has been updated successfully.", font=("Arial", 20), text_color="black")
            success_label.place(relx=0.23, rely=0.3)
            btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.destroy_message_frame1(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.42, rely=0.7)

    # Set flag and remove
    def destroy_message_frame1(self):
        self.flag = True
        self.save_flag = True
        self.screen_flag = True
        self.message_frame1.destroy()

    # Enter the value selected in the list
    def select_year(self, event):
        selected_year = self.year_listbox.get(tk.ACTIVE)
        self.year_entry.delete(0, tk.END)
        self.year_entry.insert(0, selected_year)
        self.show_year_menus()
        self.update_yearmonth()

    def select_month(self, event):
        selected_month = self.month_listbox.get(tk.ACTIVE)
        self.month_entry.delete(0, tk.END)
        self.month_entry.insert(0, selected_month)
        self.show_month_menus()
        self.update_yearmonth()

    # Showing and Hiding Lists
    def show_year_menus(self):
        if not self.year_frame.winfo_ismapped():
            self.year_frame.place(relx=0.45, rely=0.17)
            self.year_listbox.pack(side="left")
            self.year_scrollbar.pack(side="right", fill="y")
        else:
            self.year_frame.place_forget()

    def show_month_menus(self):
        if not self.month_frame.winfo_ismapped():
            self.month_frame.place(relx=0.69, rely=0.17)
            self.month_listbox.pack(side="left")
            self.month_scrollbar.pack(side="right", fill="y")
        else:
            self.month_frame.place_forget()