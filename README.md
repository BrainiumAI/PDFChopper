# PDFChopper
Splits PDF files into multiple, smaller PDF files

# PDF Splitter

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

PDF Splitter is a Python tool that allows you to split PDF files based on their size. It provides a convenient way to break down large PDF files into smaller ones, making them more manageable for storage or sharing.

## Features

- Split PDF files based on desired file size
- Maintain original file formatting and content in the split PDFs
- Command-line interface for easy usage
- Customizable output directory and file naming options

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/BrainiumAI/PDFChopper.git
   ```

2. Change into the project directory:
   ```shell
   cd pdf-splitter
   ```

3. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

To split a PDF file, use the following command:

```shell
python pdf_splitter.py --file path/to/input.pdf --size <desired_size_mb>
```

Replace `path/to/input.pdf` with the path to your input PDF file, and `<desired_size_mb>` with the desired size of each split PDF in megabytes.

Additional options:
- `--output-dir`: Specify the output directory for the split PDF files. (default: `./output`)
- `--prefix`: Specify a prefix for the output file names. (default: `split_`)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgements

This project was inspired by the need to efficiently manage and share large PDF files. Special thanks to the contributors who have helped make this project better.

## Contact

For questions or inquiries, please contact brainiumai3@gmail.com

```

Feel free to customize the content according to your specific project. Don't forget to replace placeholders like `<desired_size_mb>`, `<email@example.com>`, and provide appropriate instructions and details about your project.
