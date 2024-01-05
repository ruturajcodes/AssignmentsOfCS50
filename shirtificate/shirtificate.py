from fpdf import FPDF


class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", style='', size = 50)
        self._pdf.cell(0,60,"CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255,255,255)

        self._pdf.text(x=48,y=140,txt=f"{name} took CS50")


    def savepdf(self, pdfname):
        self._pdf.output(pdfname)



    '''
    def header(self):
        # Rendering logo:
        self.image("E:\TE Docs\CS50\Practice\shirtificate\shirtificate.png", Align.C , 70, 190)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style='', size = 50)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 65, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.set_text_color(220, 50, 50)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-140)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", size=25)
        self.set_text_color(220, 50, 50)
        # Printing page number:
        self.cell(0,0, f"{name} took CS50", align="C")
    '''

# Instantiation of inherited class
name = input("Name: ")
pdf = PDF(name)

pdf.savepdf("shirtificate1.pdf")


