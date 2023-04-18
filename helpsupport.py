from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Helpsupport:
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
        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="#ff006d")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"D:\program\python language\Smart-Ai-Attendance-system\Images_GUI\linkedin.png")
        std_img_btn=std_img_btn.resize((250,250),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.linkedin,image=self.std_img1,cursor="hand2")
        std_b1.place(x=400,y=200,width=250,height=260)

        std_b1_1 = Button(bg_img,command=self.linkedin,text="Linkedin",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="#ff006d")
        std_b1_1.place(x=400,y=465,width=245,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"D:\program\python language\Smart-Ai-Attendance-system\Images_GUI\githubs.jpg")
        det_img_btn=det_img_btn.resize((250,250),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.github,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=700,y=200,width=250,height=260)

        det_b1_1 = Button(bg_img,command=self.github,text="Github",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="#ff006d")
        det_b1_1.place(x=700,y=465,width=245,height=45)

         

        # create function for button 
    
    
    def linkedin(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/suneelprajapati"
        webbrowser.open(self.url,new=self.new)
    
    def github(self):
        self.new = 1
        self.url = "https://www.github.com/suneel-prajapati"
        webbrowser.open(self.url,new=self.new)
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()