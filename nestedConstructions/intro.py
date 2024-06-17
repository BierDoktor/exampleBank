# nested constructions = function calls inside other functions calls
#                        innermost function calls are resolved first
#                        returned value is used as argument for next outer function

bill = input('Enter the bill amount: ')
bill = float(bill)
bill = round(bill)
print('Bill amount:', bill)

print('BillNested amount:', round(float(input('Enter the bill amount: '))))