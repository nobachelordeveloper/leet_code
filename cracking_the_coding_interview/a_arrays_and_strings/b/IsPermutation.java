package cracking_the_coding_interview.a_arrays_and_strings.b;

import java.util.HashMap;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class IsPermutation {
    public Boolean answer(String string1, String string2) {
        HashMap<String, Integer> hashMap = new HashMap<>();
        Boolean isPassing = true;
        for (char letter : string1.toCharArray()) {
            String str_letter = String.valueOf(letter);
            if (hashMap.containsKey(str_letter)) {
                hashMap.put(str_letter, hashMap.get(str_letter) + 1);
            } else {
                hashMap.put(str_letter, 1);
            }
        }
        for (char letter : string2.toCharArray()) {
            String str_letter = String.valueOf(letter);
            if (hashMap.containsKey(str_letter)) {
                hashMap.put(str_letter, hashMap.get(str_letter) - 1);
            } else {
                isPassing = false;
            }
        }

        if (hashMap.values().stream().anyMatch(value -> value != 0)) {
            isPassing = false;
        }

        return isPassing;
    }

    public void run() throws FileNotFoundException, IOException, ParseException {
        String CURRENT_DIRECTORY = System.getProperty("user.dir");
        String dir_to_book = "\\cracking_the_coding_interview";
        String dir_to_chapter = "\\a_arrays_and_strings";
        String dir_to_problem = "\\b";
        String file_name = "\\test.json";

        String dir_to_test_file = CURRENT_DIRECTORY + dir_to_book + dir_to_chapter + dir_to_problem + file_name;

        JSONParser parser = new JSONParser();
        JSONArray test = (JSONArray) parser.parse(new FileReader(dir_to_test_file));
        var index = 1;
        for (Object line : test) {
            JSONObject input = (JSONObject) line;
            String string1 = (String) input.get("string1");
            String string2 = (String) input.get("string2");
            Boolean output = (Boolean) input.get("output");
            System.out.print("#" + index + ": ");
            System.out.println(this.answer(string1, string2) == output);
            index++;
        }
    }

    public void test() {
        System.out.println(this.answer("abc ","cab"));
    }

}
