#include <bits/stdc++.h>
using namespace std;
bool isvowel(char c)
{
	c=tolower(c);
	if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
	{
		return true;
	}
	return false;
}
int main(){
 string s,b,x;
 int i,max=1,k,st,en,sm,se,f=0;
 cin>>s;
 for(i=0;i<s.size();i++)
 {
    if(!(isvowel(s[i])))
    {
        x=x+s[i];
    }
    else
    {
        if(x.size()>=max)
        {
            max=x.size();
            b.clear();
            b=x;
        }
        x.clear();
    }
 }
 if(max==0)
 {
     cout<<"-1";
     exit(1);
 }
 cout<<b;
 return 0;
}
