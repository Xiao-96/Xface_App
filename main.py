import tkinter as tk
from tkinter import ttk
import customtkinter
import datetime
import os
import cv2
import subprocess
from threading import Timer

from XFace_Face_Recognition.XFace_Face_Recognition import Screen1
from XFace_Face_Recognition.XFace_Face_Recognition_Success import Screen2
from XFace_Login.XFace_Login import Screen3
from XFace_Login.XFace_Menu_Admin import Screen4
from XFace_Login.XFace_Menu_User import Screen5
from XFace_User_Register.XFace_User_Registration_Screen1 import Screen6
from XFace_User_Register.XFace_User_Registration_Screen2 import Screen7
from XFace_User_Register.XFace_User_Registration_Screen2_Error import Screen8
from XFace_User_Register.XFace_User_Registration_Screen3 import Screen9
from XFace_User_Register.XFace_Camera_Register.XFace_Camera_Register_Photo_Shoot import Screen10
from XFace_User_Register.XFace_USB.XFace_USB_Choose_File_Register import Screen12
from XFace_User_List.XFace_User_List import Screen13
from XFace_User_List.XFace_User_List_Edit_Screen import Screen14
from XFace_User_List.XFace_Edit_Register.XFace_Camera_Edit_Photo_Shoot import Screen21
from XFace_User_List.XFace_USB.XFace_USB_Choose_File_Edit import Screen11
from XFace_Department_List.XFace_Department_List import Screen15
from XFace_Department_List.XFace_Department_Registration import Screen16
from XFace_Department_List.XFace_Department_Edit import Screen17
from XFace_Edit_Attendance_Record.XFace_Edit_AttendanceRecord_Screen1 import Screen18
from XFace_ExcelOutput.XFace_ExcelOutput_Admin import Screen19
from XFace_ExcelOutput.XFace_ExcelOutput_User import Screen20
from XFace_QRcode_List.XFace_QRcode_List import Screen22
from XFace_QRcode_List.XFace_QRcode_Registration import Screen23

import CameraRspiPicam

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("XFace Base")
        self.root.geometry("1024x600") 

        # Stored Variables
        self.current_screen = 0
        self.password = ""

        # Initial value of flag
        self.recognitioncamerastartflag = True
        self.updatescreencamerastartflag_register = True

        # Disable window resizing
        self.root.resizable(False, False)
        self.root.overrideredirect(True)

        # Bind the closing event to a function
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Application screen size
        self.width = 1024
        self.height = 600
        
        # Create Canvas widget
        self.canvas = customtkinter.CTkCanvas(self.root, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)

        # Create a Frame inside the Canvas to hold the screens
        self.container = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.container, anchor=tk.NW)

        # Create an instance of Screens
        self.screen1 = Screen1(self.root, self)
        self.screen2 = Screen2(self.root, self)
        self.screen3 = Screen3(self.root, self)
        self.screen4 = Screen4(self.root, self)
        self.screen5 = Screen5(self.root, self)
        self.screen6 = Screen6(self.root, self)
        self.screen7 = Screen7(self.root, self)
        self.screen8 = Screen8(self.root, self)
        self.screen9 = Screen9(self.root, self)
        self.screen10 = Screen10(self.root, self)
        self.screen11 = Screen11(self.root, self)
        self.screen12 = Screen12(self.root, self)
        self.screen13 = Screen13(self.root, self)
        self.screen14 = Screen14(self.root, self)
        self.screen15 = Screen15(self.root, self)
        self.screen16 = Screen16(self.root, self)
        self.screen17 = Screen17(self.root, self)
        self.screen18 = Screen18(self.root, self)
        self.screen19 = Screen19(self.root, self)
        self.screen20 = Screen20(self.root, self)
        self.screen21 = Screen21(self.root, self)
        self.screen22 = Screen22(self.root, self)
        self.screen23 = Screen23(self.root, self)

        # Pack Screens initially
        self.screen1.grid(row=0, column=0, sticky="nsew")

        # Set current screen index
        self.current_screen = 1

        # FaceRecognition start
        self.facerecognition_start()
        
        # Screen1 Camera display start
        self.screen1.photo_update_start()

    def toggle_hdmi(self, state):
        if state == 'off':
            self.root.withdraw()
            os.system('echo "off" | sudo tee /sys/class/drm/card1-HDMI-A-2/status')
        elif state == 'on':
            os.system('echo "on" | sudo tee /sys/class/drm/card1-HDMI-A-2/status')
            self.root.after(500, self.recover_window)

    def schedule_hdmi_control(self):
        Timer(50, self.toggle_hdmi, args=['off']).start()
        
        Timer(55, self.toggle_hdmi, args=['on']).start()

    def recover_window(self):
        self.root.deiconify()

    # Input character limit
    def limit_char5(self,string):
        return len(string) <= 5

    def limit_char6(self,string):
        return len(string) <= 6
    
    def limit_char50(self,string):
        return len(string) <= 50

    def on_close(self):
        # Do whatever you want here, like confirmation dialog or just ignore the event
        #print("Close button clicked. Ignoring window close.")
        pass

    # Variable set
    def set_current_password(self, new_current_password):
        self.current_password = new_current_password
    
    def set_loginuserid(self,login_usernid):
        self.login_userid = login_usernid
    
    def set_loginusername(self,login_username):
        self.login_username = login_username

    def set_loginuseradminflag(self,loginuseradminflag):
        self.loginuseradminflag = loginuseradminflag

    def set_username(self, new_username):
        self.username = new_username
    
    def set_password(self, new_password):
        self.password = new_password

    def set_department(self, new_department):
        self.department = new_department

    def set_administrator(self, new_administartor):
        self.administrator = new_administartor

    def set_department_name(self, new_department_name):
        self.department_name = new_department_name

    def set_start_time(self, new_start_time):
        self.start_time = new_start_time

    def set_end_time(self, new_end_time):
        self.end_time = new_end_time
    
    def set_rest_time(self, new_rest_time):
        self.rest_time = new_rest_time
    
    def set_over_time(self, new_over_time):
        self.over_time = new_over_time

    def set_edit_user_id(self,user_id):
        self.edit_user_id = user_id

    def set_edit_user_name(self,new_user_name):
        self.edit_user_name = new_user_name

    def set_edit_current_password(self,new_current_password):
        self.edit_current_password = new_current_password

    def set_edit_department_name(self,new_department_name):
        self.edit_department_name = new_department_name
 
    # Variable get
    def get_loginusername(self):
        return self.login_username
    
    def get_loginuserid(self):
        return self.login_userid

    def get_loginuseradminflag(self):
        return self.loginuseradminflag

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
    
    def get_department(self):
        return self.department
    
    def get_administrator(self):
        return self.administrator
    
    def get_department_name(self):
        return self.department_name

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time
    
    def get_rest_time(self):
        return self.rest_time
    
    def get_over_time(self):
        return self.over_time
    
    def get_edit_user_id(self):
        return self.edit_user_id
    
    def get_edit_user_name(self):
        return self.edit_user_name

    def get_edit_current_password(self):
        return self.edit_current_password

    def get_edit_department_name(self):
        return self.edit_department_name
    
    # Face Recognition Thread Activation
    def facerecognition_start(self):
        if self.recognitioncamerastartflag:
            self.recognitioncamerastartflag = False
            CameraRspiPicam.facerecognition_start(self)
    
    # Face Recognition Success
    def facerecognition_success(self,login_userid, login_username, login_adminflag):
        self.set_loginuserid(login_userid)
        self.set_loginusername(login_username)
        self.set_loginuseradminflag(login_adminflag)
        self.screen1.next_screen(2)

    # Face Recognition Thread Suspension
    def facerecognition_stop(self):
        if not self.recognitioncamerastartflag:
            print("camera stop1") 
            CameraRspiPicam.facerecognition_stop()
            self.recognitioncamerastartflag = True            
        else:
            print("camera stop2") 
            CameraRspiPicam.facerecognition_stop()                    
    
    # Return the path to the image
    def photo_get(self,register_or_edit):
        current_directory = ""
        photoget_register_path = ""
        photoget_edit_path = ""       
        current_directory = os.path.dirname(os.path.realpath(__file__))
        if register_or_edit == "register":
            photoget_register_path = os.path.join(current_directory, "photoget_register/photoget_register.png")
            return photoget_register_path
        elif register_or_edit == "edit":
            photoget_edit_path = os.path.join(current_directory, "photoget_edit/photoget_edit.png")
            return photoget_edit_path
        else:
            print("directory error")
        
    # Return the path after image acquisition
    def get_photopath(self,register_or_edit):
        current_directory = ""
        photoget_register_path = ""
        photoget_edit_path = ""       
        current_directory = os.path.dirname(os.path.realpath(__file__))
        if register_or_edit == "register":
            photoget_register_path = os.path.join(current_directory, "photoget_register/photoget_register.png")
            return photoget_register_path
        elif register_or_edit == "edit":
            photoget_edit_path = os.path.join(current_directory, "photoget_edit/photoget_edit.png")
            if os.path.exists(photoget_edit_path):
                return True, photoget_edit_path
            else:
                return False, None
        else:
            print("directory error")
    
    # Returns the path to the "Cameralog" directory
    def get_cameralogpath(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        cameralogpath = f"{current_directory}/CameraLog"
        return cameralogpath
    
    # Returns the path to the USB flash drive
    def get_usbpath(self):
        cmd = 'df | grep /dev/sda1'
        try:
            res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        except:
            print("Error")
        print("list.returncode:",res.returncode)
        usb_path = ""
        if res.returncode == 0:
            returncode_list = res.stdout.split()
            print("returncode_list:", returncode_list)
            usb_path = returncode_list[len(returncode_list) - 1]
            print("usb_path:",usb_path)
            return usb_path, res.returncode
        else:
            print("USB no module")
            return usb_path, res.returncode
        
    # Remove the USB memory stick
    def usb_eject(self,path):
        cmd = 'df | grep {}'.format(path)
        try:
            res= subprocess.run(cmd, shell=True, capture_output=True, text=True)
        except:
            print("Eject error")
        if res.returncode == 0:
            #umount_cmd = 'echo guest | sudo eject {}'.format(path)
            umount_cmd = 'gio mount -u {}'.format(path)
            try:
                umount_res= subprocess.run(umount_cmd, shell=True, capture_output=True, text=True)
            except:
                print("Eject error")
            if umount_res.returncode == 0:
                print("eject success")
                power_off_cmd = 'udisksctl power-off -b /dev/sda1'
                try:
                    subprocess.run(power_off_cmd, shell=True, capture_output=True, text=True)
                except Exception as e:
                    print("Power-off error:", e)
            else:
                print("eject fail")
        else:
            print("No eject required")

    # Check if encodings data can be correctly obtained from the image to be registered
    def check_encodings_main(self,register_or_edit):
        current_directory = ""
        photoget_register_path = ""
        photoget_edit_path = ""          
        current_directory = os.path.dirname(os.path.realpath(__file__))
        if register_or_edit == "register":
            photoget_register_path = 'photoget_register/photoget_register.png'
            photoget_register_directory = os.path.join(current_directory, photoget_register_path)   
            check_encodings_flag = CameraRspiPicam.check_encodings_CameraRspiPicam(photoget_register_directory)
            return check_encodings_flag
        elif register_or_edit == "edit":
            photoget_edit_path = 'photoget_edit/photoget_edit.png'
            photoget_edit_directory = os.path.join(current_directory, photoget_edit_path)
            if os.path.exists(photoget_edit_directory):
                check_encodings_flag = CameraRspiPicam.check_encodings_CameraRspiPicam(photoget_edit_directory)
                return check_encodings_flag
            else:
                return True
        else:
            print("directory error")
    
    # Save encoding data to a pickle file and returns a sequence image bytes
    def get_registerfacephoto(self,userid,username,adminflag,register_or_edit):
        current_directory = ""
        photoget_register_path = ""
        photoget_edit_path = ""          
        current_directory = os.path.dirname(os.path.realpath(__file__))
        if register_or_edit == "register":
            photoget_register_path = 'photoget_register/photoget_register.png'
            photoget_register_directory = os.path.join(current_directory, photoget_register_path)   
            CameraRspiPicam.addpickle_CameraRspiPicam(userid,username,adminflag,photoget_register_directory)
            imagefile = cv2.imread(photoget_register_directory)
            _, buffer = cv2.imencode('.png', imagefile)
            return buffer.tobytes()
        elif register_or_edit == "edit":
            photoget_edit_path = 'photoget_edit/photoget_edit.png'
            photoget_edit_directory = os.path.join(current_directory, photoget_edit_path)
            if os.path.exists(photoget_edit_directory):
                CameraRspiPicam.editpickle_CameraRspiPicam(userid,username,adminflag,photoget_edit_directory)
                imagefile = cv2.imread(photoget_edit_directory)
                _, buffer = cv2.imencode('.png', imagefile)
                return True, buffer.tobytes()
            else:
                return False, None
        else:
            print("directory error")

    # Delete registered ebcoding data
    def deletepickle_main_app(self,userid):
        CameraRspiPicam.deletepickle_CameraRspiPicam(userid)

    def show_next_screen(self, index):
        # Hide the current screen
        if self.current_screen == 1:
            self.screen1.grid_remove()
        elif self.current_screen == 2:
            self.screen2.grid_remove()
        elif self.current_screen == 3:
            self.screen3.grid_remove()
        elif self.current_screen == 4:
            self.screen4.grid_remove()
        elif self.current_screen == 5:
            self.screen5.grid_remove()
        elif self.current_screen == 6:
            self.screen6.grid_remove()
        elif self.current_screen == 7:
            self.screen7.grid_remove()
        elif self.current_screen == 8:
            self.screen8.grid_remove()
        elif self.current_screen == 9:
            self.screen9.grid_remove()
        elif self.current_screen == 10:
            self.screen10.grid_remove()
        elif self.current_screen == 11:
            self.screen11.grid_remove()
        elif self.current_screen == 12:
            self.screen12.grid_remove()
        elif self.current_screen == 13:
            self.screen13.grid_remove()
        elif self.current_screen == 14:
            self.screen14.grid_remove()
        elif self.current_screen == 15:
            self.screen15.grid_remove()
        elif self.current_screen == 16:
            self.screen16.grid_remove()
        elif self.current_screen == 17:
            self.screen17.grid_remove()
        elif self.current_screen == 18:
            self.screen18.grid_remove()
        elif self.current_screen == 19:
            self.screen19.grid_remove()
        elif self.current_screen == 20:
            self.screen20.grid_remove()
        elif self.current_screen == 21:
            self.screen21.grid_remove()
        elif self.current_screen == 22:
            self.screen22.grid_remove()
        elif self.current_screen == 23:
            self.screen23.grid_remove()
                
        # Show the next screen
        if index == 1:
            self.screen1.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
            self.facerecognition_start()
            self.screen1.photo_update_start()
        elif index == 2:
            self.screen2.grid(row=0, column=0, sticky="nsew")
            self.screen2.set_time_flag()
            self.screen2.get_username()
            self.screen2.get_timecount()
            self.screen2.timecountup()
            self.current_screen = index
        elif index == 3:
            self.screen3.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 4:
            self.screen4.grid(row=0, column=0, sticky="nsew")
            self.screen4.set_currentdate()
            self.current_screen = index
        elif index == 5:
            self.screen5.grid(row=0, column=0, sticky="nsew")
            self.screen5.set_currentdate()
            self.current_screen = index
        elif index == 6:
            self.screen6.grid(row=0, column=0, sticky="nsew")
            self.screen6.clear_entry_boxes_and_checkbox()
            self.screen6.entry_keyboard()
            self.current_screen = index
        elif index == 7:
            self.screen7.grid(row=0, column=0, sticky="nsew")
            self.screen7.set_screen_flag()
            self.current_screen = index
        elif index == 8:
            self.screen8.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 9:
            self.screen9.grid(row=0, column=0, sticky="nsew")
            self.screen9.get_userid()
            self.screen9.get_username()
            self.screen9.get_password()
            self.screen9.get_department()
            self.screen9.get_facephoto()
            self.screen9.get_administrator()
            self.current_screen = index
        elif index == 10:
            self.screen10.grid(row=0, column=0, sticky="nsew")
            self.screen10.photo_update_start()
            self.current_screen = index
        elif index == 11:
            self.screen11.grid(row=0, column=0, sticky="nsew")
            self.screen11.load_image_buttons()
            self.current_screen = index
        elif index == 12:
            self.screen12.grid(row=0, column=0, sticky="nsew")
            self.screen12.load_image_buttons()
            self.current_screen = index
        elif index == 13:
            self.screen13.search()
            self.screen13.grid(row=0, column=0, sticky="nsew")
            self.screen13.entry_keyboard()
            self.current_screen = index
        elif index == 14:
            self.screen14.set_screen_flag()
            self.screen14.get_user_id()
            self.screen14.get_user_name()
            self.screen14.get_department_name()
            self.screen14.get_current_password()
            self.screen14.get_facephoto()
            self.screen14.grid(row=0, column=0, sticky="nsew")
            self.screen14.entry_keyboard()
            self.current_screen = index
        elif index == 15:
            self.screen15.search()
            self.screen15.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 16:
            self.screen16.grid(row=0, column=0, sticky="nsew")
            self.screen16.entry_keyboard()
            self.current_screen = index
        elif index == 17:
            self.screen17.get_department_name()
            self.screen17.get_start_time()
            self.screen17.get_end_time()
            self.screen17.get_rest_time()
            self.screen17.get_over_time()
            self.screen17.grid(row=0, column=0, sticky="nsew")
            self.screen17.entry_keyboard()
            self.current_screen = index
        elif index == 18:
            self.screen18.get_user_id()
            self.screen18.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 19:
            self.screen19.grid(row=0, column=0, sticky="nsew")
            self.screen19.entry_keyboard()
            self.current_screen = index
        elif index == 20:
            self.screen20.get_user_id()
            self.screen20.entry_keyboard()
            self.screen20.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 21:
            self.screen21.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 22:
            self.screen22.grid(row=0, column=0, sticky="nsew")
            self.screen22.search()
            self.screen22.entry_keyboard()
            self.current_screen = index
        elif index == 23:
            self.screen23.grid(row=0, column=0, sticky="nsew")
            self.screen23.get_user_id()
            self.screen23.entry_keyboard()
            self.current_screen = index

if __name__ == "__main__":
    app = MainApp()
    app.root.mainloop()