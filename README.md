# JSON to VCF Converter

Este script convierte un archivo JSON descargado de Telegram en un archivo VCF (vCard) que puede ser importado en aplicaciones de contactos.

## Características

- Convierte contactos de un archivo JSON exportado desde Telegram a formato VCF.
- Compatible con múltiples contactos en un solo archivo.

## Requisitos

- Python.
- Numpy (Si deseas lo reemplaza por una lista común y te deshaces de él)
- Archivo JSON exportado desde Telegram.

## Uso

1. Asegúrate de tener el archivo JSON exportado desde Telegram.
2. Ejecuta el script con el siguiente comando:

   ```bash
   python script.py input.json
   ```
# O
   ```bash
   python3 script.py input.json
   ```


3. El archivo `contacts.vcf` se generará en el mismo directorio.

## Ejemplo de Entrada

Archivo JSON de ejemplo:

```json
 "list": [
   {
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "+123456789",
    "date": "2022-12-13T20:30:44",
    "date_unixtime": "1670981444"
   },
   {
    "first_name": "Jane",
    "last_name": "Smith",
    "phone_number": "+987654321",
    "date": "2023-01-06T00:52:46",
    "date_unixtime": "1672984366"
   }]
```

## Ejemplo de Salida

Archivo VCF generado:

```
BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL:+123456789
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:Jane Smith
TEL:+987654321
END:VCARD
```

## Contribuciones

Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.
