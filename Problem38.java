import java.util.ArrayList;
import java.util.LinkedList;

/**
 * We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
 * for example, the 5-digit number, 15234, is 1 through 5 pandigital. 
 * 
 * Take the number 192 and multiply it by each of 1, 2, and 3:
 *
 *   192 × 1 = 192
 *   192 × 2 = 384
 *   192 × 3 = 576
 *
 * By concatenating each product we get the 1 to 9 pandigital, 192384576. 
 * We will call 192384576 the concatenated product of 192 and (1,2,3)
 *
 * The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
 * giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
 *
 * What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
 *  concatenated product of an integer with (1,2, ... , n) where n > 1?

 * 
 * @author jjanelle
 *
 */
//Answer 932718654
public class Problem38 {

	public static void main(String[] args) {
		//Focus on finding the fixed integer multiple.
		//	Must have fewer than 5 digits
		//	Must start with a 9, have 4 digits, which means n = 2	
		int max = 0;
		for (int i = 9999; i > 9000; i--){
			int val = 100000*i+2*i;
			if (isPandigital(val,9)&& max<val){
				max = val;
			}
		}
		System.out.println(max);
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
}
