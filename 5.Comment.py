# Calculate Bill Restaurant Sample 
#price 1,2,3, are order
#total price sum of All order item
# Tax including as per gov.
price_1 = float(input("Enter the price 1 :  "))
price_2 = float(input("Enter the price 2 :  "))
price_3 = float(input("Enter the price 3 :  "))
tax_per = float(input("Enter the Tas % :  "))
total_price = price_1 + price_2 + price_3
total_tax = (tax_per/100)*total_price
final_amount = total_price + total_tax
print("Final amount", final_amount)