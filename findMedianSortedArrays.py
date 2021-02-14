class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        a = [1,3,4]
        b = [2,5,6,7]
        ans = 4
        
        We know that the median must be at the 4th position. In the left part of the 
        merged arr, a may contribute (0,3) and b may contribute (1,4) numbers. 
        
        amin = 0
        amax = 3
        
        We are searching in terms of a always. 
        First iteration, the count is (0+3)//2 = 1:
        a -> [1]     a'=3
        b -> [2,5,6] b'=7
        since last element of b is larger than a[-1] and a'. We need less of b, so now
        amin = acount +1
        
        amin = 2
        amax = 3
        
        Second iteration, the count is (1+3)//2 = 2:
        a -> [1,3] a'=4
        b -> [2,5] b'=6
        since the last element of b is still larger than a[-1] and a'. We still need less of b, so now:
        amin = acount +1
        
        amin = 3
        amax = 3
        a -> [1,3,4] a
        """
        m = len(nums1)
        n = len(nums2)
        odd = False if (m+n)%2==0 else True
        lenmedian = (m+n)//2
        a = nums1
        b = nums2
        
        # if nums2 has length bigger than the median length, minimum 
        # number of a is 0, else the minimum is lenmedian -n 
        alenmin = 0 if n>=lenmedian else lenmedian-n

        # if nums1 has length bigger than median length, maxmimum of 
        # a is lenmedian or else it is just the length (m)
        alenmax = lenmedian if m>=lenmedian else m

    
        while True:
            # Perform binary search for the number of elements from a 
            # to be included in the left part of the merged array
            acount = (alenmin + alenmax)//2
            
            # Find the number of b to included in the left part of the arr
            bcount = lenmedian - acount
            
            # Get the element at acount and bcount (both shifted down by one for python 0 index)
            anum = a[acount-1] if acount >0 else float("-infinity")
            bnum = b[bcount-1] if bcount >0 else float("-infinity")
            aprime = a[acount] if acount < m else float("infinity")
            bprime = b[bcount] if bcount < n else float("infinity")
            
            if anum <= bprime and bnum <= aprime:
                if odd:
                    return min(aprime,bprime)
                else:   
                    return (max(anum,bnum)+min(aprime,bprime))/2
            # Too much a is included
            elif anum > bprime:
                alenmax -= 1
            elif bnum > aprime:
                alenmin += 1 
