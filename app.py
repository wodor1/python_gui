import tkinter as tk

# define the operation to be 'add' by default
operation = 'add'

def set_operation(op):
    global operation
    operation = op
    button.config(text=op)

def print_data():
    data1 = entry1.get()
    data2 = entry2.get()
    try:
        num1 = float(data1)
        num2 = float(data2)
        result = None
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                raise ValueError("Division by zero")

        if result is None:
            raise ValueError("Invalid operation")

        output_label.config(text=result)
        print(result)
    except ValueError:
        output_label.config(text="Hiba történt!")
        print("Hiba történt!")

root = tk.Tk()

root.geometry("800x500")
root.title("My First GUI App")
root.config(bg='light blue')

frame = tk.Frame(root, bg='light blue')
frame.pack()

add_button = tk.Button(frame, text="Összeadás", font=("Helvetica", 20), command=lambda: set_operation('add'))
subtract_button = tk.Button(frame, text="Kivonás", font=("Helvetica", 20), command=lambda: set_operation('subtract'))
multiply_button = tk.Button(frame, text="Szorzás", font=("Helvetica", 20), command=lambda: set_operation('multiply'))
divide_button = tk.Button(frame, text="Osztás", font=("Helvetica", 20), command=lambda: set_operation('divide'))

add_button.grid(row=0, column=0)
subtract_button.grid(row=0, column=1)
multiply_button.grid(row=0, column=2)
divide_button.grid(row=0, column=3)

label = tk.Label(root, text="Számológép", font=("Helvetica", 32), bg='light blue')
label.pack(pady=20, padx=20)

instructions_label = tk.Label(root, text="Adj meg két számot a kívánt művelethez:", font=("Helvetica", 10), bg='light blue')
instructions_label.pack()

data_label1 = tk.Label(root, text="első szám:", font=("Helvetica", 20), bg='light blue')
data_label1.pack()

entry1 = tk.Entry(root, font=("Helvetica", 20))
entry1.pack()

data_label2 = tk.Label(root, text="második szám:", font=("Helvetica", 20), bg='light blue')
data_label2.pack()

entry2 = tk.Entry(root, font=("Helvetica", 20))
entry2.pack()

button = tk.Button(root, text="Kiírat", font=("Helvetica", 20), command=print_data)
button.pack(pady=20)

output_label = tk.Label(root, text="", font=("Helvetica", 20), bg='light blue')
output_label.pack()

root.mainloop()
