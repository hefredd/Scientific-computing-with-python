import tkinter as tk
from tkinter import messagebox

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def get_card_type(card_number):
    length = len(card_number)
    if card_number.startswith('4') and length in [13, 16, 19]:
        return "Visa"
    elif (card_number.startswith(tuple(str(i) for i in range(51, 56))) or
          card_number.startswith(tuple(str(i) for i in range(2221, 2721)))) and length == 16:
        return "MasterCard"
    elif card_number.startswith(('34', '37')) and length == 15:
        return "American Express"
    elif (card_number.startswith('6011') or
          card_number.startswith('65') or
          card_number.startswith(tuple(str(i) for i in range(644, 650))) or
          card_number.startswith(tuple(str(i) for i in range(622126, 622926)))) and length == 16:
        return "Discover"
    else:
        return "Unknown"

def validate_card():
    raw_input = entry.get()
    card_translation = str.maketrans({'-': '', ' ': ''})
    card_number = raw_input.translate(card_translation)

    if not card_number.isdigit():
        messagebox.showerror("Error", "Please enter only digits, spaces, or hyphens.")
        return

    if len(card_number) < 12:
        messagebox.showerror("Error", "Card number is too short.")
        return

    if verify_card_number(card_number):
        card_type = get_card_type(card_number)
        result_var.set(f"✅ VALID\nCard Type: {card_type}")
    else:
        result_var.set("❌ INVALID")

# --- GUI Setup ---

root = tk.Tk()
root.title("Credit Card Validator")
root.geometry("350x200")
root.resizable(False, False)

tk.Label(root, text="Enter Card Number:").pack(pady=(20, 5))
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Validate", command=validate_card).pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12), fg="green")
result_label.pack()

root.mainloop()
