#include<stdio.h>
#include<math.h>
#include<conio.h>
int main()
{
    float p,r,t,si,ci;
    printf("Enter principle:");
    scanf("%f",&p);
    printf("\nEnter rate:");
    scanf("%f",&r);
    printf("\nEnter time:");
    scanf("%f",&t);
    si=(p*r*t)/100;
    ci=(p*(pow(1+r/100,t))-1);
    printf("\nThe simple interest is %.3f and compound interest is %.3f",si,ci);
    return 0;
}
