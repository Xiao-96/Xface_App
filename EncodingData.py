import os
import pickle
import cv2
if os.name != 'nt': import face_recognition

SHAREDVARS = None
current_directory = os.getcwd()  # Get current directory
pickle_path = os.path.join(current_directory, 'CameraLog', 'encodings.pickle')

class PickleDataClass():
    def __init__(self):
        if not os.path.exists(pickle_path):
            blank = {"encodings": [], "names": [],"user_id": [], "adminflag": []}
            with open(pickle_path, "wb") as f1:
                f1.write(pickle.dumps(blank))
        with open(pickle_path,'rb') as file:
            data=file.read()
        if len(data)==0:
            print("there is no data")
        try:
            pickle_data=pickle.loads(data)
        except pickle.UnpicklingError:
            print("Data is not in pickle format")
        self.data = pickle.loads(open(pickle_path, "rb").read())

    # Save encoding data to a pickle file
    def addFace(self, id, name, flag, photoget_directory):
        imgDirectory = photoget_directory
        img = cv2.imread(imgDirectory)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model='hog')
        encodings = face_recognition.face_encodings(rgb, boxes)
        
        if encodings:
            encoding = encodings[0]
            self.data["encodings"].append(encoding)
            self.data["names"].append(name)
            self.data["user_id"].append(id)
            self.data["adminflag"].append(flag)
            f = open(pickle_path, "wb")
            f.write(pickle.dumps(self.data))
            f.close()
            print("Add 1 encoded data successfully!")
        else: print("Failed to get encodings")
        self.reInitializeData()

    # Check if encodings data can be correctly obtained from the image to be registered
    def checkencoding(self,photoget_directory):
        imgDirectory = photoget_directory
        img = cv2.imread(imgDirectory)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model='hog')
        encodings = face_recognition.face_encodings(rgb, boxes)

        if encodings:
            print("get encode")
            return True
        else:
            print("not encoded")
            return False
        
    # Delete registered ebcoding data
    def deleteFace(self, id):
        indices = [i for i, n in enumerate(self.data["user_id"]) if n ==id]
        if not indices:
            return
        
        for i in reversed(indices):
            self.data["names"].pop(i)
            self.data["encodings"].pop(i)
            self.data["user_id"].pop(i)
            self.data["adminflag"].pop(i)

        with open(pickle_path, "wb") as f:
            f.write(pickle.dumps(self.data))

        print("Delete 1 encoded data successfully!")
        self.reInitializeData()
    
    def reInitializeData(self):
        self.data = pickle.loads(open(pickle_path, "rb").read())

    def faid_data(self, tag_to_find):#for my check and not needed for app
        with open(pickle_path, "rb") as f:
            data = pickle.load(f)
            names = data.get("names", [])
            user_ids = data.get("user_id",[])

            for i, name in enumerate(names):
                if name == tag_to_find:
                    if i < len(user_ids):
                        return user_ids[i]
                    else:
                        print("not found")
                        return None
            return("tag not found")
        

PickleData = PickleDataClass()

if __name__ == '__main__':#for my check and not needed for app
    print(PickleData.data)
