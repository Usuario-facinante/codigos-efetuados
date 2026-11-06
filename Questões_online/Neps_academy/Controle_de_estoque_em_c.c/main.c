#include <stdio.h>
#include <stdlib.h>
int main() {
    int opcao, tamanho = 0;
    char nome_item, *texto = NULL;
    nome_item = malloc(10 * sizeof(char));
    printf("================================\n   Controle de Estoque\n================================\nSelecione uma opção:\n1. Adicionar Item\n2. Remover Item\n3. Listar Estoque\n4. Sair\nOpção:");
    while (scanf("%d", &opcao) != 1 || 1 <= opcao || opcao <= 4) {
        printf("Opção inválida! Tente novamente.\n");
        while (getchar() != '\n');
    }
        FILE *arquivo = fopen("inventory.txt", "w");
    if (opcao == 1) {
        printf("Digite o nome do item: ");
        while ((nome_item = getchar()) != '\n' && nome_item != EOF) {

            char *temp = realloc(texto, (tamanho + 1) * sizeof(char));

            if (temp == NULL) {
                printf("Erro ao alocar memoria!\n");
                free(texto);
                return 1;
            }

            texto = temp;
            texto[tamanho] = nome_item;
            tamanho++;
        }
        char *temp = realloc(texto, (tamanho + 1) * sizeof(char));

        if (temp == NULL) {
            free(texto);
            return 1;
        }

        texto = temp;
        texto[tamanho] = '\0';
        if (arquivo == NULL) {
            printf("Erro ao abrir o arquivo!\n");
            free(texto);
            return 1;
        }
        fputs(nome_item, arquivo);
        fclose(arquivo);
    }
    if (opcao == 2) {
        FILE *arquivo = fopen("inventory.txt", "r");
        if (arquivo == NULL) {
            printf("Erro ao abrir o arquivo!\n");
            return 1;
        }
        f
    }
    return 0;
}