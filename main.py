from tkinter import *
import re
import time
import random

file=open("1-1000.txt")
all_words=file.read()
t=all_words.replace("\n"," ")
text_split=t.split()

random_words = [random.choice(text_split) for x in range(36)]
random_string = " ".join(random_words)
user_input = [0]
whitespaces_list = [0] + [i.start() for i in re.finditer(" ", random_string)]


window = Tk()
window.title("Typing Speed Test")
window.geometry("750x700")

window.config(bg='white')

n=0
match=0
count=60

def next_word(event):
    global n
    global match
    n=n+1
    z=random_words[n-1]
    correct_word = re.search(z,entry.get())
    print(f"Correct word: {correct_word}")
    if "first_word" in text.tag_names():
        text.tag_delete("first_word")
    try:
        text.tag_delete(str(n-1)+"next")
    except:
        pass
    print(text.tag_names())
    start = '1.' + str(whitespaces_list[n - 1])
    end = '1.' + str(whitespaces_list[n])
    text.tag_add(str(n), start, end)
    if correct_word:
        text.tag_config(str(n), foreground="green")
    else:
        text.tag_config(str(n), foreground="red")


    start_next='1.' + str(whitespaces_list[n]+1)
    end_next = '1.' + str(whitespaces_list[n+1])

    text.tag_add(str(n)+'next', start_next, end_next )
    text.tag_config(str(n)+'next', background='#e6ebec')

    input=entry.get()
    words=input
    user_input.append(words)
    if "TIME OVER" in user_input:
        user_input.remove("TIME OVER")
    entry.delete(0, END)

def count_time(event):
    window.unbind("<Key>")
    global count
    global match
    if count<0:
        var.set(f"\n\n\n0 sec")
    while count>0:
        count=count-1
        window.update()
        time.sleep(1)
        var.set(f"\n\n\n{count} sec")

    if count==0:
        time.sleep(0)
        window.update()
        var.set(f"\n\n\n0 sec")
        entry.delete(0, END)
        entry.insert(0,"TIME OVER")
        entry.config(state='disabled')
        clean_input=[x.rstrip() for x in user_input[1:] ]
        print(f"Clean:{clean_input}")

    for i in range(len(clean_input)):
        print(random_words[i])
        if random_words[i] == clean_input[i]:
            match += 1
        print(f"Match: {match}")

        if len(clean_input)>0:
            accuracy=int(match/len(clean_input)*100)
            var1.set(f"{accuracy}% \n\n\n Accuracy\nof typing")

        input_string=" ".join(clean_input)
        print(input_string)

        CPM=len(input_string)
        WPM=CPM/5

        wpm.set(f"\n\n{WPM} \n\n Words\n per minute\n (WPM)")
        cpm.set(f"\n\n{CPM} \n\n Characters\n per minute\n (CPM)")
        print(user_input)


window.bind("<space>", next_word)
window.bind("<Key>", count_time)


canvas = Canvas(height=90, width=750)
logo_img = PhotoImage(file="logo1.png")
canvas.create_image(375, 45, image=logo_img)
canvas.config(bg="white",highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=4)

label=Label(font=("Arial",16), wraplength=600, text="Check how fast you can type. This test takes 1 minute. Write "
                                        "words you see below, use space key after typing each word.")
label.grid(row=1, column=0, columnspan=4)
label.config(bg="white",highlightthickness=0 )

image=PhotoImage(file="canvas.png")
label1 = Label(image=image, height=211, width=750)
label1.config(bg="white",highlightthickness=0)
label1.grid(row=2, column=0, columnspan=4)


text=Text(label1)
text.tag_configure("center", justify='center')
text.insert(1.0, "")
text.place(height=180, width=650, x=40, y= 20)
text.config(highlightthickness=0, relief="flat", font=('Arial', 19, 'normal'), wrap=WORD)
text.insert(INSERT, random_string)
text.tag_add("center", "1.0", "end")

end_first = '1.' + str(whitespaces_list[n+1])
text.tag_add('first_word', "1.0", end_first)
text.tag_config("first_word", background='#e6ebec')

image1=PhotoImage(file="canvas2.png")
label2 = Label(image=image1, height=80, width=255)
label2.config(bg="white",highlightthickness=0, pady=20)
label2.grid(row=3, column=1, columnspan=2, pady=10)


entry=Entry(label2)
entry.config(bg="#f4f4f5", justify="center", font=('Arial', 19, 'normal'))
entry.place(height=40, width=230, x=10, y=20)
entry.insert(0, "")
entry.focus_set()

# button_img = PhotoImage(file="button_reset.png")
# button_img_label=Label(image=button_img)
# button=Button(image=button_img, command=reset)
# button.grid(row=3, column=3)


image2=PhotoImage(file="img_bottom.png")
cpm=StringVar()
bottom_label1=Label(image= image2, textvariable=cpm, compound=CENTER, font=("Arial", 20, "bold"))
bottom_label1.config(bg="white",highlightthickness=0)
cpm.set(" \n\n-- \n\n Characters\n per minute\n (CPM)")
bottom_label1.grid(row=4, column=0)

image3=PhotoImage(file="img_bottomgreen.png")
wpm=StringVar()
bottom_label2=Label(image= image3, compound=CENTER, textvariable=wpm, font=("Arial", 20, "bold"))
wpm.set(" \n\n-- \n\n Words\n per minute\n (WPM)")
bottom_label2.config(bg="white",highlightthickness=0 )
bottom_label2.grid(row=4, column=1)

image4=PhotoImage(file="img_bottomblue.png")
var1=StringVar()
bottom_label3=Label(compound=CENTER, image= image4, textvariable=var1, font=("Arial", 20, "bold"))
var1.set(" -- % \n\n\n Accuracy\nof typing")
bottom_label3.config(bg="white",highlightthickness=0 )
bottom_label3.grid(row=4, column=2)

image5=PhotoImage(file="img_bottomrose.png")
var=StringVar()
bottom_label4=Label(compound=CENTER, image= image5, textvariable=var, font=("Arial", 25, "bold"))
var.set("\n\n\n60 sec")
bottom_label4.config(highlightthickness=0)
bottom_label4.grid(row=4, column=3)



window.mainloop()
