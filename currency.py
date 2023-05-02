import tkinter as Tk
from tkinter import ttk


root = Tk.Tk()
root.title('Currency Converter')
root.geometry("520x300")

style = ttk.Style()
style.configure('Pink.TButton', background='#ff007f',foreground='white',font=('Arial Bold',16))


def calculate_currency_value(): 
    dollar = float(dollar_var.get())
    exchange_rate= 19.45
    TL = dollar * exchange_rate
    TL_var.set(f"Exchange: {TL:.2f}")
    
    
calculate_currency = ttk.Frame(root)
calculate_currency.pack(padx=10, pady=10, fill='x', expand=True)

dollar_label = ttk.Label(calculate_currency,text="Dollar:",font=('Arial Bold',16))
dollar_label.pack(fill='x', expand=True)

dollar_var = Tk.StringVar()
dollar_entry = ttk.Entry(calculate_currency,textvariable=dollar_var)
dollar_entry.pack(fill='x', expand=True)
dollar_entry.focus()


TL_label = ttk.Label(calculate_currency,text="TL:",font=('Arial Bold' ,16))
TL_label.pack(fill='x', expand=True)

TL_var = Tk.StringVar()
TL_entry = ttk.Entry(calculate_currency,textvariable=TL_var)
TL_entry.pack(fill='x', expand=True)

convert_button = ttk.Button(calculate_currency,text="Convert",style='Pink.TButton',command=calculate_currency_value)
convert_button.pack(fill='y', expand=False, pady=6)

style = ttk.Style()
style.configure('TLabel', background='#ffb6c1')


root.configure(bg='#ff69b4')


root.mainloop()