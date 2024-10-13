
# Image Downloader and Emailer

This project is a Flask-based web application that allows users to download images from Google based on a search keyword, zip them into a folder, and send the zip file via email. The backend uses the `icrawler` package to download images, zip the files, and send emails via SMTP.

## Features

- Download images from Google based on a search keyword.
- Specify the number of images to download.
- Zip the downloaded images into a folder.
- Send the zipped file to a specified email.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Flask
- `icrawler` for downloading images
- `python-dotenv` for environment variable management

To install the necessary dependencies, run:

```bash
pip install Flask icrawler python-dotenv
```

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/image-downloader-emailer.git
   cd image-downloader-emailer
   ```

2. **Create a `.env` file** in the root directory and set up your email credentials:

   ```bash
   SECRET_KEY=your-secret-key
   password=your-email-password
   ```

   Replace `your-secret-key` with a random string and `your-email-password` with the password for your email account.

3. **Run the Flask Application:**

   ```bash
   python app.py
   ```

   The app will be hosted on `http://127.0.0.1:5000/`.

## Usage

### Web Interface

- Open your browser and go to `http://127.0.0.1:5000/`.
- Fill in the following form fields:
  - **Keyword**: The keyword to search for images (e.g., "bike").
  - **Number of Images**: How many images to download.
  - **Output Folder**: Name of the folder where images will be stored.
  - **Email**: The email address to send the zip file to.
- Click "Submit" to download the images, zip them, and send the zip file to the provided email address.

### Sample Input

Here is an example of what the form will look like when filled out:

- **Keyword**: "bike"
- **Number of Images**: 10
- **Output Folder**: "bike_images"
- **Email**: `example@gmail.com`



![Screenshot 2024-10-14 032620](https://github.com/user-attachments/assets/8c008549-0c79-4265-aad7-3b99f2f475f1)



### Sample Output

After submitting the form:

- A folder `bike_images` will be created with 10 images of bikes.
- A zip file named `bike_images.zip` will be generated.
- The zip file will be sent as an email attachment to `example@gmail.com`.

You should see a success message: `Images downloaded, zipped, and emailed successfully!`

## Project Structure

```
image-downloader-emailer/
├── app.py                # Flask web app
├── download.py           # Downloads images
├── zip.py                # Zips the downloaded images
├── sendToEmail.py        # Sends email with the zip file attached
├── templates/
│   └── form.html         # HTML form for the web interface
└── .env                  # Environment variables (not included in the repository)
```

## Contributing

Feel free to fork the repository and submit pull requests with any enhancements or bug fixes!

## License

This project is open source and available under the [MIT License](LICENSE).

