order_list=[]
user_list=[]
food_item=[]

while True:
    choice=input('select admin/customer/exit:')
    if choice=='admin':
        print(user_list)
        print(order_list)
        food_item.append([food_list,quantity])
        print(food_item)
    elif choice=='customer':
        while True:
            Restaurant_list=['Food Plaza(Pizza/Burger)','Taste Bites(Biryani/noodles)','Spicy Hub(Veg biryani)']
            print(Restaurant_list)
            ch=input('Select restaurant:')
            if ch=='Food Plaza':
                food_list=['panner pizza','chicken pizza','chicken burger','panner burger','tandoori chicken burger','thumsup','coca cola','sprite']
                quantity=[30,50,50,20,50,50,30,40]
                price=[170,230,200,150,250,20,20,20]
                print(food_list)
                cart_items=[]
                cart_qty=[]
                cart_amt=[]
        
                while True:
                    item=input('What do you want:')
            
                    if item in food_list:
                        qty=int(input('How many packets you want:'))
                        idx=food_list.index(item)
                        if qty<=quantity[idx]:
                            amt=qty*price[idx]
                            quantity[idx]=quantity[idx]-qty
                            cart_items.append(item)
                            cart_qty.append(qty)
                            cart_amt.append(amt)
                            print(item,'is add to cart')
                        else:
                            print('out of stock')
                    if item=='done':
                        print("="*20,'Food Plaza','='*20)
                        for it in zip(cart_items,cart_qty,cart_amt):
                            print(f'{it[0]:<30}{it[1]:<10}{it[2]:<10}')
                        print('Total',' '*32,sum(cart_amt))
                        break
                user_list=[]
                name=input('Enter name:')
                address=input('Enter address:')
                phoneno=input('Enter phone number:')
                user=[]
                user.append(name)
                user.append(address)
                user.append(phoneno)
                user_list.append(user)
                #print(user_list)
                order=input('order confirmed(yes/no):')
                if order=='yes':
                    print('order confirmed successfully')
                    order_list.append([cart_items,cart_qty,cart_amt])
                    order_list.append(user)
                    #order_list.append(order)
                    print(order_list)
                else:
                    print('order cancelled')
                break
            elif ch=='Taste Bites':
                food_list=['murden biryani','chicken biryani','chicken fry biryani','egg biryani','chicken soup','murden soup','veg biryani','panner biryani','mushroom biryani','sprite','thumsup']
                quantity=[30,50,50,20,30,40,50,30,50,50,45]
                price=[170,230,200,150,100,100,150,150,150,20,20]
                print(food_list)
                cart_items=[]
                cart_qty=[]
                cart_amt=[]
        
                while True:
                    item=input('What do you want:')
            
                    if item in food_list:
                        qty=int(input('How many packets you want:'))
                        idx=food_list.index(item)
                        if qty<=quantity[idx]:
                            amt=qty*price[idx]
                            quantity[idx]=quantity[idx]-qty
                            cart_items.append(item)
                            cart_qty.append(qty)
                            cart_amt.append(amt)
                            print(item,'is add to cart')
                        else:
                            print('out of stock')
                    if item=='done':
                        print("="*20,'Food Plaza','='*20)
                        for it in zip(cart_items,cart_qty,cart_amt):
                            print(f'{it[0]:<30}{it[1]:<10}{it[2]:<10}')
                        print('Total',' '*32,sum(cart_amt))
                        break
                user_list=[]
                name=input('Enter name:')
                address=input('Enter address:')
                phoneno=input('Enter phone number:')
                user=[]
                user.append(name)
                user.append(address)
                user.append(phoneno)
                user_list.append(user)
                #print(user_list)
                order=input('order confirmed(yes/no):')
                if order=='yes':
                    print('order confirmed successfully')
                    order_list.append([cart_items,cart_qty,cart_amt])
                    order_list.append(user)
                    #order_list.append(order)
                    print(order_list)
                else:
                    print('order cancelled')
                break
            elif ch=='Spicy Hub':
                food_list=['panner manchuria','chicken manchuria','chicken noodles','gobi manchuria','veg noodles','egg noodles','thumsup','sprite']
                quantity=[30,50,50,20,30,40,50,50]
                price=[70,100,120,50,60,70,20,20]
                print(food_list)
                cart_items=[]
                cart_qty=[]
                cart_amt=[]
        
                while True:
                    item=input('What do you want:')
            
                    if item in food_list:
                        qty=int(input('How many packets you want:'))
                        idx=food_list.index(item)
                        if qty<=quantity[idx]:
                            amt=qty*price[idx]
                            quantity[idx]=quantity[idx]-qty
                            cart_items.append(item)
                            cart_qty.append(qty)
                            cart_amt.append(amt)
                            print(item,'is add to cart')
                        else:
                            print('out of stock')
                    if item=='done':
                        print("="*20,'Food Plaza','='*20)
                        for it in zip(cart_items,cart_qty,cart_amt):
                            print(f'{it[0]:<30}{it[1]:<10}{it[2]:<10}')
                        print('Total',' '*32,sum(cart_amt))
                        break
                user_list=[]
                name=input('Enter name:')
                address=input('Enter address:')
                phoneno=input('Enter phone number:')
                user=[]
                user.append(name)
                user.append(address)
                user.append(phoneno)
                user_list.append(user)
                #print(user_list)
                order=input('order confirmed(yes/no):')
                if order=='yes':
                    print('order confirmed successfully')
                    order_list.append([cart_items,cart_qty,cart_amt])
                    order_list.append(user)
                    #order_list.append(order)
                    print(order_list)
                else:
                    print('order cancelled')
                break


            
  
    else:
        print('Thank you for visiting ')
        
