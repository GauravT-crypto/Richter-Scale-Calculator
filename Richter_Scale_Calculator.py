print("Richter            Joules                              TNT")

richter_values = [1, 5, 9.1, 9.2, 9.5]

for i in richter_values:
    Energy = 10**((1.5 * i) + 4.8)
    TNT = Energy/(4.184*10**9)
    print("{}           {}               {}".format(i, Energy, TNT))


def richter_scale(richter):
    Energy = 10**((1.5 * richter) + 4.8)
    return Energy


def tnt_function(value):
    number = richter_scale(value)/(4.184*10**9)
    return number


num = float(input("Please enter a Richter scale value: "))
print("Richter scale value:", num)
richter_num = richter_scale(num)
tnt_value = tnt_function(num)
print("Equivalence in joule:", richter_num)
print("Equivalence in tons of TNT: ", tnt_value)
