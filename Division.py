# ignore this is just my rounding function
# admittedly, this script does have some division in it, but these are trivial
# this could be done by a human without division
# we could easily round numbers for instance
def round_half_up(n, decimals=0):
    return round(n*(10**decimals))/(10**decimals)
valid = False

def HalfWay(a,b,decimal):
    if a<b:
        lb = a
        ub = b
    elif b<a:
        lb = b
        ub = a
    else:
        return a
    while ub-lb > 10**(-(decimal)):
        ub -= 10**(-(decimal))
        lb += 10**(-(decimal))
    return round_half_up(lb, decimal+1)

while not valid:
    try:
        total = int(input("The numerator (up to 999,999): "))
        if total < 1000000 and total > 0:
            valid = True
        else:
            print("\nPlease select a number between (inclusive) 1 - 999,999\n")
    except ValueError:
        print("\nPlease select a number between (inclusive) 1 - 999,999\n")
    
valid = False
while not valid:
    try:
        m = int(input("\nThe denominator (up to 999,999): "))
        if m < 1000000 and m > 0:
            valid = True
        else:
            print("\nPlease select a number between (inclusive) 1 - 999,999\n")
    except TypeError:
        print("\nPlease select a number between (inclusive) 1 - 999,999\n")

lb =  0
ub = 1000000

def whole(lb, ub):
    g = HalfWay(lb, ub, 0)
    if g*m == total:
        return g, g+1
    # result found
    elif ub-lb == 1:
        return lb, ub
    # lower and upper bound are one apart, need to do the next decimal place
    elif g*m < total:
        return whole(g, ub)
    elif g*m > total:
        return whole(lb, g)

# def firstPoint(lb, ub, decimal):
#     g = HalfWay(lb, ub, decimal)
#     if g*m == total:
#         return g, g+0.1
#     # result found
#     elif round_half_up(ub-lb, decimal+1) == 10**(-(decimal)):
#         return lb, ub
#     # lower and upper bound are one apart, need to do the next decimal place
#     elif g*m < total:
#         return firstPoint(g, ub, decimal)
#     elif g*m > total:
#         return firstPoint(lb, g, decimal)

def firstPoint(lb, ub, decimal):
    for i in range(5):
        g = HalfWay(lb, ub, decimal)
        if g*m == total:
            return g, g+0.1
        # result found
        elif round_half_up(ub-lb, decimal+1) == 10**(-(decimal)):
            return lb, ub
        # lower and upper are one decimal apart, next decimal place needed
        elif g*m < total:
            lb = g
            continue
        elif g*m > total:
            ub = g
            continue

lb, ub = whole(0, total)
for i in range(1, 16):              # this function can iteratively get more decimal places, 
    lb,ub = firstPoint(lb, ub, i)   # which is the purpose for the custom rounding function 
    if lb*m == total:               # to round to specific decimal places
        result = lb
        break
    elif ub*m == total:
        result = ub
        break
    elif i == 15:
        result = round_half_up(ub, 15)
        break
    
# for some reason I can only do it to a max of 15 digits else python gives up
print(f"\nThe result is (to 100 decimal places): {result}")
