#include <bits/stdc++.h>
using namespace std;
int a[100][100];
bool issum(int x,int y,int s)
{
    int sum=0,i,j;
    for(i=x;i<x+2;i++)
    {
        for(j=y;j<y+2;j++)
        {
            sum+=a[i][j];
        }
    }
    if(sum==s)
        return true;
    else
        return false;
}
void printmatrix(int x,int y)
{
    for(int i=x;i<x+2;i++)
    {
        for(int j=y;j<y+2;j++)
        {
            cout<<a[i][j]<<" ";
        }
        cout<<endl;
    }
    return;
}
int main(){
 int r,c,i,j,s;
 cin>>r>>c;
 for(i=0;i<r;i++)
 {
     for(j=0;j<c;j++)
     {
         cin>>a[i][j];
     }
 }
 cin>>s;
 for(i=0;i<r;i++)
 {
     for(j=0;j<c;j++)
     {
         if(issum(i,j,s))
         {
            printmatrix(i,j);
            exit(1);
         }
     }
 }
 return 0;
}
