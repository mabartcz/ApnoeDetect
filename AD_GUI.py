# AD_GUI - GUI for apnoe and desaturation detection
# Martin Barton 2020 FBMI CVUT, NUDZ
# ma.barton@seznam.cz

# import the library
from AD_lunch import apnoe_detection, saturation_detection, init_copy
from appJar import gui


def AD_lunch_fce(file_path):
    global AP_total, SP_total

    # Inicializace a zkopirovani souboru
    new_file = init_copy(file_path)

    # Detekce Apnoe
    AP_total = apnoe_detection(new_file)

    # Detekce desaturace
    SP_total = saturation_detection(new_file)


# handle button events
def press(button):
    global file_path

    if button == "Exit":
        app.stop()
    if button == "Add file":
        file_path = app.openBox(title="Vyberte soubor", dirName=None, fileTypes=[('EASYS', '*.d')], asFile=False)
        value_last = file_path.rsplit("/", 1)[-1]
        app.setLabel("File_status", value_last)
        app.enableButton("Analyze")

    if button == "Analyze":
        app.disableButton("Add file")
        app.disableButton("Analyze")
        app.setLabel("Status", "Detection in progress !")
        AD_lunch_fce(file_path)
        app.setLabel("Status", "Done, " + str(AP_total) + " apnea detected and saved.\n"
                               "Done, " + str(SP_total) + " desaturation detected and saved.")
        app.enableButton("Add file")


# Promene
file_path = ""
AP_total = 0
SP_total = 0

# create a GUI variable called app
app = gui("Apnoe detektor", "600x300")
app.setBg("gray")
app.setFont(20)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Apnoe Detector")
app.setLabelBg("title", "SteelBlue")
app.setLabelFg("title", "black")

app.addLabel("File_status", "-")
app.addLabel("Status", " ")


# link the buttons to the function called press
app.addButtons(["Add file", "Analyze", "Exit"], press)
app.disableButton("Analyze")


# start the GUI
app.go()