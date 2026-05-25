# braincannon

a set of tools to post to the Bluesky social media platform using the AT Protocol API. I wanted something like the old twitter sms blind send tools but for Bluesky. You could just yeet a thought cold and not figure out the post blew up until later. 

## braincannon.py

a python script that posts to Bluesky social media platform using the AT Protocol API. 

The script should be able to post text. 

The script should be able to handle one account. 

The script should also be able to handle errors and should be able to retry failed posts.

include usage instructions including how to setup the python environment and how to run the script.

## config.yaml.example
a yaml file that contains the configuration for the braincannon.py script. it should include the following fields:
- handle: the Bluesky handle (e.g., username.bsky.social). this should be kept secure and should not be committed to the repository.
- app_password: the app-specific password generated from Bluesky settings. this should be kept secret and should not be committed to the repository.

## braincannon.sh

the executable bash script that calls the braincannon.py script and implements all the python environment setup and execution and cleanup.

## readme.md
a readme file that explains what the project is, how to use it, and how to contribute to it.
it will cover: 
- how to securely setup Bluesky app password credentials
- how to setup the python environment
- how to run the braincannon.sh script
- how to contribute to the project

## .gitignore
a gitignore file that ignores any sensitive information such as app passwords and any other files that should not be committed to the repository.