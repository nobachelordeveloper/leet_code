package cracking_the_coding_interview.a_arrays_and_strings.d;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class IsPalindromePermutation {
    public boolean answer(String s) {
        Character[] letters = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
        Map<Character, Integer> tracker = new HashMap<>();
        for (var i = 0; i < s.length(); i++) {
            Character lowerLetter = Character.toLowerCase(s.charAt(i));
            if (Arrays.stream(letters).anyMatch(c -> c == lowerLetter)) {
                if (tracker.keySet().contains(lowerLetter)) {
                    tracker.remove(lowerLetter);
                } else {
                    tracker.put(lowerLetter, 1);
                }
            }
        }
        return tracker.size() <= 1;
    }

    public void run() throws FileNotFoundException, IOException, ParseException {
        String CURRENT_DIRECTORY = System.getProperty("user.dir");
        String dir_to_book = "\\cracking_the_coding_interview";
        String dir_to_chapter = "\\a_arrays_and_strings";
        String dir_to_problem = "\\d";
        String file_name = "\\test.json";

        String dir_to_test_file = CURRENT_DIRECTORY + dir_to_book + dir_to_chapter + dir_to_problem + file_name;

        JSONParser parser = new JSONParser();
        JSONArray test = (JSONArray) parser.parse(new FileReader(dir_to_test_file));
        var index = 1;
        for (Object line : test) {
            JSONObject input = (JSONObject) line;
            String string = (String) ((JSONObject) input.get("input")).get("s");
            Boolean output = (Boolean) input.get("output");
            System.out.print("#" + index + ": ");
            System.out.println(this.answer(string) == output);
            // The .equals() method checks for content equality when used with objects.
            // The == operator checks for reference equality when used with objects.
            index++;
        }
    }
}
