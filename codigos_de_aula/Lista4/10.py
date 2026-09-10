'''Implemente um algoritmo que informe se um nome existe ou não em uma lista de nomes. Crie uma
lista com pelo menos 20 nomes e use while / break.'''
Nomes, Count = ["gabriel", "miguel", "arthur", "heitor", "bernardo", "davi", "lucas", "theo", "samuel", "benjamin", "noah", "rafael", "joão", "pedro", "isaac", "nicolas", "matheus", "lorenzo", "henrique", "guilherme", "sophia", "alice", "helena", "laura", "valentina", "isabella", "manuela", "heloísa", "júlia", "cecília", "aurora", "maitê", "lívia", "beatriz", "lorena", "clara", "elisa", "yasmin", "bianca", "rebeca", "luna", "maya", "antonella", "esther", "sarah", "marina", "olívia", "vitória", "camila", "isadora"], 0
Nome_desejado = input("Diga-me o nome que deseja e eu direi se este nome esta na lista criada.\n").lower()
while True:
    if Count == Nomes.index(Nome_desejado):
        break
    Count +=1
print (f"O nome desejado está na lista no numero {(Count)+1}")