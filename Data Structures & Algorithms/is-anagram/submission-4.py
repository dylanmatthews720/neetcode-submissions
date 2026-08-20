class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap_s = {}
        hashmap_t = {}

        for char in s:
            hashmap_s[char] = hashmap_s.get(char, 0) + 1

        for char in t:
            hashmap_t[char] = hashmap_t.get(char, 0) + 1

        for key in hashmap_s:
            if hashmap_s[key] != hashmap_t.get(key, 0):
                return False

        return True            