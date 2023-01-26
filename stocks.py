#Sophia Ramirez Velandia
#CS175L 01
#Professor Eckert Gil
#January 24rd, 2023

#Stocks

num_shares= float(input('Number of shares:'))
purchase_price=float(input('Purchased price:'))
selling_price=float(input('Selling price:'))
commission_rate=float(input('Commission rate:'))

amountPaidForStock = num_shares * purchase_price
purchaseCommission = commission_rate * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = num_shares * selling_price
sellingCommission = commission_rate * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid

print('Amount paid for the stock: $',amountPaidForStock)

print('Commission paid on the purchase: $',purchaseCommission)

print('Amount the stock sold for: $',stockSoldFor)

print('Commission paid on the sale: $',sellingCommission)

print('Profit (or loss if negative): $',profitOrLoss)
