import os
import shutil

class ImageFile:
    def getImageFile(self,path):
        allFileList = os.listdir(path)
        imageList = list()
        for file in allFileList:
            if os.path.isdir(os.path.join(path,file)):
                print("I'm a directory: " + file)
            elif os.path.isfile(path+file):
                # print(file)
                if(file).lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                    imageList.append(file)
        return imageList
    
    def mkdir(self,path):
        if not os.path.isdir(path):
            os.mkdir(path)
    
    def writeYoloFile(self,yoloData,pat):
        with open(pat, "w") as text_file:
            text_file.write(yoloData)
    def copyFile(self,fpath,path):
        shutil.copyfile(fpath, path)