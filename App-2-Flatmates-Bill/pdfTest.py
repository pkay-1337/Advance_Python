from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font(family="Times", size=24)
pdf.cell(w=0, h=24, txt="Hello PDF!", border=1, ln=1, align="C")
pdf.set_font(family="Times", size=10)
pdf.multi_cell(w=0, h=12, txt="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", border=1, align="")
pdf.output("mypdf.pdf")
