/**
 * 
 * The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
 * Find the sum of all numbers, less than one million, which are palindromic in 
 * base 10 and base 2.
 *
 * The palindromic number, in either base, may not include leading zeros.
 *
 * @author jjanelle
 *
 */
import java.util.*;
public class Problem36 {
	
	public static void main(String[] args)
	{
		ArrayList<Integer> nums = new ArrayList<Integer>();
		for (int i = 1; i < 1000000; i++){
			if (isPalindrome(String.valueOf(i)) && 
				isPalindrome(Integer.toBinaryString(i))) { nums.add(i); }
		}
		
		int sum = 0;
		for (int i = 0; i < nums.size(); i++ )
			sum += nums.get(i);
		System.out.println(sum);
	}
	//Determine whether a given string is a palindome
	public static boolean isPalindrome(String s)
	{
		int len = s.length();
		for (int i = 0; i < len/2; i++){
			if (s.charAt(i)!=s.charAt(len-1-i)) { return false; }
		}
		return true;
	}
	
}
