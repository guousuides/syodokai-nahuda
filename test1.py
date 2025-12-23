from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait, landscape
from reportlab.lib.units import mm
import os
import pandas as pd

page=canvas.Canvas('test.pdf', pagesize=portrait(A4))

x=0*mm
y=0*mm
dwidth=210*mm
dheight=297*mm

page.drawImage('名札二年.png', x, y, dwidth, dheight)
page.showPage()
page.save()