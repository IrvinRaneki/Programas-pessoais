from Tkinter import *
import webbrowser

root = Tk()
frame = Frame(root)
frame.pack()

url = 'http://www.sampleurl.com'

def OpenUrl(url):
    webbrowser.open_new(url)

button = Button(frame, text="CLICK", command=OpenUrl(url))

button.pack()
root.mainloop()
