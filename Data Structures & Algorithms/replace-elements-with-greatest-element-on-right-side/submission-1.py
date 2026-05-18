class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_so_far = arr[n-1]
        i = n-1
        arr[i]= -1
        while i>0:
            
            val = arr[i-1]
            arr[i-1] = max_so_far
            if val>max_so_far:
                max_so_far = val
            
            i = i-1

        return arr

        
