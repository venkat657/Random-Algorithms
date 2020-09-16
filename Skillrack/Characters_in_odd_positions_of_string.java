/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author ramana
 */
 import java.util.*;
public class Characters_in_odd_positions_of_string {
   

    public static void main(String[] args) {
		String a; char b; int i,c=0;
		Scanner s=new Scanner(System.in);
		a=s.next();
		b=s.next().charAt(0);
		for(i=0;i<a.length();i++)
		{
		    if(a.charAt(i)==b && (i+1)%2!=0)
		    {
		        c++;
		    }
		}
		System.out.print(c);
	}
}
