from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()

pdf.add_page()
pdf.set_font('helvetica','B',40)
pdf.cell(0, text='CS50 Shirtificate', align="C")

#setting cursor to middle
pdf.set_y(0)

#using png as image
pdf.image("shirtificate.png", x="C", y=70, w=pdf.epw)

#displaying text
pdf.set_font_size(40)
pdf.cell(0, 300, text=f"{name} took CS50", align="C")

#output
pdf.output("shirtificate.pdf")

