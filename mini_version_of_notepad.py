from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
exit_img = ImageTk.PhotoImage(Image.open ("exit.jpg"))

label_file_name = Label(root, text="File name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    text_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragraph=text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()
    
def save():
    input_name = input_file_name.get()
    file = open(input_name+".txt", "w")
    data = my_text.get("1.0",END)
    print(data)
    file.write(data)
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Update", "Success")
    
def closeWindow():
    root.destroy()
    
open_button=Button(root,image=open_img,text="OpenFile", command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
save_button=Button(root, image=save_img,text="Save File", command=save)
save_button.place(relx=0.11,rely=0.03,anchor= CENTER)
exit_button=Button(root,image=exit_img,text="Exit File", command=closeWindow)
exit_button.place(relx=0.17,rely=0.03,anchor= CENTER)

plqnets = ["Mercury","Venus","Earth"]
selectedval = StringVar()
dropdown = ttk.combobox(root, values = planets, textvariable=selectedval)

def PlanetInfo():
    planet = se;ectedval.get()
    if planet == "Mercury":
        label_planet_name['text'] = "Mercury"
        label_planet_image['image'] = Mercury
        label_planet_gravity_radius['text'] = "Gravity : 3.7 m/s \n Radius : 2,439.7 km"
        label_planet_info['text'] = "Mercury is the smallest planet in our solar system. It's just a little bigger than Earth's moon"
    elif planet == "venus":
         label_planet_name['text'] = "Venus"
         label_planet_image['image'] = Venus
         label_planet_gravity_radius['text'] = "Gravity : 8.87 m/s \n Radius : 6,051 km"
         label_planet_info['text'] = "Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky."
    elif planet == "Earth":
        label_planet_name['text'] = "Earth"
        label_planet_image['image'] = Earth
        label_planet_gravity_radius['text'] = "Gravity : 9.807 m/s \n Radius : 6,371 km"
        label_planet_info['text'] = "Earth is the only place in the known universe confirmed to host life and it's the only one known for sure to have liquid water on its surface."
dropdown.place(relx=0.5, rely=0.1 , anchor=CENTER)

btn=Button(root, text="Show planet Info" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)


label_planet.place
root.mainloop()