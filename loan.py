loan = float(input("Input the cost of the item in $: "))
pay = 50.0
totalInt = 0
if (loan <= 1000):
    interest = 0.015
else:
    interest = 0.02
x = 0
while (loan != 0):
    x += 1
    intPaid = loan * interest
    totalInt += intPaid
    loan = loan + loan * interest
    if (loan <= pay):
        print("Month:", x, "Payment:", round(loan, 2), "Interest paid:", round(intPaid, 2), "Remaining debt: 0")
        loan = 0.0
    else:
        loan -= pay
        print("Month:", x, "Payment:", round(pay, 2), "Interest paid:", round(intPaid, 2), "Remaining debt:", round(loan, 2))
print()
print("Number of months:", x)
print("Total interest paid:", round(totalInt, 2))