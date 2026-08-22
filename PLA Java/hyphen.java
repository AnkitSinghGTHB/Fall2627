import java.util.Scanner;

public class hyphen {
    public static void main(String[] args) {
        // move hyphen to the beginning
        // Scanner sc = new Scanner(System.in);
        // String s = sc.next();
        // char[] arr = s.toCharArray();
        // int n = arr.length;
        // int hypen = 0;
        // for (int i = 0; i < n; i++) {
        // if (arr[i] == '-') {
        // hypen++;
        // }
        // }
        // char[] result = new char[n];
        // int j = 0;
        // int i = 0;
        // while (i < n) {
        // if (hypen > 0) {
        // result[i] = '-';
        // hypen--;
        // i++;
        // } else {
        // if (arr[j] != '-') {
        // result[i] = arr[j];
        // i++;
        // }
        // j++;
        // }
        // }
        // System.out.println(new String(result));
        // sc.close();

        // using StringBuilder
        Scanner sc = new Scanner(System.in);
        StringBuilder st = new StringBuilder(sc.next());
        for (int i = 0; i < st.length(); i++) {
            if (st.charAt(i) == '-') {
                st.deleteCharAt(i);
                st.insert(0, '-');
            }
        }
        System.out.println(st.toString());
        sc.close();
    }
}
