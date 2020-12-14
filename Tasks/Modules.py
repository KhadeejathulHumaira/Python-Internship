import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd
db=sqlite3.connect("Customer.db")
cursor=db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS customer_details( customer_id INTEGER PRIMARY KEY AUTOINCREMENT,coffee_name TEXT, water INT,milk INT,coffee INT,money_paid REAL,balance REAL)")
Tot_water =1000
Tot_milk =1000
Tot_coffee = 500
def resource_check( water, milk, coffee) :
    global Tot_water
    global Tot_milk
    global Tot_coffee
    if Tot_water >= water :  # check whether there is sufficient resources to prepare coffee
        if Tot_milk >= milk :
            if Tot_coffee >= coffee :
                Tot_water = Tot_water - water
                Tot_milk = Tot_milk - milk
                Tot_coffee = Tot_coffee - coffee
                return True
            else:
                tk.messagebox.showinfo( message="Sorry! There is no sufficient Coffee ")
                return False
        else:
            tk.messagebox.showinfo(message="Sorry! There is no sufficient Milk")
            return False
    else:
        tk.messagebox.showinfo(message="Sorry! There is no sufficient Water")
        return False
def calcu(quarter,dimes,nickles,pennies,money):
    global val
    global cus_money
    cus_money = 0.25 * int(quarter) + 0.1 * int(dimes) + 0.05 * int(nickles) + 0.01 * int(pennies)
    if cus_money >= money :
        val = cus_money - money
        return 1

    elif cus_money == money :
        return 2
    else :
        return 3
def save(name):
    try:
        global Tot_water
        global Tot_milk
        global Tot_coffee
        global val
        global cus_money
        list1=[name,Tot_water,Tot_milk,Tot_coffee,cus_money,val]

        cursor.execute("INSERT INTO customer_details(coffee_name,water,milk,coffee,money_paid,balance ) VALUES (?,?,?,?,?,?)",list1)
        print("Successfull")
    except:
        pass
def show():
    df=pd.read_sql_query("SELECT * FROM customer_details",db)
    print(df)



