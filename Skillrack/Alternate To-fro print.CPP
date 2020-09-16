#include <bits/stdc++.h>
using namespace std;
void print(int x,int y,int i)
{
    int m=y,l=-1;
    if(i&1)
    {
       m=x;l=1;
    }
    for(int j=0;j<=abs(x-y);j++)
    {
        cout<<m<<" ";
        m+=l;
    }
}
int main(){
 int n,a[1000],i;
 cin>>n; cin>>a[0];
 for(i=1;i<n;i++)
 {
    cin>>a[i];
    print(a[i-1],a[i],i);
 }
 return 0;
}
