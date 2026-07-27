class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def giveDict(s:str):
            temp_dict = {}
            for x in s:
                if x not in temp_dict.keys():
                    temp_dict[x] = 1
                else:
                    temp_dict[x] += 1
            return temp_dict


        res = []
        
        for i in range(len(strs)):
            # print(strs[i], '---------------->')
            if len(res) == 0:
                res.append([strs[i]])
                # print(res)
            else:
                j = 0
                while j < len(res):
                    if giveDict(res[j][0]) == giveDict(strs[i]):
                        res[j].append(strs[i])
                        # print(res)
                        break
                    j += 1
                # print(j)
                if j == len(res):
                    res.append([strs[i]])
                    # print(res)


        return res
            