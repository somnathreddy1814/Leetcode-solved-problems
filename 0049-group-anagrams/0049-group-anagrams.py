class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        for word in strs:
            sorted_word="".join(sorted(word))
            # print(sorted_word)
            map[sorted_word].append(word)
            
        # print(map)
        return list(map.values())
        