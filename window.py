from tkinter import*
if __name__== '__main__':
    root=Tk();
    root.title('new window');
    #Label(root,text='this is the main top level').pack(pady=10,padx=100)#pady=length padx=width
    for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
        f= Frame(root,borderwidth=2,relief=relief);
        Label(f,text=relief,width=10).pack(side=LEFT);
        f.pack(side=LEFT,padx=5,pady=5);
    root.mainloop();