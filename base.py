import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.units import mm
import pandas as pd
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def main():
    root = tk.Tk()
    root.withdraw()  # Tkウィンドウ非表示

    # CSVファイル選択
    csv_path = filedialog.askopenfilename(
        title='CSVファイルを選択', filetypes=[('CSV Files', '*.csv')]
    )
    if not csv_path:
        print("CSVファイル選択がキャンセルされました")
        return

    # 背景画像選択
    img_path = filedialog.askopenfilename(
        title='背景画像を選択', filetypes=[('PNG Files', '*.png'), ('All files', '*.*')]
    )
    if not img_path:
        print("画像ファイル選択がキャンセルされました")
        return

    # 保存先選択
    save_path = filedialog.asksaveasfilename(
        title='保存先を選択', defaultextension='.pdf', filetypes=[('PDF Files', '*.pdf')]
    )
    if not save_path:
        print("保存先選択がキャンセルされました")
        return

    # CSV読み込み
    data = pd.read_csv(csv_path)
    page = canvas.Canvas(save_path, pagesize=portrait(A4))
    pdfmetrics.registerFont(TTFont("HGRKK", "C:/Windows/Fonts/HGRKK.TTC"))

    offset_x = 87.5 * mm
    offset_y = -59 * mm

    for idx, row in data.iterrows():
        mod = (idx % 10) + 1
        name = str(row["名前"])
        year = str(row["学部学年"])
        pos = str(row["役職"]) if not pd.isnull(row["役職"]) else ''

        base_x = 57.5*mm if mod % 2 == 1 else 57.5*mm+offset_x
        base_y = 260*mm + ((mod-1)//2)*offset_y
        right_x = 90*mm if mod % 2 == 1 else 90*mm+offset_x
        string_x = 25*mm if mod % 2 == 1 else 25*mm+offset_x
        year_y = 280*mm + ((mod-1)//2)*offset_y
        pos_y = 272.5*mm + ((mod-1)//2)*offset_y

        if mod == 1:
            page.drawImage(img_path, 0*mm, 0*mm, 210*mm, 297*mm)
        page.setFont("HGRKK", 26)
        page.drawCentredString(base_x, base_y, name)
        page.setFont("HGRKK", 13)
        page.drawRightString(right_x, year_y, year)
        page.setFont("HGRKK", 13)
        page.drawString(string_x, pos_y, pos)

        if mod == 10 or idx == len(data) - 1:
            page.showPage()

    page.save()
    print("PDF生成が完了しました:", save_path)

if __name__ == "__main__":
    main()
 