import tkinter as tk
import customtkinter
import os
import XFace_Database_Function
from Virtual_Keyboard import VirtualKeyboard
from PIL import Image
import qrcode

class Screen22(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=self.main_app.width, height=self.main_app.height)
        self.pack_propagate(0)

        # Toggle Confirm
        self.confirm = 0
        
        # Initial value of flag
        self.flag = True
        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Name Frame
        self.name_frame = customtkinter.CTkFrame(master=self, width=int(self.main_app.width/600*290), height=int(self.main_app.height/500*500), fg_color="#e6e6e6", corner_radius=0)
        self.name_frame.place(relx=0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(self, command= lambda: self.back_screen(), width=int(self.main_app.width/600*30), height=int(self.main_app.height/500*30), text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False, cursor="hand2")
        back_btn.place(relx=0.02, rely=0.02)

        # create Button
        create_btn = customtkinter.CTkButton(master=self.name_frame,  command= lambda: self.create_screen(23), text="Create", text_color="black", hover_color="gray", font=("Arial", 20), border_width=0, width=int(self.main_app.width/600*200), height=int(self.main_app.height/500*30), fg_color="white", corner_radius=10, cursor="hand2")
        create_btn.place(relx=0.2, rely=0.05)

        # Add School Name Label
        qrcode_label = customtkinter.CTkLabel(master=self.name_frame, text="QRName", text_color="black", font=("Arial", 20), fg_color="transparent")
        qrcode_label.place(relx=0.2, rely=0.12)

        #Add Entrybox for qrcode
        self.qrcode_entrybox = customtkinter.CTkEntry(master=self.name_frame, width=int(self.main_app.width/600*200), height=int(self.main_app.height/500*30), text_color="black", font=("Arial", 15))
        self.qrcode_entrybox.place(relx=0.2, rely=0.17)        

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")
        search_path = os.path.join(images_folder, "search.png")

        # Add Image
        search_pil_image = Image.open(search_path)
        search_image = customtkinter.CTkImage(search_pil_image)

        # Search Button
        self.search_btn = customtkinter.CTkButton(master=self.name_frame, command=self.search, image=search_image, text="Search", text_color="black", hover_color="gray", font=("Arial", 20), border_width=0, width=int(self.main_app.width/600*110), height=int(self.main_app.height/500*30), fg_color="white", cursor="hand2")
        self.search_btn.place(relx=0.51, rely=0.27)

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        self.info_frame = customtkinter.CTkScrollableFrame(master=self, width=int(self.main_app.width/600*298), height=int(self.main_app.height/500*500), fg_color="#d9d9d9", corner_radius=0)
        self.info_frame.place(relx=0.481)

        self.qrcode_details = XFace_Database_Function.fetch_qrcodeid() 
        self.build_qrcode_frames(self.qrcode_details)

    # Reset frame
    def build_qrcode_frames(self, qrcodes):
        self.clear_qrcode_frames()
        if len(qrcodes) == 1:
            self.add_qrcode_frame(self.info_frame, qrcodes, 1)
        else:
            for index, qrcode in enumerate(qrcodes):
                self.add_qrcode_frame(self.info_frame, qrcode, index)

    # Deleting frames
    def clear_qrcode_frames(self):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

    # Retrieve qrcode to display from DB and create frames
    def search(self):
        qrcodename = self.qrcode_entrybox.get()
        if qrcodename == '':
            qrcodes = XFace_Database_Function.fetch_qrcodeid()
        else:
            qrcodes = XFace_Database_Function.fetch_qrcodeid_by_qrcodename(qrcodename)
        self.build_qrcode_frames(qrcodes)

    # Create frames
    def add_qrcode_frame(self, parent_frame, qrcode_id, tag):
        qrcode_frame = customtkinter.CTkFrame(master=parent_frame, width=int(self.main_app.width/600*250), height=int(self.main_app.height/500*70), fg_color="white", corner_radius=10, border_width=0, border_color="#5cb6f8")
        qrcode_frame.bind('<Button-1>', lambda event: self.toggle_border(qrcode_frame))
        qrcode_frame.tag = tag
        qrcode_frame.pack(padx=10, pady=5)

        canvas = customtkinter.CTkCanvas(
            qrcode_frame,
            width=int(self.main_app.width/600*7),
            height=int(self.main_app.height/500*65),
            bg="#fce467",  # Example background color
            highlightthickness=0,
            bd=0
        )
        canvas.bind('<Button-1>', lambda event: self.toggle_border(qrcode_frame))
        canvas.place(x=15, y=2)

        if isinstance(qrcode_id, list):
            qrcode_id = qrcode_id[0]
        qrcode_name = XFace_Database_Function.fetch_qrcodename_by_qrcodeid(qrcode_id)
        name_label = customtkinter.CTkLabel(master=qrcode_frame, text=f"{qrcode_id}:{qrcode_name}", text_color="black", font=("Arial", 20), fg_color="transparent")
        name_label.bind('<Button-1>', lambda event: self.toggle_border(qrcode_frame))
        name_label.place(x=50, y=10)

    # Toggle setting
    def toggle_border(self, frame):
        if frame._border_width == 0:
            for child in frame.master.winfo_children():
                if isinstance(child, customtkinter.CTkFrame):
                    child.configure(border_width=0)
            frame.configure(border_width=2)
            color = frame.winfo_children()[0].cget("bg")
            name = frame.winfo_children()[1].cget("text")
            index = frame.tag
            self.toggle_detail_frame(1, a=color, b=name, c=index)
        else:
            frame.configure(border_width=0)
            self.toggle_detail_frame(0)

    def toggle_detail_frame(self, toggle, *args, **kwargs):
        if toggle == 1:
            if hasattr(self, 'detail_frame') and self.detail_frame.winfo_exists():
                self.detail_frame.destroy()

            detail_frame = customtkinter.CTkFrame(master=self.name_frame, width=int(self.main_app.width/600*260), height=int(self.main_app.height/500*310), fg_color="white", corner_radius=10, border_width=0)
            detail_frame.place(relx=0.05, rely=0.36)
            name = kwargs.get('b', "")

            number = name.split(':')[0]
            name1 = name.split(':')[1]

            qrinfo = XFace_Database_Function.fetch_qrcode_createdby_id(number)        
    
            qrcodename_detail_label = customtkinter.CTkLabel(master=detail_frame, justify="center", width=int(self.main_app.width/600*260), text=name1, text_color="black", font=("Arial", 25), fg_color="transparent")
            qrcodename_detail_label.place(relx=0, rely=0.2)

            createdby_label = customtkinter.CTkLabel(master=detail_frame, width=int(self.main_app.width/600*260), text=f"Created By:{qrinfo[0]}", text_color="black", font=("Arial", 25), fg_color="transparent")
            createdby_label.place(relx=0, rely=0.4)

            creationedate_label = customtkinter.CTkLabel(master=detail_frame, width=int(self.main_app.width/600*260), text=f"Creation Date:{qrinfo[1]}", text_color="black", font=("Arial", 25), fg_color="transparent")
            creationedate_label.place(relx=0, rely=0.6)

            edit_btn = customtkinter.CTkButton(master=detail_frame, command=lambda: self.reissue_to_usb(number), text="Reissue", text_color="black", hover_color="grey", font=("Arial", 20), border_width=0, width=int(self.main_app.width/600*90), height=int(self.main_app.height/500*30), fg_color="#d9d9d9", cursor="hand2")
            edit_btn.place(relx=0.1, rely=0.85)

            delete_btn = customtkinter.CTkButton(master=detail_frame, command=lambda: self.confirm_delete(number), text="Delete", text_color="black", hover_color="grey", font=("Arial", 20), border_width=0, width=int(self.main_app.width/600*90), height=int(self.main_app.height/500*30), fg_color="#d9d9d9", cursor="hand2")
            delete_btn.place(relx=0.55, rely=0.85)

            self.detail_frame = detail_frame
        else:
            if hasattr(self, 'detail_frame') and self.detail_frame.winfo_exists():
                self.detail_frame.destroy()

    # Creating a deletion confirmation frame
    def confirm_delete(self, name):
        if self.flag:
            self.message_frame1 = customtkinter.CTkFrame(master=self,width=int(self.main_app.width/600*510), height=int(self.main_app.height/500*250), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.message_frame1.place(relx=0.1, rely=0.25)

            ask_label = customtkinter.CTkLabel(master=self.message_frame1, text="Are you sure you want to Delete this data?", font=("Arial", 20), text_color="black")
            ask_label.place(relx=0.25, rely=0.35)

            # Add Button "ok"
            btn_ok = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.delete_data(name), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_ok.place(relx=0.7, rely=0.75)

            # Add Button "Cancel"
            btn_Cancel = customtkinter.CTkButton(master=self.message_frame1, width=int(self.main_app.width/600*80), command=lambda:self.cancel(), text="Cancel", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
            btn_Cancel.place(relx=0.1, rely=0.75)

            self.flag = False
            
    # Set flags and remove frame
    def cancel(self):
        self.flag = True
        self.message_frame1.destroy()

    # Delete data from DB
    def delete_data(self,number):
        XFace_Database_Function.delete_qrcode(number)
        self.message_frame = customtkinter.CTkFrame(master=self.message_frame1,width=int(self.main_app.width/600*450), height=int(self.main_app.height/500*200), fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
        self.message_frame.place(relx=0.07, rely=0.15)
        success_label = customtkinter.CTkLabel(master=self.message_frame, text="This data has been deleted successfully.", font=("Arial", 20), text_color="black")
        success_label.place(relx=0.3, rely=0.3)
        btn_ok = customtkinter.CTkButton(master=self.message_frame, width=int(self.main_app.width/600*80), command=lambda:self.delete_success(), text="OK", font=("Arial", 20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=0, hover_color="gray", cursor="hand2")
        btn_ok.place(relx=0.42, rely=0.7)
    
    # Re-create frame
    def delete_success(self):
        self.flag = True
        self.message_frame1.destroy()
        self.toggle_detail_frame(0)
        qrcodes = XFace_Database_Function.fetch_qrcodeid() 
        self.build_qrcode_frames(qrcodes)
    
    # Get the value of the qrcode to be edited and value initialization and screen transitons
    def reissue_to_usb(self, number):
        get_usbpath, returncode = self.main_app.get_usbpath()
        if returncode == 0:
            qrcode_info = XFace_Database_Function.fetch_qrcode(number)
            qr_name, start_time, end_time, password = qrcode_info
            qr_content = f"{password} Starts:{start_time} End:{end_time}"
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
        #reissue_to_usb 
    def destroy_message_frame(self,get_usbpath):
        self.flag = True
        self.main_app.usb_eject(get_usbpath)
        self.message_frame.destroy()
    
    # Set flags and remove frame
    def cancel2(self):
        self.flag = True
        self.message_frame2.destroy()
        
    # Value initialization and screen transitons
    def create_screen(self, index):
        self.qrcode_entrybox.delete(0, tk.END)
        self.toggle_detail_frame(0)
        self.main_app.show_next_screen(index)

    # Value initialization and screen transitons
    def back_screen(self):
        self.qrcode_entrybox.delete(0, tk.END)
        self.toggle_detail_frame(0)
        self.main_app.show_next_screen(4)

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
            self.qrcode_entrybox: self.keyboard_general
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