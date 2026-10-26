#include <stdio.h>
int main(void) {
    int valores[10] = {0}; i;
    for (i = 0; i < 10; i++) {
        scanf("%d", &valores[i]);
    }
    for (i = 9; i != 0; i--) {
        printf("%d", valores[i]);
    }
    return 0;
}