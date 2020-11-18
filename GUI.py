import tkinter as tk
import data_analysis


def press():
    v = list(enter.get())
    if len(v) >= 1:
        v = ''.join(v)
        if v in data_analysis.filename_list0:
            data_analysis.draw0(v)
        else:
            window0 = tk.Tk()
            window0.geometry('200x120')
            show = tk.Label(window0, text='该数据不存在。')
            show.pack()
    v = list()
    for j in range(len(data_analysis.filename_list0)):
        if listbox0.select_includes(j):
            v.append(listbox0.get(j))
    if len(v) >= 2:
        data_analysis.draw(v)
    if len(v) >= 1:
        data_analysis.draw3(v)
    for j in range(len(data_analysis.filename_list1)):
        if listbox1.select_includes(j):
            data_analysis.draw1(listbox1.get(j))
    for j in range(len(data_analysis.filename_list2)):
        if listbox2.select_includes(j):
            data_analysis.draw2(listbox2.get(j))


window = tk.Tk()
window.title('疫情实时数据分析')
window.geometry('170x665+1350+27')
window.resizable(False, False)


text = tk.Label(window, text='疫情实时数据分析', anchor='w')
text.pack()


text = tk.Label(window, text='请选择国家:(可多选)', anchor='w')
text.pack()


button = tk.Button(window, text='确定', width=10, height=1, command=press)
button.place(x=40, y=630)


enter = tk.Entry(window)
enter.pack()


listbox0 = tk.Listbox(window, selectmode='multiple')
for i in data_analysis.filename_list0:
    listbox0.insert('end', i)
listbox0.pack()


listbox1 = tk.Listbox(window)
for i in data_analysis.filename_list1:
    listbox1.insert('end', i)
listbox1.pack()


listbox2 = tk.Listbox(window)
for i in data_analysis.filename_list2:
    listbox2.insert('end', i)
listbox2.pack()


if __name__ == '__main__':
    window.mainloop()

