import ftplib
import os

# Konfigurasi FTP Agensi Microstock
FTP_HOST = "ftp.adobestock.com"  # Contoh Host FTP Adobe Stock
FTP_USER = "USERNAME_KONTRIBUTOR_ANDA"
FTP_PASS = "PASSWORD_FTP_ANDA"

DIRECTORY_TO_UPLOAD = "./downloads"  # Folder hasil unduhan gambar dari web app Canvas

def upload_images_to_agency():
    try:
        print(f"Connecting to {FTP_HOST}...")
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(user=FTP_USER, passwd=FTP_PASS)
        print("Login successful!")

        for filename in os.listdir(DIRECTORY_TO_UPLOAD):
            if filename.endswith(".jpg"):
                filepath = os.path.join(DIRECTORY_TO_UPLOAD, filename)
                with open(filepath, 'rb') as file:
                    print(f"Uploading {filename}...")
                    ftp.storbinary(f'STOR {filename}', file)
                print(f"SUCCESS: {filename} uploaded to {FTP_HOST}")

        ftp.quit()
        print("All files processed & uploaded successfully.")
    except Exception as e:
        print(f"FTP Error: {e}")

if __name__ == "__main__":
    upload_images_to_agency()
