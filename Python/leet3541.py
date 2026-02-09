class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import Counter

        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        
        # Count all letters
        freq = Counter(s)
        
        # Maximum frequency of vowels
        max_vowel = max((freq[ch] for ch in vowels_set if ch in freq), default=0)
        
        # Maximum frequency of consonants
        max_consonant = max((freq[ch] for ch in freq if ch not in vowels_set), default=0)
        
        return max_vowel + max_consonant
