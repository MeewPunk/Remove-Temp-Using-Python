import os
import shutil
import datetime

# https://www.facebook.com/SrangSrrkh

# กำหนด path ของ folder Temp ที่ต้องการลบไฟล์
folder_path = r'C:\Users\Dev2077\AppData\Local\Temp'

# วันที่ปัจจุบัน
now = datetime.datetime.now()

# วันที่ที่ต้องการลบไฟล์ออกทั้งหมด
days_to_keep = 7
delta_days = datetime.timedelta(days=days_to_keep)
date_to_keep = now - delta_days

# วนลูปเพื่อค้นหาและลบไฟล์และโฟลเดอร์ที่ไม่มีการใช้งานเกินจำนวนวันที่กำหนด
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        # ตรวจสอบวันที่ของไฟล์
        file_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        if file_date < date_to_keep:
            print('remove file:', file_path)
            try:
                os.remove(file_path)
            except:
                print('Error removing file:', file_path)

    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        # ตรวจสอบวันที่ของโฟลเดอร์
        dir_date = datetime.datetime.fromtimestamp(os.path.getctime(dir_path))
        if dir_date < date_to_keep:
            print('remove folder:', dir_path)
            try:
                shutil.rmtree(dir_path)
            except:
                print('Error removing folder:', dir_path)
