# InvoX

InvoX allows you to upload invoice images and ask questions about them. It leverages the Gemini Pro Vision model to analyze the invoice and provide answers based on the image content.

# Screenshot
![{575947D4-92D3-4FD5-B982-BCF5FA502C56}](https://github.com/user-attachments/assets/57e1e458-837e-45a8-bfb1-b1f66af4933d)


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
