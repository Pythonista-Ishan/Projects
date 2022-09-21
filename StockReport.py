# importing nse from nse tools

from nsetools import Nse
import csv
import os

# creating a Nse object
nse = Nse()

def master(c):
    if(c==0):
        print("\n\nYou've chosen to list all trading stocks.\nList will be updated in 'alllist.csv'\n\n")
        filecheck('alllist.csv')
        listall()
    elif(c==1):
        filecheck('list.csv')
        print("\n\nPlease Update the file 'list.csv' with stock symbols before proceeding.")
        pause()
        print("\n\nYou've chosen to list details of selected stocks.\nStocks will be picked from 'list.csv'\n\n")
        list()
    elif(c==2):
        print("\n\nYou've chosen to list about top gainers.\nDetails will be reflected in file 'topgainers.csv'\n\n")
        filecheck('topgainers.csv')
        topgainers()
    else:
        print("\n\nYou've chosen to list about top losers.\nDetails will be reflected in file 'toplosers.csv'\n\n")
        filecheck('toplosers.csv')
        toplosers()

def pause():
    print("Press Enter to Continue")
    t=input()
    if(t):
        return
    else:
        return(False)

def list():
    with open('list.csv') as csvf:
        csv_reader = csv.reader(csvf, delimiter=',')

        for row in csv_reader:
            print(row[0])

            # getting quote of the stock
            quote = nse.get_quote(row[0])

            # # getting symbol of the stock
            symbol = str(quote['symbol'])

            if(nse.is_valid_code(symbol)):
                # getting name of the stock
                name = str(quote['companyName'])

                # getting last Price
                lastprice = float(quote['lastPrice'])

                change = float(quote['change'])

                dayHigh = float(quote['dayHigh'])

                dayLow = float(quote['dayLow'])

                high52 = float(quote['high52'])

                low52 = float(quote['low52'])

                faceValue = float(quote['faceValue'])

                averageprice = float(quote['averagePrice'])

                print(f'Ticker: {symbol}\nCompany Name: {name}\nPrice: {lastprice}\nAverage Price: {averageprice}\nChange: {change}\nDay Low: {dayLow}\nDay High: {dayHigh}\n52 Week Low: {low52}\n52 Week High: {high52}\nFace Value: {faceValue}\n***\n')

            else:
                print(f'{symbol} is invalid.')
    print('Done\n\n')
    valchange()

def topgainers():
    topgainers = nse.get_top_gainers()
    with open('topgainers.csv',"w", newline='') as tgcsv:
        csv_writer = csv.DictWriter(tgcsv, topgainers[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(topgainers)
    print('Done\n\n')
    valchange()

def toplosers():
    toplosers = nse.get_top_losers()
    with open('toplosers.csv',"w", newline='') as tlcsv:
        csv_writer = csv.DictWriter(tlcsv, toplosers[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(toplosers)
    print('Done\n\n')
    valchange()

def listall():
    allstocks = nse.get_stock_codes()
    with open('alllist.csv',"w",) as allcsv:
        csv_writer = csv.writer(allcsv)
        for key, value in allstocks.items():
            csv_writer.writerow([key, value])
    print('Done\n\n')
    valchange()

def valchange():
    pause()
    print("Welcome!!!\nPress 0 if you want to list all trading stocks at NSE India\nPress 1 if you want to get details about specific stocks\nPress 2 if you want to see top gainers.\nPress 3 if you want to see top losers\nPress anything else if you want to EXIT\n\n")
    c= int(input("Enter choice:"))
    if(c==0 or c==1 or c==2 or c==3):
        master(c)
    else:
        print("You've Exited the program.\nThanks")

def filecheck(file_path):
    if os.path.exists(file_path):
        print(f'\nFile {file_path} already exists.\nChanges will be reflected shortly.\n')
    else:
        # create a file
        with open(file_path, 'w'):
            print(f'\nFile {file_path} created.\n')

valchange()
