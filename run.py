from api_service import ApiService
import os
from image_file import ImageFile
from tqdm import tqdm

mApiService = ApiService()
mImageFile = ImageFile()
yolotype = ["with_mask","without_mask","mask_weared_incorrect","person","hand","foot","head"]
inSaveYoloType = [4,5,6]# 要更新的資料
yolotypeStr = str(yolotype).replace("'",'"')
dirname = 'yolo_data/'
imgpath = './data/'+dirname+'images/'
imgpathData = './data/'+dirname+'image/'
labelpagth = './data/'+dirname+'label/'
findMinSize = 0.00#
mImageFile.mkdir(labelpagth)
mImageFile.mkdir(imgpathData)
filelist = mImageFile.getImageFile(imgpath)

count = 0
haveLayout = 0
# 寫入 classes.txt
with open(labelpagth+"classes.txt", "w") as text_file:
    for name in yolotype:
        text_file.write(name+'\n')

    

for i in tqdm(range(len(filelist))):
    filename = filelist[i]
    yoloStr = mApiService.upladImage(imgpath+filename,yolotypeStr)
    
    yololist = yoloStr.split('\n')
    if yoloStr == "":
        continue
    # 找出夠大的圖片
    checkSize = False
    writeStr = ""
    for item in yololist:
        if item == "":
            continue
        size = float(item.split(" ")[3])*float(item.split(" ")[4])
        if size > findMinSize:
            checkSize = True
            
        # 找出需要存擋的資料
        if int(item.split(" ")[0]) in inSaveYoloType:
            writeStr = item + '\n'
    # 若成功轉換資料，將圖片與layout複製一份
    if checkSize and writeStr != "":
        mImageFile.writeYoloFile(writeStr,labelpagth+filename.replace(".jpg",".txt").replace(".png",".txt"))
        mImageFile.copyFile(imgpath+filename,imgpathData+filename)