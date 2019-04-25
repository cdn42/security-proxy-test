import generate_files as gf
import os
from config import compressed_types, doc_types

def create_compressed (src_folder, output_folder, keyword = "compress_"):


    prefix = "gf.do_"

    for filetype in compressed_types:

        for filename in os.listdir(src_folder):
            if filename.startswith(keyword):

                archive=output_folder + (filename.split (".")[0].split("_")[1]) + "." + filetype
                sourcefile = src_folder + filename
                # params = (source file, archive file)
                params = "('" + sourcefile + "','" +  archive  + "')"

                eval (prefix + filetype + params)
                continue
            else:
                continue


def create_documents (src_folder, output_folder):


    csvdata = [
        ['Header1', 'Header2', 'Header3'],
        ['Some Data', 'Some More Data', 'Even More Data']
    ]

    prefix = "gf.do_"

    for filetype in doc_types:


        if filetype == "csv":

            gf.do_csv(csvdata, output_folder + 'sampledata.csv')

        else:
            for filename in os.listdir(src_folder):

                if filename.startswith(filetype + "_"):

                    document = output_folder + (filename.split(".")[0].split("_")[1]) + "." + filetype
                    sourcefile = src_folder + filename
                    # params = (source file, archive file)
                    params = "('" + sourcefile + "','" + document + "')"

                    eval(prefix + filetype + params)
