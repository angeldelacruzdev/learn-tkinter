import os
import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter import messagebox
 

root = tk.Tk()

root.title("Run App")


if os.path.isfile("save.txt"):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        appS = [x for x in tempApps if x.strip()]
         

apps = []
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
        
    fileName = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(fileName)
    print(fileName)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
        

def runApps():
    for app in apps:
        os.startfile(app)


def closeApp():
   if(messagebox.askokcancel("Quit",  "Do you want close App")):
       root.destroy()
    
root.overrideredirect(False)
root.configure(background="#003049")
root.attributes('-fullscreen', True)

frame = tk.Frame(root, bg="White")

frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5,
                     fg="white", bg="#f77f00", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#e63946", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

closeApp = tk.Button(root, text="Close App", padx=10,
                    pady=5, fg="white", bg="red", command=closeApp)
closeApp.pack()


root.mainloop()


with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')