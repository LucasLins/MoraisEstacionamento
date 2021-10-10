import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview, Style

from dao import *

window = Tk()
window.geometry("1280x768")
window.configure(bg="#FFFFFF")
window.resizable(False, False)
window.title("Morais Estacionamento")

style = ttk.Style()
style.theme_use("alt")
style.configure("Treeview", background="#E2F1FF", foreground="#413D4B", rowheight=25, columnheight=20, fieldbackground="#E2F1FF")
style.map('Treeview', background=[('selected', '#8aacc8')])

columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10")
table = Treeview(window, show="headings", column=columns, selectmode="browse")
table.heading('#1', text="Nome")
table.heading('#2', text="Total carro")
table.heading('#3', text="Total moto")
table.heading('#4', text="Total caminhão")
table.heading('#5', text="Vagas carro")
table.heading('#6', text="Vagas moto")
table.heading('#7', text="Vagas caminhão")
table.heading('#8', text="Taxa/h")
table.heading('#9', text="Titulo aviso")
table.heading('#10', text="Mensagem aviso")

table.column('#1',minwidth=0, width=100, stretch=NO)
table.column('#2',minwidth=0, width=100, stretch=NO)
table.column('#3',minwidth=0, width=100, stretch=NO)
table.column('#4',minwidth=0, width=100, stretch=NO)
table.column('#5',minwidth=0, width=100, stretch=NO)
table.column('#6',minwidth=0, width=100, stretch=NO)
table.column('#7',minwidth=0, width=100, stretch=NO)
table.column('#8',minwidth=0, width=100, stretch=NO)
table.column('#9',minwidth=0, width=100, stretch=NO)
table.column('#10',minwidth=0, width=100, stretch=NO)



#data = tableRegistros.find(tableRegistros.table.columns.datasaida >= "2021-09-21 13:08:00", tableRegistros.table.columns.datasaida <= "2021-09-22 13:40:00", order_by="datasaida")
#data = tableRegistros.find(tableRegistros.table.columns.datasaida >= "2021-09-21")


for item in tableEstacionamentos:
    table.insert("", tkinter.END, values=[item.nome, item.totalcarro, item.totalmoto, item.totalcaminhao, item.vagascarro,
                                          item.vagasmoto, item.vagascaminhao, item.valor, item.avisotitulo, item.avisomsg])

table.place(x=0, y=0)

def getSelection():
    selection = table.focus()
    print(table.item(selection)['values'][1])


btn = Button(window, height=2, width=5, command=lambda: getSelection())

btn.place(x=00, y=400)

window.mainloop()

