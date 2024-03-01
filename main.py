from tkinter import *
import messagebox


def add_task():
    mytask = task_entry.get()
    if mytask != "":
        with open("to_do_list.txt", "a") as f:
            f.write("Yapılacaklar : "+mytask+"\n")
        listbox_task.insert(END, "Yapılacaklar : "+ mytask)

        task_entry.delete(0, END)
        messagebox.showinfo(title="Görev Eklendi", message="Göreviniz Başarıyla Eklendi.")

    else:
         messagebox.showwarning(title="Hatalı İşlem", message="Boş Değer Girmeyiniz")

def save_and_close():
    try:
        with open("to_do_list.txt", "a") as f:
            pass
    except FileNotFoundError:
        print("Dosya bulunamadı.")

    f.close()
    window.destroy()
def delete_task():
    try :
        delete_task_index = listbox_task.curselection()
        if delete_task_index !=[]:
            if delete_task_index:
                index = int(delete_task_index[0])
                with open("to_do_list.txt", "r") as f:
                    lines = f.readlines()
                del lines[index]
                with open("to_do_list.txt", "w") as f:
                    f.writelines(lines)
                listbox_task.delete(index)
                messagebox.showinfo(title="Değer Silindi",message="Değer Silindi")
                f.close()
    except:
        messagebox.showinfo(title="Hata", message="Değer Silindi")


def loads_task():
    try:
        with open("to_do_list.txt", "r") as f:
            lines = f.readlines()
            listbox_task.delete(0,END)
            for line in lines:
                listbox_task.insert(END, line.strip())
    except FileNotFoundError:
        print("Dosya bulunamadı.")


my_font = "Arial", "14", "bold italic"
my_font1 = "Arial", "15", "bold italic"

window = Tk()
window.geometry("600x800")
window.config(bg="lavender")
listbox_task = Listbox(window, width=50, height=20,font=my_font1)
listbox_task.pack(pady=5)

task_entry = Entry(window, width=30,font=my_font1)
task_entry.pack(pady=2)
add_task_button = Button(window, width=19, text="Görev Ekle", font=my_font, command=add_task)
add_task_button.pack(pady=5)
delete_task_button = Button(window, width=19, text="Görev Sil", font=my_font, command=delete_task)
delete_task_button.pack(pady=3)
load_task_button = Button(window,width=19, text="Görev yükle", font=my_font, command=loads_task)
load_task_button.pack(pady=3)
save_task_button = Button(window,width=19, text="Kaydet Ve Çık", font=my_font, command=save_and_close)
save_task_button.pack(pady=3)
window.mainloop()
