import java.util.*;

public class lognest_seq_of_1_flip_wostring {
    public static void main(String[] args) {
        // wrong code
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int prev_len = 0;
        int curr_len = 0;
        int max_len = 0;
        while (n > 0) {
            int r = n % 10;
            if (r == 1) {
                curr_len++;
            } else {
                prev_len = curr_len;
                curr_len = 0;
            }
            max_len = Math.max(max_len, prev_len + curr_len);
            n /= 10;
        }
        System.out.println(max_len);
        sc.close();
    }
}
