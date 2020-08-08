import local_price
import ib_store

def price_ib(s1):
    price1 = s1.split(".")
    seller = s1.split("@")
    a = price1[1]
    if seller[1] == "Amazon":
        price = float("{0:.2f}".format(float(a)))
    elif seller[1] == "Flipkart":
        price = float("{0:.2f}".format(float(a)))
    return price

def price_local(s2):
    price2 = s2.split()
    b = price2[1]
    price_abd = float("{0:.2f}".format(float(b)))
    return price_abd

def compare(model_number):

    local_rate = local_price.get_local_price(model_number)
    flag = 0
    if ib_store.get_online_price(model_number) == 0:
        flag = 1
    else:
        amazon_rate, flip_rate = ib_store.get_online_price(model_number)

    if local_rate==0 and flag==1:
        return 0,0
    else:
        price_ibd = price_local(local_rate)
        if(flag==1):
            return price_ibd,1
        else:
            price_am=price_ib(amazon_rate)
            price_fl = price_ib(flip_rate)
            return min(price_ibd, price_am, price_fl),2

