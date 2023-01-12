class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 += nums2
        nums1.sort()
            
        if len(nums1)%2 ==0:
            median = float((nums1[len(nums1)//2] + nums1[len(nums1)//2-1])/2)
        else:
            median = float(nums1[len(nums1)//2])
        return median



#tests for findMedianSortedArrays function

tests = {'test': 2.00000, }
print(f"\n GOT \t<---->\t WANT\n")
for test in tests:
    print(f" {Solution.findMedianSortedArrays(Solution,[1,3],[2])} \t<---->\t 2.000000")
    print(f" {Solution.findMedianSortedArrays(Solution,[1,2],[3,4])} \t<---->\t 2.50000000")
    print(f" {Solution.findMedianSortedArrays(Solution,[1,2,12,13,100],[3,4,5,6,12,14,101])} \t<---->\t idk")