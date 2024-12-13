from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Courier', 'B', size=30)
        self.image('./shirtificate.png', 10, 70, 190)

        self.cell(w=0, h=30, text='CS50 Shirtificate', align='C')
        self.ln(10)

        self.set_font('Courier', 'B', size=30)
        self.set_text_color(255, 255, 255)
        self.cell(w=0, h=250, text=name_input, align='C')

name_input = str(f'{input('Name: ')} took CS50')

pdf = PDF()
pdf.add_page()
pdf.output('./shirtificate.pdf')