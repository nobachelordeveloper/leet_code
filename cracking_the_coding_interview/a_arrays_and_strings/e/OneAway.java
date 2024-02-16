package cracking_the_coding_interview.a_arrays_and_strings.e;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class OneAway {
    public boolean answer(String first, String second) {
        char[] longer_chars;
        char[] shorter_chars;
        if (first.length() >= second.length()) {
            longer_chars = first.toCharArray();
            shorter_chars = second.toCharArray();
        } else {
            longer_chars = second.toCharArray();
            shorter_chars = first.toCharArray();
        }
        if (longer_chars.length - shorter_chars.length > 1) {
            return false;
        }
        int index_shorter = 0;
        int index_longer = 0;
        Boolean difference_found = false;

        while (index_shorter < shorter_chars.length) {
            if (shorter_chars[index_shorter] != longer_chars[index_longer]) {
                if (difference_found) {
                    return false;
                } else {
                    difference_found = true;
                }
                if (shorter_chars.length != longer_chars.length) {
                    index_longer++;
                } else {
                    index_longer++;
                    index_shorter++;
                }
            } else {
                index_longer++;
                index_shorter++;
            }
        }
        return true;
    }

    public void run() throws FileNotFoundException, IOException, ParseException {
        String CURRENT_DIRECTORY = System.getProperty("user.dir");
        String dir_to_book = "\\cracking_the_coding_interview";
        //#1
        String dir_to_chapter = "\\a_arrays_and_strings";
        String dir_to_problem = "\\e";
        String file_name = "\\test.json";

        String dir_to_test_file = CURRENT_DIRECTORY + dir_to_book + dir_to_chapter + dir_to_problem + file_name;

        JSONParser parser = new JSONParser();
        JSONArray test = (JSONArray) parser.parse(new FileReader(dir_to_test_file));
        for (Object line : test) {
            JSONObject inputLine = (JSONObject) line;
            JSONObject input = (JSONObject) inputLine.get("input");
            //#2
            String first = (String) input.get("first");
            String second = (String) input.get("second");
            Boolean output = (Boolean) inputLine.get("output");
            System.out.print("#" + inputLine.get("index") + ": ");
            System.out.println(this.answer(first, second) == output);
            // The .equals() method checks for content equality when used with objects.
            // The == operator checks for reference equality when used with objects.
        }
    }
}
