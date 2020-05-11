#include <stdio.h>
#include <cs50.h>

int main(void)
{
   int n;
   do
   {
       n = get_int("Number 1-8: ");
   }
   while (n <= 0 || n >= 9);
   for (int i= 0; i < n; i++)
   {
       for (int k=1; k < (n-i); k++)  
       {
           printf(" ");
       } 
       for (int j=0; j <= i; j++)
       {
           printf("#");
       } 
       printf("\n");
   } 
}
