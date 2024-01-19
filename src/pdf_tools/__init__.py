"""main"""

import sys
from .modules.img_to_pdf import *
from .modules.pdf_to_img import *
from .dark_pdf import *

# todo 完成したら消す
sys.dont_write_bytecode = True

if __name__ == "__main__":
    argv = sys.argv
    yes = False
    if "-y" in argv:
        yes = True
        argv.pop(argv.index("-y"))

    # この時点でargvは、
    # {実行ファイル名} プログラム 入力 出力
    # になる

    match argv[1]:
        case "--pdf2img":
            if len(argv) == 4:
                pdf_to_img(
                    argv[2],  # 入力
                    argv[3],  # 出力
                    yes,
                )
        case "--img2pdf":
            if len(argv) == 4:
                img_to_pdf(
                    argv[2],  # 入力
                    argv[3],  # 出力
                    yes,
                )
        case "--dark-pdf":
            if len(argv) == 4:
                dark_pdf(
                    argv[2],  # 入力
                    argv[3],  # 出力
                    yes,
                )
