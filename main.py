from flask import Flask, redirect, url_for, send_from_directory, request
import os
from jinja2 import Template
import logging

def my_template(files_input):
    html_tempalte =  """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Web File Transfer</title>
        <style>
            {{ css }}
        </style>

    </head>

    <body>
        <div id="main-container">

            <h1 id="title">Web File Transfer</h1>

            <div id="file-container">

            {% for name, size in files %}
            
                {% if loop.index % 2 == 0 %}
                    <a href="/data/{{name}}" class="file-a-1" download>
                        <span class="file-name">{{ name }}</span>
                        <span class="file-desc">{{ size }}</span>
                        <!-- <span class="file-desc">21:56:14 - 29.11.2024</span> -->
                    </a>
                {% else %}
                    <a href="/data/{{name}}" class="file-a-2" download>
                        <span class="file-name">{{ name }}</span>
                        <span class="file-desc">{{ size }}</span>
                        <!-- <span class="file-desc">21:56:14 - 29.11.2024</span> -->
                    </a>
                {% endif %}
            {% endfor %}

            </div>
               

            <button id="upload-button">
                UPLOAD FILES
            </button>

            <form id="upload-form" action="#" method="post" enctype="multipart/form-data" style="display: none;">
                <input type="file" id="files" name="files[]" multiple>
                <!-- <input type="file" id="files" name="files[]"> -->
                <button type="submit">Загрузить</button>
            </form>

        </div>

        
    </body>

   

    <script>
        const uploadBtn = document.getElementById('upload-button');
        const fileInput = document.getElementById('files');

        uploadBtn.addEventListener('click', () => {
            fileInput.click(); // Открыть окно выбора файлов
        });

        fileInput.addEventListener('change', () => {
            // Автоматическая отправка формы после выбора файлов
            document.getElementById('upload-form').submit();
        });
    </script>

    <script>
            var files = document.getElementsByClassName("file-name");
            for( var i = 0; i < files.length; i++)
            {
                // if( files[i].innerHTML.length >=  35)
                // {
                //     var parser = files[i].innerHTML.split(".");
                //     parser[0] = parser[0].substr(0, 32) + "..";
                //     files[i].innerHTML = parser.join(".");
                // }
                if( files[i].innerHTML.length >=  55)
                {
                    var parser = files[i].innerHTML.split(".");
                    part_1 = parser[0].substr(0, 8);
                    part_2 = parser[0].substr(files[i].innerHTML.length - 10);
                    parser[0] = part_1 + "..." + part_2;

                    files[i].innerHTML = parser.join(".");
                }
            }

    </script>

</html>"""
    css_styles = """
    @import url('https://fonts.googleapis.com/css2?family=Ubuntu+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap');

body{
    padding:0px;
    margin: 0px;
    width:100%;
    height:100%;
    background-color: #1B1E25;
}
h1, h2, h3, h4, h5, p{
    padding:0px;
    margin:0px;
    font-family: "Ubuntu Mono", monospace;
}

#main-container{
    background-color:#1B1E25;
    width:50%;
    height:100%;
    margin-left:25%;
    margin-top:25px;

    display:flex;
    flex-direction: column;
    flex-wrap: nowrap;
    /* flex: 100px; */
    align-items: center;
    /* justify-content: space-around; */
    gap: 25px;

    
}

#title{
    text-align: center;
    font-size:100px;
    color:#F29200;
}

#file-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    align-items: center;
    /* background-color: pink; */
}

a{
    text-decoration: none;
    color:#F29200;
    font-size:24px;
    /* font-family: 'UbuntuFont', sans-serif; */
}

.file-name{
    font-family: "Ubuntu Mono", monospace;

}

.file-desc{
    font-family: "Ubuntu Mono", monospace;
    font-style: italic;
}   

.file-a-1{
    height: 50px;
    width:100%;

    display: flex;
    flex-wrap: nowrap;
    align-items: center;
    align-content: stretch;
    justify-content: space-between;
    padding: 5px;
    
    /* gap:150px; */

    background-color: #1B1E25;

    transition: all 0.15s ease-out;
}

.file-a-2{
    height: 50px;
    width:100%;

    display: flex;
    flex-wrap: nowrap;
    align-items: center;
    align-content: stretch;
    justify-content: space-between;
    padding: 5px;
    
    /* gap:150px; */

    background-color: #252933;

    transition: all 0.15s ease-out;
}

.file-a-1:hover{
    background-color: #383D4A;
    cursor: pointer;
}
.file-a-2:hover{
    background-color: #383D4A;
    cursor: pointer;
}

#upload-button{
    width:100%;
    margin-bottom: 50px;

    text-decoration: none;
    outline: none;
    cursor:pointer;
    height:50px;
    border: 2px solid #F29200;

    font-size:34px;

    color: #F29200;
    background-color: #1B1E25;
    font-family: "Ubuntu Mono", monospace;
    font-style: italic;

    transition: all 0.15s ease-out;
}

#upload-button:hover{
    background-color:#F29200;
    color:#1B1E25;
}


@media only screen and (max-width: 1400px) {
    #main-container{
        width:80%;
        margin-left:10%;
        margin-top:25px;
    }
    #title{
        text-align: center;
        font-size:75px;
        color:#F29200;
    }

    .file-a-1{
        height:75px;
    }

    .file-a-2{
        height:75px;
    }

    .file-desc{
        font-size:22px;
    }

  }

  @media only screen and (max-width: 900px) {
    #main-container{
        width:100%;
        margin-left:0%;
        margin-top:25px;
    }
    #upload-button{
        width:75%;
    }
    #title{
        font-size:60px;
    }

  }
"""

    data = {
        'files': files_input,
        'css': css_styles
    }
    template = Template(html_tempalte)
    rendered_html = template.render(data)
    return rendered_html

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), "data")

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 

app.logger.disabled = True
# logging.getLogger('werkzeug').setLevel(logging.WARNING)


@app.errorhandler(404)
def page_not_found(error):
    # logging.info("Redirecting client")
    return redirect(url_for("main_page"))

@app.route("/data/<path:filename>", methods=["GET"])
def download(filename):
    downloads = app.config['UPLOAD_FOLDER']
    logging.info('\033[96m' + f"Client downloading file '{filename}'" + '\033[0m')
    return send_from_directory(downloads, filename)


@app.route("/", methods=['POST', 'GET'])
@app.route("/index.html", methods=['POST', 'GET'])
def main_page():
    #   --- Uploading upload multiple files in method POST ---
    if request.method == "POST":
        if 'files[]' not in request.files:
            logger.error('Error in client request')
            return redirect(url_for("main_page"))
        files = request.files.getlist('files[]')
        for file in files:
            logger.info('\033[92m' + f"Uploading file to server : '{file.filename}' " + '\033[0m')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return redirect(url_for("main_page"))
    
    #   --- Showing main page ---

    # file_names = os.listdir(app.config['UPLOAD_FOLDER'])                                        # get file names
    
    file_names = []
    with os.scandir(app.config['UPLOAD_FOLDER']) as it:
        for entry in it:
            if entry.is_file() == True:
                file_names.append(entry.name)
                
    file_sizes = []                                                                             # get file sizes
    for file in file_names:
        size = os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], file))
        if size >= 1024 * 1024 * 1024:
            file_sizes.append('{:.2f}'.format(size / 1024 / 1024 / 1024) + " Gb")
        elif size >= 1024 * 1024:
            file_sizes.append('{:.2f}'.format(size / 1024 / 1024) + " Mb")
        elif size >= 1024:
            file_sizes.append('{:.2f}'.format(size / 1024) + " Kb")
        else:
            file_sizes.append(str(size) + " b")
    
    files_data = list( zip(file_names, file_sizes) )
    return my_template(files_data)




if __name__ == '__main__':

    print("""
 __        __     _       _____  _  _           
 \ \      / /___ | |__   |  ___|(_)| |  ___     
  \ \ /\ / // _ \| '_ \  | |_   | || | / _ \    
   \ V  V /|  __/| |_) | |  _|  | || ||  __/    
  __\_/\_/  \___||_.__/  |_|    |_||_| \___|    
 |_   _|_ __  __ _  _ __   ___  / _|  ___  _ __ 
   | | | '__|/ _` || '_ \ / __|| |_  / _ \| '__|
   | | | |  | (_| || | | |\__ \|  _||  __/| |   
   |_| |_|   \__,_||_| |_||___/|_|   \___||_|   
                                                   
                                           
    """)

    if os.path.exists('data') == False:
        os.mkdir('data')
    
    # print('\033[33m' + "   Use Ctrl+C to close the program" + '\033[0m')
    
    app.run(debug=False, host="0.0.0.0", port=80)