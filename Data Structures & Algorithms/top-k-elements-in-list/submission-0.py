class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        temp_dict = {}
        for x in nums:
            if x not in temp_dict.keys():
                temp_dict[x] = 1
            else:
                temp_dict[x] += 1
        temp_dict_sorted = dict(sorted(temp_dict.items(), key=lambda item: item[1], reverse=True))
        return list(temp_dict_sorted.keys())[:k]