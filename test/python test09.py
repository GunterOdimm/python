cart = [{38000,6},
		{20000,4},
		{17900,3},
		{17900,5}]

userpay = 0

for (price,qty) in cart:
	userpay += price*qty



print(userpay)