def make_change(target_amount):
    denominations = [200,100,50,20,10,5,2,1] # Order is important
    coin_count = 0
    values = []
    for coin in denominations:
        while target_amount >= coin:  # Use the current coin until its value is too large
            target_amount -= coin
            values.append(coin)
            coin_count += 1
    return coin_count, values
            
	
	

print(make_change(24)) # 3: 20p + 2p + 2p
print(make_change(163)) # 5: L1 + 50p + 10p + 2p + 1p
