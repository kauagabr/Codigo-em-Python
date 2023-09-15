import os
import PyPDF2


merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("2 Projetos de Automação em Python/Projeto 1/arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"2 Projetos de Automação em Python/Projeto 1/arquivos/{arquivo}")

merger.write("2 Projetos de Automação em Python/Projeto 1/PDF_Final.pdf")