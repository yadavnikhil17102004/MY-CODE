#include<stdio.h>

int main(){
    int r, a;
    printf("Enter a value for radius :");
    scanf("%d", &r);
    float area = 3.14 * r * r;
    printf("Area :%f", area);
    return 0;
}