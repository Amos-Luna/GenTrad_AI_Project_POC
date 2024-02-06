# GenTrad_AI_Project_POC

## Overview
The GenClass AI Project in Python is designed for users who can easly interact uploading images and classifying it and also generating images from prompts.
An aditional scope of the current project is that users can generate images from prompts and after that, they can easly classify this image generated.
Thats an funny and interactive project.

## Requirements
Verify the Python version for the current project
```
    $ python --version
    Python 3.10.9
 ```

## Development
Ensure you have all the requirements libreries installed:

Follow the instructions:

* Clone the repository on your local machine
```
    git clone https://github.com/Amos-Luna/GenTrad_AI_Project_POC.git
    cd GenTrad_AI_Project_POC
```

* Create your custom virtual environment -> example: `genclass_venv`
```
    py -m venv genclass_venv
    source genclass_venv/bin/activate
```

* Install dependencies and open VSCode
```
    pip install -r requirements.txt
    code .
```

* In the terminal you can execute the next command:
```
    streamlit run app.py
```

## Docker

You can esaly run into Docker Container by following the next step:

* Build the Docker image
```
    docker build -t genclass_ai_image:lastest .
```

* Run the Docker image to create a Docker Container
```
    docker run -d --name genclass_ai_container -p 8000:8000 genclass_ai_image
```

* Copy the url showed into the terminal. Example: 
```
    http://0.0.0.0:8000/
```

# License

This project is licensed under the MIT License - see the LICENSE file for details.