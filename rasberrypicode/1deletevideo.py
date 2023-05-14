from datetime import datetime
import os
import time 



delete = datetime(2016,6,21,00,00,00,00)
fol = os.scandir('clip')
now = datetime.today()
x = now.hour
i = 1

while i<=10:
    if x == 0:   #13คือบ่ายโมง
        for f in fol:
            x=os.stat(f)
            Result=(time.time()-x.st_mtime) 
            print("ไฟล์นี้มีอายุ: ",Result)

            if Result >= 86400:   #1วันมี86400วินาที
                print('Delete '+f.name) # แสดงชื่อไฟล์
                os.remove(f)
    elif x == 3:
        for f in fol:
            x=os.stat(f)
            Result=(time.time()-x.st_mtime) 
            print("ไฟล์นี้มีอายุ: ",Result)

            if Result >= 86400:   #1วันมี86400วินาที
                print('Delete '+f.name) # แสดงชื่อไฟล์
                os.remove(f)
    elif x == 6:
        for f in fol:
            x=os.stat(f)
            Result=(time.time()-x.st_mtime) 
            print("ไฟล์นี้มีอายุ: ",Result)

            if Result >= 86400:   #1วันมี86400วินาที
                print('Delete '+f.name) # แสดงชื่อไฟล์
                os.remove(f)
    elif x == 9:
        for f in fol:
            x=os.stat(f)
            Result=(time.time()-x.st_mtime) 
            print("ไฟล์นี้มีอายุ: ",Result)

            if Result >= 86400:   #1วันมี86400วินาที
                print('Delete '+f.name) # แสดงชื่อไฟล์
                os.remove(f)
    elif x == 12:
        for f in fol:
            x=os.stat(f)
            Result=(time.time()-x.st_mtime) 
            print("ไฟล์นี้มีอายุ: ",Result)

            if Result >= 86400:   #1วันมี86400วินาที
                print('Delete '+f.name) # แสดงชื่อไฟล์
                os.remove(f)
    elif x == 15:
        for f in fol:
            x=os.stat(f)
            Result=(time.time()-x.st_mtime) 
            print("ไฟล์นี้มีอายุ: ",Result)

            if Result >= 86400:   #1วันมี86400วินาที
                print('Delete '+f.name) # แสดงชื่อไฟล์
                os.remove(f)
    elif x == 18:
        for f in fol:
            x=os.stat(f)
            Result=(time.time()-x.st_mtime) 
            print("ไฟล์นี้มีอายุ: ",Result)

            if Result >= 86400:   #1วันมี86400วินาที
                print('Delete '+f.name) # แสดงชื่อไฟล์
                os.remove(f)
    elif x == 21:
        for f in fol:
            x=os.stat(f)
            Result=(time.time()-x.st_mtime) 
            print("ไฟล์นี้มีอายุ: ",Result)

            if Result >= 86400:   #1วันมี86400วินาที
                print('Delete '+f.name) # แสดงชื่อไฟล์
                os.remove(f)

fol.close()
