import pyttsx3
import PyPDF2
import os, sys

os.chdir(r'C:\Users\admin\Desktop\COMP246 SEC.004\Textbooks') #absolute path of pdf
book = open('Software Engineering A Practitioners Approach 9th Edition.pdf','rb') #name of pdf
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages) #return total page numbers of pdf
speaker = pyttsx3.init()

for num in range(311,pages): #set the starting page and range
    page = pdfReader.getPage(311) #starting from page 311
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

