from fpdf import FPDF

pdf = FPDF(orientation='P', format='A4')
pdf.add_page()
pdf.image('./shirtificate.png')
# pdf.set_font(family='Courier')
# pdf.text(105, 146.5, text='CS50 Shirtificate')

pdf.output('./shirtificate.pdf')