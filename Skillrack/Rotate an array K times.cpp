#include <bits/stdc++.h>
using namespace std;
int main(){
 vector<int> a;
 int n,i;
 long int k;
  int x;
 cin>>n;
 for(i=0;i<n;i++)
 {
    cin>>x;
    a.push_back(x);
 }
 cin>>k;
 long int v= k%n;
 for(i=n-v;i<n;i++)  //O(n) 
 {
    cout<<a[i]<<" "; 
 }
 for(i=0;i<n-v;i++)
 {
     cout<<a[i]<<" ";
 }
 return 0;
}
