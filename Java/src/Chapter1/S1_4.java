package Chapter1;

import java.util.ArrayList;
import java.util.Scanner;

public class S1_4 {
	public static void s1(String s){
		char[] s_array = new char[200];
		s_array = s.toCharArray();
		
		ArrayList<Character> s_list = new ArrayList<Character>();
		for(char c:s_array){
			s_list.add(c);
		}
		
		for(int i=0;i<s_list.size();i++){
			if(s_list.get(i) == ' '){
				s_list.remove(i);
				s_list.add(i,'%');
				s_list.add(i+1,'2');
				s_list.add(i+2,'0');
				
			}
		}
		StringBuffer newStr = new StringBuffer();
		for(char c:s_list){
			newStr.append(c);
		}
		System.out.println(newStr);
		
	}
	
	public static void main(String[] args){
		Scanner readerScanner =new Scanner(System.in);
		System.out.println("Please input s here:");
		String s = readerScanner.nextLine();
		s1(s);
	}

}
