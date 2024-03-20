namespace leet_code_algorithm
{
    public class ValidParentheses
    {
        public static bool IsValid(string s)
        {
            var stack = new Stack<char>();
            Dictionary<char, char> parentheses = [];
            parentheses.Add(')', '(');
            parentheses.Add('}', '{');
            parentheses.Add(']', '[');
            for (int i = 0; i < s.Length; i++)
            {
                char letter = s[i];
                if (parentheses.ContainsKey(letter))
                {
                    char topElement = stack.Count == 0 ? '#' : stack.Pop();
                    if (topElement != parentheses[letter])
                    {
                        return false;
                    }
                }
                else
                {
                    stack.Push(letter);
                }
            }
            return stack.Count == 0;
        }
    }
}

// public static bool IsValid(string s)
// {
//     var stack = new Stack<char>();
//     foreach (var c in s)
//     {
//         if (c == '(' || c == '[' || c == '{')
//         {
//             stack.Push(c);
//         }
//         else if (c == ')' && (stack.Count == 0 || stack.Pop() != '('))
//         {
//             return false;
//         }
//         else if (c == ']' && (stack.Count == 0 || stack.Pop() != '['))
//         {
//             return false;
//         }
//         else if (c == '}' && (stack.Count == 0 || stack.Pop() != '{'))
//         {
//             return false;
//         }
//     }
//     return stack.Count == 0;
// }