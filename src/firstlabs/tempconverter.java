package firstlabs;

import java.util.Scanner;

public class tempconverter {
    public static void main(String[]arg)
    { Scanner in = new Scanner(System.in);
    System.out.println("Enter a temperature in Celsius: ");
    float temp = in.nextFloat();
    in.close();
    float newtemp = (temp * 9/5) + 32;
    System.out.println(newtemp);
    }
}
