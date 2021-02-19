from tkinter import*
import pygame

pygame.init()
root = Tk()
root.title("Who wants to be a millionaiure")
root.geometry('1352x652+0+0')
root.configure(background='black')

#==============Frames==========================
ABC=Frame(root,bg='black')
ABC.grid()

ABC1=Frame(root,bg='black',bd=20,width=900,height=600)
ABC1.grid(row=0,column=0)
ABC2=Frame(root,bg='black',bd=20,width=452,height=600)
ABC2.grid(row=0,column=1)

ABC1a=Frame(ABC1,bg='black',bd=20,width=900,padx=230,height=200)
ABC1a.grid(row=0,column=0)
ABC1b=Frame(ABC1,bg='black',bd=20,width=900,height=200)
ABC1b.grid(row=1,column=0)
ABC1c=Frame(ABC1,bg='black',bd=20,width=900,height=200)
ABC1c.grid(row=2,column=0)


#==============Images==========================


def Change50_50():
       canvas = Canvas (ABC1a, bg='black' , width=180, height=80)
       canvas.grid (row=0, column=0)
       canvas.delete ("all")
       image1=PhotoImage (file=r"C:\Users\HP\Desktop\change50.png")
       canvas.create_image (90, 40, image =image1)
       canvas.image = image1


def PeopleChange():
    canvas = Canvas(ABC1a, bg='black', width=180, height=80)
    canvas.grid(row=0, column=1)
    canvas.delete("all")
    image1 = PhotoImage(file=r"C:\Users\HP\Desktop\changeaudience.png")
    canvas.create_image(90, 40, image=image1)
    canvas.image = image1


def ChangePhone():
    canvas = Canvas(ABC1a, bg='black', width=180, height=80)
    canvas.grid(row=0, column=2)
    canvas.delete("all")
    image1 = PhotoImage(file=r"C:\Users\HP\Desktop\changephone.png")
    canvas.create_image(90, 40, image=image1)
    canvas.image = image1


def MillionPicture1():
    canvas = Canvas(ABC2, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file=r"C:\Users\HP\Desktop\Picture1.png")
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def MillionPicture2():
    canvas = Canvas(ABC2, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file=r"C:\Users\HP\Desktop\Picture2.png")
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def MillionPicture3():
    canvas = Canvas(ABC2, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file=r"C:\Users\HP\Desktop\Picture3.png")
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def MillionPicture4():
    canvas = Canvas(ABC2, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file=r"C:\Users\HP\Desktop\Picture4.png")
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1

#==============Images==========================


CentreImage=PhotoImage(file=r"C:\Users\HP\Desktop\Centre.png")
LogoCentre=Button(ABC1b,image=CentreImage,bg='black',width=300,height=200)
LogoCentre.grid()

Image50_50 = PhotoImage ( file=r"C:\Users\HP\Desktop\fiftyfifty.png")
Live50_50 = Button (ABC1a, image = Image50_50, bg='black', width=180, height=150,command=Change50_50)
Live50_50.grid (row=0, column=0)

ImagePhone = PhotoImage (file=r"C:\Users\HP\Desktop\phonefront.png" )
LivePhone = Button (ABC1a, image = ImagePhone, bg='black' , width=180, height=150,command=ChangePhone)
LivePhone.grid (row=0, column=2)

ImagePeople = PhotoImage ( file=r"C:\Users\HP\Desktop\audience.png" )
LivePeople = Button (ABC1a, image = ImagePeople, bg='black', width=180, height=150, command=PeopleChange)
LivePeople.grid (row=0, column=1)

MillionImage=PhotoImage( file=r"C:\Users\HP\Desktop\Picture0.png")
MillionImg = Button (ABC2, image = MillionImage, bg='black', width=430, height=800)
MillionImg.grid (row=0, column=0)

#=================Million Question======================================


Question1 = StringVar()
Question2 = StringVar()
Question3 = StringVar()
Question4 = StringVar()


Answer1 = StringVar()
Answer2 = StringVar()
Answer3 = StringVar()
Answer4 = StringVar()


Question1.set ("Q1: What is 2 + 32")
Answer1. set("22")
Answer2. set("32")
Answer3 . set("31")
Answer4 . set("34")


def Question2():
      Question1. set ("Q1: What is the Capital of Syria ?")
      Answer1.set ("Damascus")
      Answer2.set ("Islamabad")
      Answer3.set ("Yemen")
      Answer4.set ("Beirut")
      MillionPicture1()


def Question3():
    Question1.set("Q1: What is the Capital of North Korea ?")
    Answer1.set("Seoul")
    Answer2.set("Pyong Yang")
    Answer3.set("Sanaa")
    Answer4.set("Hanoi")
    MillionPicture2()


def Question4():
    Question1.set("Q1: What is the Capital of Bhutan ?")
    Answer1.set("Kathmandu")
    Answer2.set("Islamabad")
    Answer3.set("Thimphu")
    Answer4.set("Beijing")
    MillionPicture3()


def Question5():
    Question1.set("Q1: What is the 1156^2 ?")
    Answer1.set("1336336")
    Answer2.set("2569856")
    Answer3.set("2356489")
    Answer4.set("12459875")
    MillionPicture4()

#==============Text labels buttons==========================

txtQuestion = Entry (ABC1c, font=('arial', 18, 'bold'), bg='blue', fg='white', bd=5, width =44,
                     justify =CENTER, textvariable=Question1)
txtQuestion. grid (row =0, column=0, columnspan=4, pady=4)

lblQuestionA = Label (ABC1c, font=('arial', 14, 'bold') , text="A: ", bg='black', fg='white', bd=5,
justify =CENTER)
lblQuestionA. grid (row =1, column=0, pady=4, sticky=W)

txtQuestion1 = Button (ABC1c, font=('arial', 14, 'bold'), bg ="blue", fg ="white", bd=1, width = 17, height=2,
                       justify = CENTER,textvariable=Answer1,command=Question3)
txtQuestion1.grid (row = 1 , column=1, pady =4)

lblQuestB = Label (ABC1c, font=('arial', 14, 'bold'), text="B: ",bg='black', fg ="white", justify = LEFT)
lblQuestB.grid (row=1, column=2, sticky=W)

txtQuestion2 = Button (ABC1c, font=('arial', 14, 'bold'), bg ="blue", fg ="white", bd=1, width = 17, height=2,
                       justify = CENTER,textvariable=Answer2, command=Question4)
txtQuestion2. grid (row = 1 , column=3, pady =4)

lblQuestC = Label (ABC1c, font= ('arial',14,'bold' ) , text="C: ", bg='black', fg ="white", justify = LEFT)
lblQuestC.grid (row = 2, column=0, sticky=W)

txtQuestion3 = Button (ABC1c, font=('arial', 14, 'bold' ), bg ="blue", fg ="white", bd=1, width = 17, height=2,
                       justify = CENTER,textvariable=Answer3 ,command=Question5)
txtQuestion3. grid (row = 2 , column=1, pady =4)

lblQuestD = Label (ABC1c, font= ('arial',14,'bold' ) , text="D: ", bg='black', fg ="white", justify = LEFT)
lblQuestD. grid (row=2, column=2, sticky=W)

txtQuestion4 = Button (ABC1c, font=('arial', 14, 'bold'), bg ="blue", fg ="white", bd=1, width = 17, height=2,
                       justify = CENTER,textvariable=Answer4,command=Question2)

txtQuestion4. grid (row = 2, column=3, pady =4)







root.mainloop()
