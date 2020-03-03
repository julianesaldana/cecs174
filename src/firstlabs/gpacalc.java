package firstlabs;

import java.util.Scanner;

public class gpacalc {
    public static void main(String[] arg) {
        Scanner ask = new Scanner(System.in);
        while (true) {
            double total_score = 0;
            System.out.println("How many classes are you taking?");
            double numclasses = ask.nextInt();
            for (int i = 0; i < numclasses; i++) {
                System.out.println("What is the grade of class " + (i + 1) + " ?");
                String grade = ask.nextLine();
                if (grade.equals("A")) {
                    total_score += 4;
                }
                if (grade.equals("B")) {
                    total_score += 3;
                }
                if (grade.equals("C")) {
                    total_score += 2;
                }
                if (grade.equals("D")) {
                    total_score += 1;
                }
                if (grade.equals("F")) {
                    total_score += 0;
                }
            }
            double gpa = (total_score / numclasses);
            System.out.println("Your final gpa is " + gpa);
            System.out.println("Would you like to try again?");
            String response = ask.nextLine();
            if (response.equals("yes")) {
                continue;
            } else {
                ask.close();
                break;
            }
        }
    }
}