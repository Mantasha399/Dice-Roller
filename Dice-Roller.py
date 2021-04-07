from tkinter import *
import random 

#Setting the window
root=Tk()
root.title("Roll Dice")
root.geometry("500x400")

#Creating a label for showing the dice value
label=Label(root,font=('helvetica',250,'bold'),text='')


#Function to change the value of dice as per button click 
def rolldice():
        
	dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	label.configure(text=f'{random.choice(dice)}')	
	label.pack()

#creating button for clicking 
button=Button(root,font=('helvetica',25,'bold'),text='roll dice',command=rolldice,bg="skyblue")
button.pack()

root.mainloop()
