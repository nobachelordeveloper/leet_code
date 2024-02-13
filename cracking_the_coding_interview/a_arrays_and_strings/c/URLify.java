package cracking_the_coding_interview.a_arrays_and_strings.c;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

// Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.
// EXAMPLE
// Input: "Mr John Smith     ", 13
// Output: "Mr%20John%20Smith"

public class URLify {
    public String answer(String string, Integer true_length) {
        if (string == "") {
            return "";
        }
        StringBuilder stringBuilder = new StringBuilder();
        var charArray = string.toCharArray();
        for (int i = 0; i < true_length; i++) {
            if (i > string.length() - 1) {
                stringBuilder.append("%20");
            } else if (charArray[i] == ' ') {
                stringBuilder.append("%20");
            } else {
                stringBuilder.append(charArray[i]);
            }
        }
        String result = stringBuilder.toString();
        return result;
    }

    public void run() throws FileNotFoundException, IOException, ParseException {
        String CURRENT_DIRECTORY = System.getProperty("user.dir");
        String dir_to_book = "\\cracking_the_coding_interview";
        String dir_to_chapter = "\\a_arrays_and_strings";
        String dir_to_problem = "\\c";
        String file_name = "\\test.json";

        String dir_to_test_file = CURRENT_DIRECTORY + dir_to_book + dir_to_chapter + dir_to_problem + file_name;

        JSONParser parser = new JSONParser();
        JSONArray test = (JSONArray) parser.parse(new FileReader(dir_to_test_file));
        var index = 1;
        for (Object line : test) {
            JSONObject input = (JSONObject) line;
            String string = (String) ((JSONObject) input.get("input")).get("string");
            Integer true_length = ((Long) ((JSONObject) input.get("input")).get("true_length")).intValue();
            String output = (String) input.get("output");
            System.out.print("#" + index + ": ");
            System.out.println(this.answer(string, true_length).equals(output));
            // The .equals() method checks for content equality when used with objects.
            // The == operator checks for reference equality when used with objects.
            index++;
        }
    }

    public void test() {
        System.out.println(this.answer("Trailing    ", 11));
    }
}
