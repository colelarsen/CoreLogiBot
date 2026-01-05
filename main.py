import requests
import os


def send_image(image_path):
    url = 'http://localhost:8080/ocr/scan_image'
    file_to_send = image_path
    files = {'image': (file_to_send, open(file_to_send, 'rb'), 'image/png', {'Expires': '0'})}
    reply = requests.post(url=url, files=files)
    return reply.text

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image saved to {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} has been deleted successfully.")
    else:
        print(f"{file_path} does not exist.")

