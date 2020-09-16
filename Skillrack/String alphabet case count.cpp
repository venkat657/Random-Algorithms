#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s; int pos,i,co=0; char c;
	getline(cin,s);
	cin>>pos;
	cin>>c;
    if(c=='l'||c=='L')
    {
    	c=(char)pos+96;
	}
	else
	{
		c=(char)pos+64;
	}
	for(i=0;i<s.size();i++)
	{
		if(s[i]==c)
		{
			co++;
		}
	}
	if(co==0)
	{
		co=-1;
	}
	cout<<co;
	return 0;
}
