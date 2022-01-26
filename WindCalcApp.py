from PeakVelocityGUI import PeakPressureGui
from MenuGui import MenuBar
from tkinter import *

root = Tk()
root.title('Wiatr')
menubar = MenuBar.configure(root)
test = PeakPressureGui(root)
test.frame.grid(row=0, column=0)
root.config(menu=menubar)
root.mainloop()