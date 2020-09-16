#include <bits/stdc++.h>
using namespace std;
int main(){
 int n,i,j,k=0;
 string a[1000],b[1000]; double x[1000],y[1000],points[1000];
 double totalpoints[1000]={0.0};
 cin>>n;
 for(i=0;i<n;i++)
 {
     cin>>a[i]>>x[i]>>y[i];
     points[i]=(3-sqrt(x[i]*x[i]+y[i]*y[i]))*100;
     if(points[i]<0)
     {
         points[i]=0;
     }
 }
 for(i=0;i<n;i++)
 {
     if(a[i]!="Dumb")
     {
        b[k]=a[i];
        totalpoints[k]=points[i];
     for(j=i+1;j<n;j++)
     {
        if(a[i]==a[j])
        {
        totalpoints[k]=totalpoints[k]+points[j];
        a[j]="Dumb";
     }
     }
     k++;
 }
}
for(i=0;i<k;i++)
{
    for(j=i+1;j<k;j++)
    {
        if(totalpoints[i]<totalpoints[j])
        {
            double x=totalpoints[i];
            totalpoints[i]=totalpoints[j];
            totalpoints[j]=x;
            string g=b[i];
            b[i]=b[j];
            b[j]=g;
        }
    }
    cout<<b[i]<<" "<<fixed<<setprecision(2)<<totalpoints[i]<<endl;
}
}
