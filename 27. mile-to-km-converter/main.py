import tkinter as tk


def conversion():
    miles = float(mile_entry.get())
    km = round(miles * 1.609)
    km_units.config(text=f'{km}')


window = tk.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Labels
is_equal_widget = tk.Label(text="is aprox. equal to")
is_equal_widget.grid(column=0, row=1)

km_units = tk.Label(text="0")
km_units.grid(column=1, row=1)

km_text = tk.Label(text="Km")
km_text.grid(column=2, row=1)

mile_text = tk.Label(text="Miles")
mile_text.grid(column=2, row=0)

# Entry
mile_entry = tk.Entry(width=10)
mile_entry.insert(0, "0")
mile_entry.grid(column=1, row=0)

# Button
calculate = tk.Button(text="Calculate", command=conversion)
calculate.grid(column=1, row=2)

window.mainloop()
