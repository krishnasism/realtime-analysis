def start():
    import application
    application.start()

import tkinter
import cv2
import PIL.Image, PIL.ImageTk

window = tkinter.Tk()

btn_start = tkinter.Button(window,text="Start Listening", width=50, height=50, command=start)
btn_start.config( height = 50, width = 55 )
btn_start.pack()
cv_img = cv2.cvtColor(cv2.imread("welcome_to_the_app.jpg"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=1366, height=768)
canvas.pack()
photo=PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))

canvas.create_image(0,0,image=photo,anchor=tkinter.NW) 




window.mainloop()

