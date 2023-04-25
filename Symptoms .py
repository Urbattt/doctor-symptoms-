from tkinter import *  
from tkinter import messagebox
root = Tk() 
root.title("Cardiovascular Problems")
root.geometry("600x600")

question1_radioButton = StringVar(value = "0")
Question1 = Label(root, text = "Do you have shortness of breath during routine activities?")
Question1.pack()
question1_r1 = Radiobutton(root, text = "yes", variable = question1_radioButton, value = "yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text = "no", variable = question1_radioButton, value = "no")
question1_r2.pack()

question2_radioButton = StringVar(value = "0")
Question2 = Label(root, text = "Do you have swelling in the feel/ankles/legs or abdomen?")
Question2.pack()
question2_r1 = Radiobutton(root, text = "yes", variable = question2_radioButton, value = "yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text = "no", variable = question2_radioButton, value = "no")
question2_r2.pack()

question3_radioButton = StringVar(value = "0")
Question3 = Label(root, text = "Do you experience confusion, disorientation or loss of memory?")
Question3.pack()
question3_r1 = Radiobutton(root, text = "yes", variable = question3_radioButton, value = "yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text = "no", variable = question3_radioButton, value = "no")
question3_r2.pack()

question4_radioButton = StringVar(value = "0")
Question4 = Label(root, text = "Do you experience shortness of breath while at rest?")
Question4.pack()
question4_r1 = Radiobutton(root, text = "yes", variable = question4_radioButton, value = "yes")
question4_r1.pack()
question4_r2 = Radiobutton(root, text = "no", variable = question4_radioButton, value = "no")
question4_r2.pack()

question5_radioButton = StringVar(value = "0")
Question5 = Label(root, text = "Do you experience persistent wheezing/choghing that produces white or pink blood tinged mucus?")
Question5.pack()
question5_r1 = Radiobutton(root, text = "yes", variable = question5_radioButton, value = "yes")
question5_r1.pack()
question5_r2 = Radiobutton(root, text = "no", variable = question5_radioButton, value = "no")
question5_r2.pack()

def fever_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question5_radioButton.get()=="yes":
        score = score+20
        print(score)
    
    
    if score <=40:
        messagebox.showinfo("Report","You don't need to go visit a doctor")
    elif score > 40 and score <=60:
        messagebox.showinfo("Report", "I storngly adivse you to vist a doctor")
    else : 
        messagebox.showinfo("Report", "I strongly advise you to visit a doctor")
        
btn = Button(root, text = "click me", command = fever_score)
btn.pack()
root.mainloop()