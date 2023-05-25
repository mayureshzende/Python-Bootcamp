from xhtml2pdf import pisa             # import python module
from bs4 import BeautifulSoup
  
# Opening the html file
HTMLFile = open("./html/test.html", "r")
  
# Reading the file
index = HTMLFile.read()

soup = BeautifulSoup(index, 'html.parser')

# Format the parsed html file
strhtm = soup.prettify()
# print(strhtm)

output_filename = "test.pdf"

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result
    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err


convert_html_to_pdf(strhtm, output_filename)