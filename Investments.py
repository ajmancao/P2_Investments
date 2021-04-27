import csv
n = input("How much do you want to invest?")  # investment

file_name = "stocks.csv"

def line2word(line):
    return line.replace("\n", "").split(",")

def get_data_from_file(file_name):  # to sort first line into keys and the rest into values
    stocks = []
    with open(file_name) as fh:
        keys = line2word(fh.readline())
        for line in fh:
            stocks.append(dict(zip(keys, line2word(line))))
    for i in stocks:
        print(i)
get_data_from_file(file_name)
print("\n")

stock_list = []
def show(stock_list):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            stock_list.append(line)
    print(f"Here are the stocks I have considered for you:")
    for i in stock_list:
        print(f" - {i[0]} - Market Cap: {i[2]}")
show(stock_list)
print("\n")

def find_cheapest_stock(stock_list):
    mStock = min(stock_list, key=lambda i: 0 < float(i[4]))
    print(f"{mStock[0]} is the cheapest stock.")
find_cheapest_stock(stock_list)

investment = float(n)
def get_num_of_shares(stock_list, investment):
    mShare = min(stock_list, key=lambda i: i[3])
    print(f"You can buy {int(investment // float(mShare[3]))} shares.")
get_num_of_shares(stock_list, investment)
print("\n")

def find_bargain_stock(stock_list):
    mBarg = min(stock_list, key=lambda i: i[-1].split(":"))
    print(f"{mBarg[0]} is trading relatively low, considering its 52 Week Range")
    print(f"At ${mBarg[3]} per share, you can buy {int(investment // float(mBarg[3]))} shares.")
find_bargain_stock(stock_list)