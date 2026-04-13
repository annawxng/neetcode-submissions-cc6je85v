class Solution:
    # act, cat, 
    # sorted_s = "".join(sorted(s))

    # for word in strs => sort each word, and store as key, keep idx
    # dict[word : idx]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            ana_dict[sorted_word].append(word)
        return list(ana_dict.values())