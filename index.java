import java.util.Scanner;

public class index{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int i =0;
        
        while(i<number){
            System.out.print(i + 2);
            int j=i;
            while (j < i + i) {
                System.out.print(j+3);
                j++;
            }
            System.out.println();
            i++;
        }
    }
}