# TASK 2: Stock Portfolio Tracker 
# ● Goal: Build a simple stock tracker that calculates total investment based on manually defined stock 
# prices. 
# ● Simplified Scope: 
# ○ User inputs stock names and quantity. 
# ○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}). 
# ○ Display total investment value and optionally save the result in a .txt or .csv file. 
# ● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling 
# (optional).

def Stock_Portfolio_Tracker():
    companys={
        'GPT':200,
        'Microsoft':300,
        'Tsla':500,
        'Gemini':200,
        'Deepseek':400,
    }

    total_investment = 0
    Stock_data = []
    investment=0

    print("<======== Avaliable Stock =======> \n")
    for stock, price in companys.items():
        print(f"{stock}: {price}")
    
    
    while True:
        stock_name = input("Enter the stock name : (name or exit) :> ")

        if stock_name.lower() == 'exit':
            print("Exiting...")
            break

        if stock_name not in companys:
            print("Stock not found")
            continue

        quantity = int(input("Enter the stock quantity: "))
        investment +=  companys[stock_name]*quantity
        total_investment += investment 

        Stock_data.append(f"{stock_name} - {quantity} - {investment}")
        print(f"Stock name: {stock_name}\tQuantity: {quantity}\tInvestment: {investment}")
        print(f"Overall Investment: {total_investment}")

    save = input("Do you want to save stock data into csv file : (yes/no) :> ")
    if save.lower() == 'yes':
        with open('Stockdata.csv','w') as file:
            file.write('Stock\tQuantity\tInvestment')
            for item in companys:
                file.write(f"{item}\n")
            file.write(f"Total Investment : {total_investment}")
        print("File save successfully into csv formate ")

Stock_Portfolio_Tracker()