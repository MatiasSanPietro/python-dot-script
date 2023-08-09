import tkinter as tk
import pyperclip


def remove_dots(number):
    number = number.replace(".", "")
    return number


def toggle_conversion():
    global is_conversion_active
    is_conversion_active = not is_conversion_active
    if is_conversion_active:
        btn_toggle.config(text="Apagar")
        convert_number()
    else:
        btn_toggle.config(text="Encender")


def convert_number():
    global last_processed_number
    if is_conversion_active:
        number_input = pyperclip.paste()
        if number_input and number_input != last_processed_number:
            processed_number = remove_dots(number_input)
            if processed_number != last_processed_number:
                last_processed_number = processed_number
                pyperclip.copy(processed_number)
                history.append(processed_number)
    root.after(1000, convert_number)


def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Historial de Números")
    for number in history:
        btn_copy = tk.Button(
            history_window,
            text=number,
            command=lambda num=number: copy_from_history(num),
        )
        btn_copy.pack(pady=5)


def copy_from_history(number):
    pyperclip.copy(number)


is_conversion_active = False
last_processed_number = ""
history = []

root = tk.Tk()
root.title("Fedu v3")
root.geometry("210x70")

btn_toggle = tk.Button(root, text="Encender", command=toggle_conversion)
btn_toggle.pack(pady=5)

btn_history = tk.Button(root, text="Mostrar Historial", command=show_history)
btn_history.pack(pady=1)

root.mainloop()
