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
public class AdjacentAlphabetpairs {

    public static void main(String[] args) {
	 String a; int i,m=0;
	 Scanner s=new Scanner(System.in);
     a=s.next();
     for(i=0;i<a.length()-1;i++)
     {
        if(a.charAt(i+1)-a.charAt(i)==1)
        {
            m++;
        }
     }
     System.out.print(m);
	}
}
