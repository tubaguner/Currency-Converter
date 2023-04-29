import tkinter as Tk
from tkinter import ttk

root = Tk.Tk()
root.title('Currency Converter')
root.geometry("520x300")


def calculate_currency_value(): 
    dollar= 19.45
    num = 1
    #currency = (TL*19.45)
    #dollar = dollar_var.get()
    #TL = TL_var.get()
    currency = (num*dollar)
    TL_var.set(f"Currency: {Currency:.2f}")
    
    


calculate_currency = ttk.Frame(root)
calculate_currency.pack(padx=10, pady=10, fill='x', expand=True)

dollar_label = ttk.Label(calculate_currency,text="Dollar:")
dollar_label.pack(fill='x', expand=True)

dollar_var = Tk.StringVar()
dollar_entry = ttk.Entry(calculate_currency,textvariable=dollar_var)
dollar_entry.pack(fill='x', expand=True)
dollar_entry.focus()

# TL
#TL_label = ttk.Label(calculate_currency,text="TL:")
#TL_label.pack(fill='x', expand=True)

#TL_var = Tk.StringVar()
#TL_entry = ttk.Entry(calculate_currency,textvariable=TL_var)
#TL_entry.pack(fill='x', expand=True)

TL_label = ttk.Label(calculate_currency,text="TL:")
TL_label.pack(fill='x', expand=True)

TL_var = Tk.StringVar()
TL_entry = ttk.Entry(calculate_currency,textvariable=TL_var)
TL_entry.pack(fill='x', expand=True)

convert_button = ttk.Button(calculate_currency,text="Convert",command=calculate_currency_value)
convert_button.pack(fill='y', expand=False, pady=10)



root.mainloop()