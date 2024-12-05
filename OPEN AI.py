##import tkinter
##from tkinter import*
##from PIL import Image, ImageTk
##import pymysql
##from tkinter import messagebox
##from tkinter import ttk
##import os
##import openai
##import requests
##import io
##
##top=Tk()
##top.title("Main page")
##top.geometry("800x750")
##top.config(bg="black")
##top.resizable(False,False)
###database connection
##"""connection = pymysql.connect(
##        host="localhost",
##        user="root",
##        password="1234",
##        database="python_morning"
##    )
##my_database = connection.cursor()"""
###first page
##lab1=Label(top,text="IMAGE GENERATOR",
##           font=('century gothic', 45, 'bold'),fg="white",bg='black')
##lab1.place(x=110,y=200)
##
##lab1=Label(top,text="This is an AI Image Generator.\n It creates an image from scratch from a text description.",
##           font=('century gothic', 15, 'bold'),fg="white",bg='black')
##lab1.place(x=110,y=350)
##
###image generate
##def generate():
##    openai.api_key=os.getenv("API_KEY")
##    user_prompt=eb1.get("0.0",tkinter.END)
##    user_prompt+="in style: "+eb2.get()
##
##    response=openai.Image.create(
##        prompt=user_prompt,
##        n=1,
##        size="400x350"
##    )
##    
##    image_urls=[]
##    for i in range(len(response['data'])):
##        image_urls.append(response['data'][i]['url'])
##    print(image_urls)
##
##    image=[]
##    for url in image_urls:
##        response =requests.get(url)
##        image=Image.open(io.BytesIO(response.content))
##        photo_image=ImageTk.PhotoImage(image)
##        images.append(photo_image)
##
##    def update_image(index=0):
##        canvas.image=images[index]
##        canvas.create_image(0,0,anchor="nw",image=image[index])
##        index=(index+1)%len(images)
##        canvas.after(3000,update_image,index)
##
##    update_image()
##
##
##def login():
####        x=eb1.get()
####        y=eb2.get()   
####        sql="SELECT * from details where user=%s and pw=%s"
####        my_database.execute(sql,[(x),(y)])
####        result=my_database.fetchall()
####        print(result)
###main page
####        if(result):
##            page4=Frame(page2,bg='black',height=800,width=500)
##            page4.pack(fill=X)
##
##            lab1=Label(page4,text="prompt",
##                   font=('century gothic', 10, 'bold',))
##            lab1.place(x=60,y=280)
##            entry1 = Entry(page4, font=('Century Gothic', 10))
##            entry1.place(x=150,y=280,width=150)
##
##            lab2=Label(page4,text="stlye",
##                   font=('century gothic', 10, 'bold',))
##            lab2.place(x=60,y=340)
##            entry2 = ttk.Combobox(page4,values=["realistic","cartoon","3D illustration","Flat Art"])
##            entry2.place(x=150,y=340,width=150)
##
##            lab3=Label(page4,text="#image",
##                   font=('century gothic', 10, 'bold',))
##            lab3.place(x=60,y=400)
##            entry3 = Scale(page4, from_=1, to=10, font=('Century Gothic', 10), orient=HORIZONTAL,bg="#060606", fg="white")
##            entry3.place(x=150,y=400,width=150)
##
##            canvas = Canvas(page4, width=400, height=450, bg="white")
##            canvas.place(x=350, y=140)
##
##            generate_button=ttk.Button(page4,text="generate",command=generate)
##            generate_button.place(x=100,y=480,width=150)
##
##def save():
##    a=ebb1.get()
##    b=ebb2.get()
##    c=ebb3.get()
##    if(ebb1.get()=="" or ebb2.get()=="" or ebb3.get()==""  ):
##        messagebox.showerror("Error","Enter all the details")
##    elif(ebb2.get() != ebb3.get() ):
##        messagebox.showerror("Error","Check the password")        
##    # Executing an SQL query to insert the name into the database
##    else:
##        messagebox.showinfo("Info","Successfully Saved..!")
##        page3.destroy()
##        # Closing the cursor and connection
##
##    
###third page
##def data_store():
##    global ebb1,ebb2,ebb3,page3
##    page3=Frame(page2,bg='black',height=1000,width=600)
##    page3.pack(fill=X)
##
##    lab1=Label(page3,text="IMAGE GENERATOR",
##           font=('century gothic', 45, 'bold'),fg="white",bg='black')
##    lab1.place(x=100,y=150)
##
##    lb2=Label(page3,text="Username ",
##           font=('century gothic', 15, 'bold'),fg="white",bg='black')
##    lb2.place(x=220,y=300)
##    ebb1=Entry(page3,font=('century gothic', 15, 'bold'))
##    ebb1.place(x=350,y=300,width=150)
##
##    lb3=Label(page3,text="Password ",
##           font=('century gothic', 15, 'bold'),fg="white",bg='black')
##    lb3.place(x=220,y=360)
##    ebb2=Entry(page3,show="*",font=('century gothic', 15, 'bold'))
##    ebb2.place(x=350,y=360,width=150)
##
##    lb3=Label(page3,text="Confirm ",
##           font=('century gothic', 15, 'bold'),fg="white",bg='black')
##    lb3.place(x=220,y=420)
##    ebb3=Entry(page3,show="*",font=('century gothic', 15, 'bold'))
##    ebb3.place(x=350,y=420,width=150)
##
##    b1 = Button(page3,text='save',command=save,bg="#ad2315",fg="white",
##            font=("Consolas", 13, "bold"),height="1",width="13",bd=0)
##    b1.place(x=300, y=500)
##
###second page
##def second():
##    global page2,eb1,eb2
##    page2=Frame(top,bg='black',height=1000,width=600)
##    page2.pack(fill=X)
##
####    img=Image.open('goat2.jpg')
####    img=img.resize((800,600))
####    img2=ImageTk.PhotoImage(img)
####    imglabel=Label(page2,image=img2,bg="#1A5276")
####    imglabel.image=img2
####    imglabel.place(x=0,y=0)
##    
##    lab1=Label(page2,text="IMAGE GENERATOR",
##           font=('century gothic', 45, 'bold'),fg="white",bg='black')
##    lab1.place(x=110,y=150)
##
##    lab2=Label(page2,text="Username ",
##           font=('century gothic', 15, 'bold'),fg="white",bg='black')
##    lab2.place(x=250,y=300)
##    eb1=Entry(page2,font=('century gothic', 15, 'bold'))
##    eb1.place(x=380,y=300,width=150)
##
##    lab3=Label(page2,text="Password ",
##           font=('century gothic', 15, 'bold'),fg="white",bg='black')
##    lab3.place(x=250,y=350)
##    eb2=Entry(page2,font=('century gothic', 15, 'bold'))
##    eb2.place(x=380,y=350,width=150)
##
##
##    b1 = Button(page2,text='Login',command=login,bg="red",fg="white",
##            font=("Consolas", 13, "bold"),height="1",width="13",bd=0)
##    b1.place(x=320, y=420)
##
##    lab4=Label(page2,text="New to Ai image generator? ",
##           font=('century gothic', 15, 'bold'),fg="white",bg='black')
##    lab4.place(x=200,y=490)
##
##    b1 = Button(page2,text='Sign up',command=data_store,bg="black",fg="white",
##            font=("Consolas", 13, "bold"),height="1",width="13",bd=0)
##    b1.place(x=480, y=490)
##
##
##
##    
##b6 = Button(top,text='Sign in',command=second,bg="red",fg="white",
##            font=("Consolas", 13, "bold"),height="1",width="13",bd=0)
##b6.place(x=550, y=600)
##
##top.mainloop()




import tkinter
from tkinter import*
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox
from tkinter import ttk
import os
import openai
import requests
import io

top=Tk()
top.title("Main page")
top.geometry("800x750")
top.config(bg="black")
top.resizable(False,False)
#database connection
"""connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="python_morning"
    )
my_database = connection.cursor()"""
#first page
lab1=Label(top,text="IMAGE GENERATOR",
           font=('century gothic', 45, 'bold'),fg="white",bg='black')
lab1.place(x=110,y=200)

lab1=Label(top,text="This is an AI Image Generator.\n It creates an image from scratch from a text description.",
           font=('century gothic', 15, 'bold'),fg="white",bg='black')
lab1.place(x=110,y=350)

#image generate
def generate():
    openai.api_key="sk-Dp4D-91R0VgtY2jo829RAHmJ31Dm4lozG7yI5hi2x7T3BlbkFJOmfA27s0__ybYM3hj-s_VZriv3ht1KnQCvZBCmJoAA"
    user_prompt = eb1.get() 
##    user_prompt=eb1.get("0.0",tkinter.END)
    user_prompt+="in style: "+eb2.get()

    response=openai.Image.create(
        prompt=user_prompt,
        n=1,
        size="512x512"
    )
    
    image_urls=[]
    for i in range(len(response['data'])):
        image_urls.append(response['data'][i]['url'])
    print(image_urls)

    image=[]
    for url in image_urls:
        response =requests.get(url)
        image=Image.open(io.BytesIO(response.content))
        photo_image=ImageTk.PhotoImage(image)
        images.append(photo_image)

    def update_image(index=0):
        canvas.image=images[index]
        canvas.create_image(0,0,anchor="nw",image=image[index])
        index=(index+1)%len(images)
        canvas.after(3000,update_image,index)

    update_image()


def login():
##        x=eb1.get()
##        y=eb2.get()   
##        sql="SELECT * from details where user=%s and pw=%s"
##        my_database.execute(sql,[(x),(y)])
##        result=my_database.fetchall()
##        print(result)
#main page
##        if(result):
            page4=Frame(page2,bg='black',height=800,width=500)
            page4.pack(fill=X)

            lab1=Label(page4,text="prompt",
                   font=('century gothic', 10, 'bold',))
            lab1.place(x=60,y=280)
            entry1 = Entry(page4, font=('Century Gothic', 10))
            entry1.place(x=150,y=280,width=150)

            lab2=Label(page4,text="stlye",
                   font=('century gothic', 10, 'bold',))
            lab2.place(x=60,y=340)
            entry2 = ttk.Combobox(page4,values=["realistic","cartoon","3D illustration","Flat Art"])
            entry2.place(x=150,y=340,width=150)

            lab3=Label(page4,text="#image",
                   font=('century gothic', 10, 'bold',))
            lab3.place(x=60,y=400)
            entry3 = Scale(page4, from_=1, to=10, font=('Century Gothic', 10), orient=HORIZONTAL,bg="#060606", fg="white")
            entry3.place(x=150,y=400,width=150)

            canvas = Canvas(page4, width=400, height=450, bg="white")
            canvas.place(x=350, y=140)

            generate_button=ttk.Button(page4,text="generate",command=generate)
            generate_button.place(x=100,y=480,width=150)

def save():
    a=ebb1.get()
    b=ebb2.get()
    c=ebb3.get()
    if(ebb1.get()=="" or ebb2.get()=="" or ebb3.get()==""  ):
        messagebox.showerror("Error","Enter all the details")
    elif(ebb2.get() != ebb3.get() ):
        messagebox.showerror("Error","Check the password")        
    # Executing an SQL query to insert the name into the database
    else:
        messagebox.showinfo("Info","Successfully Saved..!")
        page3.destroy()
        # Closing the cursor and connection

    
#third page
def data_store():
    global ebb1,ebb2,ebb3,page3
    page3=Frame(page2,bg='black',height=1000,width=600)
    page3.pack(fill=X)

    lab1=Label(page3,text="IMAGE GENERATOR",
           font=('century gothic', 45, 'bold'),fg="white",bg='black')
    lab1.place(x=100,y=150)

    lb2=Label(page3,text="Username ",
           font=('century gothic', 15, 'bold'),fg="white",bg='black')
    lb2.place(x=220,y=300)
    ebb1=Entry(page3,font=('century gothic', 15, 'bold'))
    ebb1.place(x=350,y=300,width=150)

    lb3=Label(page3,text="Password ",
           font=('century gothic', 15, 'bold'),fg="white",bg='black')
    lb3.place(x=220,y=360)
    ebb2=Entry(page3,show="*",font=('century gothic', 15, 'bold'))
    ebb2.place(x=350,y=360,width=150)

    lb3=Label(page3,text="Confirm ",
           font=('century gothic', 15, 'bold'),fg="white",bg='black')
    lb3.place(x=220,y=420)
    ebb3=Entry(page3,show="*",font=('century gothic', 15, 'bold'))
    ebb3.place(x=350,y=420,width=150)

    b1 = Button(page3,text='save',command=save,bg="#ad2315",fg="white",
            font=("Consolas", 13, "bold"),height="1",width="13",bd=0)
    b1.place(x=300, y=500)

#second page
def second():
    global page2,eb1,eb2
    page2=Frame(top,bg='black',height=1000,width=600)
    page2.pack(fill=X)

##    img=Image.open('goat2.jpg')
##    img=img.resize((800,600))
##    img2=ImageTk.PhotoImage(img)
##    imglabel=Label(page2,image=img2,bg="#1A5276")
##    imglabel.image=img2
##    imglabel.place(x=0,y=0)
    
    lab1=Label(page2,text="IMAGE GENERATOR",
           font=('century gothic', 45, 'bold'),fg="white",bg='black')
    lab1.place(x=110,y=150)

    lab2=Label(page2,text="Username ",
           font=('century gothic', 15, 'bold'),fg="white",bg='black')
    lab2.place(x=250,y=300)
    eb1=Entry(page2,font=('century gothic', 15, 'bold'))
    eb1.place(x=380,y=300,width=150)

    lab3=Label(page2,text="Password ",
           font=('century gothic', 15, 'bold'),fg="white",bg='black')
    lab3.place(x=250,y=350)
    eb2=Entry(page2,font=('century gothic', 15, 'bold'))
    eb2.place(x=380,y=350,width=150)


    b1 = Button(page2,text='Login',command=login,bg="red",fg="white",
            font=("Consolas", 13, "bold"),height="1",width="13",bd=0)
    b1.place(x=320, y=420)

    lab4=Label(page2,text="New to Ai image generator? ",
           font=('century gothic', 15, 'bold'),fg="white",bg='black')
    lab4.place(x=200,y=490)

    b1 = Button(page2,text='Sign up',command=data_store,bg="black",fg="white",
            font=("Consolas", 13, "bold"),height="1",width="13",bd=0)
    b1.place(x=480, y=490)



    
b6 = Button(top,text='Sign in',command=second,bg="red",fg="white",
            font=("Consolas", 13, "bold"),height="1",width="13",bd=0)
b6.place(x=550, y=600)

top.mainloop()
