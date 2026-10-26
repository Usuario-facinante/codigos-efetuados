#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void) {
    int i, quantidade = 0;
    char string[50], desejado;
    scanf("%49s", string);
    scanf(" %c", &desejado);
    for (i = 0; string[i] != '\0'; i++) {
        if (string[i] == desejado) {
            quantidade += 1;
        }
    }
    printf("%d", quantidade);
    return 0;
}