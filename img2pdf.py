'''
portal
'''

import glob
import re
import img2pdf

img_folder_path = input("image folder path? : ")

if len(img_folder_path) == 0:
    image_pathes = [
        p for p in glob.glob(img_folder_path + "*") if re.search(".*\.(jpg|png)", p)
    ]
elif img_folder_path[len(img_folder_path) - 1] == "/":
    image_pathes = [
        p for p in glob.glob(img_folder_path + "*") if re.search(".*\.(jpg|png)", p)
    ]
else:
    image_pathes = [
        p for p in glob.glob(img_folder_path + "/*") if re.search(".*\.(jpg|png)", p)
    ]

pdf_name = input("pdf name?          : ")

print('Detect iamges:')
for i in image_pathes:
    print('-\t' + i)



with open(pdf_name + ".pdf", "wb") as f:
    f.write(img2pdf.convert(image_pathes))

