import tkinter as tk

def calculate_monthly_payment():
    loan_amount = float(entry_loan_amount.get())
    interest_rate = float(entry_interest_rate.get())
    loan_term = int(entry_loan_term.get())

    monthly_interest_rate = interest_rate / 100 / 12
    total_payments = loan_term * 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)

    result_label.config(text="Monthly Payment: {:.2f}".format(monthly_payment))

# Create the main window
window = tk.Tk()
window.title("Wassgoodiiee Mortgage Calculator")
window.geometry("400x300")  # Set the width and height of the window

# Configure font size
font = ("Arial", 12)

# Create labels
label_loan_amount = tk.Label(window, text="Loan Amount:", font=font)
label_loan_amount.pack()
label_interest_rate = tk.Label(window, text="Interest Rate (%):", font=font)
label_interest_rate.pack()
label_loan_term = tk.Label(window, text="Loan Term (years):", font=font)
label_loan_term.pack()

# Create entry fields
entry_loan_amount = tk.Entry(window, font=font)
entry_loan_amount.pack()
entry_interest_rate = tk.Entry(window, font=font)
entry_interest_rate.pack()
entry_loan_term = tk.Entry(window, font=font)
entry_loan_term.pack()

# Create button
button_calculate = tk.Button(window, text="Calculate", command=calculate_monthly_payment, font=font)
button_calculate.pack()

# Create result label
result_label = tk.Label(window, font=font)
result_label.pack()

# Start the main loop
window.mainloop()