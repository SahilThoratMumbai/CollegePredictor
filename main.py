#import lib
from tkinter import *
from tkinter import messagebox
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from PIL import Image, ImageTk

root=Tk()
root.title("MHTCET PERCENTILE COLLEGE PREDICTOR")
root.geometry("1000x600+50+50")
root.configure(bg="thistle1")
root.resizable(False, False)

f=("Impact",30,"bold")

lab_header=Label(root,text="MHT-CET PERCENTILE COLLEGE PREDICTOR",font=f,bd=3,fg="white",bg="PaleGreen4",relief="groove")
lab_header.place(x=230,y=20)

lab_percentile = Label(root,text="Enter MHT-CET Percentile :" , font=f,bg="orange",bd=2,relief="groove",fg="white")
ent_percentile=Entry(root,font=f,bg="papayawhip",bd=3,relief="groove",fg="dimgrey")
lab_percentile.place(x=50,y=120)
ent_percentile.place(x=530,y=120)

c = IntVar()
c.set(1)
lab_location = Label(root, text="Location" , font=f,bg="lightpink1",fg="white",bd=2,width=10,pady=10,relief="sunken")
rb_mumbai = Radiobutton(root, text="Mumbai" , font=f , variable=c , value=1,bg="navajowhite3",fg="lightgoldenrodyellow",bd=2,relief="sunken",pady=6,padx=3)
rb_navimumbai = Radiobutton(root, text="Navi Mumbai" , font=f , variable=c , value=2,bg="lightcyan3",fg="lavender",bd=2,relief="sunken",pady=6,padx=3 )

lab_location.place(x=50 , y=220)
rb_mumbai.place(x=300 , y=220)
rb_navimumbai.place(x=500 , y=220)

img1=Image.open('MU.jpg');
img1=img1.resize((220,100),Image.LANCZOS)
root.photo1=ImageTk.PhotoImage(img1)

root.img_1=Label(root,image=root.photo1)
root.img_1.place(x=2,y=0,width=200,height=100)

img2=Image.open('student.png');
img2=img2.resize((200,200),Image.LANCZOS)

root.photo2=ImageTk.PhotoImage(img2)

root.img_2=Label(root,image=root.photo2)
root.img_2.place(x=790,y=370,width=200,height=200)

def find():
	data=pd.read_csv("D:\Machine_Learning_Revision\CET\mhtcet.csv")
	features=data[["Percentile","Location"]]
	target=data["College"]
	nfeatures=pd.get_dummies(features)
	mms=MinMaxScaler()
	mfeatures=mms.fit_transform(nfeatures)

	x_train,x_test,y_train,y_test=train_test_split(mfeatures,target,test_size=0.2)
	model=RandomForestClassifier()
	model.fit(x_train,y_train)
	if float(ent_percentile.get())<=20:
		messagebox.showerror("Error","You are not eligible for Engineering Donation Bharo")
	else:
		if c.get()==1:
			x=[ent_percentile.get()]+[1,0]
		else:
			x=[ent_percentile.get()]+[0,1]


		d=mms.transform([x])
		ans=model.predict(d)
	
		lab_ans.configure(text=ans[0])

btn_predict=Button(root , text="Predict College", font=f , command=find,bg="lawngreen",bd=4,fg="black",relief="raised")
lab_ans=Label(root,font=f,bg="darkolivegreen4",bd=5,fg="darkolivegreen2",relief="raised")
btn_predict.place(x=300 , y=350)
lab_ans.place(x=330 , y=500)

root.mainloop()