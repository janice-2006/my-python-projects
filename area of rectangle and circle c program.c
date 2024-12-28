#include<stdio.h>
int main()
{
    float r,l,b,area_of_circle,area_of_rectangle;
    printf("Enter the radius:");
    scanf("%f",&r);
    printf("\nEnter the length and breadth:");
    scanf("\n%f %f",&l,&b);
    area_of_circle=3.14*r*r;
    area_of_rectangle=l*b;
    printf("\nThe area of circle is %.2f  and area of the rectangle is %.2f",area_of_circle,area_of_rectangle);
    return 0;
}
