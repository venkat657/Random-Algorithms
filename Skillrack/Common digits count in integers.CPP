#include <bits/stdc++.h>
using namespace std;
int main(){
 long int a[100000],n,i,j;
 int c=0,b[10]={0};
 cin>>n;
 for(i=0;i<n;i++)
 {
     cin>>a[i];
     int f[10]={0};
    while(a[i]>0)
    {
        int x=a[i]%10;
        a[i]=a[i]/10;
        if(f[x]==0)
        {
            f[x]=1;
            b[x]=b[x]+1;
        }
    }
 }
 for(i=0;i<10;i++)
 {
  if(b[i]==n)
  {
      c++;
  }
 }
 cout<<c;
 return 0;
}
