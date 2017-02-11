import java.util.*;

public class Problem35 {

	public static void main(String[] args)
	{
		boolean[] isNotPrime= sieveEras(1000000); 
		int count = 2; //include 2 and 5, which are ignored by algorithm
		for (int i = 2; i < isNotPrime.length; i++)
		{
			if (isNotPrime[i]==false && hasEvenOrFive(i)==false){
				if (isCircularPrime(i,isNotPrime))
					count++;
			}
		}
		System.out.println(count);
	}

	//Return true if any of the digits of a number are even or 5
	public static boolean hasEvenOrFive(int n)
	{
		while (n > 0){
			if (n%10%2==0 || n%10%5==0) return true;
			n /= 10;
		}
		return false;
	}
	
	//Rotate an integer by shifting all of its digits
	//one place to the left
	public static int rotate(int n){
		String s = String.valueOf(n);
		if (s.length() > 1){ 
			s = s.substring(1)+s.charAt(0);
		}
		return Integer.parseInt(s);
	}

	//Return true if a number is a circular prime, false
	//otherwise
	public static boolean isCircularPrime(int n, boolean[] notPrime)
	{
		int temp = n;
		do {
			temp = rotate(temp);
			if (notPrime[temp]==true) {
				return false;
			}
		} while (temp != n);

		return true;
	}

	//Construct a boolean array whose indices correspond
	//to integers. Array contains true if number is not prime,
	//false if number is prime
	public static boolean[] sieveEras(int limit)
	{
		//Entries that contain a true are not prime.
		boolean[] isNotPrime = new boolean[limit+1]; //+1 so indices match integers
		isNotPrime[0]=true;
		isNotPrime[1] = true;

		//Sieve of Eratosthenes
		for (int i = 2; i*i <= limit; i++) {
			if (isNotPrime[i]==false){ //if a prime number is next
				//mark multiples of i as non-prime
				for (int j = i; i*j <= limit; j++) {
					isNotPrime[i*j] = true;
				}
			}
		}
		return isNotPrime;		
	}

	//Determine whether an integer is prime
	public static boolean isPrime(int n)
	{
		for (int i = 2; i <= (int)(Math.sqrt(n)+1); i++){
			if (n%i==0) return false;
		}
		return true;
	}
	/*
	 * NOTE
	 * If a number n is not a prime, 
	 * it can be factored into two factors a and b:
	 * n = a*b
	 * 
	 * If both a and b were greater than the square root of n,
	 * a*b would be greater than n. So at least one of those 
	 * factors must be less or equal to the square root of n, 
	 * and to check if n is prime, we only need to test for 
	 * factors less than or equal to the square root.
	 */
}
