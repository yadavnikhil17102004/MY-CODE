#include<stdio.h>
int main(){
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    int c = a*b;
    printf("Area of Square is :%d", c);
    return 0;
}