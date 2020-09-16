#include<stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
char a[10000]; int i,x,f=0;
scanf("%[^\n]%*c",a);
scanf("%d",&x);
for(i=0;i<strlen(a);i++)
{
    printf("%c",a[i]);
    if((i+1)%x==0)
    {
        i=i+x;
    }
}
}
