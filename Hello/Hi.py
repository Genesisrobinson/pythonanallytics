def electrocity(value):
    temp=1
    amount=0
    amount1=0
    amount2=0
    amount3=0
    amount4=0
    while (temp<=value):
        if (temp <= value):
            amount1 += 7.50
        elif (temp > 70 and temp <= 160):
            amount2 += .60
        elif (temp > 160 and temp <= 320):
            amount3 += .50
        else:
            amount4 += .40
        temp+=1
    amount=amount1+amount2+amount3+amount4
    return amount
amount=electrocity(100)
print(amount)
text="Hi How ARe you I'm fine"
for x in text:
    print(x)

