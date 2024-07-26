import tkinter as tk
import customtkinter
import os
from tkinter import messagebox
from PIL import Image, ImageTk
import XFace_Database_Function
from io import BytesIO 
from Virtual_Keyboard import VirtualKeyboard
from Virtual_Keyboard_Number import VirtualKeyboardNumber

class Screen14(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

        # Initial value of flag
        self.flag = True
        self.user_name_flag = True
        self.department_name_flag = True
        self.current_password_flag = True
        self.screen_flag = True

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        step_frame = customtkinter.CTkFrame(master=self, width=int(self.main_app.width/600*600), height=int(self.main_app.height/500*50), fg_color="#e6e6e6", corner_radius=0)
        step_frame.place(relx=0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(self, command= lambda: self.back_screen(), width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        # Add Date Label
        date_label = customtkinter.CTkLabel(master=step_frame, text="Edit User information", text_color="black", font=("Arial", 20))
        date_label.place(relx=0.098, rely=0.35)

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        # Add Frame Step Frame 2
        self.step_frame2 = customtkinter.CTkFrame(master=self, width=int(self.main_app.width/600*600), height=int(self.main_app.height/500*200), fg_color="#e6e6e6", corner_radius=0)
        self.step_frame2.place(relx=0,rely=0.1)

        # Add Profile Picture
        self.profile_picture = tk.Label(self.step_frame2, width=175, height=175, borderwidth=0, bg="white")
        self.profile_picture.place(relx=0.15, rely=0.1)

        # Add Text "User Name"
        name_label = customtkinter.CTkLabel(master=self.step_frame2, text="User Name", font=("Arial", 20), text_color="black")
        name_label.place(relx=0.45, rely=0)

        vcmd50 = (self.register(self.main_app.limit_char50), '%P')
        vcmd6 = (self.register(self.main_app.limit_char6), '%P')

        # Add Text Entry for User Name
        self.username_entrybox = customtkinter.CTkEntry(master=self.step_frame2, width=int(self.main_app.width/600*300) , height=int(self.main_app.height/500*30), text_color="black", font=("Arial", 15), validate="key", validatecommand=vcmd50)
        self.username_entrybox.place(relx=0.45, rely=0.125)

        # Add Text "Password"
        name_label = customtkinter.CTkLabel(master=self.step_frame2, text="Password", font=("Arial", 20), text_color="black")
        name_label.place(relx=0.45, rely=0.275)

        # Add Text Entry for Password
        self.password_entrybox = customtkinter.CTkEntry(master=self.step_frame2, width=int(self.main_app.width/600*300), height=int(self.main_app.height/500*30), text_color="black", font=("Arial", 15), validate="key", validatecommand=vcmd6)
        self.password_entrybox.place(relx=0.45, rely=0.4)

        # Add Text "Department"
        Department_label = customtkinter.CTkLabel(master=self.step_frame2, text="Department", font=("Arial", 20), text_color="black")
        Department_label.place(relx=0.45, rely=0.55)

        # Add ComboBox for Department
        self.department_entrybox = customtkinter.CTkEntry(master=self.step_frame2, width=int(self.main_app.width/600*300) , height=int(self.main_app.height/500*30), text_color="black", font=("Arial", 15))
        self.department_entrybox.place(relx=0.45, rely=0.7)
        self.department_button = customtkinter.CTkButton(master=self.step_frame2, text="▼", command=self.show_department_menus, text_color="black", font=("Arial",15), fg_color="white", width=int(self.main_app.width/600*35), height=int(self.main_app.height/500*30), cursor="hand2")
        self.department_button.place(relx=0.895, rely=0.7)

        #----------------------------------------------------------------------------
        #                                     Frame 3
        #----------------------------------------------------------------------------

        # Add Frame Step Frame 3
        self.step_frame3 = customtkinter.CTkFrame(master=self, width=int(self.main_app.width/600*600), height=int(self.main_app.height/500*250), fg_color="#e6e6e6", corner_radius=0)
        self.step_frame3.place(relx=0,rely=0.5)

        # Add Edit Facial information
        edit_facial_label = customtkinter.CTkLabel(master=self.step_frame3, text="Edit Facial information", text_color="black", font=("Arial", 20))
        edit_facial_label.place(relx=0.098, rely=0)

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")
        cam_path = os.path.join(images_folder, "camera.png")
        img_path = os.path.join(images_folder, "image.png")

        # Add Image  
        self.cam_image = tk.PhotoImage(file=cam_path)
        self.img_image = tk.PhotoImage(file=img_path) 
        # Camera Button
        cam_btn = tk.Button(self.step_frame3, image=self.cam_image, borderwidth=0, width=int(self.main_app.width/600*150), height=int(self.main_app.height/500*140), command=lambda:self.next_screen_photoshot(21), cursor="hand2")
        cam_btn.place(relx=0.1, rely=0.2)

        # Add Image  
        img_btn = tk.Button(self.step_frame3, image=self.img_image, borderwidth=0, width=int(self.main_app.width/600*150), height=int(self.main_app.height/500*140), command=self.create_usb_loading, cursor="hand2")
        img_btn.place(relx=0.433, rely=0.2)
        
        # Add Button "Save"
        btn_save = customtkinter.CTkButton(master=self.step_frame3, command= lambda:self.save(13), width=int(self.main_app.width/600*80), text="Save", font=("Arial", 20), text_color="black", corner_radius=15, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
        btn_save.place(relx=0.8, rely=0.64)

        # Initialize department Frame with Listbox and Scrollbar
        self.department_frame = tk.Frame(self, bg="#424242")
        self.department_listbox = tk.Listbox(self.department_frame, font=("Arial", 15), width=int(self.main_app.width/600*25), height=3)
        department_names = XFace_Database_Function.fetch_departmentname()
        for department in department_names:
            self.department_listbox.insert("end", department)
        self.department_listbox.bind("<Double-Button-1>", self.select_department)
        self.department_scrollbar = tk.Scrollbar(self.department_frame, orient="vertical", command=self.department_listbox.yview)
        self.department_listbox.config(yscrollcommand=self.department_scrollbar.set)

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
            self.username_entrybox: self.keyboard_general,
            self.password_entrybox: self.keyboard_number
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
            
    # Create Error Frames
    def create_error_frame(self):

        self.error_frame = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*500), height=int(self.main_app.height/500*250), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
        self.error_frame.place(relx=0.1, rely=0.25)

        # Add Error label1
        error_label1 = customtkinter.CTkLabel(master=self.error_frame, text="A face was not detected in the image.", font=("Arial", 25), text_color="black", justify="center")
        error_label1.place(relx=0.1, rely=0.3)

        # Add Error label2
        error_label2 = customtkinter.CTkLabel(master=self.error_frame, text="Please select the photo again.", font=("Arial", 25), text_color="black", justify="center")
        error_label2.place(relx=0.2, rely=0.4)

        # Add Button "OK"
        btn_ok = customtkinter.CTkButton(master=self.error_frame, width=int(self.main_app.width/600*80), command=self.destroy_error_frame, text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=1)
        btn_ok.place(relx=0.75, rely=0.75)

    # Remove keybord settings and screen transitions 
    def create_usb_loading(self):
        self.unbind_all("<Button-1>") 
        self.main_app.show_next_screen(11)

    # Remove frame
    def destroy_error_frame(self):
        if self.error_frame:
            self.error_frame.destroy()

    # Deletion of "photoget_edit.png"files and frame and set flag and screen transitions
    def back_screen(self): 
        if self.flag:
            
            current_directory = os.getcwd()
            target_path = 'photoget_edit/photoget_edit.png'
            target_file_path = os.path.join(current_directory, target_path)
            if os.path.exists(target_file_path):
                os.remove(target_file_path)
            self.unbind_all("<Button-1>")
            self.user_name_flag = True
            self.department_name_flag = True
            self.current_password_flag = True

            loginuseradminflag = self.main_app.get_loginuseradminflag()
            if loginuseradminflag:
                self.main_app.show_next_screen(13)
            else:
                self.main_app.show_next_screen(5) 
    
    # Save encoding data to pickle file and input values to DB and deletion of "photoget_edit.png"files
    def save(self, index):
        new_username, password, department = self.username_entrybox.get(), self.password_entrybox.get(), self.department_entrybox.get()
        if self.flag:
            if new_username == "" or len(password) < 6:
                self.message_frame = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
                self.message_frame.place(relx=0.25, rely=0.32)
                success_label = customtkinter.CTkLabel(master=self.message_frame, text="Please confim the UserName and Password.", font=("Arial", 20), text_color="black")
                success_label.place(relx=0.05, rely=0.3)
                btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.destroy_message_frame_noencoding(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                btn_ok.place(relx=0.34, rely=0.7)
                self.flag = False
            else:
                userinfo = XFace_Database_Function.fetch_userinfo_by_userid(self.usern_id_txt)
                userid, username, _, _, adminflag, face_photo = userinfo[0]
                check_encodings_flag = self.main_app.check_encodings_main("edit")
                if check_encodings_flag:
                    flag, face_photo_retake = self.main_app.get_registerfacephoto(userid, new_username, adminflag, "edit")
                    if flag:
                        XFace_Database_Function.update_userinfo(userid, new_username, password, department, adminflag, face_photo_retake)
                    else:
                        XFace_Database_Function.update_userinfo(userid, new_username, password, department, adminflag, face_photo)
                    self.username_entrybox.delete(0, tk.END)
                    self.password_entrybox.delete(0, tk.END)
                    self.department_entrybox.delete(0, tk.END)
                    current_directory = os.getcwd()
                    target_path = 'photoget_edit/photoget_edit.png'
                    target_file_path = os.path.join(current_directory, target_path)
                    if os.path.exists(target_file_path):
                        os.remove(target_file_path)

                    self.message_frame = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
                    self.message_frame.place(relx=0.25, rely=0.32)
                    success_label = customtkinter.CTkLabel(master=self.message_frame, text="Updated successfully.", font=("Arial", 20), text_color="black")
                    success_label.place(relx=0.25, rely=0.3)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.destroy_message_frame(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.34, rely=0.7)
                    self.flag = False
                else:
                    self.message_frame = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*150), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
                    self.message_frame.place(relx=0.25, rely=0.32)
                    success_label = customtkinter.CTkLabel(master=self.message_frame, text="Not get encodedata. Try again", font=("Arial", 20), text_color="black")
                    success_label.place(relx=0.17, rely=0.3)
                    btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.destroy_message_frame_noencoding(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
                    btn_ok.place(relx=0.34, rely=0.7)
                    self.flag = False

    # Deletion of "photoget_edit.png"files and frame and set flag and screen transitions
    def destroy_message_frame(self):
        self.flag = True
        self.user_name_flag = True
        self.department_name_flag = True
        self.current_password_flag = True
        self.message_frame.destroy()
        self.unbind_all("<Button-1>") 
        loginuseradminflag = self.main_app.get_loginuseradminflag()
        if loginuseradminflag:
            self.main_app.show_next_screen(13)
        else:
            self.main_app.show_next_screen(5)

    # Set flags and remove frame
    def destroy_message_frame_noencoding(self):
        self.flag = True
        self.message_frame.destroy()

    # Remove keybord settings and set flag and screen transitons
    def next_screen_photoshot(self,index):
        if self.screen_flag:
            self.screen_flag = False
            self.unbind_all("<Button-1>") 
            self.main_app.show_next_screen(index)

    # Obtaining the user ID to be edited
    def get_user_id(self):
        self.usern_id_txt = self.main_app.get_edit_user_id()

    # Retrieve the entered value
    def get_department_name(self):
        if self.department_name_flag:
            self.department_name_flag = False
            self.department_entrybox_txt = self.main_app.get_edit_department_name()
            self.department_entrybox.delete(0, tk.END) 
            self.department_entrybox.insert(0, self.department_entrybox_txt)
        else:
            pass

    def get_user_name(self):
        if self.user_name_flag:
            self.user_name_flag = False
            self.username_entrybox_txt = self.main_app.get_edit_user_name()
            self.username_entrybox.delete(0, tk.END)
            self.username_entrybox.insert(0, self.username_entrybox_txt)
        else:
            pass

    def get_current_password(self):
        if self.current_password_flag:
            self.current_password_flag = False
            self.password_entrybox_txt = self.main_app.get_edit_current_password()
            self.password_entrybox.delete(0, tk.END)
            self.password_entrybox.insert(0, self.password_entrybox_txt)
        else:
            pass

    # Display acquired images on screen
    def get_facephoto(self):
        flag, profile_path = self.main_app.get_photopath("edit")
        
        if flag:
            profile_image = Image.open(profile_path)
            resized_image = profile_image.resize((175, 175), Image.Resampling.LANCZOS)
            self.portrait_image = ImageTk.PhotoImage(resized_image)
        else:
            user_name = self.main_app.get_edit_user_name()
            photo_data = XFace_Database_Function.fetch_facephoto_by_username(user_name)
            if photo_data and photo_data[0]:
                portrait_image = Image.open(BytesIO(photo_data[0]))
                resized_image = portrait_image.resize((200,200), Image.Resampling.LANCZOS)
                self.portrait_image = ImageTk.PhotoImage(resized_image)
            else:
                not_found_image = Image.open('XFace_User_List/images/loading.png')  
                resized_image = not_found_image.resize((120,120), Image.Resampling.LANCZOS)
                self.portrait_image = ImageTk.PhotoImage(resized_image)

        self.profile_picture.configure(image=self.portrait_image)
        
    # Enter the value selected in the list
    def select_department(self, event):
        selected_department = self.department_listbox.get(tk.ACTIVE)
        self.department_entrybox.delete(0, tk.END)
        self.department_entrybox.insert(0, selected_department)
        self.show_department_menus()

    # Showing and Hiding Lists
    def show_department_menus(self):
        if not self.department_frame.winfo_ismapped():
            self.department_listbox.delete(0, 'end')
            department_names = XFace_Database_Function.fetch_departmentname()
            for department in department_names:
                self.department_listbox.insert("end", department)
            self.department_frame.place(relx=0.45, rely=0.44)
            self.department_listbox.pack(side="left")
            self.department_scrollbar.pack(side="right", fill="y")
        else:
            self.department_frame.place_forget()

    # Set screen_flag
    def set_screen_flag(self):
        self.screen_flag = True