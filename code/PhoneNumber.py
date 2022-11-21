from ast import List


class Solution:
    def letterCombinations(self, digits: str):
        dict = {2: ["a","b","c"], 3: ["d","e","f"], 4: ["g","h","i"], 5:["j","k","l"], 6: ["m","n","o"], 7: ["p","q","r","s"], 8: ["t","u","v"], 9: ["w","x","y","z"]}
        digits.split()
        li = []
        for i in digits:
                li.append(dict[int(i)])
        
        final = []
        for list in li:
            
        
        return li

print(Solution.letterCombinations(Solution,"23"), " --> ", '["ad","ae","af","bd","be","bf","cd","ce","cf"]')
print(Solution.letterCombinations(Solution,"234"))