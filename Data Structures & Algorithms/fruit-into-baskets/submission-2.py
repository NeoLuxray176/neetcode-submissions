class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Task
        # Find the type that occurs the most and second most in the array

        # General idea
        # Starting from every tree we need to pick every fruit
        # So we want to find the longest sequence consisting of only one of two numbers starting from an index

        n = len(fruits)
        res, curr_res = 0, 0
        curr_set = set()

        for i in range(n):
            curr_res = 0
            curr_set = set()
            for j in range(i, n):
                if len(curr_set) < 2:
                    curr_set.add(fruits[j])
                    curr_res += 1
                elif fruits[j] in curr_set:
                    curr_res += 1
                else:
                    break
                    curr_set = set()
                    curr_set.add(fruits[j])
                    curr_res = 1
                
                # print(curr_res, curr_set)
                res = max(res, curr_res)

        return res


        
        