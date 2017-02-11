/**
 * It was proposed by Christian Goldbach that every odd composite number can be
 * written as the sum of a prime and twice a square.
 * 
 * 9 = 7 + 2×1^2 
 * 15 = 7 + 2×2^2 
 * 21 = 3 + 2×3^2 
 * 25 = 7 + 2×3^2 
 * 27 = 19 + 2×2^2 
 * 33 = 31 + 2×1^2
 * 
 * It turns out that the conjecture was false.
 * 
 * What is the smallest odd composite that cannot be written as the sum of a
 * prime and twice a square?
 * 
 * @author jjanelle
 *
 */
public class Problem46 {

	public static void main(String[] args) {
		boolean[] isPrime = sieveEras(10000000);
		
		
		boolean notFound = true;
		int current = 2;
		while(notFound){
			current++;
			if (current%2==1 && isPrime[current]==false){ //if current number is odd and composite
				if (goldbachWorks(current,isPrime)==false){
					System.out.println(current);
					notFound = false;
				}
			}
		}
		
		
 		//for (int i = 2; i <= 100; i++) System.out.println("i = "+i + "\tPrime: "+isPrime[i]);
	}

	public static boolean goldbachWorks(int n, boolean[] isPrime)
	{
		double square;
		for (int i = 3; i < n; i++){
			if (isPrime[i]==false) continue; //skip non-primes
			square = Math.sqrt((n-i)/2);
			if (square == (int)square) return true;
		}
		return false;
	}
	
	/**
	 * Semi-optimized Sieve of Erastosthenes. Creates a boolean
	 * array in which true means index is prime, false means that 
	 * index is composite.
	 * @param limit Upper bound of prime number list
	 * @return A prime number boolean array 
	 */
	public static boolean[] sieveEras(int limit)
	{
		boolean[] isPrime = new boolean[limit+1]; //+1 so indices match integers
		for (int i = 0; i < isPrime.length; i++) isPrime[i] = true; //Assume all prime to start
		isPrime[0]=false;
		isPrime[1]=false;

		int ub = (int)(Math.sqrt(limit)+1);
		//Sieve of Eratosthenes
		for (int i = 2; i <= ub; i++) {
			if (isPrime[i]){ //if a prime number is next
				//mark multiples of i as non-prime
				for (int j = i; i*j <= limit; j++) {
					isPrime[i*j] = false;
				}
			}
		}
		return isPrime;		
	}
}
