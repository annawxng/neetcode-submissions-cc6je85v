class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        adj_list = defaultdict(list)
        for i, val in enumerate(nums):
            adj_list[val].append(i)
        for key, vec in adj_list.items():
            left = target - key
            if left in adj_list:
                if left == key:
                    print("left == key")
                    if len(vec) != 1:
                        return vec
                    continue
                print(f"adding {vec[0]} and {adj_list[left][0]}")
                res.append(vec[0]);
                res.append(adj_list[left][0])
                return res
        return res
                
            

        