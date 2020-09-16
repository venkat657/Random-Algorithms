#include <bits/stdc++.h>
using namespace std;
int main(){
 string s; int i;
 cin>>s;
 for(i=0;i<s.size();i++)
 {
    if(s[i]==s[i-1] && s[i]!=s[i+1])
    {
        s[i]=toupper(s[i]);
    }
 }
 cout<<s;
 return 0;
}
