# Generate Files

# All these functions take an input and output filename
# They write to disk

def do_b64 (source, archive):

    import base64

    with open(source, 'rb') as f:
        data = f.read()
        f.close()

    b64 = base64.encodestring(data)

    with open(archive, 'wb') as f:
        f.write (b64)
        f.close()


def do_gz (source, archive):

    return (do_gzip(source, archive))


def do_gzip (source, archive):

    import gzip
    import shutil

    try:
        with open(source, 'rb') as f_in:
            with gzip.open(archive, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        return 0
    except:
        return 1

def do_tar (source, archive):

    import tarfile

    try:
        tar = tarfile.open(archive, "w")
        tar.add(source)
        tar.close()
        return 0
    except:
        return 1


def do_tgz (source, archive):

    import tarfile

    try:
        tar = tarfile.open(archive, "w:gz")
        tar.add(source)
        tar.close()
        return 0
    except:
        return 1

def do_tz (source, archive):

    return (do_tgz (source, archive))


def do_rar (source, archive):

    import os

    command = "rar a " + archive + " " + source
    print("* I'm broken *")

    try:
        #os.system(command)
        return 0
    except:
        return 1

def do_zip (source, archive):

    from zipfile import ZipFile

    try:
        with ZipFile(archive, 'w') as zip:
            zip.write(source)
        return 0
    except:
        return 1





# Document Types


# Function:     do_csv
# Purpose:      Write a CSV file from data

# Source:

#   data = [
#               ['Header1','Header2','Header3'],
#               ['Some Data','Some More Data','Even More Data']
#           ]

# Output:      csv

def do_csv (source, output_file):

    import csv

    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    try:
        with open(output_file, 'w') as f:
            writer = csv.writer(f, dialect='myDialect')
            for row in source:
                writer.writerow(row)
            f.close()
        return 0
    except:
        return 1


# Function:     do_docx
# Purpose:      Write a Word Document from data

# Source:       text data
# Output:       docx

def do_docx (source, output):

    try:
        with open(source, 'r')  as f:
            data = f.read()

        from docx import Document
        document = Document()
        document.add_heading(data, 0)
        document.save(output)
        return 0
    except:
        return 1


# Function:     do_xlsx
# Purpose:      Write an Excel file from a CSV

# Source:       csv
# Output:       xlsx

def do_xlsx (source, output_file):

    import xlsxwriter
    import csv

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet()

    data = []

    csv.register_dialect('myDialect',
                         delimiter=',',
                         quoting=csv.QUOTE_ALL,
                         skipinitialspace=True)
    with open(source, 'r') as f:
        reader = csv.reader(f, dialect='myDialect')
        for row in reader:
            data.append (row)

    rowcount = 0
    colcount = 0

    for rowdata in data:
        for columndata in rowdata:
            worksheet.write(rowcount, colcount, columndata)
            colcount = colcount + 1
        rowcount = rowcount+1
        colcount = 0

    workbook.close()



