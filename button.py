from tkinter import*
if __name__== '__main__':
    root=Tk();
    root.title('new window');
    Label(root, text='your buttons are here').pack(pady=10);
    Button(root, text='this is the right button').pack(side=LEFT);
    Button(root, text='this is the wrong button').pack(side=LEFT);
    root.mainloop();
        