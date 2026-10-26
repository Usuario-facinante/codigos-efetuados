#include <stdio.h>
#include <string.h>
int main(void) {
    char string[50];
    scanf("%49s", &string);
    printf("%zu", strlen(string));
    return 0;
}