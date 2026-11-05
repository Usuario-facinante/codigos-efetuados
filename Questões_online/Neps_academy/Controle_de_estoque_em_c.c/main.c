#include <stdio.h>
#include <stdlib.h>
int main() {
    int opcao;
    char *nome_item;
    nome_item = malloc(10 * sizeof(char));
    printf("================================\n   Controle de Estoque\n================================\nSelecione uma opção:\n1. Adicionar Item\n2. Remover Item\n3. Listar Estoque\n4. Sair\nOpção:");
    while (scanf("%d", &opcao) != 1 || 1 <= opcao || opcao <= 4) {
        printf("Opção inválida! Tente novamente.\n");
        while (getchar() != '\n');
    }
    printf("Digite o nome do item: ");

    return 0;
}