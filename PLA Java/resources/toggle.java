import java.util.*;

public class toggle {
    // 100 closed doors, 100 monkeys, every monkey that visits a door either opens a
    // closed door or closes an open door. the first monkey that is let out of the
    // cage visits and opens all the hundred doors. the second monkey that is
    // released visits doors of the order 2,4,6,8,10
    // basically i need to get the odd number of factors of each number form 1 to n
    // and count them
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // now i get factors of each value from 1 to n
        // okay but this is O(n^2), how do i get O(nlogn)
        // observation, it is the count of square values from 1 to n
        // int count = 0;
        // for (int i = 1; i <= n; i++) {
        // int visits = 0;
        // for (int j = 1; j <= i; j++) {
        // if (i % j == 0) {
        // visits++;
        // }
        // }
        // if (visits % 2 != 0) {
        // count++;
        // }
        // }

        // okay this is O(n) soln
        int count = 0;
        for (int i = 1; i < n; i++) {
            // if i is perfect square then count++
            int root = (int) Math.sqrt(i);
            if (root * root == i) {
                count++;
            }
        }
        System.out.println(count);
        sc.close();
    }
}