#include <bits/stdc++.h>
using namespace std;
int main(){
 int n,i,count=0;
 string s[1000];
 cin>>n;
 for(i=0;i<n;i++)
 {
     cin>>s[i];
 }
 bool original[26];
 memset(original,true,26); //copies the value true or sets all the elements in the array original to 'true' in the memory
 for(i=0;i<n;i++)
 {
     bool duplicate[26]={false};
    for(int j=0;j<s[i].size();j++)
    {
        if(original[s[i][j] - 'a']) //checks if the character has already been encountered in previous strings
        {
            duplicate[s[i][j] - 'a']=true; //marks true for the occurrence of that character in this string too
        }
    }
    memcpy(original,duplicate,26); // copies all the values of duplicate array to original array,irrespective of changing values -
 }                                 //- the values of common repeating characters will be retained.
 for(i=0;i<26;i++)
 {
     if(original[i])
     {
         count++;      //for whatever char positions the value is true, count is incremented as it is understood that the truth values are placed in their alphabet positions
     }
 }
 cout<<count;
 return 0;
}
