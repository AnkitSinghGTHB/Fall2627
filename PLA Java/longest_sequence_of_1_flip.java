import java.util.*;

public class longest_sequence_of_1_flip {
    public static void main(String[] args) {
        // find the length of the longest sequence of 1s possible by flipping at most
        // one '0' to '1'
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) {
            sc.close();
            return;
        }
        String s = sc.next();

        int maxLen = 0;
        int currentLen = 0;
        int previousLen = 0;
        boolean hasZero = false;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '1') {
                currentLen++;
            } else if (c == '0') {
                hasZero = true;
                if (i > 0 && s.charAt(i - 1) == '0') {
                    previousLen = 0;
                } else {
                    previousLen = currentLen;
                }
                currentLen = 0;
            }

            if (hasZero) {
                maxLen = Math.max(maxLen, previousLen + 1 + currentLen);
            } else {
                maxLen = Math.max(maxLen, currentLen);
            }
        }

        System.out.println(maxLen);
        sc.close();
    }
}
