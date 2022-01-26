from tkinter import *
from PIL import Image, ImageTk


class MenuBar(object):

    def __init__(self, root):

        self.menubar = Menu(root)
    
    @staticmethod
    def configure(root):
        
        menubar = Menu(root)
        def about():
            aboutwin = Toplevel()
            aboutwin.title('About...')
            about_label = Label(aboutwin, text='Prosty program do wyznaczania wartości szczytowej ciśnienia prędkości.')
            about_label.grid(sticky=W, row=0, column=0, padx=5, pady=5)
            contact_label = Label(aboutwin, text='Wszelkie uwagi należy kierować do autora programu pod adresem E-mail: pawelprograms@gmail.com')
            contact_label.grid(sticky=W, row=1, column=0, padx=5, pady=5)
        
        def zones():
            zonewin = Toplevel(root)
            zonewin.title('Strfey obciążenia wiatrem')
            load = Image.open('zone.jpg')
            zone_image = ImageTk.PhotoImage(load)
            zone_image_label = Label(zonewin, image=zone_image)
            zone_image_label.image = zone_image
            zone_image_label.grid(row=0,column=0)
        
        def terraincat():
            terwin = Toplevel(root)
            terwin.title('Kategorie terenu')
            load = Image.open('terraincat.jpg')
            ter_image = ImageTk.PhotoImage(load)
            ter_image_label = Label(terwin, image=ter_image)
            ter_image_label.image = ter_image
            ter_image_label.grid(row=0,column=0)



        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='About...', command = about)

        filemenu.add_separator()

        filemenu.add_command(label='Exit', command=root.quit)
        menubar.add_cascade(label='About', menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Strefy Wiatru', command=zones)
        helpmenu.add_command(label='Kategorie Terenu', command=terraincat)
        menubar.add_cascade(label='Help', menu=helpmenu)

        return menubar

   
        
if __name__ == '__main__':
    root = Tk()
    menubar = MenuBar.configure(root)
    root.config(menu=menubar)
    root.mainloop()