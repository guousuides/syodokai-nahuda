from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait, landscape
from reportlab.lib.units import mm
import os
import pandas as pd
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


data=pd.read_csv("名簿test.csv",encoding="utf-8")
page=canvas.Canvas("名札test2.pdf",pagesize=portrait(A4))
pdfmetrics.registerFont(TTFont("HGRKK", "C:/Windows/Fonts/HGRKK.TTC"))
pdfmetrics.registerFont(TTFont("HGRME", "C:/Windows/Fonts/HGRME.TTC"))

page.drawImage("名札二年.png",0*mm,0*mm,210*mm,297*mm)# a4

# csvファイルで行数を10で割ったときの余りが1の時の情報を下のように配置する
page.setFont("HGRKK", 26)
page.drawCentredString(57.5*mm,260*mm,"郭嘉宏")
page.setFont("HGRKK", 13)
page.drawRightString(90*mm,280*mm,"基幹理工学部二年")
page.setFont("HGRKK", 13)
page.drawString(25*mm,275*mm,"にーと")

offset_x=87.5*mm
offset_y=-59*mm

# csvファイルで行数を10で割ったときの余りが2の時の情報を下のように配置する
page.setFont("HGRKK", 26)
page.drawCentredString(57.5*mm+offset_x,260*mm,"郭嘉宏")
page.setFont("HGRKK", 13)
page.drawRightString(90*mm+offset_x,280*mm,"基幹理工学部二年")
page.setFont("HGRKK", 13)
page.drawString(25*mm+offset_x,275*mm,"にーと")

# csvファイルで行数を10で割ったときの余りが3の時の情報を下のように配置する
page.setFont("HGRKK", 26)
page.drawCentredString(57.5*mm,260*mm+offset_y,"郭嘉宏")
page.setFont("HGRKK", 13)
page.drawRightString(90*mm,280*mm+offset_y,"基幹理工学部二年")
page.setFont("HGRKK", 13)
page.drawString(25*mm,275*mm+offset_y,"にーと")

# csvファイルで行数を10で割ったときの余りが4の時の情報を下のように配置する
page.setFont("HGRKK", 26)
page.drawCentredString(57.5*mm+offset_x,260*mm+offset_y,"郭嘉宏")
page.setFont("HGRKK", 13)
page.drawRightString(90*mm+offset_x,280*mm+offset_y,"基幹理工学部二年")
page.setFont("HGRKK", 13)
page.drawString(25*mm+offset_x,275*mm+offset_y,"にーと")

# csvファイルで行数を10で割ったときの余りが5の時の情報を下のように配置する
page.setFont("HGRKK", 26)
page.drawCentredString(57.5*mm,260*mm+offset_y*2,"郭嘉宏")
page.setFont("HGRKK", 13)
page.drawRightString(90*mm,280*mm+offset_y*2,"基幹理工学部二年")
page.setFont("HGRKK", 13)
page.drawString(25*mm,275*mm+offset_y*2,"にーと")


# csvファイルで行数を10で割ったときの余りが6の時の情報を下のように配置する
page.setFont("HGRKK", 26)
page.drawCentredString(57.5*mm+offset_x,260*mm+offset_y*2,"郭嘉宏")
page.setFont("HGRKK", 13)
page.drawRightString(90*mm+offset_x,280*mm+offset_y*2,"基幹理工学部二年")
page.setFont("HGRKK", 13)
page.drawString(25*mm+offset_x,275*mm+offset_y*2,"にーと")

# csvファイルで行数を10で割ったときの余りが7の時の情報を下のように配置する
page.setFont("HGRKK", 26)
page.drawCentredString(57.5*mm,260*mm+offset_y*3,"郭嘉宏")
page.setFont("HGRKK", 13)
page.drawRightString(90*mm,280*mm+offset_y*3,"基幹理工学部二年")
page.setFont("HGRKK", 13)
page.drawString(25*mm,275*mm+offset_y*3,"にーと")

# csvファイルで行数を10で割ったときの余りが8の時の情報を下のように配置する
page.setFont("HGRKK", 26)
page.drawCentredString(57.5*mm+offset_x,260*mm+offset_y*3,"郭嘉宏")
page.setFont("HGRKK", 13)
page.drawRightString(90*mm+offset_x,280*mm+offset_y*3,"基幹理工学部二年")
page.setFont("HGRKK", 13)
page.drawString(25*mm+offset_x,275*mm+offset_y*3,"にーと")

# csvファイルで行数を10で割ったときの余りが9の時の情報を下のように配置する
page.setFont("HGRKK", 26)
page.drawCentredString(57.5*mm,260*mm+offset_y*4,"郭嘉宏")
page.setFont("HGRKK", 13)
page.drawRightString(90*mm,280*mm+offset_y*4,"基幹理工学部二年")
page.setFont("HGRKK", 13)
page.drawString(25*mm,275*mm+offset_y*4,"にーと")

# csvファイルで行数を10で割ったときの余りが0の時の情報を下のように配置する
page.setFont("HGRKK", 26)
page.drawCentredString(57.5*mm+offset_x,260*mm+offset_y*4,"郭嘉宏")
page.setFont("HGRKK", 13)
page.drawRightString(90*mm+offset_x,280*mm+offset_y*4,"基幹理工学部二年")
page.setFont("HGRKK", 13)
page.drawString(25*mm+offset_x,275*mm+offset_y*4,"にーと")

page.showPage()
page.save()