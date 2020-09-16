#include<bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cin>>n;
  int a[n],i,j,b[n]={0},count=0;
  char l;
  for(i=0;i<n;i++)
  {
    cin>>a[i];
    if(i!=n-1)
    {
      cin>>l;
    }
    while(a[i]>0)
    {
      int x=a[i]%6;
      b[i]+=x;
      a[i]=a[i]/6;
    }
  }
  for(i=0;i<n;i++)
  {
    for(j=i+1;j<n;j++)
    {
      if(b[i]>b[j])
      {
        count++;
      }
    }
  }
  cout<<count;
  return 0;
}
    
