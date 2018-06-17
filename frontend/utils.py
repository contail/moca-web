import os
import glob
from datetime import datetime


file_path = '/Users/contail/Downloads/allPhoto/talent'+'/*'
for i in glob.glob(file_path):
    unique_filename = datetime.now().strftime("%Y%m%d%H%M%s")
    chnage_name = i.replace('pic_',str(unique_filename))
    os.rename(i,chnage_name)