# Newspaper_Mining

    This project aims at first collecting data through web scraping.The files are downloaded using
    the wget module which refers to the API links stored in text files. Data is cleaned to bring 
    efficiency in the data for better results.The text files thus obtained are free from UTF-8
    characters and contains simple text. These cleaned files are sent for data processing.The
    total number of words and sentences related to COVID-19 are evaluated from the total number
    of words and sentences respectively from every single newspaper.The percentage of total words
    and sentences are calculated which gives a proper understanding of rising and declining
    COVID-19 related articles.The data is visualized in the form of graphs to understand trends,
    outliers, and patterns.


This is a project which will make it easy for people so they can find out the graphs and data
of the occurences in newspapers. Our motive for this program was simple and straight forward
i.e to extract the data from the pdfs into a text file and then being able to use that data as
many times we want for the analysis. So the program was made to do this task.


We noticed that some newspapers dont support the pdf to text converions and give us incomplete
data so for those cases we have also provided the OCR converter for the pdf to text using text
from image recognition.


# NOTE

    We have made a variable in every program which will contain the value of the pdfs which you have downloaded
    PLEASE CHANGE IT WHEN YOU HAVE DOWNLOADED MORE FILES OR EVEN WHEN YOU HAVE CLEANED MORE FILES!
    So please make sure to change the value of the variable called "downloaded" and "max1"
    We will suggest that you keep our directory structure so that you dont have to change anything in the code
    and would be able to straight away start using it.
    Thank you!

# Convesions Supported:

    - Ocr_conversion using pdf2image and pytesseract library and PIL

    - Converting PDF to text using Pdf2Text library


# Downloding the Dataset:


As we have already provided a rar file which has the cleaned data from the newspaper
"THE HINDU" from March to June so you can extract the dataset and directly run the
programs for the searching of the words.

Else we have also provided our own link catcher and downloader:

# Steps to follow:
      
      Run the Link_catcher.py and wait for it to complete
      
      Then run the Download_files.py which will use the links catched by the
      above program and then use the wget function to download the files.

# Programs to run on the Dataset:


- Count_occurences.py and Count_occurences_multiple.py for finding a single word or having a set of words respectively 

- Delimeter_checker.py for findind the number of sentences which contain our word or set of words provided to the program by us in the code.

- Bad_word_removal.py is the one which removes the words which are commonly used in the sentance just to add meaning to it and gives us a better number.


# Folder Structer:

    --FOLDER HAVING THE CODE
    Folders to creat inside the above one ->
    -- --Combined_Dataset
    -- --Newspaper_Cleaned
    -- --Nespaper_PDF
    -- --Better_cleaned
    And then paste our code in it.
    -- --OUR CODE FROM GITHUB
    
# Authors
Tanishq Chamoli

Sonam Garg

Shriya Verma

# Mentor-
Dr.Ankit Gupta
