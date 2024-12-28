#include<stdio.h>
#include<math.h>
#include<conio.h>
int main()
{
   int op,a,b;
   printf("Enter values for a and b:");
   scanf("%d %d",&a,&b);
   printf("Select operator[+,-,*,/]":);
   scanf("%c",&op);
   if(op=='+'){
    printf(a+b);
   }
   else if(op=='-'){
    printf(a-b);
   }
   else if(op=='*'){
    printf(a*b);
   }
   else if(op=='/'){
    printf(a/b);
   }
   else{
    printf("Invalid operator");
   }
    return 0;
}
