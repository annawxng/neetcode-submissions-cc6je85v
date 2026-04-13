class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        f_list = []
        for word in strs:
            length = len(word)
            f_string = f"{length}#{word}"
            f_list.append(f_string)
        return("".join(f_list))

    def decode(self, s: str) -> List[str]:
        marker = "#"
        start = 0
        res = []
        while start < len(s):
            pos = s.find(marker, start)
            if pos == -1:
                break
            str_length = int(s[start:pos])
            curr_word = s[(pos + 1):(pos + str_length + 1)]
            res.append(curr_word)
            start = pos + str_length + 1
        return res

