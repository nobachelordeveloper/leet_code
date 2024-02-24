package add_binary;

public class Add_binary {
    public String addBinary(String a, String b) {
        String total = "";
        int carry = 0;
        int range;
        if (a.length() >= b.length()) {
            range = a.length();
        } else {
            range = b.length();
        }
        for (var i = 0; i < range; i++) {
            int int_a;
            int int_b;
            if (i < a.length()) {
                int_a = Integer.parseInt(String.valueOf(a.charAt(a.length() - 1 - i)));
            } else {
                int_a = 0;
            }
            if (i < b.length()) {
                int_b = Integer.parseInt(String.valueOf(b.charAt(b.length() - 1 - i)));
            } else {
                int_b = 0;
            }
            int sum = int_a + int_b + carry;
            total = String.valueOf(sum % 2) + total;
            carry = Math.floorDiv(sum, 2);
        }
        if (carry == 1) {
            total = "1" + total;
        }
        return total;
    }
}
