def total_calc(bill_amount,tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    print("THE AMOUNT YOU NEED TO PAY IS Rs",total)
total_calc(2453,5)