package ransom_note;

public class Ransom_note {
    // My Solution
    public boolean canConstruct(String ransomNote, String magazine) {
        char[] ransom_array = ransomNote.toCharArray();
        char[] magazine_array = magazine.toCharArray();
        StringBuilder magazine_string_builder = constructStringBuilder(magazine_array);
        for (char letter : ransom_array) {
            if (magazine_string_builder.chars().anyMatch(c -> c == letter)) {
                int index = magazine_string_builder.toString().indexOf(String.valueOf(letter));
                magazine_string_builder = magazine_string_builder.deleteCharAt(index);
            } else {
                return false;
            }
        }
        return true;
    }

    public StringBuilder constructStringBuilder(char[] characters) {
        StringBuilder build = new StringBuilder();
        for (char letter : characters) {
            build.append(letter);
        }
        return build;
    }

    // Optimal Solution
    public boolean canConstructOptimal(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length())
            return false;
        int counter[] = new int[26];
        for (char c : magazine.toCharArray()) {
            counter[c - 'a']++;
        }
        for (char c : ransomNote.toCharArray()) {
            if (counter[c - 'a'] == 0)
                return false;
            else
                counter[c - 'a']--;
        }
        return true;
    }
}