package Chapter1;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.Arrays;

/*下面的s5必须好好研究，为什么在负数的时候依然可以实现*/

public class S1_1 {
	
	public static boolean s1(String s){
		for(int i=0;i<s.length();i++){
			for (int j=i+1;j<s.length();j++){
				if (s.charAt(i)==s.charAt(j)){
					return false;
				}
			}
		}
		return true;
		
		
	}
	
	public static boolean s2(String s){
		Set<Character> stringSet = new HashSet<Character>();
		for(int i=0;i<s.length();i++){
			stringSet.add(s.charAt(i));
		}
		
		if (stringSet.size() != s.length()){
			return false;
		}
		else
			return true;
		
	}
	
	public static boolean s3(String s){
		char ch[] = s.toCharArray();
		Arrays.sort(ch);
		//s = ch.toString();
		for(int i=0;i<ch.length-1;i++){
			if (ch[i]==ch[i+1]){
				return false;
			}
		}
		return true;
	}
	
	public static boolean s4(String s){
		if (s.length()>256) return false;       //ascii字符最大为256
		boolean checker[] = new boolean[256];
		//boolean[] checker = new boolean[256];  //这样也行
		for(int i=0;i<s.length();i++){
			int num = s.charAt(i);
			if(checker[num]) return false;
			checker[num] = true;
		}
		return true;
		
	}
	
	public static boolean s5(String s){ //这里为负数的时候居然也可以，得仔细研究研究
		int checker = 0;
		for(int i=0;i<s.length();i++){
			int num = s.charAt(i);
			System.out.printf("%d,",num);
			num -=97;
			System.out.printf("%d	",num);
			if((checker &(1<<num))>0){
				return false;
			}
			checker |=(1<<num);
		
		}
		System.out.println(Integer.toBinaryString(checker));
		return true;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner reader = new Scanner(System.in);
		System.out.println("Please input s:");
		for(int i=0;i<5;i++){
			System.out.printf("This is the %dth time.Please input s:",i);
			String s = reader.next();
			boolean result = s5(s);
			System.out.println(result);
		}

	}

}
