from tkinter import*
from tkinter import ttk
import webbrowser
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\program\python language\Smart-Ai-Attendance-system\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"D:\program\python language\Smart-Ai-Attendance-system\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer Panel",font=("verdana",30,"bold"),bg="white",fg="#ff006d")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1


         # Attendance System  button 3
        att_img_btn=Image.open(r"D:\program\python language\Smart-Ai-Attendance-system\Images_GUI\sunil.png")
        att_img_btn=att_img_btn.resize((250,250),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.sunil,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=550,y=100,width=250,height=250)

        att_b1_1 = Button(bg_img,command=self.sunil,text="Sunil Prajapati",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="#ff006d")
        att_b1_1.place(x=550,y=350,width=250,height=45)

         # Help  Support  button 4
    def sunil(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/suneelprajapati"
        webbrowser.open(self.url,new=self.new)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()