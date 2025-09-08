from report import PdfReport
from flat import Bill, Flatmate

bill = Bill(amount=float(input("Input Bill amount : ")), period=input("Enter Period : "))
fm1 = Flatmate(name=input("Enter Flatmate 1 name : "), days_in_house=int(input("His days in flat : ")))
fm2 = Flatmate(name=input("Enter Flatmate 2 name : "), days_in_house=int(input("His days in flat : ")))
report = PdfReport("flatmate_billing_report.pdf")
report.generate_pdf(fm1, fm2, bill)
print("Billing Report PDF Generated")
