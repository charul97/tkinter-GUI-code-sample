from tkinter import *
#from tkinter.messagebox import *



'''
def show_answer():
    Ans = trans()
    blank.insert(0, Ans)


main = Tk()
#size of the window
main.geometry("1000x1000")
#S = Scrollbar(main)
main.title("Translator")     #Title of the main window
Label(main, text = " You can translate your text here!",bg= "DarkRed", fg="white",height= 2, font= "arial").grid(row=0)
Label(main, text = " Enter the text here: ", bg= "white",height= 2).grid(row=4)
Label(main, text = " Translated text: ", bg= "white",height= 2).grid(row=27)
#num1 = Entry(main)
#blank = Entry(main)

T1 = Text(main, height=20, width= 100)
T1.grid(row = 5)
T2 = Text(main, height=20, width= 100)
T2.grid(row =30)
xscrollbar = Scrollbar(T1, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0,sticky=E+W)

yscrollbar = Scrollbar(T1)
yscrollbar.grid(row=0, column=1,sticky=N+S)


#text = Text(frame, wrap=NONE, bd=0,
            #xscrollcommand=xscrollbar.set,
           #yscrollcommand=yscrollbar.set)


Button(main, text='Quit', command=main.destroy,bg= "DarkRed", fg="white").grid(row=62, column=0, sticky=W, pady=4)
Button(main, text='Translate', command=show_answer,bg= "DarkRed", fg="white").grid(row=60, column=0, sticky=W, pady=4)
Button(main, text='clear', command=show_answer,bg= "DarkRed", fg="white").grid(row=64, column=0, sticky=W, pady=4)
mainloop()
'''


master = Tk()


filename = PhotoImage(file = "/home/charul/Desktop/del3.png")
background_label = Label(master, image=filename)
background_label.place(anchor=N, x= 180, bordermode=OUTSIDE, height=210, width=320)


Label(master, text="Your search",font=("Helvetica", 16), fg="red", bg="#BBDEFB", padx=20, pady=40).grid(row=3, column=1, sticky=E)


e1 = Entry(master)

e1.grid(row=3, column=2,columnspan= 4, rowspan=2, sticky=W)

Button(master, text='Start Live Streaming Twitter Data', command=master.quit, bg="#0D47A1", fg="white",activebackground="black", activeforeground="white", bd=4, width=30 ).grid(row=13, column=1, sticky=E, pady=10, padx=20)
Button(master, text='Stop Twitter Streaming', command=master.quit,bg="#0D47A1", fg="white",activebackground="black", activeforeground="white", bd=4, width=30).grid(row=13, column=3, sticky=W, pady=10)
Button(master, text='Show Results', command=master.quit, bg="#0D47A1", fg="white",activebackground="black", activeforeground="white", bd=4).grid(row=15, column=3, sticky=W, pady=10, padx= 0)

text1 = Text(master,height=30, bg="black", fg="white")
text2 = Text(master,height=30, bg="black", fg="white")

text1.grid(row = 18,column=1, padx=40)
text1.insert(INSERT, "Summarized result from Web")



text2.grid(row = 18,column=3, padx=40)
text2.insert(INSERT, "Summarized result from Twitter")

master.configure(background='#BBDEFB')
mainloop( )
