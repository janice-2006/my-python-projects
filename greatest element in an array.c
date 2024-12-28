#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,n,arr[100];
    printf("Enter the number of elements:");
    scanf("%d",&n);
    for(i=0;i<n;i++){
        printf("\nEnter element:",i+1);
        scanf("%d",&arr[i]);
    }
    for(i=1;i<n;i++){
        if(arr[0]<arr[i]){
            arr[0]=arr[i];
        }
    }
    printf("\nThe array is %d",arr[100]);
    printf("\nThe largest element in the array is %d",arr[0]);
    return 0;

}


