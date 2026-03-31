class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        less_len = len(strs[0])

        for i in range(1, len(strs)):
            # print(strs[i], len(strs[i]))
            if len(strs[i]) < less_len:
                less_len = len(strs[i])

        # print(less_len)
        res = []
        
        for i in range(less_len):
            a = strs[0][i]
            # for j in range(1, len(strs)):
            #     if a!= strs[j][i]:
            #         break
            index = 1
            while index < len(strs):
                if a!= strs[index][i]:
                    break
                else:
                    index += 1

            if index != len(strs):
                break
            else:
                res.append(a)

        # print(res)
        if res == []:
            return ""
        else:
            string = "".join(res)
            return string