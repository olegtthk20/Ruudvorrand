from tkinter import *
from math import *
def lahenda():
    if (a.get()!=''and b.get()!=''and c.get()!=''):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        a.configure(bg='lightblue')
        b.configure(bg='lightblue')
        c.configure(bg='lightblue')
        D=b_*b_-4*a_*c_
        if D>0:
            vst1=( -1*b_ + sqrt(D))/(2*a_)
            vst2=( -1*b_ - sqrt(D))/(2*a_)
            t=f'X1={vst1}, \nX2={svt2}'
        elif D=0:
            vst1=(-1*b_)/(2*a_)
            t=f'X1={vts1}'
        else:
            t='Корней нет'
        vastus.configure(text=f'D={D}\n{t}', font='Calibri 26')
    else:
        if a.get()=='':
            a.configure(bg='red')
        elif b.get()=='':
            b.configure(bg='red')
        elif c.get()=='':
            c.configure(bg='red')
aken=Tk()
aken.geometry('900x500')
lbl=Label(aken,text='решение квадратного уравнения', font='Calibri 26', fg='darkgreen', bg='lightblue')
lbl.pack()
a=Entry(aken, font='Calibri 26', fg='darkgreen', bg='lightblue',width=3)
a.pack(side=LEFT)
x2=Label(aken,text='x**2+', font='Calibri 26', fg='darkgreen',)
x2.pack(side=LEFT)
b=Entry(aken, font='Calibri 26', fg='darkgreen', bg='lightblue',width=3)
b.pack(side=LEFT)
x=Label(aken,text='x+', font='Calibri 26', fg='darkgreen',)
x.pack(side=LEFT)
c=Entry(aken, font='Calibri 26', fg='darkgreen', bg='lightblue',width=3)
c.pack(side=LEFT)
y=Label(aken,text='=0', font='Calibri 26', fg='darkgreen',)
y.pack(side=LEFT)
btn=Button(aken,text='решить', font='Calibri 26', bg='darkgreen', command=lahenda)
btn.pack(side=LEFT)
vastus=Label(aken, height=4, width=60, bg='lightyellow')
vastus.pack(side=LEFT)




aken.mainloop()