from tkinter import *


#window
window = Tk()
window.minsize(width=200, height=200)
window.title("BMI Calculator")

#label
my_label = Label(text="Enter your weight (kg)")
my_label.pack()

#entry
my_entry = Entry(width=10)
my_entry.pack()

#Label2
my_label2 = Label(text="Enter your height (cm)")
my_label2.pack()

#Entry2
my_entry2 = Entry(width=10)
my_entry2.pack()

#Button
def calculate():
    try:
        weight = float(my_entry.get())
        height = float(my_entry2.get()) / 100  # Boyu metreye dönüştürmek için 100'e böldük
        BMI = weight / (height ** 2)

        if BMI < 18.5:
            result = "You are underweight"
        elif 18.5 <= BMI < 24.9:
            result = "You are normal"
        elif 25.0 <= BMI < 29.9:
            result = "You are overweight"
        else:
            result = "You are obese"

        result_label.config(text="Your BMI is: {:.2f}\n{}".format(BMI, result))
    except ValueError:
        result_label.config(text="Enter a valid number!")

#button
my_button = Button(text="Calculate BMI",command=calculate)
my_button.pack()

#Result label
result_label = Label(window,text="")
result_label.pack()

window.mainloop()