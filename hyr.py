from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import pickle
root = Tk()
root.title("Employees Management System")
root.geometry('1300x1000')
def Exit1() :
    res=tkinter.messagebox.askquestion(message="Do you want to exit")
    if res == "yes":
        root.destroy()
def ClearFrame():
    for widget.destroy in frame_2.winfo_children():
        widget.destroy()

def Clear():
    E_1.delete(0,END)
    E_2.delete(0,END)
    E_3.delete(0,END)
    E_4.delete(0,END)
    E_5.delete(0,END)
    ClearFrame()


def ViewAll():
    for widget in frame_2.winfo_children():
        widget.destroy()
    try:
        with open("Employee",'rb') as fil:
            Label(frame_2,text="%s %s %s %s %s %s %s" % ("      ID |","     Name |","       EMAIL |","      MOBILE |","       DEPARTMENT |","      DESIGNATION |","      SALARY "))
            Label(frame_2,text="%s" % "*"*60).pack()
            Rec=pickle.load(fil)
            c=len(Rec)
            for i in Rec:
              Label(frame_2,text="%s %s %s %s %s %s %s" % (i["ID"]+" | ",i["Name"]+" | ",i["Mob"]+" | ",i["Email"]+" | ",i["Depart"]+" | ",i["Desig"]+" | ",i["Salary"]+" | "))
    except FileNotFoundError:
        Label(frame_2,text="%s" % "File doesn't exist" ).pack()
    except EOFError:
        Label(frame_2,text="%s"% "File doesn't exist").pack()

def AddRec():
    try:
        fil=open("Employee","ab+")
        if fil.tell()>0:
            fil.seek(0)
            Rec1=pickle.load(fil)
        else:
            Rec1=[]

            Rec={}

            if any(dict.get('ID') == E_1.get()for dict in Rec1):
                tkinter.messagebox.showerror(message="Employee Id already exist")
                E_1.delete(0,END)
            else:
                Rec["ID"]=E_1.get()
            if len(E_2.get())<=0:
                tkinter.messagebox.showerror(message="Name has not been entered")
            else:
                Rec["Name"]=E_2.get()

            if len(E_3.get())!= 10 or E_3.get().isdigit()==False:
                tkinter.messagebox.showerror(message="Mobile No is not valid")
            else:
                Rec["Mob"]=E_3.get()

            if '@' not in E_4.get() or '.' not in E_4.get():
                tkinter.messagebox.showerror(message="Mail adress is not valid")
            else:
                Rec["Email"]=E_4.get()

            if len(E_5.get())==0 or int(E_5.get())<=0:
                tkinter.messagebox.showerror(message="Salary adress is not valid")
            else:
                Rec["Salary"]=int(E_5.get())

            Rec["Desig"]=Des.get()
            Rec["DeptID"]=Dept.get()
            Rec1.append(Rec)
            fil.close()

            if len(E_1.get())>0 and len(E_2.get())>0 and len(E_3.get())==10 and E_3.get().isdigit==True and'@' in E_4.get() and  len(E_5.get())>0:
                res = tkinter.messagebox.askyesno(massage="Confirm to update the file")
                if res==True:
                    with open("Employee",'wb') as fil :
                        pickle.dump(Rec1,fil)
                        Clear()
    except ValueError:
        tkinter.messagebox.showerror(message="Invalid value entered for Salary")

def RemRecord():
    if len(E_1.get())==0:
        tkinter.messagebox.showinfo(message="Enter the Employee Id to search for the record")
    ClearFrame()
    try:
        with open("Employee",'rb+') as fil:
            Rec=pickle.load(fil)
            for i in range(0,len(Rec)):
                if Rec[i]["ID"]==E_1.get():
                    Label(frame_2,text="%s" % "Record Found").pack()
                    N=Rec[i]
                    E_2.insert(0,N["Name"])
                    E_3.insert(0, N["Mob"])
                    E_4.insert(0, N["Email"])
                    E_5.insert(0, N["Salary"])
                    if N["DeptID"]=="MGR":
                        Dept.current(0)
                    elif N["DeptID"]=="CLK":
                        Dept.current(1)
                    elif N["DeptID"] == "vp":
                        Dept.current(2)
                    else:
                        Dept.current(3)

                    if N["Desig"]=="HR":
                        Des.current(0)
                    elif N["Desig"]=="IT":
                        Des.current(1)
                    elif N["Desig"] == "SALES":
                        Des.current(2)
                    else:
                        Des.current(3)

                    ch=tkinter.messagebox.askyesno(message="Delete the account")
                    if ch==True:
                        Rec.pop(i)
                        Label(frame_2,text="%s" % "Record Deleted").pack()
                    break
                else:
                    Label(frame_2,text="%s" % "Record Not Found").pack()

                fil.seek(0)
                pickle.dump(Rec,fil)

    except  FileNotFoundError:
        print(LabelFrame, "File Doesn't exist") # Think about might be mistakes F ?
    except KeyError:
        print("Record Not found")
    except IndexError:
        print("Record Not found")

def Search():
    if len(E_1.get())==0:
        tkinter.messagebox.showinfo(message="Enter the Employee Id to search for the record ")
    ClearFrame()
    try:
        with open("Employee",'rb') as fil:
            Rec=pickle.load(fil)
            for i in range(0,len(Rec)):
                if Rec[i]["ID"]==E_1.get():
                    Label(frame_2,text="%s" % "Record Found").pack()
                    N=Rec[i]
                    E_2.delete(0,END)
                    E_2.insert(0,N["Name"])
                    E_3.delete(0, END)
                    E_3.insert(0, N["Mob"])
                    E_4.delete(0,END)
                    E_4.insert(0,N["Email"])
                    E_5.delete(0,END)
                    E_5.insert(0,N["Salary"])
                    if N["DeptID"]=="MGR":
                        Dept.current(0)
                    elif N["DeptID"]=="CLK":
                        Dept.current(1)
                    elif N["DeptID"] == "VP":
                        Dept.current(2)
                    else:
                        Dept.current(3)


                    if N["Desig"] == "HR":
                         Des.current(0 )
                    elif N["Desig"] == "IT":
                        Des.current(1)
                    elif N["Desig"] =="SALES":
                        Des.current(2)
                    else:
                        Des.current(3)

                    Label(frame_2,text="%s" % "Record Found", font=('Trebuchet',20)).pack()
                    break
                else:
                    Label(frame_2, text="%s" % "Record Found").pack()

    except  FileNotFoundError:
        print(LabelFrame, "File Doesn't exist") # Think about might be mistakes F ?
    except KeyError:
        print("Record Not found")
    except IndexError:
        print("Record Not found")

def UpdateRec():
    if len(E_1.get())==0:
        tkinter.messagebox.showinfo(message="Click on Search to search and then update")
        Clear()
    try:
        with open("Employee",'rb+') as fil:
            found=-1
            Rec1=pickle.load(fil)
            Rec={}
            for p in Rec1:
                if E_1.get()==p["ID"]:
                    found=0
                    if len(E_2.get())<=0:
                        tkinter.messagebox.showerror(message="Name not entered")
                    else:
                        p["NAME"]=E_2.get()
                    if len(E_3.get())!=10 or E_3.get().isdigit()==False:
                        tkinter.messagebox.showerror(message="Mobile No is not valid")
                    else:
                        p["Mob"]=E_3.get()

                    if '@' not in E_4.get() or '.' not in E_4.get():
                        tkinter.messagebox.showerror(message="Mail adress is not valid")
                    else:
                        p["Email"] = E_4.get()

                    if len(E_5.get()) == 0 or int(E_5.get()) <= 0:
                        tkinter.messagebox.showerror(message="Salary adress is not valid")
                    else:
                        p["Salary"] = int(E_5.get())

                    p["Desig"] = Des.get()
                    p["DeptID"] = Dept.get()
                    break
                else:
                     Label(frame_2, text="%s" % "Record Found").pack()
                if found==0 and len(E_1.get())>0 and len(E_2.get())>0 and len(E_3.get())==10 and E_3.get().isdigit==True and'@' in E_4.get() and  len(E_5.get())>0:
                     res = tkinter.messagebox.askyesno(massage="Confirm to update the file")
                     if res==True:
                         fil.seek(0)
                         pickle.dump(Rec1,fil)
                         Label(frame_2, text="%s" % "Record Found").pack()


    except EOFError:
        print("Record not found")
    except FileNotFoundError:
        print(LabelFrame,"File is not exist")

def Report():
    Clear()
    try:
        with open("Employee", 'rb') as fil:
            Label(frame_2, text="%s %s %s %s %s %s %s" % ( "      ID |", "     NAME |", "       Basic Salary |", "       HRA |", "      DA |","      TAX |","GROSS SALARY"))
            Label(frame_2, text="%s" % "*" * 100).pack()

            for i in Rec:
                HRA=round(30*i["Salary"]/100,0)
                DA=round(15*i["Salary"]/100,0)
                TAX = round(((i["Salary"]+HRA+DA)*15/100), 0)
                GROSS=HRA+DA+i["Salary"] - TAX
                Label(frame_2,text="%s %s %s %s %s %s %s" % (i["ID"]+"  |  ",i["NAME"]+"  |  ", str(i["Salary"])+"  |  ", str(HRA)+"  |  ",str(DA)+"  |  ", str(TAX)+"  |  ",str(GROSS)+"  |  "))

    except FileNotFoundError:
        print("File doesn't exist")

Label(root, text="Employee Management System",font=("Arial bold",30),fg="blue").pack()
frame_1=Frame(root,borderwidth=3, relief="solid")
frame_1.pack(side="left",expand=True,fill="both")
frame_2=Frame(root,borderwidth=3, relief="solid")
frame_2.pack(side="left",expand=True,fill="both")
Label(frame_2, text="Welcome To the Employee Management System",font=("Trebuchet",30)).grid(row=0,column=0)

Label(frame_1, text="Employee ID").grid(row=0,column=0)
E_1=Entry(frame_1,bd=4)
E_1.grid(row=0,column=1,padx=13,pady=10)

Label(frame_1, text="Employee NAME").grid(row=1,column=0)
E_2=Entry(frame_1,bd=4)
E_2.grid(row=1,column=1,padx=13,pady=10)

Label(frame_1, text="MOBILE").grid(row=2,column=0)
E_3=Entry(frame_1,bd=4)
E_3.grid(row=2,column=1,padx=13,pady=10)

Label(frame_1, text="EMAIL").grid(row=3,column=0)
E_4=Entry(frame_1,bd=4)
E_4.grid(row=3,column=1,padx=13,pady=10)

Label(frame_1, text="DEPARTMENT").grid(row=4, column=0)
Dept=ttk.Combobox(frame_1)
Dept['values']=['MGR','CLK','VP','PRESS']
Dept.current(0)
Dept.grid(row=4,column=1,padx=13,pady=10)

Label(frame_1, text="DESIGNATION").grid(row=5, column=0)
Dept=ttk.Combobox(frame_1)
Dept['values']=['HR','IT','SALES','FIN']
Dept.current(0)
Dept.grid(row=5,column=1,padx=13,pady=10)

Label(frame_1, text="SALARY").grid(row=6,column=0)
E_5=Entry(frame_1,bd=4)
E_5.grid(row=6,column=1,padx=13,pady=10)

Add=Button(frame_1, text="ADD RECORD", command=AddRec,padx=13,pady=10)
Add.grid(row=20, column=0, sticky=NSEW, padx=13,pady=10)
DEL=Button(frame_1, text="DELETE RECORD", command=RemRecord)
DEL.config(relief=RAISED)
DEL.grid(row=20, column=1, sticky=NSEW, padx=13,pady=10)
Upd=Button(frame_1, text="UPDATE RECORD", command=UpdateRec)
Upd.grid(row=20, column=2, sticky=NSEW, padx=13,pady=10)
Ser=Button(frame_1, text="SEARCH RECORD", command=Search,padx=13,pady=10)
Ser.grid(row=21, column=0, sticky=NSEW, padx=13,pady=10)
View=Button(frame_1, text="VIEW ALL", command=ViewAll)
View.grid(row=21, column=1, sticky=NSEW, padx=13,pady=10)
Clr=Button(frame_1, text="CLEAR", command=Clear)
Clr.grid(row=21, column=2, sticky=NSEW, padx=13,pady=10)
Exit=Button(frame_1, text="EXIT", command=Exit1,padx=13,pady=10)
Exit.grid(row=22, column=0, sticky=NSEW, padx=13,pady=10)
Sal=Button(frame_1, text="SALARY GENERATION", command=Report)
Sal.grid(row=22, column=0, sticky=NSEW, padx=13,pady=10)








