from fpdf import FPDF
from flat import Bill, Flatmate
class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, fm1, fm2, bill):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font(family="Times", size=24)
        pdf.image("./files/house.png", h=24)
        pdf.cell(w=0, h=24, txt="Flatmate Bills!", border=1, ln=1, align="C")
        pdf.set_font(family="Times", size=16)
        pdf.cell(w=50, h=20, txt="Period", border=1, ln=0, align="C")
        pdf.cell(w=0, h=20, txt=bill.period, border=1, ln=1, align="C")


        pdf.cell(w=50, h=20, txt=fm1.name, border=1, ln=0, align="C")
        pdf.cell(w=0, h=20, txt=f"{fm1.pays(bill)}", border=1, ln=1, align="C")
        
        pdf.cell(w=50, h=20, txt=fm2.name, border=1, ln=0, align="C")
        pdf.cell(w=0, h=20, txt=f"{fm2.pays(bill)}", border=1, ln=1, align="C")
        pdf.output(self.filename)


bill = Bill(amount=float(input("Input Bill amount : ")), period=input("Enter Period : "))
fm1 = Flatmate(name=input("Enter Flatmate 1 name : "), days_in_house=int(input("His days in flat : ")))
fm2 = Flatmate(name=input("Enter Flatmate 2 name : "), days_in_house=int(input("His days in flat : ")))
report = PdfReport("flatmate_billing_report.pdf")
report.generate_pdf(fm1, fm2, bill)
print("Billing Report PDF Generated")
