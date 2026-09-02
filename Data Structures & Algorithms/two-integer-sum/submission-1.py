class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use a dictionary
        n = len(nums)
        rems = {}

        for i in range(n):
            if nums[i] in rems:
                print(f"Found solution {i} {rems[nums[i]]}")
                a, b = i, rems[nums[i]][0]
                if a < b:
                    return [a, b]
                else:
                    return [b, a]
            
            rem = target - nums[i]
            if rem not in rems:
                rems[rem] = [i]
            else:
                rems[rem].append(i)

        return [-1, -1]
