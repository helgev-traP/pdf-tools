"""make pdf dark"""

import os
import shutil
import glob
import numpy as np
import cv2
import modules


def dark_pdf(input_path, output_path, y) -> bool:
    """main"""
    wip_index = 0
    while True:
        try:
            os.mkdir("dark_pdf_wip_" + str(wip_index))
        except FileExistsError:
            wip_index += 1
            continue
        wip_path = "dark_pdf_wip_" + str(wip_index)
        break

    modules.pdf_to_img(
        pdf_path=input_path,
        output_folder_path=wip_path,
        y=y,
    )
    # todo 画像を黒くするの を差し込む
    img_path_list = glob.glob(wip_path + "/*." + "jpg")

    for img_path in img_path_list:
        img = cv2.imread(img_path)
        img = cv2.bitwise_not(img)
        cv2.imwrite(img_path, img)
    # todo end
    modules.img_to_pdf(
        img_folder_path=wip_path,
        output_path=output_path,
        y=y,
    )
    # wipを削除
    shutil.rmtree(wip_path)

    # return
    return True
