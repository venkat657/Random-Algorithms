#include <bits/stdc++.h>
using namespace std;
int ma=0,k,st,en;
void largestseq(int j,int m,int a[],int n)
{
	int i,k=0,s=j,e;
	for(i=j+1;i<n;i++)
	{
		k++;
		if(a[i]==m)
		{
			e=i;
			break;
		}
	}
	if(k>=ma)
	{
		st=s;
		ma=k;
		en=e;
	}
	return;
}
int main(){
int n,m,i,a[10000],f=0;
 cin>>n>>m;
 for(i=0;i<n;i++)
 {
    cin>>a[i];
 }
 for(i=0;i<n;i++)
 {
 	if(a[i]==m)
 	{
 		largestseq(i,m,a,n);
    }
 }
 for(i=st+1;i<en;i++)
 {
     cout<<a[i]<<" ";
 }
 return 0;
}
