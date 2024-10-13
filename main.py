import subprocess
import sys

def main(keyword, num_images, output_folder, email):
    try:
        download_command = ['python', 'download.py', keyword, str(num_images), output_folder]
        subprocess.run(download_command, check=True)
        print(f"Downloaded {num_images} images with keyword '{keyword}'.")

        
        zip_command = ['python', 'zip.py', output_folder, f"{output_folder}.zip"]
        subprocess.run(zip_command, check=True)
        print(f"Images zipped into {output_folder}.zip.")

        email_command = ['python', 'sendToEmail.py', f"{output_folder}.zip", email]
        subprocess.run(email_command, check=True)
        print(f"Zip file {output_folder}.zip sent to {email}.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python main.py <keyword> <num_images> <output_folder> <email>")
        sys.exit(1)

    keyword = sys.argv[1]
    num_images = int(sys.argv[2])
    output_folder = sys.argv[3]
    email = sys.argv[4]

    main(keyword, num_images, output_folder, email)
