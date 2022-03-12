from math import floor
maxDigits = 2022
total = 9
comb = []
for repeatedDigit in range(10):
    for digits in range(2, maxDigits + 1):
        print(repeatedDigit, digits)
        for numRepeat in range(floor(digits / 2) + 1, digits + 1):
            #print(repeatedDigit, digits, numRepeat)
            if repeatedDigit == 0:
                total += comb(digits - 1, numRepeat) * (9 ** (digits - numRepeat))
            else:
                # repeated digit first
                total += comb(digits - 1, numRepeat - 1) * (9 ** (digits - numRepeat))
                if digits > 2:
                    # non-repeated digit first
                    total += 8 * comb(digits - 1, numRepeat) * (9 ** (digits - numRepeat - 1))
print(round(total) % 1000000007)