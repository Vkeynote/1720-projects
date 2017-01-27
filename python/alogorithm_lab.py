dec_Num = raw_input("input here: ")
def binary_converter(dec_Num):
    bin_Num = 0
    power = 0
##    in_Num = float(input())
##    in_Num = dec_Num
    
    while dec_Num > 0:
        
        bin_Num += 10 ** power * (dec_Num %2)
        dec_Num //= 2
        power += 1
        
    return bin_Num
print (str(binary_converter(dec_Num)))
