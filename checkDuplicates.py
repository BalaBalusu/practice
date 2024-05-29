class Solution:
    #simple solution to iterate and exit - hasset
    def containsDuplicate(self, nums: List[int]) -> bool:
        addNums=set()
        for number in nums:
          if number in addNums:
             print("checking number in new Array addNums")
             return True
          addNums.add(number)
        
        return False
    
    #to count the occurences of the number can be implemented using HashMap
    def countDuplicates(self, nums: List[int]) -> bool:
        addNums = {}
        for number in nums:
            
            if number in addNums and addNums[number]>=1:
                return True
            addNums.get(number, 0)+1
        return False
            