package firstlabs;

import java.util.Scanner;

public class wordcount {
    public static void main(String[]arg){
        Scanner in = new Scanner(System.in);
        System.out.println("Enter a sentence: ");
        String sentence = in.nextLine();
        System.out.println("Number of words: " + wordCount(sentence));

    }
    static int wordCount(String sentence){
        return sentence.split(" ").length;
    }
}
