#include <bits/stdc++.h>
using namespace std;
int main()
{
   int x,k=0,a[1000]={0},i,j,n;
   cin>>n; j=log10(n)+1; j=pow(10,j-1);
	while(j>=1)
	{
		a[k]=n/j;
		n%=j;
		j/=10;
		a[k]+=2;
		if(a[k]>=10)
		{
		    if(a[k]==11)
		    {
		        a[k]=1;
		    }
		    else
		    {
		        a[k]=0;
		    }
		}
		cout<<a[k];
		k++;
		}
}
