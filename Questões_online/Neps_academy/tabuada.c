#include <stdio.h>
int main (){
    int numero;
    int i;
    scanf("%d", &numero);
    for (i = 1; i < 11; i++) {
        printf("%d * %d = %d\n", numero, i, numero * i);
    }
    return 0;
}