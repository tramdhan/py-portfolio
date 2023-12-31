import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("../data/invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="Letter")
    pdf.add_page()

    #  abstract filename without extension
    filename = Path(filepath).stem
    #  invoice_num = filename.split("-")[0]
    #  invoice_date = filename.split("-")[1]

    # equivalent of the 2 lines above
    invoice_num, invoice_date = filename.split("-")

    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(100,100,100)

    #  header
    pdf.cell(w=50, h=8, txt=f"Invoice #: {invoice_num}", align="L", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date : {invoice_date}", align="L", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # col headers from excel sheet, removing underscores and covert to uppercase
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    #  render each invoice item from the excel file
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    #  summary row
    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    #  add sum sentence
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"The invoice total is {total_sum}", ln=1)

    # add company name and logo
    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=23, h=8, txt=f"Acme Inc.")
    pdf.image("../assets/images/20.png", w=10)

    pdf.output(f"../PDFs/{invoice_num}.pdf")

"""
Notes:
Bigger pieces of text that expand across multiple lines.For such text, you should use the multi_cell method:

pdf.multi_cell(w, h, txt)

complete example:

from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font(family="Times", size=12)
pdf.multi_cell(w=0, h=6, txt=content)
pdf.output("output.pdf")
"""