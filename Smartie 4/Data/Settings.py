from tkinter import *
import smartieJson as sj


#'#E4ACEE' '#000000'

##################
#GLOBAL VARIABLES#
##################






###########
#FUNCTIONS#
###########
def audcomm():
    #getting data from settings
    var = sj.read()
    #selecting the audio key
    var = var['audio']

    #Finding if it is = to 0
    if var == '0':
        #printing it if it is 0
        print(var)
        #changing it to 1
        sj.update('audio', '1')
        
    elif var == '1':
        print(var)
        sj.update('audio', '0')

#######################
#SETTING UP THE WINDOW#
#######################

#Create the GUI window
root = Tk()

#Set the window title
root.title("Settings Panel")

#Creates the size of the window
root.geometry("400x400+120+120")



######################
#CREATING THE WIDGETS#
######################
audiocheck = Checkbutton(root, text = "Audio", command = audcomm)
#Auto ticks the button if the setting is enabled
data = sj.read()
if data['audio'] == 1 or data['audio'] == "1":
 audiocheck.select()




##################
#PACK THE WIDGETS#
##################
#Puts the button on screen
audiocheck.pack()
audiocheck.pack()



#Creates a loop for the GUI to run in
root.mainloop()
