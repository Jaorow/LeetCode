class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = [i for i in s]
        sum = 0
        i = 0
        while i < len(s):
            try:
                v = s[i]
                if s[i] == "I":
                    if s[i+1] == "V":
                        sum += 4
                        i += 1
                    elif s[i+1] == "X":
                        sum += 9
                        i += 1
                    else:
                        sum += dict[s[i]]

                elif s[i] == "X":
                    if s[i+1] == "L":
                        sum += 40
                        i += 1
                    elif s[i+1] == "C":
                        sum += 90
                        i += 1
                    else:
                        sum += dict[s[i]]

                elif s[i] == "C":
                    if s[i+1] == "D":
                        sum += 400
                        i += 1
                    elif s[i+1] == "M":
                        sum += 900
                        i += 1
                    else:
                        sum += dict[s[i]]

                else:
                    sum += dict[s[i]]

                i += 1     
            except IndexError:
                if i != len(s):
                    sum += dict[s[i]]
                    i += 1


                
        return sum

class Solution2:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))


print(Solution.romanToInt(Solution,"IX"))
print(Solution2.romanToInt(Solution,"MCMXCIV"))
print(Solution.romanToInt(Solution,"III"))
print(Solution.romanToInt(Solution,"LVIII"))