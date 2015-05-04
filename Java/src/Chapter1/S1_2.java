package Chapter1;

import java.util.Scanner;

public class S1_2 {
	public static String s1(String s){
		String newString = "";
		for (int i=s.length()-1;i>=0;i--){
			newString +=s.charAt(i);
		}
		return newString;
	}
	
	public static String s2(String s){
		char ch[] = new char[s.length()];
		if (s.length()%2==1){
			int medium = (s.length()-1)/2;
			for(int i=1;i<=medium;i++){
				ch[medium+i] = s.charAt(medium-i);
				ch[medium-i] = s.charAt(medium+i);
				ch[medium]   = s.charAt(medium);
			}
			System.out.println(ch);
			return String.valueOf(ch);
			//return ch.toString();
		}
		else{
			int medium = s.length()/2;
			for (int i=1;i<=medium;i++){
				ch[medium+i-1] = s.charAt(medium-i);
				ch[medium-i] = s.charAt(medium+i-1);
			}
			System.out.println(ch);
			return String.valueOf(ch);
			//return ch.toString();
		}
	}
	
	public static String s3(String s){//利用迭代的方法求解，但是明显此方法并不优，尤其空间复杂度非常高。
		if(s.length()==0){
			return "";
		}
		return s.charAt(s.length()-1)+s3(s.substring(0,s.length()-1));
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner readerScanner = new Scanner(System.in);
		System.out.println("Please input s:");
		String s = readerScanner.nextLine();
		//System.out.printf(s);
		s = s3(s);
		System.out.println(s);

	}

}
