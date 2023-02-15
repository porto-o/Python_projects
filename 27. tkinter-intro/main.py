import tkinter

window = tkinter.Tk()
window.title("Helo world!")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)  # General padding

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


# to edit parameters of the label we can use list notation or with config method
# my_label["text"] = lorem ipsum
# my_label.config(text="lorem ipsum")


def button_clicked():
    my_label.config(text=user_input.get())


# There are 3 layout managers: pack(), grid() and place
# pack() by default put the elements of the center top if there is not any element
# otherwise it will be move down the element
# place() uses coordinates to position the elements
# grid() uses a grid system to position the elements

# Button
my_button = tkinter.Button(text="Click me!", command=button_clicked)
my_button.grid(column=1, row=1)

my_second_btn = tkinter.Button(text="Click me also!")
my_second_btn.grid(column=2, row=0)

# Entry
user_input = tkinter.Entry(width=10)
user_input.grid(column=3, row=2)

window.mainloop()
