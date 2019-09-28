package lecture_1;

import java.util.Scanner;

public class fibonacci_nth_term {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
				Scanner s = new Scanner(System.in);
				int a = s.nextInt();
				int b = s.nextInt();
				int i = 1;
				for(i = 1; i<=a*b; i++){
					if(i%a==0 && i%b==0){
						System.out.println(i);
						break;

					}
				}
			}
		}
