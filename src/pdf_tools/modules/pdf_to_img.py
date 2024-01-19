import glob
import re
from pdf2image import convert_from_path
import os
import pathlib


def pdf_to_img(
    pdf_path,
    output_folder_path,
    y=False,
    # poppler=None,
):
    '''pdf to img'''
    return
    images = convert_from_path(pdf_path=pdf_path)

    for i, img in enumerate(images):
        img.save()
