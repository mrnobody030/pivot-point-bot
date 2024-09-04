#import customtkinter as ctk
from datetime import date
from time import sleep
from main import stratigy
from signal_generator import signal_generator
from requests.exceptions import ConnectionError

today = date.today()

##########################################################################################################################
####################################################### MAIN FUNCTION ####################################################

def start():
    do_again = True
    symbols_for_trade = []
    while do_again == True:
        do_again = False
        file = open("data.csv","r")

        lines = file.readlines()

        table = []
        for a in lines:
            a = a.strip().split(" ")
            a = [i for i in a if i]
            
            table.append(a)
        file.close()


        file = open("data.csv","w")
        for row in table:
            if len(row) != 1 :
                if str(today) == row[3]:
                    file.write(row[0] +"    "+ row[1] +"    "+ row[2] +"    "+ row[3] + "\n")
                    continue
            try:
                P_point = stratigy(row[0])
                if P_point[1] == True:
                    file.write(str(row[0]) + "    True    " + str(P_point[1]) + "   " + str(today) + "\n")
                    symbols_for_trade.append(row[0])
                else:
                    file.write(str(row[0]) + "    False    no_point   " + str(today) + "\n")
                sleep(15)
            except ConnectionError:
                print("please check if you are connected to the internet")
            except :
                do_again = True
                file.write(str(row[0]) + "\n")
                print("an error acured on " + row[0])
    file.close()
    print(" ".join(symbols_for_trade))
#    root.destroy()

##########################################################################################################################

def test():
    file = open("data.csv","r")

    lines = file.readlines()

    table = []
    for a in lines:
        a = a.strip().split(" ")
        a = [i for i in a if i]
        
        table.append(a)
    file.close()

    for row in table:
        if row[1] == "True":
            signal_generator(row[0], float(row[2]))


##########################################################################################################################
# this section is to rewrite the symbols if they get deleted
base_data = """EUR/USD
GBP/USD
USD/JPY
USD/CHF
USD/CAD
AUD/USD
NZD/USD
EUR/GBP
EUR/JPY
GBP/JPY
EUR/AUD
GBP/CHF
USD/SGD
USD/HKD
USD/TRY"""
def return_database():
    global base_data
    file = open("data.csv", "r")
    lines = file.readlines()
    if len(lines) < 3:
        file.close()
        file = open("data.csv", "w")
        file.write(base_data)

a = start()
b = return_database()