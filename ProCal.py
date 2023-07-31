#import librarys
from tkinter import *
from tkcalendar import *


# Assign variable to instructor
pr = Tk()
pr.title("Calender")
pr.geometry("350x300")
pr.configure(bg="white")


Cal = Calendar(pr, selectmode = "day", date_pattern = 'dd/mm/yyyy')
Cal.pack(pady = 20)

# define function to select date
def get_date():
    label.config(text = Cal.get_date())

#create a button to select date 
button = Button(pr, text = "Select the date", command= get_date)
button.pack(padx=20)

# create a label to see selected date
label = Label(pr, text="")
label.configure(bg= "white", font= "20",)
label.pack(pady=15)

pr.mainloop()



