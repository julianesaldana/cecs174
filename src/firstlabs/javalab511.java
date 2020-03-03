package firstlabs;

import java.util.Scanner;

public class javalab511 {
    public static void main(String[]arg)
    { Scanner in = new Scanner(System.in);
    System.out.println("Enter the first integer: ");
    int first = in.nextInt();
    System.out.println("Enter the second integer: ");
    int second = in.nextInt();
    System.out.println("Enter the third integer: ");
    int third = in.nextInt();
    in.close();
    if (first == second && first == third){
        System.out.println("All the same");
    } else if (first != second && first != third && second != third){
        System.out.println(("All different"));
    } else
        System.out.println("Neither");
    }

}
