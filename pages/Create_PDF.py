from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="letter")
pdf.set_auto_page_break(auto=False, margin=0)  # Avoid automatic page breaks

df = pd.read_csv("../data/pdf_topics.csv")

"""
pdf cell props:
w=0, max width
ln=1, single line break
h=12, recommended to set to font-size
"""

# create PDF pages for each "Topic" in the CSV
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=14)
    pdf.set_text_color(0,179,0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(12,27,200,27)  # start and end positions of line

    # set footer, 240 below text from top of page
    pdf.ln(240)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    #  for each Topic above, create a num of blank pages per the "Pages" equal to Pages value in CSV
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set footer, 250 below top of page, since no text header
        pdf.ln(250)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
