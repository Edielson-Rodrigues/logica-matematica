#include <stdio.h>

int main() {
    int numero1 = 4;  
    int numero2 = 6;  
    int produto = numero1 * numero2;

    if (produto % 2 == 0) {
        printf("O produto de %d e %d é %d, que é um número par.\n", numero1, numero2, produto);
    } else {
        printf("A regra não se aplica. O produto de %d e %d não é um número par.\n", numero1, numero2);
    }

    return 0;
}
