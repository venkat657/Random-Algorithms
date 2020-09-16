#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,x,a[1000],k=0,i;
	cin>>n;
	while(n>0)
	{
		a[k]=n%10;
		n/=10;
		k++;
	}
	for(i=k-1;i>=0;i--)
	{
		cout<<a[i];
	}
	return 0;
}
