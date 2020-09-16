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
public class Skip_twoODD_oneEven_reverse_traverse {
    public static void main(String[] args) {
       int i,a[]=new int[10000],n;
        Scanner s=new Scanner(System.in);
        n=s.nextInt();
        for(i=0;i<n;i++)
        {
          a[i]=s.nextInt();
        }
        for(i=n-1;i>=0;)
        {
            if(a[i]%2==0)
            {
                System.out.print(a[i]+" ");
                i-=2;
            }
            else if(a[i]%2!=0)
            {
                System.out.print(a[i]+" ");
                i-=3;
            }
        }
	}
}
