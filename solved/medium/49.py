# type: ignore
from collections import defaultdict


def is_anagram(s: str, t: str) -> bool:
    if sorted(s) == sorted(t):
        return True
    return False


def main(strs: list[str]) -> list[list[str]]:
    anagrams_types = defaultdict()
    response_list = []
    for s in strs:
        s_ana = ''.join(sorted(s))
        if s_ana in anagrams_types.keys():
            anagram_type = anagrams_types.get(s_ana)
            response_list[anagram_type].append(s)
        else:
            anagrams_types[s_ana] = len(anagrams_types)
            response_list.append([s])
    return response_list


r = main(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
print(r)


# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
