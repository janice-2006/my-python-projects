#include <stdio.h>
#include <stdlib.h>

int main()
{
   int i,t,n;
   printf("Enter number of terms:");
   scanf("%d",&n);
   int t1=0, t2=1;
   int nextterm=t1+t2;
   printf("%d %d",t1,t2);
   for(i=3;i<=n;i++){
    printf("%d",nextterm);
    t1=t2;
    t2=nextterm;
    nextterm=t1+t2;
   printf(" ");
   }
   return 0;
}
