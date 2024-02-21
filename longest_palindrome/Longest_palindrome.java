package longest_palindrome;

import java.util.HashMap;

public class Longest_palindrome {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> letter_tracker = new HashMap<>();
        int count = 0;
        char[] s_char_array = s.toCharArray();
        for (char letter : s_char_array) {
            if (letter_tracker.containsKey(letter)) {
                letter_tracker.remove(letter);
                count += 2;
            } else {
                letter_tracker.put(letter, 1);
            }
        }
        if (!letter_tracker.isEmpty()) {
            count += 1;
        }
        return count;
    }

    public int longestPalindromeOptimal(String s) {
        int[] count = new int[128];
        for (char c : s.toCharArray())
            count[c]++;

        int ans = 0;
        for (int v : count) {
            ans += v / 2 * 2;
            if (ans % 2 == 0 && v % 2 == 1)
                ans++;
        }
        return ans;
    }
}
