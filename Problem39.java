import java.util.HashSet;
import java.util.Set;

/**
 * If p is the perimeter of a right angle triangle with 
 * integral length sides, {a,b,c}, there are exactly three
 * solutions for p = 120.
 * {20,48,52}, {24,45,51}, {30,40,50}
 * 
 * For which value of p <= 1000, is the number of solutions maximized?
 * 
 * @author jjanelle  
 */
public class Problem39 {

public static void main(String[] args) {
	int maxCount = 0;
	int maxI = 0;
	for (int i = 1000; i>= 12; i--){ //i is perimeter
		int count = 0;
		Integer[] factors = getFactorList(i);//don't need to consider repeated factors, right integer triangle cannot be isosceles
		//System.out.println(Arrays.toString(factors));
		if (factors.length>1){
			for (int j = 0; j<factors.length; j++){ //j holds index of next factor
				for (int k = factors[j]+1; k < i; k++){
					int s1 = factors[j];
					int s3 = i-k-factors[j];
					if (s1+k+s3==i && s1*s1+k*k==s3*s3 ){
						count+=1;
					}
				}
			}
		}
		if (count > maxCount){
			maxCount = count;
			maxI = i;
		}
	}
	System.out.println(maxI);
}

//Get a list of all factors of an integer n
public static Integer[] getFactorList(int n)
{
	Set<Integer> factors = new HashSet<Integer>();
	for (int i = 2; i <= (int)(Math.sqrt(n)+1); i++){
		if (n%i==0){
			factors.add(i);
			factors.add(n/i);
		}
	}
	factors.add(1);
	return factors.toArray(new Integer[0]);
}
}
