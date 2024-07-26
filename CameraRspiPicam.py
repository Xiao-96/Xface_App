## Preparation for running
#### Put files FaceRecognition and EncodingData and testpic(a image of face) in the same directory
#### Also need CameraLog/cap.jpg
#### Connect a picamera3

import os
import time
import subprocess
import FaceRecognition
import numpy as np
from threading import Thread, Event

### camera settings #################
WIDTH = 640 #800
HEIGHT = 480 #600

current_directory = os.getcwd()  # Get current directory
imgpath = 'CameraLog/cap.png'
file_path = os.path.join(current_directory, imgpath)
#####################################################################

### Save images and perform facial recognition #######################
def save_and_recognition():
    result = FaceRecognition.recognition()
    return result

def capture_video():
    cmd = [
        'libcamera-vid',
        '--timeout', '0',           
        '--nopreview',              
        '--width', str(WIDTH),      
        '--height', str(HEIGHT),   
        '--framerate', '10',       
        '--codec', 'yuv420',       
        '--output', '-'         
    ]
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=10**8)

def capture_frame():
    cmd = [
        'ffmpeg',
        '-f', 'v4l2',
        '-i', '/dev/video0',
        '-vf', 'fps=20',           
        '-f', 'image2',           
        file_path  
    ]
    return subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#####################################################################

### facerecognition flag ##########
facerecognitionthread = None
facerecognitionflag = Event()

### facerecognition start ##########
def facerecognition_start(mainapp):
    global facerecognitionthread
    facerecognitionflag.set()# True
    facerecognitionthread = Thread(args=(mainapp,), target=main)
    facerecognitionthread.daemon = True
    facerecognitionthread.start()

### facerecognition stop ##########
def facerecognition_stop():
    facerecognitionflag.clear()  # Set the event to false to stop the thread loop
    facerecognitionthread.join()  # Wait for the thread to finish

### main loop #######################################################
def main(mainapp):
    try:
        print("COUNT")
        while facerecognitionflag.is_set():
            result = save_and_recognition()
            if result[0] != "":
                login_username,login_userid,login_adminflag = result
                mainapp.facerecognition_success(login_userid,login_username, login_adminflag)
            time.sleep(1)

    except Exception as e:
        print("Exception occurred:", e)
    
    finally:
        facerecognitionflag.clear()

# Check if encodings data can be correctly obtained from the image to be registered
def check_encodings_CameraRspiPicam(photoget_directory):
    check_encodings_flag = FaceRecognition.check_encodings_Facerecognition(photoget_directory)
    return check_encodings_flag

# Save encoding data to a pickle file
def addpickle_CameraRspiPicam(userid,username,adminflag,photoget_directory):
    FaceRecognition.addpickle_Facerecognition(userid,username,adminflag,photoget_directory)

# Delete registered ebcoding data and save encoding data to a pickle file
def editpickle_CameraRspiPicam(userid,username,adminflag,photoget_directory):
    FaceRecognition.deletepickle_Facerecognition(userid) 
    FaceRecognition.addpickle_Facerecognition(userid,username,adminflag,photoget_directory)

# Delete registered ebcoding data
def deletepickle_CameraRspiPicam(userid):
    FaceRecognition.deletepickle_Facerecognition(userid)

if __name__ == '__main__':
    class MainApp:
        def FaceRecognition_match(self, userid, recognitiontime):
            print(f"User {userid} recognized at {recognitiontime}")
    mainapp = MainApp()
    main(mainapp)