from tkinter import messagebox
import tkinter as tk
import customtkinter
import XFace_Database_Function
from PIL import Image

class Screen3(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)
        
        # Count for length password
        self.user_id_count = 0
        self.password_count = 0

        # Initial value
        self.user_id = ""
        self.password = ""
        self.password_visible = False

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Password Frame
        self.password_frame = customtkinter.CTkFrame(self, width=int(self.main_app.width/600*350), height=int(self.main_app.height/500*500), fg_color="#424242", corner_radius=0)
        self.password_frame.place(relx=0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(self, command= lambda: self.back_screen(), width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), text="<", text_color="white", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        # Add Password Label
        password_label = customtkinter.CTkLabel(self.password_frame, text_color="#a8a8a8", text="UserID", font=("Arial", 20))
        password_label.place(relx=0.086, rely=0.236)

        #--------------------------------------------
        #               Password Canvas
        #--------------------------------------------

        # Create Canvas
        canvas = customtkinter.CTkCanvas(
            self.password_frame,
            width = 600,
            height = 10,
            bg = "#424242",
            highlightthickness = 0,
            bd = 0
        )
        canvas.place(relx=0.077, rely=0.39)

        # Add Line
        canvas.create_line(5, 5, 73, 5, width=0.5, fill="white")
        canvas.create_line(90, 5, 158, 5, width=0.5, fill="white")
        canvas.create_line(175, 5, 243, 5, width=0.5, fill="white")
        canvas.create_line(260, 5, 328, 5, width=0.5, fill="white")
        canvas.create_line(345, 5, 413, 5, width=0.5, fill="white")
        canvas.create_line(430, 5, 498, 5, width=0.5, fill="white")

        # Add New Password Label
        user_id_label = customtkinter.CTkLabel(self.password_frame, text_color="#a8a8a8", text="Password", font=("Arial", 20))
        user_id_label.place(relx=0.086, rely=0.44)

        eye_slash_icon = Image.open('XFace_Login/images/eye_slash_icon.png')  
        resized_eye_slash_icon = eye_slash_icon.resize((20,20), Image.Resampling.LANCZOS)
        self.eye_slash_icon = customtkinter.CTkImage(light_image=resized_eye_slash_icon)

        eye_icon = Image.open('XFace_Login/images/eye_icon.png')  
        resized_eye_icon = eye_icon.resize((20,20), Image.Resampling.LANCZOS)
        self.eye_icon = customtkinter.CTkImage(light_image=resized_eye_icon)

        self.toggle_visibility_btn = customtkinter.CTkButton(self, image=self.eye_slash_icon, text="", fg_color="#424242", width=int(self.main_app.width/600*50), command=self.toggle_password_visibility, corner_radius=10, hover_color="gray", cursor="hand2")
        self.toggle_visibility_btn.place(relx=0.233, rely=0.44)

        #--------------------------------------------
        #             New Password Canvas
        #--------------------------------------------

        # Create Canvas
        canvas2 = customtkinter.CTkCanvas(
            self.password_frame,
            width = 600,
            height = 10,
            bg = "#424242",
            highlightthickness = 0,
            bd = 0
        )
        canvas2.place(relx=0.077, rely=0.59)

        # Add Line
        canvas2.create_line(5, 5, 73, 5, width=1, fill="white")
        canvas2.create_line(90, 5, 158, 5, width=1, fill="white")
        canvas2.create_line(175, 5, 243, 5, width=1, fill="white")
        canvas2.create_line(260, 5, 328, 5, width=1, fill="white")
        canvas2.create_line(345, 5, 413, 5, width=1, fill="white")
        canvas2.create_line(430, 5, 498, 5, width=1, fill="white")

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------
        # Add Numpad Frame
        self.numpad_frame = customtkinter.CTkFrame(self, width=int(self.main_app.width/600*240), height=int(self.main_app.height/500*305), fg_color="#424242", corner_radius=0)
        self.numpad_frame.place(relx=0.6, rely=0.2)

        #--------------------------------------------
        #                   Numpad
        #--------------------------------------------

        num1_btn = customtkinter.CTkButton(master=self.numpad_frame, text="1", text_color="black", font=("Tahoma", 35), width=int(self.main_app.width/600*75), height=int(self.main_app.height/500*75), fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num1_btn.grid(row=1, column=1)

        num2_btn = customtkinter.CTkButton(master=self.numpad_frame, text="2", text_color="black", font=("Tahoma", 35), width=int(self.main_app.width/600*75), height=int(self.main_app.height/500*75), fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num2_btn.grid(row=1, column=2, padx=1)

        num3_btn = customtkinter.CTkButton(master=self.numpad_frame, text="3", text_color="black", font=("Tahoma", 35), width=int(self.main_app.width/600*75), height=int(self.main_app.height/500*75), fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num3_btn.grid(row=1, column=3)

        num4_btn = customtkinter.CTkButton(master=self.numpad_frame, text="4", text_color="black", font=("Tahoma", 35), width=int(self.main_app.width/600*75), height=int(self.main_app.height/500*75), fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num4_btn.grid(row=2, column=1, pady=1)

        num5_btn = customtkinter.CTkButton(master=self.numpad_frame, text="5", text_color="black", font=("Tahoma", 35), width=int(self.main_app.width/600*75), height=int(self.main_app.height/500*75), fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num5_btn.grid(row=2, column=2, padx=1, pady=1)

        num6_btn = customtkinter.CTkButton(master=self.numpad_frame, text="6", text_color="black", font=("Tahoma", 35), width=int(self.main_app.width/600*75), height=int(self.main_app.height/500*75), fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num6_btn.grid(row=2, column=3, pady=1)

        num7_btn = customtkinter.CTkButton(master=self.numpad_frame, text="7", text_color="black", font=("Tahoma", 35), width=int(self.main_app.width/600*75), height=int(self.main_app.height/500*75), fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num7_btn.grid(row=3, column=1)

        num8_btn = customtkinter.CTkButton(master=self.numpad_frame, text="8", text_color="black", font=("Tahoma", 35), width=int(self.main_app.width/600*75), height=int(self.main_app.height/500*75), fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num8_btn.grid(row=3, column=2, padx=1)

        num9_btn = customtkinter.CTkButton(master=self.numpad_frame, text="9", text_color="black", font=("Tahoma", 35), width=int(self.main_app.width/600*75), height=int(self.main_app.height/500*75), fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num9_btn.grid(row=3, column=3)

        del_btn = customtkinter.CTkButton(master=self.numpad_frame, text="⌫", text_color="black", font=("Tahoma", 30), width=int(self.main_app.width/600*75), height=int(self.main_app.height/500*75), fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        del_btn.grid(row=4, column=1, pady=1)

        num0_btn = customtkinter.CTkButton(master=self.numpad_frame, text="0", text_color="black", font=("Tahoma", 35), width=int(self.main_app.width/600*75), height=int(self.main_app.height/500*75), fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num0_btn.grid(row=4, column=2, padx=1, pady=1)

        def add_to_password(number):

            if (self.user_id_count < 6):
                # Add number to userid
                self.user_id += str(number)

            if (self.user_id_count == 6):

                if (self.password_count < 6):

                    # Add number to password
                    self.password += str(number)
                      
            # Run Function display_userid_and_password
            self.display_userid_and_password()

            print("----------------------")
            print("Count UserID : ",self.user_id_count)
            print("Count Password : ",self.password_count)
            print("----------------------")
            print("UserID : ",self.user_id)
            print("Password : ",self.password)
        
        # Set function number pad
        num1_btn.configure(command=lambda: add_to_password(1))
        num2_btn.configure(command=lambda: add_to_password(2))
        num3_btn.configure(command=lambda: add_to_password(3))
        num4_btn.configure(command=lambda: add_to_password(4))
        num5_btn.configure(command=lambda: add_to_password(5))
        num6_btn.configure(command=lambda: add_to_password(6))
        num7_btn.configure(command=lambda: add_to_password(7))
        num8_btn.configure(command=lambda: add_to_password(8))
        num9_btn.configure(command=lambda: add_to_password(9))
        num0_btn.configure(command=lambda: add_to_password(0))
        del_btn.configure(command=lambda: delete_from_password())

        def delete_from_password():
            if self.user_id:

                if not self.password:

                    # Delete New Password Right Position
                    self.user_id = self.user_id[:-1]

                    # Delete New Password From Screen
                    last_widget_index = len(self.password_frame.winfo_children()) - 1
                    last_label_widget = self.password_frame.winfo_children()[last_widget_index]
                    last_label_widget.destroy()
                
                    # Reduce New Password Count -1
                    self.user_id_count -= 1

                if self.password:

                    # Delete Retype Password Right Position
                    self.password = self.password[:-1]

                    # Delete Retype Password From Screen
                    last_widget_index = len(self.password_frame.winfo_children()) - 1
                    last_label_widget = self.password_frame.winfo_children()[last_widget_index]
                    last_label_widget.destroy()
                
                    # Reduce Retype Password Count -1
                    self.password_count -= 1

    # Clear password and reset count
    def clear_password(self, frame):
        self.user_id_count = 0
        self.password_count = 0
        self.user_id = ""
        self.password = "" 

        for child in frame.winfo_children():
            if isinstance(child, customtkinter.CTkLabel) and child.cget("text") not in ["UserID", "Password"]:
                child.destroy()

    # Show/hide passwords 
    def update_password_display(self):
        for child in self.password_frame.winfo_children():
            if isinstance(child, customtkinter.CTkLabel) and child.winfo_y() == 306: 
                child.destroy()

        for i in range(len(self.password)):
            display_text = self.password[i] if self.password_visible else "*"
            password_label = customtkinter.CTkLabel(self.password_frame, text_color="#a8a8a8", text=display_text, font=("Arial", 30))
            password_label.place(relx=0.13+i*0.143, rely=0.51)

    
    def toggle_password_visibility(self):
        self.password_visible = not self.password_visible
        if self.password_visible:
            self.toggle_visibility_btn.configure(image=self.eye_icon)
        else:
            self.toggle_visibility_btn.configure(image=self.eye_slash_icon)
        self.update_password_display() 

    # User ID and pasword entry display
    def display_userid_and_password(self):

        # Check length password
        if (self.user_id_count < 6):
            
            if len(self.user_id) >= self.user_id_count + 1:

                # Add Password on Screen
                user_id_label = customtkinter.CTkLabel(self.password_frame, text_color="#a8a8a8", text=self.user_id[self.user_id_count], font=("Arial", 30))
                user_id_label.place(relx=0.13+self.user_id_count*0.143, rely=0.31)

                # Count New Password Add
                self.user_id_count += 1

        if (self.user_id_count == 6):

            if (self.password_count < 6):

                # Show Retype Password In Terminal
                print("Password:", self.password)
                print("----------------------")
        
                if len(self.password) >= self.password_count + 1:

                    # Add Password on Screen
                    display_text = self.password[self.password_count] if self.password_visible else "*"
                    password_label = customtkinter.CTkLabel(self.password_frame, text_color="#a8a8a8", text=display_text, font=("Arial", 30))
                    password_label.place(relx=0.13+self.password_count*0.143, rely=0.51)
                    # Count Retype Password Add
                    self.password_count += 1

        if self.user_id_count + self.password_count  == 12:
            self.check_password() 
    
    # Check entered user ID, password and DB data
    def check_password(self):

        print("UserID Final: ", self.user_id)
        print("Password Final: ", self.password)
        print("----------------------")

        userid = self.user_id
        password = self.password
        user = XFace_Database_Function.check_user(userid, password)

        if user:
            self.clear_password(self.password_frame)
            self.main_app.set_loginuseradminflag(user[4])
            self.main_app.set_loginuserid(userid)
            self.main_app.set_loginusername(user[1])
            self.main_app.show_next_screen(2)
        else:
            self.message_frame = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*325), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame.place(relx=0.57, rely=0.16)
            error_label = customtkinter.CTkLabel(master=self.message_frame, text="Incorrect username or password.", font=("Arial", 20), text_color="black")
            error_label.place(relx=0.15, rely=0.3)
            btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.message_frame.destroy(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.35, rely=0.7)   
 
    # Value initialization and screen transitons
    def back_screen(self):
        self.clear_password(self.password_frame)
        self.main_app.show_next_screen(1)
        