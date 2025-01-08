// Binary to Decimal Conversion (including float numbers)
#include <stdio.h>
#include <math.h>

int bin_dec_int(int n) {
    int decimal = 0;
    int base = 1;
    while (n > 0) {
        int last_digit = n % 10;
        decimal += last_digit * base;
        base *= 2;
        n /= 10;
    }
    return decimal;
}

float bin_dec_frac(float frac) {
    float decimal = 0.0;
    float base = 0.5;
    while (frac > 0.0) {
        frac *= 10;
        int digit = (int)frac;
        decimal += digit * base;
        base /= 2;
        frac -= digit;
    }
    return decimal;
}

void bin_dec(float num) {
    int int_part = (int)num;
    float frac_part = num - int_part;
    
    int int_decimal = bin_dec_int(int_part);
    float frac_decimal = bin_dec_frac(frac_part);
    
    printf("Decimal: %d", int_decimal);
    if (frac_part > 0.0) {
        printf(".%f", frac_decimal);
    }
    printf("\n");
}

int main() {
    while (1) {
        float a;
        printf("Enter a Binary Number: ");
        scanf("%f", &a);
        bin_dec(a);
    }
    return 0;
}