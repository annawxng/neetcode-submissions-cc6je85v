class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each word
        # key -> [og strs] -- map contains list so we need the defaultdict(list)
        mp = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            mp[key].append(word)

        return list(mp.values())



