import math

class Solution:
    def numSquares(self, n: int) -> int:
        squares = self.find_list_squares(self,n)
        min = n

        # check if number is root
        root = math.sqrt(n)
        if int(root + 0.5) ** 2 == n:
            return n

        print(squares)
        for i in squares:
            if i == 1:
                pass
            else:
                print(f"--{i}--")
                for j in squares:
                    total = 0
                    while total+j < n:
                        total += j
                    print(f"{i} + {j}")
        
        return min

    
    def find_list_squares(self,number):
        l = []
        while number > 0:
            root = math.sqrt(number)
            if int(root + 0.5) ** 2 == number:
                l.append(number)
            number -= 1
        return l

print(Solution.numSquares(Solution,12))
print("\n")
# print(Solution.numSquares(Solution,20))