import random
from tkinter import *
from tkinter import messagebox


def convert(s):
    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in range(0,len(s)):
        new += s[x]

        # return string
    return new
def indexing(a,t):
    lst=[]
    for e in range (0,len(a)):
        if a[e]==t:
            lst.append(int(e))
    return lst



state=["Andhra  Pradesh", "Arunachal  Pradesh","Assam","Bihar", "Chhattisgarh","Goa","Gujarat","Haryana","Himachal  Pradesh","Jammu  and  Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra",
	"Manipur",
	"Meghalaya",
        "Mizoram",

	"Nagaland",
	"Odisha",
	"Punjab",
	"Rajasthan",
	"Sikkim",
       "Tamil  Nadu",
	"Telangana",
	"Tripura",
	"Uttar  Pradesh",
	"Uttarakhand",
       "West  Bengal",

	"Andaman",
	"Chandigarh",
       "Dadar" ,
	"Daman" ,
	"Delhi",
       "Lakshadweep",
	"Puducherry"]

s = random.choice(state)

s=s.lower()
vow=['a','e','i','o','u']
count = 0
#c=""

a = []
for e in range(0,len(s)):
    if(s[e]!=' '):
        a.append('_')
    else:
        a.append(' ')
for i in range(0,len(vow)):
    if(vow[i] in s):
        u=indexing(s,vow[i])
        print(u)
        for x in range(0,len(u)):
            a[u[x]]=vow[i]

print("line worked")
print(str(a))
#gui elements begin
screen=Tk()


screen.geometry("1000x1000")

screen.wm_minsize(width=300,height=300)
screen.wm_maxsize(width=1366,height=768)
#screen.configure(background='black')

f1=Frame(screen,borderwidth=2,relief="solid")
f1.place(x=10,y=10,width=400,height=200)
q=IntVar()


q.set(1)
r1=Radiobutton(f1,text="State",value=1,variable=q)

r2=Radiobutton(f1,text="Movie",value=2,variable=q)

r3=Radiobutton(f1,text="Country",value=3,variable=q)
r1.place(x=50,y=60)
r2.place(x=120, y=60)
r3.place(x=70,y=60)
pic=PhotoImage(file="C:/Users/sgbhidu.LAPTOP-QSE5SAAV/Desktop/000091-0012-000071_tnb.png")
#pic.resize((1200,700))
label=Label(screen,image=pic)
label.place(x=0,y=0,relwidth=1,relheight=1)
#label.pack()
header=Label(screen,text="HANGMAN",font=("the Gingerbread House",48,'bold'),bd=4,relief='solid',fg="#bb0a1e",compound=CENTER,bg='#008080')
header.pack()
box=Canvas(screen,borderwidth=3,bd=2,relief="solid")

box.place(x=10,y=100,width=500,height=500)

box.create_rectangle(80,50,85,400,fill="black")#support stick
box.create_rectangle(80,400,400,420,fill="black")#base stick
box.create_rectangle(80,50,270,55,fill="black")#top stick
box.create_line(240,50,240,137.5,width=5)#rassi




v=StringVar()
label1=Label(screen,text="Enter your text",font=("A Lolita Scorned",32,'bold'),bg='#008080',fg='white',bd=3,relief='solid')
label1.place(x=800,y=100)
e1=Entry(screen,width=25,textvariable=v,font=("the Gingerbread House",32,'bold'),text="enter your text or word")

e1.place(x=800,y=270,width=250,height=60)
label2=Label(screen,text=convert(a),font=("Bodoni",24,'bold'),bg='white',fg='black',bd=3,relief='solid')
label2.place(x=11,y=525,width=495,height=70)


def action():
    global count
    global indexing
   # global c
    global a
    global s
    global v
    #label2.configure(text=v.get())
    c=str(e1.get())
    #print(c)
    c=c.lower()

    #print(c)


    l4.configure(text="Attempts\n remaining :-" + str(6 - count))
    if (count > 5):
        messagebox.showinfo("Trials Exceeded...", "YOU LOSE")
        box.create_line(240, 237.5, 290, 284.5, width=3)  # right hand
        return


    if (not c in s ):
        count = count + 1
        messagebox.showwarning("INCORRECT!","Guess another word")
        l4.configure(text=" Attempts\n remaining :- " + str(6 - count)+ " ")
    else:

        if ((c == s or convert(a)==s) and count <= 6):
            label2.config(text=s)

            messagebox.showinfo("VICTORY!!!!","Congratulations you won!!")

            return
        print(v.get())
        for e in range(0,len(c)):
            lst=indexing(s,c[e])
            print(lst)
            for i in range(0,len(lst)):
                a[lst[i]]=s[lst[i]]
    if (count == 1 and not c in s):
        box.create_oval(190, 137.5, 290, 237.5, fill="white", width=3)  # face

    if (count == 2 and not c in s):
        box.create_line(240, 237.5, 240, 337.5, width=3)  # body

    if (count == 3 and not c in s):
        box.create_line(240, 337.5, 190, 385, width=3)  # left leg

    if (count == 4 and not c in s):
        box.create_line(240, 337.5, 290, 385, width=3)  # right leg

    if (count == 5 and not c in s):
        box.create_line(240, 237.5, 190, 284.5, width=3)  # left hand


    print(a)
    label2.config(text=convert(a))
#label2.config(text=a)
b1=Button(screen,text="Check",font=("A Lolita Scorned",36,"bold"),bd=2,relief='solid',command=action,bg='#008080',fg='white')
b1.place(x=800,y=450,width=160,height=90)


#l3=Label(text=" Warning:- ", font=('A Lolita Scorned',24,'bold'),bd=2,relief='solid',bg='#008080',fg='white')
#l3.place(x=800,y=450)
#@l3.config(width=15,height=2)
l4=Label(text=" Attempts\n remaining:- 6 ",font=('A Lolita Scorned',24,'bold'),bd=2,relief='solid')

l4.place(x=300,y=150)

print(s)

screen.mainloop()


                #label will be configed here





