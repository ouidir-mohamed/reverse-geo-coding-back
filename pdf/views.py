from distutils import errors
from os import remove
import os
import re
import uuid
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from reverseGeoCodeing.settings import BASE_DIR, STATIC_ROOT
from utils.line_converter import convertLatLngLine
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class ConvertPdfView(APIView):

    def post(self,request, format=None):
        
        from pdf2docx import Converter
      
        file=request.FILES['file']
        randomName = str(uuid.uuid4())
        pdffilename="static/"+randomName+".pdf"
        pdf_file = default_storage.save(pdffilename, ContentFile(file.read()))

        randomName = str(uuid.uuid4())
        docx_file = "static/"+randomName+".docx"  
        # convert pdf to docx
        cv = Converter(pdf_file)
        cv.convert(docx_file)      # all pages by default
        cv.close()

        os.remove(pdf_file)
        from docx import Document
      
        doc = Document(docx_file)
 



     



        
            


        for k,table in enumerate(doc.tables):
            for i,row in enumerate(table.rows):
                for j,cell in enumerate(row.cells):
                    for p in cell.paragraphs:
                        if(True or(i==2 and (j==1 or j==3) and k==5)):
                            # print (p._p.xml)
                            GetParagraphText(p)

        os.remove(docx_file)
        
        randomName = str(uuid.uuid4())
        edited_docx_file = "static/"+randomName+".docx"  
        edited_docx_path=request.get_host()+"/"+edited_docx_file
        doc.save(edited_docx_file)

     
        return Response({"docx":edited_docx_path})

        

from docx.text.paragraph import Paragraph


def GetParagraphText(paragraph):
    # print("execution")

    def GetTag(element):
        return "%s:%s" % (element.prefix, re.match("{.*}(.*)", element.tag).group(1))
    
    text = ''
    runCount = 0
    documentText=""
    for parent in paragraph._p:
        
        for child in parent:
            tag = GetTag(child)
            # if tag == "w:t":
            #     text += paragraph.runs[runCount].text
            #     runCount += 1
            if tag == "w:hyperlink":
                runCount+=1
                
                for subChild in child:
                    if GetTag(subChild) == "w:r":
                        text+=subChild.text
                        documentText=subChild
                        documentText.text=""

                        # subChild.text=convertLatLngLine(subChild.text)
                
    if runCount>0:
        documentText.text=convertLatLngLine(text)
        print(text,'\n-----------',runCount)  

    




