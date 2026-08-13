class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}

        if len(s) != len(t):
            return False

        for c in s:
            hashmap_s[c] = hashmap_s.get(c, 0) + 1

        for c in t:
            hashmap_t[c] = hashmap_t.get(c,0) + 1

        for key in hashmap_s:
            if hashmap_s[key] != hashmap_t.get(key, 0):
                return False


        return True        
