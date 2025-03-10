# InvoX

InvoX allows you to upload invoice images and ask questions about them. It leverages the Gemini Pro Vision model to analyze the invoice and provide answers based on the image content.

# Screenshot
![{86A39CCA-CC68-43DA-80AD-BFDCE39F38DC}](https://github.com/user-attachments/assets/a694d06d-0cf0-4c6f-a54b-61e6c747bac5)

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Himank-Khatri/InvoX
    ```
2.  Navigate to the project directory:

    ```bash
    cd InvoX
    ```
3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4.  Obtain a Google Generative AI API key.
5.  Set the API key as an environment variable:

    ```bash
    GOOGLE_API_KEY=<your_api_key>
    ```

## Usage

1.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```
2.  Open the application in your browser.
3.  Upload an invoice image using the file uploader in the sidebar.
4.  Ask questions about the invoice in the chat input.
5.  The application will analyze the image and provide answers based on the content.

## Environment Variables

*   `GOOGLE_API_KEY`: Your Google Generative AI API key.

## Dependencies

*   streamlit
*   google-generativeai
*   python-dotenv
*   langchain
*   PyPDF2
*   chromadb

## Contributing

Contributions are welcome! Please submit a pull request with your changes.
