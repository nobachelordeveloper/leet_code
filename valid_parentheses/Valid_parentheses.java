package valid_parentheses;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class Valid_parentheses {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> parentheses = new HashMap<>();
        parentheses.put(')', '(');
        parentheses.put('}', '{');
        parentheses.put(']', '[');
        for (int i = 0; i < s.length(); i++) {
            char letter = s.charAt(i);
            if (parentheses.containsKey(letter)) {
                char topElement = stack.empty() ? '#' : stack.pop();
                if (topElement != parentheses.get(letter)) {
                    return false;
                }
            } else {
                stack.push(letter);
            }
        }
        return stack.isEmpty();
    }

    public void test() {
        System.out.print(this.isValid("()"));
    }
}
