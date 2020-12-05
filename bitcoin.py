# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 00:13:14 2020

@author: s0536
"""

import json
import requests


TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice/EUR.json'
response = requests.get(TICKER_API_URL)



data = response.json()
y = json.dumps(data)


ext='"Euro", "rate_float":' 
pos1 = y.find(ext) + len(ext)
end  = y[(pos1+1):pos1+(len(y)-pos1)]
pos2 = end.find('}')
value= y[(pos1+1):pos1+pos2+1]

BTC=float(value)
print('current rate:',BTC , 'EUR')


import tkinter as tk

root=tk.Tk()

price = tk.Label(root, text="bought for [EUR]:",height=2, width=50)
price.pack()
entry = tk.Entry(root)
entryString = entry.get()
entry.pack()

amount = tk.Label(root, text="amount [BTC]:",height=2, width=50)
amount.pack()
entry3 = tk.Entry(root)
entryString3 = entry3.get()
entry3.pack()

tax = tk.Label(root, text="tax (0.1 for 10 %):",height=2, width=50)
tax.pack()
entry4 = tk.Entry(root)
entryString4 = entry4.get()
entry4.pack()

def profit_calculator():
    global profit
    global bought
    global amountbought
    global taxes
    
    taxes=float(entry4.get())
    amountbought=float(entry3.get())
    bought=int(entry.get())
    profit = BTC*amountbought-float(entry.get())*amountbought
    profittax= profit*(1-taxes)
    print('Profit:',profit, 'EUR')
    print('Profit after tax:',profittax, 'EUR')



def stop_calculator():
    
    stop = float(entry2.get())*bought/(1-taxes) + bought
    profittax= profit*(1-taxes)
    print('stop by:',stop, 'EUR')
   


minprofit = tk.Label(root, text="minprofit (0.1 for 10 %)",height=2, width=50)
minprofit.pack()
entry2 = tk.Entry(root)
entryString2 = entry2.get()
entry2.pack()

button_calc = tk.Button(root, text="Calculate profit", command=profit_calculator,bg='green',height=1, width=20)
button_calc.pack()

button_calc2 = tk.Button(root, text="Calculate stop price", command=stop_calculator, bg='red',height=1, width=20)
button_calc2.pack()

root.mainloop()















    
    

  