import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("../data/invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="Letter")
    pdf.add_page()
    #  abstract filename without extension
    filename = Path(filepath).stem
    invoice_num = filename.split("-")[0]
    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(0, 179, 0)
    pdf.cell(w=50, h=8, txt=f"Invoice #: {invoice_num}", align="L", ln=1, border=0)
    pdf.output(f"../PDFs/{invoice_num}.pdf")