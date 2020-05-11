#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main (void)
{
    int x;
    do
    {
        float y = get_float("Change: ");
        x = round(y*100);
    }
   while (x <= 0);
    
   int dv = x / 25;
   int d = (x % 25)/10;
   int p = ((x % 25)%10)/5;
   int o = (((x % 25)%10)%5)/1;    
   printf("%d\n", dv + d + p + o);
}
