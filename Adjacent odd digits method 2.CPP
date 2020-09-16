#include <bits/stdc++.h>
using namespace std;
int main()
{
   string s; int i;
   cin>>s;
   if(s[1]%2!=0)
   {
       cout<<s[0];
   }
	for(i=1;i<s.size()-1;i++)
	{
	    if(s[i+1]%2!=0 && s[i-1]%2!=0)
	    {
		cout<<s[i];
	    }
		}
		if(s[s.size()-2]%2!=0)
		{
		    cout<<s[s.size()-1];
		}
}
