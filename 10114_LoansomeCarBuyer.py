import sys

while True:
    [dur_months, down_payment, loan_amount, q] = list(map(float, sys.stdin.readline().strip().split()))
    dur_months, q = int(dur_months), int(q)
    if dur_months < 0:
        sys.exit()

    updates = {}
    for _ in range(q):
        [month, decr] = list(map(float, sys.stdin.readline().strip().split()))
        month = int(month)
        updates[month] = decr

    # Couple of important points that are not mentioned in the problem (why?)
    # 1. The car value is loan amount + down payment
    # 2. monthly payment to the loan is assumed to be total loan / duration
    # 3. The loan payment might stop after some months, but the depreciation will continue

    # This is not an ALGO question.
    # This is "guess the rules for this financing" question.

    car_value = loan_amount + down_payment
    if 0 in updates:
        car_value = (1 - updates[0]) * car_value
    int_payment = loan_amount / dur_months

    prev_dep_rate = updates[0]
    i = 0
    while loan_amount > car_value:
        i += 1
        rate = updates[i] if i in updates else prev_dep_rate
        prev_dep_rate = rate
        car_value = (1 - rate) * car_value
        loan_amount -= int_payment

    if i == 1:
        print("1 month")
    else:
        print("%d months" % i)
