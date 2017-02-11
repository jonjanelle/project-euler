import java.util.LinkedList;

/**
 * 
 * We shall say that an n-digit number is pandigital
 * if it makes use of all the digits 1 to n exactly once. 
 * For example, 2143 is a 4-digit pandigital and is also prime.
 * 
 * What is the largest n-digit pandigital prime that exists?
 * 
 * @author jjanelle
 *
 */
public class Problem41 {

	public static void main(String[] args) 
	{
		for (int i = 7; i >= 4; i--){ 
			int lb = (int)Math.pow(10,i-1);
			for (int j = 10*lb-1; j > lb; j--){
				if (j%2==0||j%5==0) continue;
				if (isPrime(j)&&isPandigital(j,i)){
					System.out.println(j);
					System.exit(0);
				}
			}
		}
	}

	//Determine whether a given integer is 1 to n pandigital
	public static boolean isPandigital(int number, int n)
	{
		LinkedList<Integer> digits = new LinkedList<Integer>();
		for (int i = 1; i <=n; i++){ digits.add(i); }
		while (number > 0){
			Integer d = new Integer(number%10);
			if (!digits.remove(d)) return false;
			number/=10;
		}
		return true;
	}

	//Determine whether an integer is prime
	public static boolean isPrime(int n)
	{
		for (int i = 2; i <= (int)(Math.sqrt(n)+1); i++){
			if (n%i==0) return false;
		}
		return true;
	}
}
