from flask import Flask, make_response, render_template, send_from_directory
from general_all_files import create_compressed, create_documents
from config import compressed_types
import os


# GLOBAL APP NAME ETC

APPNAME = "security-proxy-test"
VERSION = "v1"

app = Flask(__name__)

# Functions

@app.route('/', methods=['GET'])
def root_page():

    #generate list of files in templates/files/compressed

    dirpath = os.path.dirname(os.path.realpath(__file__)) + '/files/'

    # Compressed Files
    files_comp = []

    for filetype in compressed_types:
        for filename in os.listdir(dirpath):
            if filename.endswith("." + filetype):
                files_comp.append([filetype,filename])

    return render_template('index.html', files_list = files_comp)

    #else:
        #return make_response("Access Denied", 401)


@app.route('/fetch/<string:filename>', methods=['GET'])
def return_file(filename):

    dirpath = os.path.dirname(os.path.realpath(__file__))
    fetchfile=dirpath + "/files/" + filename

    exists = os.path.isfile(fetchfile)
    if exists:
        root_dir = os.path.dirname(os.getcwd())
        return send_from_directory(os.path.join(dirpath, 'files'), filename)

    else:
        return make_response("No Such File", 404)


@app.route('/generate/', methods=['GET'])
def generate_files():

    dirpath = os.path.dirname(os.path.realpath(__file__))

    src_folder = dirpath + "/source-files/"
    output_folder = dirpath + "/files/"

    create_compressed(src_folder, output_folder)
    create_documents(src_folder, output_folder)

    return make_response("OK", 200)


# Main Application Loop
if __name__ == '__main__':

    # Ensure an empty files directory exists
    if not os.path.exists('/app/files'):
        os.makedirs('/app/files')

    # Let's go :)
    app.run(debug=True, host='0.0.0.0', port=9000)



