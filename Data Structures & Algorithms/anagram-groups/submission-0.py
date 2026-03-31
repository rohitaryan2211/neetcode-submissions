class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        if len(strs) == 1:
            res.append(strs)
            return res
        
        category = {}
        
        for i in range(len(strs)):
            new_list = list(strs[i])
            new_list.sort()
            # print(new_list)
            sorted_word = ''.join(str(x) for x in new_list)
            # print(sorted_word)
            if sorted_word not in category:
                category[sorted_word] = [strs[i]]
            else:
                category[sorted_word].append(strs[i])
            
        # print(list(category.keys()))
        keys = list(category.keys())
        for x in keys:
            l = category[x]
            res.append(l)
        
        return res 
            
             