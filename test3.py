from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.units import mm
import pandas as pd
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

data = pd.read_csv("名簿test.csv", encoding="utf-8")
page = canvas.Canvas("名札test3.pdf", pagesize=portrait(A4))
pdfmetrics.registerFont(TTFont("HGRKK", "C:/Windows/Fonts/HGRKK.TTC"))
pdfmetrics.registerFont(TTFont("HGRME", "C:/Windows/Fonts/HGRME.TTC"))

page.drawImage("名札二年.png", 0*mm, 0*mm, 210*mm, 297*mm)  # A4

offset_x = 87.5*mm
offset_y = -59*mm

for idx, row in data.iterrows():
    mod = (idx % 10) + 1  # 1〜10で余り処理
    name = str(row["名前"])
    faculty_year = str(row["学部学年"])
    position = str(row["役職"]) if not pd.isnull(row["役職"]) else ''
    
    # 位置計算
    base_x = 57.5*mm if mod % 2 == 1 else 57.5*mm + offset_x
    base_y = 260*mm + ((mod-1)//2)*offset_y
    right_x = 90*mm if mod % 2 == 1 else 90*mm + offset_x
    string_x = 25*mm if mod % 2 == 1 else 25*mm + offset_x
    year_y = 280*mm + ((mod-1)//2)*offset_y
    position_y = 275*mm + ((mod-1)//2)*offset_y
    
    page.setFont("HGRKK", 26)
    page.drawCentredString(base_x, base_y, name)
    page.setFont("HGRKK", 13)
    page.drawRightString(right_x, year_y, faculty_year)
    page.setFont("HGRKK", 13)
    page.drawString(string_x, position_y, position)
    
    # 10枚ごとに次ページ
    if mod == 10 or idx == len(data) - 1:
        page.showPage()
        page.drawImage("名札二年.png", 0*mm, 0*mm, 210*mm, 297*mm)

page.save()
