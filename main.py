import fsfunc
import sys
import numpy as np
from VCF import VCF
import time


def main():
    # Verifica si se ha proporcionado un argumento
    if len(sys.argv) < 2:
        print("Uso: python script.py <path>")
        sys.exit(1)

    # Obtiene el path del archivo desde los argumentos
    file_path = sys.argv[1]

    # Intenta abrir y leer el archivo
    try:
        contacts_object = fsfunc.getFile(file_path)
        # print(contacts_object)

    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    contacts = []

    start = time.time()

    data = np.array(contacts_object)

    for contact in data:
        contactName = VCF(
            contact["first_name"],
            contact["first_name"] + " " + contact["last_name"],
            contact["phone_number"],
            contact["date"],
        )
        contacts.append(contactName)
    with open("contacts.vcf", "w") as f:
        for contact in contacts:
            f.write(contact.getContact())
    elapsed = time.time()
    print(f"Done in {start - elapsed} seconds")


if __name__ == "__main__":
    main()
