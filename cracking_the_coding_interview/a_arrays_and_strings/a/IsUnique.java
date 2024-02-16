package cracking_the_coding_interview.a_arrays_and_strings.a;

import java.util.HashMap;

public class IsUnique {
    public Boolean answer(String string) {
        HashMap<String, Integer> hashMap = new HashMap<>();
        for (char letter : string.toCharArray()) {
            String str_letter = String.valueOf(letter);
            if (hashMap.containsKey(str_letter)) {
                return false;
            } else {
                hashMap.put(str_letter, 1);
            }
        }
        return true;
    }
    public void run() {
        System.out.println(this.answer("hello")); 
        System.out.println(this.answer("world")); 
        System.out.println(this.answer("apple")); 
        System.out.println(this.answer("12345")); 
        System.out.println(this.answer("abracadabra")); 
    }
}
