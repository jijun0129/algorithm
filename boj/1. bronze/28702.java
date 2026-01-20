import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str1 = sc.next();
		String str2 = sc.next();
		String str3 = sc.next();
		int ans = 0;
		String ans_str = "";
		
		
		if(Character.isDigit(str1.charAt(0))) {
			ans = Integer.parseInt(str1) + 3;
		} else if (Character.isDigit(str2.charAt(0))){
			ans = Integer.parseInt(str2) + 2;
		} else if (Character.isDigit(str3.charAt(0))){
			ans = Integer.parseInt(str3) + 1;
		}
		
		if(ans % 3 == 0) {
			ans_str += "Fizz";
		}
		if (ans % 5 == 0) {
			ans_str += "Buzz";
		}
		if(ans % 3 != 0 && ans % 5 != 0) {
			ans_str = Integer.toString(ans);
		}
		
		System.out.println(ans_str);
		
		sc.close();
	}
}
