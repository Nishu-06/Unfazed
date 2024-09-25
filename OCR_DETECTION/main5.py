import os
import csv
import pytesseract
from PIL import Image, ImageTk
import tkinter as tk


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
def extract_text_from_image(image_path):
    try:
      
        img = Image.open(image_path)

        
        crop_box = (30, 200, 1000, 400) 
        cropped_img = img.crop(crop_box)

        extracted_text = pytesseract.image_to_string(cropped_img)
        
        
        diagnosis = ""
        for line in extracted_text.splitlines():
            if "provisional diagnosis" in line.lower():
                
                diagnosis = line.split(":", 1)[1].strip() if ":" in line else ""
                break
        
        
        show_image_and_text(cropped_img, diagnosis)

        
        return diagnosis if diagnosis else "Diagnosis not found"
    
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return "Error"

def show_image_and_text(image, diagnosis):
  
    window = tk.Tk()
    window.title("Extracted Diagnosis")

    
    img_tk = ImageTk.PhotoImage(image)
    
   
    label_image = tk.Label(window, image=img_tk)
    label_image.pack()

    
    label_text = tk.Label(window, text=diagnosis, font=("Arial", 14))
    label_text.pack()

    window.mainloop()

def process_images_to_csv(folder_path, output_csv_file):

    with open(output_csv_file, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['File Name', 'Provisional Diagnosis'])  
    
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')): 
                image_path = os.path.join(folder_path, filename)
                extracted_text = extract_text_from_image(image_path)
                
             
                csv_writer.writerow([filename, extracted_text])
                print(f"Processed {filename}: {extracted_text}")


folder_path = r"C:\Users\singh\Desktop\Bajaj\PS2-Samples-HackRX5"
output_csv_file = r"C:\Users\singh\Desktop\Bajaj\output.csv"


process_images_to_csv(folder_path, output_csv_file)
