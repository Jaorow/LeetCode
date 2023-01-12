class Solution:
    def reverse(self, x: int) -> int:

        if x >= 2147483647 or x <= -2147483648:
            return 0
        # if len(x) >= 10 and x[-1] == 2:
        #     if x 

        li = [l for l in str(x)]
        li.reverse()
        if li[-1] == "-":
            li.remove("-")
            s = int("-"+"".join(li))
        else:
            s = int("".join(li))
        
        if s >= 2147483647 or s <= -2147483648:
            return 0

        return s

print(Solution.reverse(Solution,123))
print(Solution.reverse(Solution,-123))
print(Solution.reverse(Solution,120))
print(Solution.reverse(Solution,0))
print(Solution.reverse(Solution,1))
print(Solution.reverse(Solution,-1))
print(Solution.reverse(Solution,1534236469))
print(Solution.reverse(Solution,15342364691534236469))