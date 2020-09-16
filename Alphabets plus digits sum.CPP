#include <bits/stdc++.h>
using namespace std;
int main(){
 string s,b;
 int s1=0,i; char d;
 cin>>s;
 for(i=0;i<s.size();i++)
 {
     if(isdigit(s[i]))
     {
         s1+=(int)(s[i])-48;
         if(s1>26)
         {
             s1=s1-26;
         }
     }
     else if(isalpha(s[i]))
     {
         d=s[i];
         if(isupper(s[i]))
         {
         d=tolower(s[i]);
         }
         b+=d;
     }
 }
 for(i=0;i<b.size();i++)
 {
    if(b[i]+s1<='z')
    {
        char x=b[i]+s1;
        cout<<x;
    }
    else
    {
        char x=b[i]+s1-26;
        cout<<x;
    }
 }
 return 0;
}
