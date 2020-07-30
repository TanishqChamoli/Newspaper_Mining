from PIL import Image
import pytesseract
import os
from pdf2image import convert_from_path
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
loop = 0
dowloaded = 53
with open("TOI_links.txt","r") as p:
    x = p.read()
    for link in x.split():
        if loop > dowloaded:
            exit()
        loop+=1
        link = link.split("/")[-1]
        file_name = link
        print(file_name)
        if os.path.isfile("C:/Users/LENOVO/Desktop/Internship/TOI/Extracted/" +file_name+ '.txt'):
            print("The file has already been parsed")        
        else:
            try:
                pages = convert_from_path("C:/Users/LENOVO/Desktop/Internship/TOI/PDF/"+file_name, 100)
                counter=0
                for page in pages:
                    counter+=1
                    print("image : ",counter)
                    if os.path.isfile("C:/Users/LENOVO/Desktop/Internship/TOI/Extracted/out"+str(counter)+".jpg"):
                        os.remove("C:/Users/LENOVO/Desktop/Internship/TOI/Extracted/out"+str(counter)+".jpg")
                        print("Previous has been removed")
                    page.save("C:/Users/LENOVO/Desktop/Internship/TOI/Extracted/out"+str(counter)+'.jpg', 'JPEG')
                    print("saved")
                text = []
                with open("C:/Users/LENOVO/Desktop/Internship/TOI/Extracted/" +file_name+ '.txt','w') as f:
                    for i in range(1,counter+1):
                        try:
                            image = Image.open("C:/Users/LENOVO/Desktop/Internship/TOI/Extracted/out"+str(counter)+'.jpg')
                            print("The counter of the image is",i)
                            tmp = pytesseract.image_to_string(image)
                            text.append(tmp)
                            f.write(tmp)
                        except:
                            pass
            except:
                print("The file isn't downloaded")
            # print(text)