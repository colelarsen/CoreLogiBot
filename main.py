import requests
import os

from google_sheet import read
from google_sheet import update_values

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

#The worst direct search method known to man but we don't have that many values
def update_differences_in_sheet(stockpile):
    human_readable_dif = ""
    update_vals = []
    cur_sheet = read(stockpile=stockpile)
    
    for row in cur_sheet:
        if len(row) >= 5:
            item_name = row[4]            
            item_quantity = 0
            if row[3] != '':
                item_quantity = int(row[3])

            difference = item_quantity
            for row in cur_sheet:
                if len(row) >= 2 and row[1] == item_name:
                    difference = item_quantity - int(row[0])

            if difference > 0:
                need_item_row = [difference, item_name]
                update_vals.append(need_item_row)
                human_readable_dif += item_name + ": " + str(difference) + "\n"
    
    #Fill end with empty rows to overwrite anything else
    for i in range(0, 255):
        update_vals.append(['',''])
    
    update_values(update_vals, range_name="!G3:H900", stockpile=stockpile)
    
    return human_readable_dif

                


