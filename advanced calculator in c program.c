#include<stdio.h>
int main{}
{
    int a,b;
    printf("enter values for a and b:");
    scanf("%d %d",&a,&b);
    if(a>b){
        printf("a is larger than b");
    }
    else if(a==b){
        printf("a is equal to b");
    }
    else{
        printf("b is larger than a");
    }
    return 0;
}
