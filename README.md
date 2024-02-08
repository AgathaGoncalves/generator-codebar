Barcode Generator
Description / Descrição
This is a Python project that allows generating barcodes from user-provided product numbers.
Este é um projeto Python que permite gerar códigos de barras a partir de números de produtos fornecidos pelo usuário.

How it works / Como funciona
The program accepts a product number as input and generates a barcode corresponding to that number.
It uses the barcode library to generate the barcodes and the Pillow library for image manipulation.

O programa aceita um número de produto como entrada e gera um código de barras correspondente a esse número.
Ele utiliza a biblioteca barcode para gerar os códigos de barras e a biblioteca Pillow para manipulação de imagens.

Installation / Instalação
Clone this repository to your local environment:

bash
Copy code
git clone https://github.com/your_username/barcode-generator.git
Navigate to the project directory:

bash
Copy code
cd barcode-generator
Install the dependencies:

Copy code
pip install -r requirements.txt
Usage / Uso
Run the Python program barcode_generator.py:

Copy code
python barcode_generator.py
Follow the instructions provided by the program to input the product number.
The program will generate the corresponding barcode and save it as a PNG image in the output directory.

Example / Exemplo
python
Copy code
from barcode_generator import generate_barcode

product_number = "123456789"
image_path = generate_barcode(product_number)

print(f"Barcode generated successfully: {image_path}")
Contributing / Contribuindo
Contributions are welcome! Feel free to open a PR or an issue reporting bugs or suggesting new features.
Contribuições são bem-vindas! Sinta-se à vontade para abrir um PR ou uma issue relatando bugs ou sugerindo novos recursos.

License / Licença
This project is licensed under the MIT License.
Este projeto é licenciado sob a MIT License.
