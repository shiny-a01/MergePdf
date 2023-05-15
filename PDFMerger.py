import sys
import os
from PyPDF2 import PdfMerger
from datetime import datetime


def merge_pdfs(file_paths, output_path):
    merger = PdfMerger()

    for path in file_paths:
        merger.append(path)

    try:
        merger.write(output_path)
        abs_output_path = os.path.abspath(output_path)
        print(f"結合が成功しました。出力ファイル: {abs_output_path}")
    except Exception as e:
        print(f"結合中にエラーが発生しました: {e}")
    finally:
        merger.close()


# ドラッグアンドドロップされたすべてのPDFファイルのパスを取得
# パスはコマンドライン引数や別の方法で取得することもできます
file_paths = []
if len(sys.argv) > 1:
    # コマンドライン引数からPDFファイルのパスを取得
    file_paths = sys.argv[1:]
else:
    print("PDFファイルが指定されていません。終了します。")
    sys.exit(1)

# 指定されたファイルが全てPDFファイルであるか確認
for file_path in file_paths:
    if not file_path.lower().endswith(".pdf"):
        print(f"読み込まれたファイルの種類が正しくありません: {file_path}")
        sys.exit(1)

# 結合後のPDFファイルの保存先パス
now = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = f"output_{now}.pdf"

# PDFファイルを結合する
merge_pdfs(file_paths, output_path)
