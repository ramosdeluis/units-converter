from tkinter import *

from converter import Converter

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
choices = {'in': 'meter', 'out': 'kilometer'}


def listbox_select_in(event):
    choices['in'] = list_box_in.get(list_box_in.curselection())


def listbox_select_out(event):
    choices['out'] = list_box_out.get(list_box_out.curselection())


list_box_in = Listbox(width=10, exportselection=0)
list_box_out = Listbox(width=10, exportselection=0)
units_list = ['millimeter', 'centimeter', 'decimeter', 'meter', 'decameter', 'hectometer',
              'kilometer', 'inches', 'feet', 'yard', 'rod', 'chain', 'furlong', 'mile']
for item in units_list:
    list_box_in.insert(units_list.index(item), item)
    list_box_out.insert(units_list.index(item), item)

list_box_in.grid(column=1, row=2)
list_box_out.grid(column=3, row=2)

list_box_in.bind("<<ListboxSelect>>", listbox_select_in)
list_box_out.bind("<<ListboxSelect>>", listbox_select_out)

# Creating the Entry

entry = Entry(width=15)
entry.grid(column=1, columnspan=3, row=3)

# Creating the button.

val = 1


def click_button():
    user_number = entry.get()
    try:
        user_number = float(user_number)
        converter = Converter(user_number, choices)
        try:
            label_four.config(text=f"{converter.user_value} {converter.choices['in']}\n=")
            label_four.grid(column=1, columnspan=3, row=5)
            label_tree.config(text=f"{converter.calculate():.4f} "
                                   f"{converter.choices['out']}s")
        except:
            label_tree.config(text=f"{converter.reverse_calculate():.4f} "
                                   f"{converter.choices['out']}s")
    except ValueError:
        label_tree.config(text=f"Sorry, '{user_number}' \nis not an option.")


convert_button = Button(text='Convert', command=click_button)

convert_button.grid(column=1, columnspan=3, row=4)

# quit_button = Button(text='Quit')
# quit_button.grid(column=5, row=0)

# Output interface.

label_tree = Label(text='Awaiting the command...', font=("Comic Sans MS", 15, "bold"))
label_tree.grid(column=1, columnspan=3, row=6)

label_four = Label(font=("Comic Sans MS", 15, "bold"))

window.mainloop()
