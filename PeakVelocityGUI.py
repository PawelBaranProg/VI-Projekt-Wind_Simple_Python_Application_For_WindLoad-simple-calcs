from tkinter import *
from PeakVelocityPressure import PeakVelocityPressure
from tkinter import messagebox


class PeakPressureGui(object):

    def __init__(self, root):

        self.zone = IntVar()
        self.terraincategory = IntVar()

        self.frame = Frame(root, borderwidth=5)

        data_label = LabelFrame(self.frame, text='Dane:')
        data_label.grid(row = 0, column  = 0, padx=5, pady=5)

        # Wysokość nad poziomem morza 

        building_height_label = Label(data_label, text = 'Wysokość nad poziomem terenu[m]:')
        building_height_label.grid(sticky=W, row=0, column=0, columnspan=5, padx=5, pady=5)

        building_height_entry = Entry(data_label, width=6)
        building_height_entry.grid(row=0, column =6, padx=5, pady=5)

        over_sea_level_label = Label(data_label, text = 'Wysokość nad poziomem morza[m]:')
        over_sea_level_label.grid(sticky=W, row=1, column=0, columnspan=5, padx=5,pady=5)

        over_sea_level_entry = Entry(data_label, width=6)
        over_sea_level_entry.grid(row=1, column=6,  padx=5, pady=5)


        # Wybór strefy obciążenia wiatrem

        zone_label = Label(data_label, text='Strefa obciążenia wiatrem: ')
        zone_label.grid(sticky = W, row=2, column=0, columnspan=4, padx=5, pady=5)


        z1 = Radiobutton(data_label, text ='1', variable = self.zone, value = 1)
        z1.grid(row=3, column=0, padx=5, pady=5)

        z2 = Radiobutton(data_label, text ='2', variable = self.zone, value = 2)
        z2.grid(row=3, column=1, padx=5, pady=5)

        z3 = Radiobutton(data_label, text ='3', variable = self.zone, value = 3)
        z3.grid(row=3, column=2, padx=5, pady=5)

        # Wybór kategori terenu:

        terraincategory_label = Label(data_label, text ='Kategoria terenu:')
        terraincategory_label.grid(sticky = W, row=4, column=0, columnspan=4, padx=5, pady=5)

        k1 = Radiobutton(data_label, text = '0', variable = self.terraincategory, value=0)
        k1.grid(row=5, column=0, padx=5, pady=5)

        k2 = Radiobutton(data_label, text = 'I', variable = self.terraincategory, value=1)
        k2.grid(row=5, column=1, padx=5, pady=5)

        k3 = Radiobutton(data_label, text = 'II', variable = self.terraincategory, value=2)
        k3.grid(row=5, column=2, padx=5, pady=5)

        k4 = Radiobutton(data_label, text = 'III', variable = self.terraincategory, value=3)
        k4.grid(row=5, column=3, padx=5, pady=5)

        k5 = Radiobutton(data_label, text = 'IV', variable = self.terraincategory, value=4)
        k5.grid(row=5, column=4, padx=5, pady=5)

        def create_case():
            try:
                building_height = float(building_height_entry.get())
                above_see = float(over_sea_level_entry.get())
            except ValueError:
                messagebox.showerror('Złe dane', 'Wprowadź wysokość w liczbach')
            zone = self.zone.get()
            terraincategory = self.terraincategory.get()

            case = PeakVelocityPressure(zone=zone, terraincat=terraincategory, above=above_see, height=building_height)
            return case
        
        result_label = Label(self.frame, text='Wyniki obliczeń wg PN-EN 1991-1-4:2008:')
        result_label.grid(row=2, column=0, padx=5, pady=5)

        ce_label = Label(self.frame, text = 'Wartość współczynnika ekspozycji: ')
        ce_label.grid(sticky=W, row=3, column=0, padx=5, pady=5)

        qbf_label = Label(self.frame, text = 'Wartość szczytowa ciśnienia prędkości:BRAK')
        qbf_label.grid(sticky=W, row=4, column=0, padx=5, pady=5)


        def evaluate():
            case = create_case()
            ce = case.exposurefactorcoef()
            qbf = case.peakvelocitypressure()
            ce_label.config(text = 'Wartość współczynnika ekspozycji: ' + str(ce) )
            qbf_label.config(text='Wartość szczytowa ciśnienia prędkości: ' + str(qbf) + ' kPa')
            
        
        evaluate = Button(self.frame, text='Oblicz!', command = evaluate)
        evaluate.grid(row=1, column=0, padx=5, pady=5)

if __name__ == '__main__':
    root = Tk()
    root.title('Wiatr')
    test = PeakPressureGui(root)
    test.frame.grid(row=0, column=0)
    root.mainloop()
