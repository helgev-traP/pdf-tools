from setuptools import setup, find_packages

setup(
    name="pdf-tools",
    version="0.0.0",
    packages=find_packages(),
    install_requires=[
        "img2pdf",
        "pdf2image",
        "opencv-python",
    ],
)
