# YouTube Downloader

<br><br>
<br>


## Overview
Want to download any video from youtube? let's start!
<br> Just paste the URL of the chosen youtube's video in the website!
<br><br>
## Tools Used

- Flask and python
- Pytube


## Test Locally

- Clone this repo:

    ```python
    $ git clone git@github.com:tamarheisler/YouTube-downloader.git
    ```

- Change directory to the cloned repo:

    ```python
    $ cd YouTube-downloader
    ```

- Create and active your virtual environment:

    ```python
    $ mkvirtualenv venv
    ```

- Install project dependencies:

    ```python
    (venv)$ pip3 install -r requirements.txt
    ```

- Run the flask server:

    ```python
    (venv)$ flask run
    ```

- Paste the localhost link in your browser to see the application

## Test Locally Using Docker
Install Docker:
Install Docker on your computer. You can download Docker from the official website: [Download Docker]([url](https://www.docker.com/get-started)).
Build the Docker image:

- Open the command prompt and enter:
    ```bash
  docker build -t YouTube-downloader
    ```

This command builds a Docker image based on the instructions in the Dockerfile in the repository.
- Run the application with Docker:

After building the image, run the application with Docker by entering the command:
    ```bash
docker run -p 5000:5000 YouTube-downloader
    ```
- The parameter -p 5000:5000 maps the port from the container to the host.
- Check the running application:
- Open your web browser and navigate to http://localhost:5000.
- Your application should be available, and you can perform the desired operations.


## Test Locally Using Bat file or Bash file
click the Bat file for windows os, and the Bash file for Unix os. 
- all libraries will be installed automatically.


## Screenshots

  - Entering the website:
  <img src="https://github.com/tamarheisler/YouTube-downloader/blob/master/screenshots/1.png"> <br><br>
  - While downloading:
  <img src="https://github.com/tamarheisler/YouTube-downloader/blob/master/screenshots/2.png"><br><br>
  - When the download have succeed:
  <img src="https://github.com/tamarheisler/YouTube-downloader/blob/master/screenshots/3.png"><br><br>
