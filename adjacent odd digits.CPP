#include <iostream>
using namespace std;
int main(){
 long int n[1000000],i,x,k=0;;
 cin>>x;
 while(x>0)
 {
    n[k]=x%10;
    x=x/10;
    k++;
 }
 for(i=k-1;i>=0;i--)
 {
    if(i==0||i==k-1)
    {
        if(n[i+1]&1 && i==0)
        {
            cout<<n[i];
        }
        else if(n[i-1]&1 && i==k-1)
        {
            cout<<n[i];
        }
    }
    else if(n[i+1]&1 && n[i-1]&1)
    {
        cout<<n[i];
    }
 }
 return 0;
}
