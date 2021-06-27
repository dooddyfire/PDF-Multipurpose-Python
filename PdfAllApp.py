# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 02:17:09 2020

@author: MSI
"""

from termcolor import cprint
from PyPDF2 import PdfFileMerger,PdfFileWriter,PdfFileReader 
from tkinter import * 
from tkinter import simpledialog 
from tkinter import messagebox 
from tkinter import filedialog
import os  
import webbrowser 
from tkinter import ttk

def PdfToText(file): 
    with open(file,'rb') as f: 
        pdf = PdfFileReader(f)
        A=[]        
        for i in range(pdf.getNumPages()): 
            #print(pdf.getPage(i).extractText())
            A.append(pdf.getPage(i).extractText())
        print(A)
        with open("ReadPdf.txt","w+") as txt:
            txt.writelines(A)

def ReadPdf(file): 
    with open(file,'rb') as f: 
        pdf = PdfFileReader(f)
        A=[]        
        for i in range(pdf.getNumPages()): 
            #print(pdf.getPage(i).extractText())
            A.append(pdf.getPage(i).extractText())
        return "".join(A)
    
def MergePdf(f1,f2,f3): 
    file1 = open(f1,'rb')
    file2 = open(f2,'rb')
    
    pdf1 = PdfFileReader(file1)
    pdf2 = PdfFileReader(file2)
    
    writer = PdfFileWriter()
    for i in range(pdf1.getNumPages()): 
        writer.addPage(pdf1.getPage(i))
    
    for i in range(pdf2.getNumPages()): 
        writer.addPage(pdf2.getPage(i))
    
    mergepdf =  open(f3,'wb')
    writer.write(mergepdf)
    
    file1.close()
    file2.close()
    mergepdf.close()

def MarkPdf(f1,water,result): 
    file= open(f1,'rb')
    reader = PdfFileReader(file)
    page= reader.getPage(0)
    
    water = open(water,'rb')
    reader2 = PdfFileReader(water)
    waterpage = reader2.getPage(0)
    page.mergePage(waterpage)
    writer = PdfFileWriter()
    writer.addPage(page)
    for pageNum in range(reader.numPages): # this will give length of book
     pageObj = reader.getPage(pageNum)
     writer.addPage(pageObj)
    resultFile = open(result,'wb') # here we are writing so 'wb' is for write binary
    
    writer.write(resultFile)
    file.close()
    resultFile.close()
        
    
def xy(e): 
    label['text']=f"x : {e.x} , y : {e.y}"

def RotatePdf(original,out,ang):
    pdf_in = open(original, 'rb')
    pdf_reader = PdfFileReader(pdf_in)
    writer = PdfFileWriter()

    for i in range(pdf_reader.numPages):
        page = pdf_reader.getPage(i)

        page.rotateClockwise(ang)
        writer.addPage(page)

    pdf_out = open(out, 'wb')
    writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()

def load(e):
    file1 = filedialog.askopenfilename()
    ent.insert(0,file1)
def load2(e):
    file2 = filedialog.askopenfilename()
    ent2.insert(0,file2)
    
def process(): 
    global angle 
    try:
        print(x.get())
        #lb.delete(0,END)
        if int(x.get())!=0:
            if int(x.get()) == 1:
                ask = simpledialog.askinteger("ask", "Choose 1 to Edit PDF file1 , Choose 2 to Edit PDF file2")
                if ask==1:
                    print(ReadPdf(file1.get()))
                    PdfToText(file1.get())
                    lb['text']=ReadPdf(file1.get())
                    lb.config(text=ReadPdf(file1.get()))
                    print(100)
                    #lb.insert(0,ReadPdf(file1.get()))
                elif ask==2:
                    print(ReadPdf(file2.get()))
                    PdfToText(file2.get())
                    lb['text']=ReadPdf(file2.get())
                    lb.config(text=ReadPdf(file2.get()))
                    print(100)
                    #lb.insert(0,ReadPdf(file2.get()))
                webbrowser.open("file:///" + os.getcwd()+"/ReadPdf.txt")
            elif int(x.get()) == 2: 
        
                MergePdf(file1.get(),file2.get(),"MergePdf.pdf")
                
                webbrowser.open("file:///" + os.getcwd()+"/MergePdf.pdf")
                    
          
            elif int(x.get()) == 3: 
                
                
                MarkPdf(file1.get(),file2.get(),'WaterMarkResult.pdf')
                #lb.insert(0,ReadPdf(file1.get()))  
                webbrowser.open("file:///" + os.getcwd()+"/WaterMarkResult.pdf")
                    
            elif int(x.get()) == 4: 
                global angle
                ask = simpledialog.askinteger("ask", "Choose 1 to Edit PDF file1 , Choose 2 to Edit PDF file2")
                if ask==1:
                   RotatePdf(file1.get(),'Rotate.pdf',angle)
                      
                elif ask==2:
                    RotatePdf(file2.get(),'Rotate.pdf',angle)
                webbrowser.open("file:///" + os.getcwd()+"/Rotate.pdf")
            file1.set("")
            file2.set("")
            ent.delete(0,END)
            ent2.delete(0,END)
        elif int(x.get())==0:
            messagebox.showinfo(title="Select Mode",message="Please Select At Least One Mode")            
            file1.set("")
            file2.set("")
        root.update()
    except NameError:
        messagebox.showinfo(title="Set Angle",message="Please Set Angle On Top Of Window or Set File Path")
    

def setRotate():
    global angle
    angle = simpledialog.askinteger("Rotate Angle","Please input rotate angle : ")
    lbang['text'] = angle
    
def shift(): 
    x1,y1,x2,y3 = canvas.bbox('uno')
    if x2<0 or y1<0:
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords('uno',x1,y1)
    else: 
        canvas.move('uno',-2,0)
    canvas.after(1000//fps,shift)

if __name__ == '__main__': 
    #cprint(ReadPdf('test.pdf'),'yellow',attrs=['bold'])
    #MergePdf('sample.pdf','test.pdf','Result.pdf')
    #MarkPdf('sample.pdf','marker.pdf','ggwp.pdf')
    root = Tk()
    root.config(background='gainsboro')
    root.geometry("500x300+0+0")
    root.title('PDF APP')
    root.iconbitmap("hourglass")

    s = ttk.Style()
    s.configure(style='Auu.TButton',font=('Arial',10),background='red')
    file1 = StringVar()
    frame = Frame(root,bg='powder blue',relief='ridge',bd=3)
    frame.pack()
    ttk.Label(frame,text="PDF EDITOR",foreground='black',font=('Arial',15,'bold'),background='powder blue').pack(side=TOP,anchor=CENTER)
    ttk.Label(frame,text="Rotate Angle : ",foreground='black',font=('Arial',15,'bold'),background='powder blue').pack(side=LEFT)
    lbang = ttk.Label(frame,text="",foreground='black',background='powder blue',font=('Arial',15,'bold'))
    lbang.pack(side=LEFT)
    btns = ttk.Button(frame,text="Set",command=setRotate,style="Auu.TButton")
    btns.pack(side=BOTTOM)
    x = IntVar()

    frameR = Frame(root,bg='powder blue',relief='ridge',bd=3)
    frameR.pack(pady=5)
    rd1=Radiobutton(frameR,text='Read',value=1,variable=x,bg='powder blue',font=('Arial',15,'bold'))
    rd1.deselect()
    rd1.pack(side=LEFT,padx=10)
    rd2=Radiobutton(frameR,text='Merge',value=2,variable=x,bg='powder blue',font=('Arial',15,'bold'))
    rd2.deselect()
    rd2.pack(side=LEFT,padx=10)

    rd3=Radiobutton(frameR,text='Watermark',value=3,variable=x,bg='powder blue',font=('Arial',15,'bold'))
    rd3.deselect()
    rd3.pack(side=LEFT,padx=10)

    
    rd4=Radiobutton(frameR,text='Rotate',value=4,variable=x,bg='powder blue',font=('Arial',15,'bold'))
    rd4.deselect()

    rd4.pack(side=LEFT,padx=10)
    frameFile1 = Frame(root,bg='powder blue',relief='ridge',bd=3)
    frameFile1.pack(pady=5)
    

    
    file1 = StringVar()
    file2 = StringVar()
    
    label1=ttk.Label(frameFile1,text="PDF File 1:",foreground='black',font=('Arial',15,'bold'),background='powder blue')
    label1.pack(side=LEFT,padx=2,ipadx=15)
    
    ent = ttk.Entry(frameFile1,textvariable =file1 ,foreground='black',font=('Arial',15,'bold'),background='powder blue')
    ent.pack(side=LEFT,padx=2,ipadx=15)
    btn1 = ttk.Button(frameFile1,text='Load File',style='Auu.TButton')
    btn1.bind('<Button-1>',load)
    btn1.pack(side=LEFT)
    
    frameFile2 = Frame(root,bg='powder blue',relief='ridge',bd=3)
    frameFile2.pack()
    
    label2 = ttk.Label(frameFile2,text="PDF File 2:",foreground='black',font=('Arial',15,'bold'),background='powder blue')
    label2.pack(side=LEFT,padx=2,ipadx=15)
    
    ent2 = ttk.Entry(frameFile2,textvariable =file2 ,foreground='black',font=('Arial',15,'bold'),background='powder blue')
    ent2.pack(side=LEFT,padx=2,ipadx=15)
    btn2 = ttk.Button(frameFile2,text='Load File',style='Auu.TButton')
    btn2.bind('<Button-1>',load2)
    btn2.pack(side=LEFT)
    btn2.pack(side=LEFT)
    
    btn3 = Button(root,text="Process",bg='pink',fg='black',cursor='hand2',font=('Arial',15,'bold'),bd=5,activebackground='red',command=process)
    btn3.pack(pady=10)
    
    frameRead = Frame(root,bg='powder blue',relief='ridge',bd=5)
    frameRead.pack(fill=X)
    
    framebot = Frame(root,relief='ridge',bd=5)
    framebot.pack(side=BOTTOM,fill=X)
    canvas = Canvas(framebot,bg='black')
    canvas.pack(side=BOTTOM,fill=X)
    
    textvar = "Developed By Supapong Sakulkoo"
    text = canvas.create_text(0,-2000,text=textvar,fill='yellow',tags='uno',anchor='w',font=('Arial',15,'bold'))
    x1,y1,x2,y2 = canvas.bbox('uno')
    canvas['width'] = x2-x1
    canvas['height'] =y2-y1
    fps = 50
    shift()

    root.mainloop()