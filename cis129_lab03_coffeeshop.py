def main():
    print ('*' * 39)
    print('My Coffee and Muffin Shop')
    
    # get input from customer
    print("Number of coffees bought?")
    nbrofcoffees = int(input())
    print("Number of muffins bought?")
    nbrofmuffins = int(input())
    print ('*' * 39) 
    print()

    # local variables
    priceofcoffee = 5
    priceofmuffins = 4
    tax = float(0.06)
    subtotal = (nbrofcoffees * float(priceofcoffee)) + (nbrofmuffins * float(priceofmuffins))
    taxCost = subtotal * tax 
    totalCost = subtotal + taxCost
    totalCoffee = nbrofcoffees * priceofcoffee
    totalMuffin = nbrofmuffins * priceofmuffins
    
    # print receipt

    print('*' * 39)
    print('My Coffee and Muffin Shop Receipt')
    if nbrofcoffees >= 1:
        print(f'{nbrofcoffees} Coffee at ${priceofcoffee:.2f} each: ${totalCoffee:.2f}')
    if nbrofmuffins >= 1:
        print(f'{nbrofmuffins} Muffins at ${priceofmuffins:.2f} each: ${totalMuffin:.2f}')
    print(f'6% tax: ${taxCost}')
    print('-' * 9)
    print(f'Total: $ {totalCost}')
    print('*' * 39)
    
#display the receipt to the customer
    

main()
