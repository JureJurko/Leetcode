class Solution:
    def __init__(self):
        self.mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.result = []

    def letterCombinations(self, digits: str) -> List[str]:
        curr_combo = ""
        self.helper(curr_combo, list(digits), len(digits))
        return self.result
    
    def helper(self, curr_combo, digits, max_length):
        if max_length == 0:
            return 
        if len(curr_combo) == max_length:
            self.result.append(curr_combo)
            return
        
        curr_letters = list(self.mappings[digits[len(curr_combo)]])
        for letter in curr_letters:
            curr_combo += letter
            self.helper(curr_combo, digits, max_length)
            curr_combo = curr_combo[:-1]
        return
        