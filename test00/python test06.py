# -*- coding: utf-8 -*-

cart = [{"price":38000,"qty":6},
		{"price":20000,"qty":4},
		{"price":17900,"qty":3},
		{"price":17900,"qty":5}]

tpl ="{0}원 x {1}개 ->총 {2}원"
print(tpl.format(cart[0]['price'],cart[0]['qty'],cart[0]['price']*cart[0]['qty']))
print(tpl.format(cart[1]['price'],cart[1]['qty'],cart[1]['price']*cart[1]['qty']))
print(tpl.format(cart[2]['price'],cart[2]['qty'],cart[2]['price']*cart[2]['qty']))
print(tpl.format(cart[3]['price'],cart[3]['qty'],cart[3]['price']*cart[3]['qty']))
