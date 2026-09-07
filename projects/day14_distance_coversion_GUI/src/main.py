import tkinter

# GUI setup
window = tkinter.Tk()
window.title("Miles to Km Converter!")
window.minsize(width=300, height=100)

# an empty element in the first column
spacer = tkinter.Frame(width=50, height=1)
spacer.grid(row=0, column=0)

# variable to save the output
output_val = tkinter.IntVar()
output_val.set(0)

output_msg = tkinter.StringVar()
output_msg.set("is equal to 0 Km")

input = tkinter.Entry(text=0)
input.grid(column=1, row=0)

input_label = tkinter.Label(text="Miles")
input_label.grid(column=2, row=0)

output_label = tkinter.Label(textvariable=output_msg)
output_label.grid(column=1, row=2)

# take the input, convert to a string, and compile & set the new output message
def convert_dist():
    m = int(input.get())
    output_val.set(1.609 * m)
    output_msg.set(f"are equal to {output_val.get()} Km")

# triggers convert_dist on press
button = tkinter.Button(text="Calculate", command=convert_dist)
button.grid(column=1, row=3)

window.mainloop()
