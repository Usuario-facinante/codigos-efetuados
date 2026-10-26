    #include <stdio.h>
    #include <string.h>
    int main(void) {
        char string[50];
        int i;
        scanf ("%50s", string);
        printf("Vogais:");
        for (i = 0; strlen(string) >= i; i++) {
            if (string[i] == 'a' || string[i] == 'e' || string[i] == 'i' || string[i] == 'o' || string[i] == 'u') {
                printf("%c", string[i]);
            }
        }
        printf("\nConsoantes:");
        for (i = 0; strlen(string) >= i; i++) {
            if (string[i] != 'a' && string[i] != 'e' && string[i] != 'i' && string[i] != 'o' && string[i] != 'u') {
                printf("%c", string[i]);
            }
        }
        return 0;
    }