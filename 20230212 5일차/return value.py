def tax_calculator(money):
    return money * 0.35

def pay_tax(tax):
    print("thank you for paying",tax)

pay_tax(tax_calculator(150000))