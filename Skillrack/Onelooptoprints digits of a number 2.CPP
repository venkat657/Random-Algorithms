#include <bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	cin>>s;
	for(int i=0;i<s.size();i++)
	{
		int x=s[i] - '0'; x=x*2;
		cout<<x;
	}
	
	return 0;
}
