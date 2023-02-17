import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(foreground=GREEN, text="Timer")
    global reps
    reps = 0
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_sec)
        timer_label.config(foreground=RED, text="Break")
    elif reps % 2 == 0:
        countdown(short_sec)
        timer_label.config(foreground=PINK, text="Break")
    else:
        countdown(work_sec)
        timer_label.config(foreground=GREEN, text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

# Label
timer_label = tk.Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)

check_mark = tk.Label(foreground=GREEN, background=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)

# Button
start = tk.Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = tk.Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

# Canvas allows us to lay out things one in top of another (draw something and then on top of that also draw...)
canvas = tk.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
# highlightthickness removes the border around the image
photo = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)  # to center de image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
