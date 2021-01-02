package firstlabs;

import java.util.Scanner;

public class javalab619 {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        String user = in.nextLine();
        for (int i = user.length() - 1; i > -1; i--) {
            if (user.charAt(i) == ' ') {
                continue;
            } else {
                System.out.print(user.charAt(i));
            }
        }
    }
}