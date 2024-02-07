package reverse_words_in_a_string;

public class Reverse_words_in_a_string {
	//My Answer
	public String reverseWords(String s) {
		var wordList = s.trim().split("\\s+");
		for (int i = 0; i < wordList.length / 2; i++) {
			var temp = wordList[i];
			wordList[i] = wordList[wordList.length - 1 - i];
			wordList[wordList.length - 1 - i] = temp;
		}
		return String.join(" ", wordList);
	}

	public String usingStringBuilder(String s) {
		String[] words = s.split("\\s+");
		StringBuilder sb = new StringBuilder();
		for (int i = words.length - 1; i >= 0; i--) {
			sb.append(words[i]).append(" ");
		}
		return sb.toString().trim();
	}
}

// https://code.visualstudio.com/docs/java/java-debugging