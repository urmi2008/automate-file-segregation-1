import sys 
import time 
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
from_dir= "C:/Users/dell/Downloads"
to_dir="C:/Users/dell/Desktop/downloaded images" 

dir_tree= {
    "image_files":['.jpg','.jpeg','.png','.gif','.jfif'],
    "video_files":['.mpg','.mp2','.mpeg','.mpe','.mpv','.mp4','.mov','.avi'],
    "document_files":['.ppt','.xls','.xlsx','.pdf','.txt','.csv'],
    "setup_files":['.exe','.bin','.cmd','.msi','.dmg']
}
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name=os.path.basename(event.src_path)
                print("downloaded"+file_name)
                path1= from_dir+'/'+ file_name
                path2=to_dir+'/'+key 
                path3=to_dir+'/'+key+'/'+file_name
                if os.path.exists(path2):
                    print("directory exists")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("making directory")
                    os.makedirs(path2)
                    print("moving")
                    shutil.move(path1,path3)
                    time.sleep(1)
event_handler=FileMovementHandler() 
observer=Observer
observer.schedule(event_handler,from_dir,recursive=False) 
observer.start()
try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
            