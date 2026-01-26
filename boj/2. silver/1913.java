import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int number = sc.nextInt();
		int[][] arr = new int[n][n];
		int[] di = {0, -1, 0, 1};
		int[] dj = {-1, 0, 1, 0};
		int ni = n/2, nj = n/2;
		int index = 0;
		int ri = 0, rj = 0;
			
		for(int i = 1; i <= n*n; i++) {
			if(number == i) {
				ri = ni + 1;
				rj = nj + 1;
			}
			arr[ni][nj] = i;
			if(0 <= ni + di[(index+1) % 4] && ni + di[(index+1) % 4] < n &&
					0 <= nj + dj[(index+1) % 4] && nj + dj[(index+1) % 4] < n &&
					arr[ni + di[(index+1) % 4]][nj + dj[(index+1) % 4]] != 0) {
				ni = ni + di[index];
				nj = nj + dj[index];
			} else {
				index += 1;
				if(index == 4) {
					index = 0;
				}
				ni = ni + di[index];
				nj = nj + dj[index];
			}
		}

		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				System.out.print(arr[i][j] + " ");
			}
		System.out.println("");
		}
		System.out.println(ri + " " + rj);
		
		sc.close();
	}
}
