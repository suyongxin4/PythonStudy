class Solution:
    # @return a tuple, (index1, index2)
    # def twoSum(self, num, target):
    #     isFound = False
    #     i = 0
    #     length = len(num)
    #     targetNum = list(map(lambda x: target - x, num))
    #     while i < length:
    #         j = i + 1
    #         while j < length:
    #             if num[i] == targetNum[j]:
    #                 isFound = True
    #                 break
    #             j = j + 1
    #         if isFound:
    #             break
    #         i = i + 1
    #     if isFound:
    #         return (i + 1, j + 1)
    #     else:
    #         return (0, 0)

    def twoSum(self, num, target):
        length = len(num)
        if length == 0:
            return (0, 0)
        diffNum = list(enumerate(map(lambda x: target - x - x, num)))
        diffNum.sort(key=lambda t: t[1])
        start = 0
        end = length - 1
        while start < end:
            diffSum = diffNum[start][1] + diffNum[end][1]
            if diffSum == 0:
                break;
            elif diffSum > 0:
                end = end - 1
            else:
                start = start + 1
        else:
            return (0, 0)
        i = diffNum[start][0]
        j = diffNum[end][0]
        if i > j:
            temp = i;
            i = j;
            j = temp;
        return (i + 1, j + 1)
