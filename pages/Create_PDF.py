from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="letter")

df = pd.read_csv("../data/pdf_topics.csv")

"""
pdf cell props:
w=0, max width
ln=1, single line break
h=12, recommended to set to font-size
"""

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=14)
    pdf.set_text_color(0,179,0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(12,27,200,27)  # start and end positions of line

    for i in range(row["Pages"] - 1):
        pdf.add_page()

pdf.output("output.pdf")
