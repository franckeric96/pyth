from tkinter import *

root = Tk()
# personnalité ma fenetre

root.title('formulaire')
root.geometry('1000x800')
root.minsize(400, 380)

bigframe = Frame(root)

frame = Frame(bigframe)

frame_left = Frame(frame)

label_nom = Label(frame_left, text="nom", font=(
    "Courrier", 25))
label_nom.pack()

entry_nom = Entry(frame_left, font=(
    "Courrier", 25))
entry_nom.pack()

label_prenoms = Label(frame_left, text="prénoms", font=(
    "Courrier", 25))
label_prenoms.pack()

entry_prenoms = Entry(frame_left, font=(
    "Courrier", 25))
entry_prenoms.pack()

label_email = Label(frame_left, text="email", font=(
    "Courrier", 25))
label_email.pack()

entry_email = Entry(frame_left, font=(
    "Courrier", 25))
entry_email.pack()


frame_left.pack(side=LEFT)


# frame à droite


frame_right = Frame(frame)

label_specialite = Label(frame_right, text="specialité", font=(
    "Courrier", 25))
label_specialite.pack()

entry_specialite = Entry(frame_right, font=(
    "Courrier", 25))
entry_specialite.pack()

label_contact = Label(frame_right, text="contact", font=(
    "Courrier", 25))
label_contact.pack()

entry_contact = Entry(frame_right, font=(
    "Courrier", 25))
entry_contact.pack()

label_adresse = Label(frame_right, text="adresse", font=(
    "Courrier", 25))
label_adresse.pack()

entry_adresse = Entry(frame_right, font=(
    "Courrier", 25))
entry_adresse.pack()

frame_right.pack(side=RIGHT)


frame.pack(expand=YES)

button = Button(bigframe, text='ajouter', bg='green', font=('Courrier', 20))
button.pack(pady=25)

bigframe.pack(expand=YES)


# ceartion de menu

menu_bar = Menu(root)

# créer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="All")
menu_bar.add_cascade(label="USER", menu=file_menu)


file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="All")
menu_bar.add_cascade(label="PROJECT", menu=file_menu)


file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="All")
menu_bar.add_cascade(label="TO DO", menu=file_menu)


file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="All")
menu_bar.add_cascade(label="ACCOUNT", menu=file_menu)

# configurer notre menu
root.config(menu=menu_bar)


root.mainloop()
