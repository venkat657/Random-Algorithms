#include <bits/stdc++.h>
using namespace std;
string a,b,c;
void check(string a1,string b1,string c1)
{
    int i,j;
        for(i=0;i<a1.size()-1;i++)
        {
            if(b1[i]==a1[0] && c1[i]==a1[a1.size()-1])
            {
                a=a1;
                b=b1;
                c=c1;
                return;
            }
            else if(b1[i]==a1[a1.size()-1] && c1[i]==a1[0])
            {
                a=a1;
                b=c1;
                c=b1;
                return;
            }
        }
}
int main()
{
string s1,s2,s3;
int i,j;
cin>>s1>>s2>>s3;
check(s1,s2,s3);
check(s2,s1,s3);
check(s3,s1,s2);
for(i=0;i<a.size();i++)
{
    for(j=0;j<a.size();j++)
    {
        if(j==0)
        {
            cout<<b[i];
        }
        else if(j==a.size()-1)
        {
            cout<<c[i];
        }
        else if(b[i]==a[0] && c[i]==a[a.size()-1])
        {
            cout<<a[j];
        }
        else
        {
            cout<<"+";
        }
    }
    cout<<endl;
}
return 0;
}
