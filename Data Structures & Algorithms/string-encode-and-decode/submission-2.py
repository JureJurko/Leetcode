class Solution:
    def encode(self, strs: List[str]) -> str:
        l = ""
        for s in strs:
            l = l + str(len(s)) + "|" + s
        
        return l


    def decode(self, s: str) -> List[str]:
        l = []

        i = 0
        while i < len(s):
            num = ""
            while s[i] != "|":
                num = num + s[i]
                i += 1

            i += 1
            num = int(num)
            l.append(s[i: i + num])
            i = i + num
        
        return l