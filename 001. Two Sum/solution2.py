class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        #dictionary O(n)
        dict = {}
        for i in range(len(num)):
            if num[i] not in dict:
                dict[target-num[i]] = i
            else:
                return (dict[num[i]]+1, i+1)
        return (0, 0)