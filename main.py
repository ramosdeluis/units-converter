from tkinter import *

# Creating the Window.
window = Tk()
window.title('Units Converter')
window.minsize(300, 300)
window.config(padx=40, pady=15)

# Creating the labels.

label_one = Label(text='Select the units')
label_one.config(font=("Comic Sans MS", 20, "bold"))
label_one.grid(column=1, columnspan=3, row=0)

label_two = Label(text='->\nto\n->')
label_two.grid(column=2, row=2)

# Creating the two list box.
list_box_in = Listbox(width=10, exportselection=0)
list_box_out = Listbox(width=10, exportselection=0)
units_list = ['millimeter', 'centimeter', 'decimeter', 'meter', 'decameter', 'hectometer',
              'kilometer', 'foot', 'yard', 'rod', 'chain', 'furlong', 'mile']
for item in units_list:
    list_box_in.insert(units_list.index(item), item)
    list_box_out.insert(units_list.index(item), item)

list_box_in.grid(column=1, row=2)
list_box_out.grid(column=3, row=2)

# Creating the Entry

entry = Entry(width=15)
entry.grid(column=1, columnspan=3, row=3)

# Creating the button.

convert_button = Button(text='Convert')
# quit_button = Button(text='Quit')

convert_button.grid(column=1, columnspan=3, row=4)
# quit_button.grid(column=5, row=0)

# Output interface.

label_tree = Label(text='Awaiting the command...', font=("Comic Sans MS", 15, "bold"))
label_tree.config(padx=10, pady=20)
label_tree.grid(column=1, columnspan=3, row=5)

window.mainloop()
