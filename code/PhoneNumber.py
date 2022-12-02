from ast import List

# TODO look into pythons zip methodss peeps will think im weird


class Solution:
    def letterCombinations(self, digits: str):
        dict = {2: ["a","b","c"], 3: ["d","e","f"], 4: ["g","h","i"], 5:["j","k","l"], 6: ["m","n","o"], 7: ["p","q","r","s"], 8: ["t","u","v"], 9: ["w","x","y","z"]}
        digits.split()
        li = []
        for i in digits:
            li.append(dict[int(i)])
        
        return li

print(Solution.letterCombinations(Solution,"23"), " --> ", '["ad","ae","af","bd","be","bf","cd","ce","cf"]')


print(len(Solution.letterCombinations(Solution,"234")), " --> ", len(["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]))



print(len(Solution.letterCombinations(Solution,"2344")), " --> ", len(["adgj","adgk","adgl","adhj","adhk","adhl","adij","adik","adil","aegj","aegk","aegl","aehj","aehk","aehl","aeij","aeik","aeil","afgj","afgk","afgl","afhj","afhk","afhl","afij","afik","afil","bdgj","bdgk","bdgl","bdhj","bdhk","bdhl","bdij","bdik","bdil","begj","begk","begl","behj","behk","behl","beij","beik","beil","bfgj","bfgk","bfgl","bfhj","bfhk","bfhl","bfij","bfik","bfil","cdgj","cdgk","cdgl","cdhj","cdhk","cdhl","cdij","cdik","cdil","cegj","cegk","cegl","cehj","cehk","cehl","ceij","ceik","ceil","cfgj","cfgk","cfgl","cfhj","cfhk","cfhl","cfij","cfik","cfil"]))
print(Solution.letterCombinations(Solution,"234")," --> ", '["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]')


        # length = len(digits)
        # for i in li[0]:
        #     count = 1
        #     while count < length:
        #         for j in li[count]:
        #             print(i+j)
        #         count += 1