package Chapter1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;


public class S1_3 {
	
	public static boolean s1(String s1,String s2){//时间复杂度为O(n*log(n))
		char ch1[] = s1.toCharArray();
		char ch2[] = s2.toCharArray();
		Arrays.sort(ch1);
		Arrays.sort(ch2);
		if (Arrays.equals(ch1, ch2)){
			return true;
		}
		else {
			return false;
		}
		
	}
	
	public static boolean s2(String s1,String s2){//时间复杂度为O(n)
		int[] s1_array = new int[256];
		int[] s2_array = new int[256];
		for(int i=0;i<s1.length();i++){
			int num = s1.charAt(i);
			s1_array[num] +=1;
		}
		for(int i=0;i<s2.length();i++){
			int num = s2.charAt(i);
			s2_array[num] +=1;
		}
		if(Arrays.equals(s1_array, s2_array)) return true;
		else return false;
		
	}
	
	
	//此方法比s2的优势在于空间复杂度更低，但是需要特别注意的是，
	//必须保证s1,s2长度相等的情况下本程序的后半部分才能正常工作。想想为什么？
	public static boolean s2_better(String s1,String s2){
		if(s1.length()!=s2.length()) return false;//这句话最好是在每个程序都加上，因为会提升效率
		int[] s1_array = new int[256];
		for(int i=0;i<s1.length();i++){
			int num = s1.charAt(i);
			s1_array[num]++;
		}
		for(int i=0;i<s2.length();i++){
			int num = s2.charAt(i);
			if((s1_array[num]--)==0){
				return false;
			}		
		}
		return true;
	}
	
	public static boolean s3(String s1,String s2){//时间复杂度为O(n)
		Map<Character,Integer> s1_map = new HashMap<Character,Integer>();
		Map<Character,Integer> s2_map = new HashMap<Character,Integer>();
		for(int i=0;i<s1.length();i++){
			char c = s1.charAt(i);
			if(s1_map.containsKey(c)){
				s1_map.put(c,s1_map.get(c)+1);
			}
			else{
				s1_map.put(c, 1);
			}	
		}
		
		for(int i=0;i<s2.length();i++){
			char c = s2.charAt(i);
			if(s2_map.containsKey(c)){
				s2_map.put(c,s2_map.get(c)+1);
			}
			else{
				s2_map.put(c, 1);
			}
		}
		
		if(s1_map.equals(s2_map)){
			return true;
		}
		else{
			return false;
		}
	}

	public static boolean s4(String s1,String s2){//时间复杂度为O(n^2)
		char[] ch1 = s1.toCharArray();
		char[] ch2 = s2.toCharArray();
		
		ArrayList<Character> ch2_list = new ArrayList<Character>();
		for(char c:ch2){
			ch2_list.add(c);
		}

		for(char i:ch1){
			int id = ch2_list.indexOf(i);//主要是这里也需要O(n)的查询
			if(id>-1){
				ch2_list.remove(id);
			}
			else return false;
		}
		return true;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner reader = new Scanner(System.in);
		System.out.println("Please input s1:");
		System.out.println("Please input s2:");
		String s1 = reader.nextLine();
		String s2 = reader.nextLine();
		boolean result = s2_better(s1,s2);
		System.out.println(result);
	}

}
