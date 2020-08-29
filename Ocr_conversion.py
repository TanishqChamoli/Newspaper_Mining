from PIL import Image
import pytesseract
import os
from pdf2image import convert_from_path

# this should have the path of the tesseract on you're pc or you must have it in the env variables

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
        if os.path.isfile("./TOI/Extracted/" +file_name+ '.txt'):
            print("The file has already been parsed")        
        else:
            try:
                pages = convert_from_path("./TOI/PDF/"+file_name, 100)
                counter=0
                for page in pages:
                    counter+=1
                    print("image : ",counter)
                    if os.path.isfile("./TOI/Extracted/out"+str(counter)+".jpg"):
                        os.remove("./TOI/Extracted/out"+str(counter)+".jpg")
                        print("Previous has been removed")
                    page.save("./TOI/Extracted/out"+str(counter)+'.jpg', 'JPEG')
                    print("saved")
                text = []
                with open("./TOI/Extracted/" +file_name+ '.txt','w') as f:
                    for i in range(1,counter+1):
                        try:
                            image = Image.open("./TOI/Extracted/out"+str(counter)+'.jpg')
                            print("The counter of the image is",i)
                            tmp = pytesseract.image_to_string(image)
                            f.write(tmp)
                        except:
                            pass
            except:
                print("The file isn't downloaded")
            # print(text)



# please install this one->
# C:\Program Files\poppler-0.68.0\bin in the env variables