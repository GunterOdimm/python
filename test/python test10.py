inven = [{291,500},
		{586,320},
		{460,100},
		{558,120},
		{18,92},
		{72,30}]


userpay = 0

for (price,qty) in inven:
	userpay += price*(qty*0.9)

print(userpay)