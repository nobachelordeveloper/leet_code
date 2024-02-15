package valid_anagram;

import java.util.HashMap;

public class Valid_anagram {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> tracker = new HashMap<>();
        char[] s_to_char_array = s.toCharArray();
        char[] t_to_char_array = t.toCharArray();
        for (char letter : s_to_char_array) {
            if (tracker.containsKey(letter)) {
                tracker.put(letter, tracker.get(letter) + 1);
            } else {
                tracker.put(letter, 1);
            }
        }
        for (char letter : t_to_char_array) {
            if (tracker.containsKey(letter)) {
                tracker.put(letter, tracker.get(letter) - 1);
            } else {
                return false;
            }
        }
        if (tracker.values().stream().allMatch(value -> value == 0)) {
            return true;
        } else {
            return false;
        }
    }

    // COUNTING CHARACTERS IN STRINGS IN JAVA
    public boolean isAnagramOptimal(String s, String t) {
        int[] count = new int[26];

        // Count the frequency of characters in string s
        for (char x : s.toCharArray()) {
            count[x - 'a']++;
        }

        // Decrement the frequency of characters in string t
        for (char x : t.toCharArray()) {
            count[x - 'a']--;
        }

        // Check if any character has non-zero frequency
        for (int val : count) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
}
