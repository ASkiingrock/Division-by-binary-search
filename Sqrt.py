# ignore this is just my rounding function
# admittedly, this script does have some division in it, but these are trivial
# this could be done by a human without division
# we could easily round numbers for instance
def round_half_up(n, decimals=0):
    return round(n*(10**decimals))/(10**decimals)
valid = False

while not valid:
    try:
        total = int(input("The number to be square rooted: "))
        if total < 1000000 and total > 0:
            valid = True
        else:
            print("\nPlease select a number between (inclusive) 1 - 999,999\n")
    except ValueError:
        print("\nPlease select a number between (inclusive) 1 - 999,999\n")

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

lb =  0
ub = 1000000

def whole(lb, ub):
    g = HalfWay(lb, ub, 0)
    if g*g == total:
        return g, g+1
    # result found
    elif ub-lb == 1:
        return lb, ub
    # lower and upper bound are one apart, need to do the next decimal place
    elif g*g < total:
        return whole(g, ub)
    elif g*g > total:
        return whole(lb, g)

# def firstPoint(lb, ub, decimal):
#     g = HalfWay(lb, ub, decimal)
#     if g*g == total:
#         return g, g+0.1
#     # result found
#     elif round_half_up(ub-lb, decimal+1) == 10**(-(decimal)):
#         return lb, ub
#     # lower and upper bound are one apart, need to do the next decimal place
#     elif g*g < total:
#         return firstPoint(g, ub, decimal)
#     elif g*g > total:
#         return firstPoint(lb, g, decimal)

def firstPoint(lb, ub, decimal):
    for i in range(10):
        g = HalfWay(lb, ub, decimal)
        if g*g == total:
            return g, g+0.1
        # result found
        elif round_half_up(ub-lb, decimal+1) <= 10**(-(decimal)):
            return lb, ub
        # lower and upper are one decimal apart, next decimal place needed
        elif g*g < total:
            lb = g
            continue
        elif g*g > total:
            ub = g
            continue
    return lb, ub

lb, ub = whole(0, total)

for i in range(1, 16):              # this function can iteratively get more decimal places, 
    lb,ub = firstPoint(lb, ub, i)   # which is the purpose for the custom rounding function 
    if lb*lb == total:              # to round to specific decimal places
        result = lb
        break
    elif ub*ub == total:
        result = ub
        break
    elif i == 15:
        result = round_half_up(ub, 15)
        break

# for some reason I can only do it to a max of 15 digits otherwise floatin point arithmetic just gives sup
print(f"\nThe result is (to 15 decimal places): {result}")


