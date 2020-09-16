#include <bits/stdc++.h>
using namespace std;
int main(){
int n,m,i,a[10000],st,end,s,e,f=0,k=0,max=0;
 cin>>n>>m;
 for(i=0;i<n;i++)
 {
    cin>>a[i];
    if(a[i]==m)
    {
      if(f==0)
      {
          st=i;
          f=1;
      }
      else
      {
          f=0;
          end=i;
          if(k>=max)
          {
              max=k;
              k=0;
              s=st;
              e=end;
          }
        st=i;
        f=1;
      }
    }
    if(f==1)
    {
        k++;
    }
 }
 for(i=s+1;i<e;i++)
 {
     cout<<a[i]<<" ";
 }
 return 0;
}
