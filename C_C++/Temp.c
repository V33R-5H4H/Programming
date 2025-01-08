//Binary to Decimal Conversion (including float numbers)
#include<stdio.h>
#include<math.h>
void bin_dec_int(int n){
    if (n == 0) {
        printf("0");
        return;
    }
    int dec[32];
    int i;
    for( i=0;i<=32;i++){
        int x=n%10;
        dec[i]=(x)*pow(2,i);
        n=n/10;
    }
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", dec[j]);
    }
}
void bin_dec(float num) {
    int int_part = (int)num;
    float frac_part = num - int_part;
    printf("Decimal : ");
    bin_dec_int(int_part);
    //bin_dec_frac(frac_part);
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