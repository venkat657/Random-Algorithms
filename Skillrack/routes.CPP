#include<bits/stdc++.h>
using namespace std;
int traverse(int a[][100],int n,int r,int c,int w)
{
if(r==n-1 && c==n-1)
{
if(a[r][c]>w)
{
w=a[r][c];
}
return w;
}
if(r==n-1 && c!=n-1)
{
	 w=a[r][c+1]>w?a[r][c+1]:w;
return traverse(a,n,r,c+1,w);
}
if(r!=n-1 && c==n-1)
{
	w=a[r+1][c]>w?a[r+1][c]:w;
return traverse(a,n,r+1,c,w);
}
if(a[r][c+1]<a[r+1][c])
{
  w=a[r][c+1]>w?a[r][c+1]:w;
return traverse(a,n,r,c+1,w);
}
else if(a[r+1][c]<a[r][c+1] && r!=n-1)
{
w=a[r+1][c]>w?a[r+1][c]:w;
return traverse(a,n,r+1,c,w);
}
}
int main()
{
int n,i,j,a[100][100],w;
cin>>n;
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
cin>>a[i][j];
}
}
i=0; j=0;
w=traverse(a,n,i,j,1);
cout<<w; 
return 0;
}
