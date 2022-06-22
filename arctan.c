#include <stdio.h>
#include <cs50.h> //for user's input.
#include <math.h> //for `pow()` function.

int main(void)
{
    double x = get_double("Arctan: ");
    double answer = 0;

    // Check if |x| <= 1
    if (x <= 1 && x >= -1)
    {
        for (int n = 0; n < 9999; n++)
        {
            int power = (2 * n) + 1;
            int denominator = power;
            double negative_one = pow(-1, n);
            double numerator = pow(x, power) * negative_one;

            double function = numerator / denominator;
            answer += function;
        }
    }
    
    //If |x| >=1
    else
    {
        printf("ERROR\nThere is an error when solving arctan for values that are not in the interval [-1,1]\n");
        return 1;
    }

    printf(" = %.4f rad \n", answer);
    return 0;
}

// There is an error when dealing with x > 1, or x < -1.
// By searching, I found that the error is becaue arctan(x) in Taylor's series is true when |x| <= 1. <<needs more searching.
