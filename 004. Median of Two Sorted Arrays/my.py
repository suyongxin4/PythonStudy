class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lenA = len(A)
        lenB = len(B)
        if lenA + lenB == 0:
            return None
        elif lenA == 0:
            return self._getMedian(B)
        elif lenB == 0:
            return self._getMedian(A)
        else:


    def _getMedian(self, li):
        l = len(li)
        if l % 2 == 0:
            i = l >> 1
            return li[i] / 2 + li[i - 1] / 2
        else:
            return li[(l - 1) >> 1]

    def _binarySearch(li, target):
        
