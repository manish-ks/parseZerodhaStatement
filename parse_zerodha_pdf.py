import PyPDF2 as pyPdf
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

fh_pdf = open('/home/maxz/zerodhaKiteFirstShot/zerodha_statement/CHRM2898_01092016_2-1.pdf','rb')
fh_txt = open('/home/maxz/zerodhaKiteFirstShot/output_from_pdf.txt','w+')
parser = PDFParser(fh_pdf)
doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize("")
if not doc.is_extractable:
    raise PDFTextExtractionNotAllowed
rsrcmgr = PDFResourceManager()
device = PDFDevice(rsrcmgr)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in doc.get_pages():
    interpreter.process_page(page)
    print("Page is: ", page)

#print("Number of pages", reader.getNumPages())
#contents = reader.getPage(0).extractText().split('\n')
#fh_txt.write(repr(contents))
fh_pdf.close()
fh_txt.close()


##import PyPDF2 as pyPdf
##fh_pdf = open('/home/maxz/zerodhaKiteFirstShot/zerodha_statement/CHRM2898_01092016_2-1.pdf','rb')
##fh_txt = open('/home/maxz/zerodhaKiteFirstShot/output_from_pdf.txt','w+')
##reader = pyPdf.PdfFileReader(fh_pdf)
##print("Number of pages", reader.getNumPages())
##contents = reader.getPage(0).extractText().split('\n')
##fh_txt.write(repr(contents))
##fh_pdf.close()
##fh_txt.close()
