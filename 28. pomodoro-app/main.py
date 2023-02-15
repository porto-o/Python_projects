import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

window.after(1000, )

# Label
timer_label = tk.Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)

check_mark = tk.Label(text="✔", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)

# Button
start = tk.Button(text="Start")
start.grid(column=0, row=2)

reset = tk.Button(text="Reset")
reset.grid(column=2, row=2)

# Canvas allows us to lay out things one in top of another (draw something and then on top of that also draw...)
canvas = tk.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
# highlightthickness removes the border around the image
photo = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)  # to center de image
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
