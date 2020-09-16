#include <iostream>
#include <cstdio> 
#include <ctime> 
using namespace std;
int main() 
{ 
clock_t start = clock(); 
//Your entire code goes here 
clock_t end = clock(); 
double time = (double) (end-start) / CLOCKS_PER_SEC * 1000.0; 
cout<<time;
}
