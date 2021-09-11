import tkinter as tkr
app = tkr. Tk(__name__)
app.title('MY Calculater')
app.geometry('500x500')
tkr.Label(app,text='First Number').place(x=15,y=15)
tkr.Label(app,text='Second Number').place(x=350,y=15)
tkr.Label(app,text='Result').place(x=150,y=250)
tkr.Label(app,text='Operations').place(x=200,y=90)



f=tkr.Variable(app)
s=tkr.Variable(app)
r=tkr.Variable(app)

tkr.Entry(app,textvariable=f).place(x=15,y=50)
tkr.Entry(app,textvariable=s).place(x=350,y=50)
tkr.Entry(app,textvariable=r).place(x=200,y=250)



def f1():
    print(float(f.get())+float(s.get()))
    r.set(float(f.get())+float(s.get()))

def f2():
    print(float(f.get())*float(s.get()))
    r.set(float(f.get())*float(s.get()))

def f3():
    print(float(f.get())-float(s.get()))
    r.set(float(f.get())-float(s.get()))

def f4():
    print(float(f.get())/float(s.get()))
    r.set(float(f.get())/float(s.get()))

tkr.Button(app,text='+',command=f1).place(x=150,y=120)
tkr.Button(app,text='*',command=f2).place(x=200,y=120)
tkr.Button(app,text='-',command=f3).place(x=250,y=120)
tkr.Button(app,text='/',command=f4).place(x=300,y=120)

        











app.mainloop()
