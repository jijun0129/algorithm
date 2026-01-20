import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String ISBN = sc.next();
		
		int sum = 0;
		int star = -1;
		for(int i =0; i < 13; i++) {
			if(ISBN.charAt(i) != '*') {
				sum += i % 2 == 0 ? (ISBN.charAt(i) - '0') : (ISBN.charAt(i) - '0') * 3;
			} else {
				star = i;
			}
		}
	 	
		int answer = (10 - (sum % 10)) % 10;
		if(star % 2 == 1) {
			while(answer % 3 != 0) {
				answer += 10  ;
			}
			answer = answer / 3;
		}
		System.out.println(answer);
		
		sc.close();
	}
}
