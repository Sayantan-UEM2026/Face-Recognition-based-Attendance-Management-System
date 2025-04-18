from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition 
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        #first
        img=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\khhg.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second
        img1=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\fac.png") 
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #second
        img2=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\jgtf.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #big image
        #second
        img3=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\oui.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710) 

        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #Student Details button

        img4=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\stu.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
       
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=50,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=50,y=400,width=220,height=40)

        #Face Detector button
        img5=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\OIP.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
       
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=350,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=350,y=400,width=220,height=40)

        #Attendance button

        img6=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\tfu.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
       
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_details)
        b1.place(x=650,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650,y=400,width=220,height=40)

        #Help Desk button

        #img7=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\h.jpg")
        #img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        #self.photoimg7=ImageTk.PhotoImage(img7)
       
        #b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        #b1.place(x=1100,y=100,width=220,height=220)

        #b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        #b1_1.place(x=1100,y=300,width=220,height=40)


        #Train Data button

        img8=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\f.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
       
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=950,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=950,y=400,width=220,height=40) 

        #Photos button

        img9=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\meg.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
       
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=1250,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1250,y=400,width=220,height=40) 
        

        #Developer button

        #img10=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\d.jpg")
        #img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        #self.photoimg10=ImageTk.PhotoImage(img10)
       
        #b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        #b1.place(x=800,y=380,width=220,height=220)

        #b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        #b1_1.place(x=800,y=580,width=220,height=40) 
        

        #Exit button

        #img11=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\exe.jpg")
        #img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        #self.photoimg11=ImageTk.PhotoImage(img11)
       
        #b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        #b1.place(x=1100,y=380,width=220,height=220)

        #b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        #b1_1.place(x=1100,y=580,width=220,height=40) 

        command="self.student_details()"
    def open_img(self):
        os.startfile("data")
        #=================================== Functions =========================================

    def student_details(self):

        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def train_data(self):

        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):

        self.new_window = Toplevel(self.root)
        self.app =Face_Recognition(self.new_window) 

    def attendance_details(self):

        self.new_window = Toplevel(self.root)
        self.app =Attendance(self.new_window)









if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
