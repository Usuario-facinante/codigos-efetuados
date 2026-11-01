#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
void soma(double num1, double num2) {
    printf("Resultado: %.2f + %.2f = %.2f\n", num1, num2, num1 + num2);
}
void subtracao(double num1, double num2) {
    printf("Resultado: %.2f - %.2f = %.2f\n", num1, num2, num1 - num2);
}
void multipli(double num1, double num2) {
    printf("Resultado: %.2f * %.2f = %.2f\n", num1, num2, num1 * num2);
}
void divisao(double num1, double num2) {
    printf("Resultado: %.2f / %.2f = %.2f\n", num1, num2, num1 / num2);
}
void resultado(int operador, double num1, double num2) {
    switch (operador){
        case 1:
            soma(num1, num2);
            break;
        case 2:
            subtracao(num1, num2);
            break;
        case 3:
            multipli(num1, num2);
            break;
        case 4:
            if (num2 != 0) {
                divisao(num1, num2);
            }
            else {
                printf("Erro: Divisão por zero não é permitida.\n");
        break;
        }
    }
}
int main(void) {
    char Jogar_novamente = 's';
    while (tolower(Jogar_novamente) == 's') {
        int operacao, c; 
        double primeiro_numero, segundo_numero;
        printf("===============================\nCalculadora Simples\n===============================\nSelecione uma operação:\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair\nOpção: ");
        while (scanf("%d", &operacao) != 1 || operacao < 1 || operacao > 5 || (c = getchar()) != '\n') {
            while ((c = getchar()) != '\n' && c != EOF) {}
            printf("ERROR!\nSelecione uma das operações disponíveis.\nOpção: ");
        }
        if (operacao == 5) {
            printf("Obrigado por usar a calculadora! Até a próxima.\n");
            return 0;
}
        printf("Digite o primero número: ");
        while(scanf("%lf", &primeiro_numero) != 1) {
                while ((c = getchar()) != '\n' && c != EOF) {}
            printf("Erro: A entrada não foi um número. Digite um número: ");
       };
        printf("Digite o segundo número: ");
        while(scanf("%lf", &segundo_numero) != 1) {
            while ((c = getchar()) != '\n' && c != EOF) {}
            printf("Erro: A entrada não foi um número. Digite um número: ");
       };
        resultado(operacao, primeiro_numero, segundo_numero);
        printf("Deseja realizar outra operação? (s/n): ");
        scanf (" %c", &Jogar_novamente);
        while (tolower(Jogar_novamente) != 'n' && tolower(Jogar_novamente) != 's'){
            printf("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.\n");
            scanf(" %c", &Jogar_novamente);
        }
        if (tolower(Jogar_novamente) == 'n') {
            printf("Obrigado por usar a calculadora! Até a próxima.");
            return 0;
        }
    }
}