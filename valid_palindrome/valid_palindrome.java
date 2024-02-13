package valid_palindrome;

public class valid_palindrome {
    public boolean isPalindrome(String s) {
        var lowerS = s.toLowerCase();
        var sCharArray = lowerS.toCharArray();
        StringBuilder formatted = new StringBuilder();
        StringBuilder reversed = new StringBuilder();
        for (var i = 0; i < sCharArray.length; i++) {
            String letter = Character.toString(sCharArray[i]);
            if (letter.matches("^[a-z0-9]$")) {
                formatted.append(letter);
            }
        }
        for (var x = formatted.length() - 1; x > -1; x--) {
            reversed.append(formatted.charAt(x));
        }

        return formatted.toString().equals(reversed.toString());
    }

    public boolean isPalindromeOptimal(String s) {
        // Convert the string to lowercase and remove non-alphanumeric characters
        String cleanString = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");

        // Check if the clean string is a palindrome
        int left = 0;
        int right = cleanString.length() - 1;

        while (left < right) {
            if (cleanString.charAt(left) != cleanString.charAt(right)) {
                return false; // Characters do not match, not a palindrome
            }
            left++;
            right--;
        }

        return true; // All characters match, it's a palindrome
    }
}
