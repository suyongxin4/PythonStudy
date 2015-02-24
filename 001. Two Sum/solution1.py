class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        target_dict=dict((val,index+1) for index,val in enumerate(num))
        for (i,v) in enumerate(num):
            index=target_dict.get(target-v)
            if index and index!=i+1:
                return (i+1,index)
