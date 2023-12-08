import glob
import re
from pdf2image import convert_from_path
import os
import pathlib


def pdf_to_img(pdf_path, output_folder_path, y=False, poppler=None):
    images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler)

    for i, img in enumerate(images):
        img.save()
