class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        Merge_list = nums1+nums2
        l = len(nums1)+len(nums2)
        Merge_list.sort()
        if l%2 == 0:
            return (Merge_list[int(l/2 - 1)]+Merge_list[int(l/2)])/2
        else:
            return(Merge_list[int(l/2)])
