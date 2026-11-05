class Solution:
    def encode(self, strs: List[str]) -> str:
        l = []
        for s in strs:
            l.append(str(len(s)))
            l.append("|")
            l.append(s)
        
        return "".join(l)


    def decode(self, s: str) -> List[str]:
        l = []

        i = 0
        while i < len(s):
            j = i
            while s[i] != "|":
                i += 1

            num = int(s[j:i])
            i += 1
            l.append(s[i: i + num])
            i = i + num
        
        return l