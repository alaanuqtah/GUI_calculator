import tkinter as tk

calc=""

def add_to_calc(symbol):
    global calc
    calc+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calc)


def evaluate_calc():
    global calc
    try:
        result= str(eval(calc))
        calc=""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
        global calc
        calc=""
        text_result.delete(1.0,"end")




#GUI 

root=tk.Tk()
root.geometry("300x275")
text_result=tk.Text(root,height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)

#the digits
btn_1=tk.Button(root,text="1",command=lambda: add_to_calc(1),width=5,font=("Arial",14))
btn_1.grid(row=2,column=1)

btn_2=tk.Button(root,text="2",command=lambda: add_to_calc(2),width=5,font=("Arial",14))
btn_2.grid(row=2,column=2)

btn_3=tk.Button(root,text="3",command=lambda: add_to_calc(3),width=5,font=("Arial",14))
btn_3.grid(row=2,column=3)

btn_4=tk.Button(root,text="4",command=lambda: add_to_calc(4),width=5,font=("Arial",14))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(root,text="5",command=lambda: add_to_calc(5),width=5,font=("Arial",14))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(root,text="6",command=lambda: add_to_calc(6),width=5,font=("Arial",14))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(root,text="7",command=lambda: add_to_calc(7),width=5,font=("Arial",14))
btn_7.grid(row=4,column=1)

btn_8=tk.Button(root,text="8",command=lambda: add_to_calc(8),width=5,font=("Arial",14))
btn_8.grid(row=4,column=2)

btn_9=tk.Button(root,text="9",command=lambda: add_to_calc(9),width=5,font=("Arial",14))
btn_9.grid(row=4,column=3)

btn_0=tk.Button(root,text="0",command=lambda: add_to_calc(0),width=5,font=("Arial",14))
btn_0.grid(row=5,column=2)

#the symbols / operations

btn_add=tk.Button(root,text="+",command=lambda: add_to_calc("+"),width=5,font=("Arial",14))
btn_add.grid(row=2,column=4)

btn_minus=tk.Button(root,text="-",command=lambda: add_to_calc("-"),width=5,font=("Arial",14))
btn_minus.grid(row=3,column=4)

btn_mul=tk.Button(root,text="x",command=lambda: add_to_calc("*"),width=5,font=("Arial",14))
btn_mul.grid(row=4,column=4)

btn_div=tk.Button(root,text="/",command=lambda: add_to_calc("/"),width=5,font=("Arial",14))
btn_div.grid(row=5,column=4)

btn_opBracket=tk.Button(root,text="(",command=lambda: add_to_calc("("),width=5,font=("Arial",14))
btn_opBracket.grid(row=5,column=1)

btn_clBracket=tk.Button(root,text=")",command=lambda: add_to_calc(")"),width=5,font=("Arial",14))
btn_clBracket.grid(row=5,column=3)

btn_eql=tk.Button(root,text="=",command=lambda: evaluate_calc(),width=11,font=("Arial",14))
btn_eql.grid(row=6,column=3,columnspan=2)

btn_clear=tk.Button(root,text="C",command=clear_field,width=11,font=("Arial",14))
btn_clear.grid(row=6,column=1,columnspan=2)

root.mainloop()