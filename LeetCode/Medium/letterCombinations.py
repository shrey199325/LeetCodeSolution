class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = digits.split()
        result = []
        num_pad = {"2": ["a","b","c"],
                  "3": ["d","e","f"],
                  "4": ["g","h","i"],
                  "5": ["j","k","l"],
                  "6": ["m","n","o"],
                  "7": ["p","q","r","s"],
                  "8": ["t","u","v"],
                  "9": ["w","x","y","z"]}
        for i in digits:
            if not result:
                result = num_pad[i]
                continue
            temp = result
            result = []
            for j in num_pad[i]:
                for t in temp:
                    result.append(j+t)
        return result

res = Solution().letterCombinations("5437")



abc = ["jgdp","jgdq","jgdr","jgds","jgep","jgeq","jger","jges","jgfp","jgfq","jgfr","jgfs","jhdp","jhdq","jhdr","jhds","jhep","jheq","jher","jhes","jhfp","jhfq","jhfr","jhfs","jidp","jidq","jidr","jids","jiep","jieq","jier","jies","jifp","jifq","jifr","jifs","kgdp","kgdq","kgdr","kgds","kgep","kgeq","kger","kges","kgfp","kgfq","kgfr","kgfs","khdp","khdq","khdr","khds","khep","kheq","kher","khes","khfp","khfq","khfr","khfs","kidp","kidq","kidr","kids","kiep","kieq","kier","kies","kifp","kifq","kifr","kifs","lgdp","lgdq","lgdr","lgds","lgep","lgeq","lger","lges","lgfp","lgfq","lgfr","lgfs","lhdp","lhdq","lhdr","lhds","lhep","lheq","lher","lhes","lhfp","lhfq","lhfr","lhfs","lidp","lidq","lidr","lids","liep","lieq","lier","lies","lifp","lifq","lifr","lifs"]

print(res)
print(abc)
