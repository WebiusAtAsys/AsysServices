import fpdf
from fpdf import FPDF
import time
import pandas as pd
import matplotlib.pyplot as plt
#import dataframe_image as dfi

def create_letterhead(pdf, WIDTH):
    pdf.image("./resources/letterhead.png", 0, 0, WIDTH)

def create_title(title, pdf):
    
    # Add main title
    pdf.set_font('Helvetica', 'b', 20)  
    pdf.ln(40)
    pdf.write(5, title)
    pdf.ln(10)
    
    # Add date of report
    pdf.set_font('Helvetica', '', 14)
    pdf.set_text_color(r=128,g=128,b=128)
    today = time.strftime("%d/%m/%Y")
    pdf.write(4, f'{today}')
    
    # Add line break
    pdf.ln(10)

def write_to_pdf(pdf, words):
    
    # Set text colour, font size, and font type
    pdf.set_text_color(r=0,g=0,b=0)

    pdf.write(5, words)
    pdf.set_font('Helvetica', '', 12)


class PDF(FPDF):

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')


def ArrangePDF():
    pdf = PDF() # A4 (210 by 297 mm)
    #Linker Rand
    pdf.set_left_margin(Marginleft)
    pdf.set_right_margin(Marginright)
    return pdf


def Create1Page(TITLE, Kundenkuerzel, TaskToDo, NameCus, StrCus, PLZOrtCus, TelCus, EMailCus, NameASYS, StrASYS, TelASYS, EMailASYS, onWhat, Microscope, Laser):

    # Add Page 1
    pdf.add_page()

    # Add lettterhead and title
    create_letterhead(pdf, WIDTH)
    create_title(TITLE, pdf)

    # Add some words to PDF
    write_to_pdf(pdf, Kundenkuerzel+" - "+TaskToDo+ " "+ Laser+" \n")
    write_to_pdf(pdf, "\n")

    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Customer:        ")
    write_to_pdf(pdf, NameCus+"\n")
    write_to_pdf(pdf, "                              "+StrCus+"\n")
    write_to_pdf(pdf, "                              "+PLZOrtCus+"\n")
    write_to_pdf(pdf, "                              "+TelCus+"\n")
    write_to_pdf(pdf, "                              "+EMailCus+"\n")
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Sales:               ")
    write_to_pdf(pdf, NameASYS+"\n")
    write_to_pdf(pdf, "                              "+StrASYS+"\n")
    write_to_pdf(pdf, "                              "+PLZOrtASYS+"\n")
    write_to_pdf(pdf, "                              "+TelASYS+"\n")
    write_to_pdf(pdf, "                              "+EMailASYS+"\n")
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Application Request:             ")
    write_to_pdf(pdf, TaskToDo+" on "+ onWhat+"\n")
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Used Equipment:                   ")
    write_to_pdf(pdf, Microscope+"\n")
    write_to_pdf(pdf, "                                                         "+Laser+"\n")


def Create2Page(TaskToDo,  Amountdevices, samplex, sampley, Thickness):
        ## Variablen 2 Seite
    if TaskToDo == 'Laser depaneling':
        VerbTasktoDo = 'depanel'

    
    if Amountdevices == 1:
        containsorcontain = 'contain'
        devicesordevice = 'device'
    else:
        containsorcontain = 'contains'
        devicesordevice = 'devices'


    ##### Add Page 2
    pdf.add_page()
    create_letterhead(pdf, WIDTH)
    pdf.ln(40)
    pdf.set_font('Helvetica', 'b', 20) 
    write_to_pdf(pdf,"1. Application Request")
    pdf.ln(10)

    write_to_pdf(pdf,  "ASYS was asked to " + VerbTasktoDo + " " + onWhat+ " samples. Each sample "+ containsorcontain+" "\
        + str(Amountdevices)+ " "+devicesordevice+". It has a width of " +str(samplex) +" mm, a height of "+ str(sampley)+" mm and a thickness of "\
        + str(Thickness) +" mm. " )
    write_to_pdf(pdf,  "ASYS tried to find the best parameters in terms of focus position, speed, number of passes, laser power and frequency." )
    write_to_pdf(pdf, "\n")

    Currentheight = pdf.get_y()
    pdf.image("./resources/annual_sales.png", x=Marginleft+0.3*WIDTH-Marginleft,  w=0.6*WIDTH-Marginleft)
    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Figure 1: ")
    write_to_pdf(pdf, "Front view of the sample\n")

    pdf.image("./resources/annual_sales.png", x=Marginleft+0.3*WIDTH-Marginleft,  w=0.6*WIDTH-Marginleft)
    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Figure 2: ")
    write_to_pdf(pdf, "Back view of the sample\n")

def Create3Page(Laser, beamsource, wavelength, maxpower, Beamexpaner, lens, spotsize, scanfield):
    ##### Add Page 3
    pdf.add_page()
    create_letterhead(pdf, WIDTH)
    pdf.ln(40)
    pdf.set_font('Helvetica', 'b', 20) 
    write_to_pdf(pdf,"2. Experimental Setup")
    pdf.ln(10)
    pdf.set_font('Helvetica', 'b', 14) 
    write_to_pdf(pdf,"2.1 Equipment")
    pdf.ln(10)
    write_to_pdf(pdf, "ASYS used a " + Laser + " to perfom the application experiments.\n" )
    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Laser:\n")
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "Source:                      "+beamsource+"\n")
    write_to_pdf(pdf, "Wavelength:              "+wavelength+"\n")
    write_to_pdf(pdf, "Max Power:               "+maxpower+"\n")
    write_to_pdf(pdf, "Beam Expander:       "+Beamexpaner+"\n")
    write_to_pdf(pdf, "Lens:                         "+lens+"\n")
    write_to_pdf(pdf, "Spot Size:                 "+spotsize+"\n")
    write_to_pdf(pdf, "Scan field:                 "+scanfield+"\n")


def Create4Page():
    ##### Add Page 4
    pdf.add_page()
    create_letterhead(pdf, WIDTH)
    pdf.ln(40)
    pdf.set_font('Helvetica', 'b', 14) 
    write_to_pdf(pdf,"2.2 Fiducial Recognition")

    pdf.ln(10)
    write_to_pdf(pdf, "The board has several printed fiducials.Regarding the tests on our Polyphos DP 9000 \
    test machine it was not possible to use these fiducials. Because of the used setup the processing area \
    has only a size of 180 mm x 180 mm and therefore it is too small for the whole panel. \
    With a different setup the processing area will be increased and then three of the printed fiducials \
    can be used as global fiducials. With those, the boards can be positioned under the processing area. \
    From former applications it can be pointed out that the camera capture and processing time for the \
    three fiducials is approx. ~ 1000 ms. \
    For these tests a WeldMark Job with the cut outline was created and the panel was placed manually. \n")


def Create5Page():
    pass

def Create6Page():
    pass

def Create7Page():
    pass

def Create8Page():
    pass

def Create9Page():
    pass

def Create10Page():
    pass

def Create11Page():
    pass




# Global Variables
TITLE = "Application Report"
WIDTH = 210
HEIGHT = 297
Marginleft = 30
Marginright = 20

########Variablen erste Seite
Kundenkuerzel = 'BOSBLA'

NameCus = 'Stefan Winkler'
StrCus = 'Johannisstra 15'
PLZOrtCus = '89231 Senden'
TelCus ='0157821456'
EMailCus = 'max@hallo.de'


NameASYS = 'Stefan Winkler'
StrASYS = 'Johannisstra 15'
PLZOrtASYS = '89231 Senden'
TelASYS ='0157821456'
EMailASYS = 'max@hallo.de'

NameAppl = 'Stefan Winkler'
StrAppl = 'Johannisstra 15'
PLZOrtAppl = '89231 Senden'
TelAppl ='0157821456'
EMailAppl = 'max@hallo.de'

TaskToDo = 'Laser depaneling'
onWhat = 'FR4'
Amountdevices = 216

Microscope = 'Keyence VHX-7100 Digital Microscope'
Laser = 'Polyphos 9000 GN'



## Variablen 3. Seite
beamsource  = "40 W GREEN"
wavelength = "532 nm"
maxpower = "40 W"
Beamexpaner = "1x to 8x motorized"
lens = "255 mm f-theta"
spotsize = "approx 50 µm 1/e²"
scanfield = "180x180 mm²"

samplex = 120
sampley = 250
Thickness = 1.6


TimeperCircuitQuality = 4.8
# Create PDF

def generatePdf():

    pdf = ArrangePDF()
    Create1Page(TITLE, Kundenkuerzel, TaskToDo, NameCus, StrCus, PLZOrtCus, TelCus, EMailCus, NameASYS, StrASYS, TelASYS, EMailASYS, onWhat, Microscope, Laser)
    # Create2Page(TaskToDo,  Amountdevices, samplex, sampley, Thickness)
    # Create3Page(Laser, beamsource, wavelength, maxpower, Beamexpaner, lens, spotsize, scanfield)
    # Create4Page()
    # Create5Page()





    ##### Add Page 5
    pdf.add_page()
    create_letterhead(pdf, WIDTH)
    pdf.ln(40)
    pdf.set_font('Helvetica', 'b', 20) 
    write_to_pdf(pdf,"3. Results")
    pdf.ln(10)
    pdf.set_font('Helvetica', 'b', 14) 
    write_to_pdf(pdf,"3.1 Best quality optimization")
    pdf.ln(10)
    write_to_pdf(pdf, "By varying the laser parameters such as power, frequency, cut line geometry, \
    the number of crossings and the spot size and therefore the fluence, it was tried to achieve the \
    best cutting result. Two different sets of parameter were investigated: one with the best cut quality \
    (and still acceptable laser time) and one with the fastest laser time (and acceptable cut quality). \
    It is also possible to combine the set of parameter in the way to achieve the desired compromise between \
    laser time and amount of discoloration of the cutting edge.\n" )


    ##### create table #####
    Bestquality = pd.DataFrame()
    settings = [[40,1200,450,40,50]]
    Bestquality = pd.DataFrame(settings, columns = ['Frequency [kHz]','Scan Speed [mm/s]','Passes [-]','Power [W]','Spot Size [µm]' ])

    dfi.export(Bestquality, 'resources/Bestquality.png')


    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Table 1: ")
    write_to_pdf(pdf, "Best quality settings\n")
    write_to_pdf(pdf, "\n")
    pdf.image("./resources/Bestquality.png", x=Marginleft+0.2*WIDTH-Marginleft,  w=0.8*WIDTH-Marginleft)
    write_to_pdf(pdf, "\n")


    write_to_pdf(pdf, "With the parameter from Table 1 the total laser time for one single circuit is ~4.85\
    seconds. With 216 single circuits on one board this time sums up to ~1048 seconds for the whole board. \n")
    write_to_pdf(pdf, "\n")

    BestqualityTime = pd.DataFrame()
    settings = [["Handling, In-, Outlet, Jump etc." ,7], ["Fiducial Recognition",1], ["Process Time", TimeperCircuitQuality*Amountdevices]]
    BestqualityTime = pd.DataFrame(settings, columns = ['Process [-]','Duration [s]'])

    dfi.export(BestqualityTime, 'resources/BestqualityTime.png')

    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Table 2: ")
    write_to_pdf(pdf, "Process time best quality settings\n")
    write_to_pdf(pdf, "\n")
    pdf.image("./resources/BestqualityTime.png", x=Marginleft+0.3*WIDTH-Marginleft,  w=0.5*WIDTH-Marginleft)
    write_to_pdf(pdf, "\n")

    ########Page 6
    pdf.add_page()
    create_letterhead(pdf, WIDTH)
    pdf.ln(40)
    write_to_pdf(pdf,  "ASYS tried to find the best parameters in terms of focus position, speed, number of passes, laser power and frequency." )
    write_to_pdf(pdf, "\n")

    pdf.image("./resources/annual_sales.png", x=Marginleft+0.3*WIDTH-Marginleft,  w=0.6*WIDTH-Marginleft)
    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Figure 3: ")
    write_to_pdf(pdf, "Overview of the high quality samples\n")




    ##### Add Page 7
    pdf.add_page()
    create_letterhead(pdf, WIDTH)
    pdf.ln(40)
    write_to_pdf(pdf, "More detailled impressions of the samples" )
    write_to_pdf(pdf, "\n")

    Currentheight = pdf.get_y()
    pdf.image("./resources/annual_sales.png", x=Marginleft,  w=WIDTH/2-Marginleft)
    pdf.image("./resources/annual_sales.png", x=WIDTH/2, y=Currentheight, w=WIDTH/2-Marginleft)
    write_to_pdf(pdf, "\n")

    Currentheight = pdf.get_y()
    pdf.image("./resources/annual_sales.png", x=Marginleft,  w=WIDTH/2-Marginleft)
    pdf.image("./resources/annual_sales.png", x=WIDTH/2, y=Currentheight, w=WIDTH/2-Marginleft)
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Figure 4: ")
    write_to_pdf(pdf, "Detailled microscopig impressions\n")


    # Add some words to PDF
    write_to_pdf(pdf, "2. The visualisations below shows the trend of total sales for Heicoders Academy and the breakdown of revenue for year 2016:")






    ##### Add Page 8
    pdf.add_page()
    create_letterhead(pdf, WIDTH)

    pdf.ln(40)
    pdf.set_font('Helvetica', 'b', 14) 
    write_to_pdf(pdf,"3.2 Fast cycle time optimization")
    pdf.ln(10)
    write_to_pdf(pdf, "On this optimization we foused on a fast cycle time.\n" )


    ##### create table #####
    Bestcycletime = pd.DataFrame()
    settings = [[40,1600,450,40,50]]
    Bestcycletime = pd.DataFrame(settings, columns = ['Frequency [kHz]','Scan Speed [mm/s]','Passes [-]','Power [W]','Spot Size [µm]' ])

    dfi.export(Bestcycletime, 'resources/Bestcycletime.png')


    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Table 3: ")
    write_to_pdf(pdf, "Fast cycle time settings\n")
    write_to_pdf(pdf, "\n")
    pdf.image("./resources/Bestcycletime.png", x=Marginleft+0.2*WIDTH-Marginleft,  w=0.8*WIDTH-Marginleft)
    write_to_pdf(pdf, "\n")


    write_to_pdf(pdf, "With the parameter from Table 3 the total laser time for one single circuit is ~3\
    seconds. With "+str(Amountdevices)+" single circuits on one board this time sums up to ~1048 seconds for the whole board. \n")
    write_to_pdf(pdf, "\n")

    BestqualityTime = pd.DataFrame()
    settings = [["Handling, In-, Outlet, Jump etc." ,7], ["Fiducial Recognition",1], ["Process Time", TimeperCircuitQuality*Amountdevices]]
    BestqualityTime = pd.DataFrame(settings, columns = ['Process [-]','Duration [s]'])

    dfi.export(BestqualityTime, 'resources/BestCycleTimeTime.png')

    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Table 4: ")
    write_to_pdf(pdf, "Process time best quality settings\n")
    write_to_pdf(pdf, "\n")
    pdf.image("./resources/BestCycleTimeTime.png", x=Marginleft+0.3*WIDTH-Marginleft,  w=0.5*WIDTH-Marginleft)
    write_to_pdf(pdf, "\n")

    ########Page 9
    pdf.add_page()
    create_letterhead(pdf, WIDTH)
    pdf.ln(40)
    write_to_pdf(pdf,  "ASYS tried to find the best parameters in terms of focus position, speed, number of passes, laser power and frequency." )
    write_to_pdf(pdf, "\n")

    pdf.image("./resources/annual_sales.png", x=Marginleft+0.3*WIDTH-Marginleft,  w=0.6*WIDTH-Marginleft)
    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Figure 5: ")
    write_to_pdf(pdf, "Overview of the fast cycle time samples\n")




    ##### Add Page 10
    pdf.add_page()
    create_letterhead(pdf, WIDTH)
    pdf.ln(40)
    write_to_pdf(pdf, "More detailled impressions of the samples" )
    write_to_pdf(pdf, "\n")

    Currentheight = pdf.get_y()
    pdf.image("./resources/annual_sales.png", x=Marginleft,  w=WIDTH/2-Marginleft)
    pdf.image("./resources/annual_sales.png", x=WIDTH/2, y=Currentheight, w=WIDTH/2-Marginleft)
    write_to_pdf(pdf, "\n")

    Currentheight = pdf.get_y()
    pdf.image("./resources/annual_sales.png", x=Marginleft,  w=WIDTH/2-Marginleft)
    pdf.image("./resources/annual_sales.png", x=WIDTH/2, y=Currentheight, w=WIDTH/2-Marginleft)
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Figure 6: ")
    write_to_pdf(pdf, "Detailled microscopig impressions\n")


    # Add some words to PDF
    write_to_pdf(pdf, "2. The visualisations below shows the trend of total sales for Heicoders Academy and the breakdown of revenue for year 2016:")

    ####Page 11
    pdf.add_page()
    create_letterhead(pdf, WIDTH)
    pdf.ln(40)
    pdf.set_font('Helvetica', 'b', 20) 
    write_to_pdf(pdf,"4. Summary")
    pdf.ln(10)

    write_to_pdf(pdf,  "Everything is fine" )
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "\n")
    pdf.set_font('Helvetica', 'B', 14)
    write_to_pdf(pdf, "Contact:")
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "                              "+NameAppl+"\n")
    write_to_pdf(pdf, "                              "+StrAppl+"\n")
    write_to_pdf(pdf, "                              "+PLZOrtAppl+"\n")
    write_to_pdf(pdf, "                              "+TelAppl+"\n")
    write_to_pdf(pdf, "                              "+EMailAppl+"\n")
    write_to_pdf(pdf, "\n")
    write_to_pdf(pdf, "\n")

    # Generate the PDF
    return pdf.output("annual_performance_report.pdf", 'F')

'''
Main Function
'''
if __name__ == "__main__":
    generatePdf()