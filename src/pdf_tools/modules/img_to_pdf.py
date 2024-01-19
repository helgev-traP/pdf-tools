"""img_to_pdf"""

import glob
import re
import sys
import os
import img2pdf


def img_to_pdf(img_folder_path, output_path, y=False):
    """
    main
    実行に成功した場合にTrueを返す
    """
    if img_folder_path[len(img_folder_path) - 1] == "/":
        image_pathes = [
            p for p in glob.glob(img_folder_path + "*") if re.search(".*\.(jpg|png)", p)
        ]
    else:
        image_pathes = [
            p
            for p in glob.glob(img_folder_path + "/*")
            if re.search(".*\.(jpg|png)", p)
        ]

    if len(image_pathes) == 0:
        print("no images.")
        sys.exit()

    if len(glob.glob(pdf_name + ".pdf")) != 0:
        while True and y == False:
            choice = input(pdf_name + ".pdf already exist. Overwrite it?(y/n)")
            if choice == "" or choice == "y":
                break
            elif choice == "n":
                return False

        os.remove(pdf_name + ".pdf")

    print("Detect iamges:")

    for i, image_pathe in enumerate(image_pathes):
        print(" -> ", end="")
        print(i, end="")
        print(".\t" + image_pathe)

    while True and y == False:
        choice = input("conform?")
        if choice == "" or choice == "y":
            break
        elif choice == "n":
            return False

    with open(pdf_name + ".pdf", "wb") as f:
        f.write(img2pdf.convert(image_pathes))

    return True


if __name__ == "__main__":
    img_folder_path = input("image folder path? : ")

    if len(img_folder_path) == 0:
        image_pathes = [p for p in glob.glob("*") if re.search(".*\.(jpg|png)", p)]
    elif img_folder_path[len(img_folder_path) - 1] == "/":
        image_pathes = [
            p for p in glob.glob(img_folder_path + "*") if re.search(".*\.(jpg|png)", p)
        ]
    else:
        image_pathes = [
            p
            for p in glob.glob(img_folder_path + "/*")
            if re.search(".*\.(jpg|png)", p)
        ]

    if len(image_pathes) == 0:
        print("no images.")
        sys.exit()

    pdf_name = input("pdf name?          : ")
    print()

    if len(glob.glob(pdf_name + ".pdf")) != 0:
        while True:
            choice = input(pdf_name + ".pdf already exist. Overwrite it?(y/n)")
            if choice == "" or choice == "y":
                break
            elif choice == "n":
                sys.exit()

        os.remove(pdf_name + ".pdf")

    print("Detect iamges:")
    for i, image_pathe in enumerate(image_pathes):
        print(" -> ", end="")
        print(i, end="")
        print(".\t" + image_pathe)

    with open(pdf_name + ".pdf", "wb") as f:
        f.write(img2pdf.convert(image_pathes))
