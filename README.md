# bibliomathica
Library of fun mathematics

This is a personal project between myself and William Zhang. We both are passionate about math, but find that gradeschool courses take the fun away. We always wanted somewhere to go to find fun problems and resources across different domains, so hence this project was born. We are aware that Google and Youtube exist, but this is aimed to be a fun collection that serves as a central library. Enjoy

<img src="./src/media/demopics/explore.png/" width="470" height="220"></img> <img src="./src/media/demopics/collection.png/" width="470" height="220"></img>
<img src="./src/media/demopics/login.png/" width="470" height="185"></img> <img src="./src/media/demopics/topics.png/" width="470" height="140"></img>

**Python**<br>
First make a virtual environment installed:
```sh
python -m venv /path/to/new/virtual/environment
```
Activate the pipenv virtual environment:
```sh
source venv/bin/activate
```
Then run the following command from `src` to install all the required dependencies:
```sh
pip install -r requirements.txt
```
<!-- **Javascript**<br>
Within the src folder we are going to install a few things. First you will need `node` and `npm` (node package manager). Installing these may vary depending on your machine, on Linux run the following in the Terminal:<br>
&emsp;`sudo apt install nodejs` (the `npm` binary comes along with `nodejs`)<br>Then we will use `npm` to install `webpack`, `babel` and `react`. These can all installed with the following commands.<br>
Then we will install all frontend packages with the following command (from package.json)
```sh
npm install
``` -->

**Development**<br>
<!-- In `src/javascript/config.js` modify the `web_config.dev` object with the address and port you are hosting the django server on. Also make sure that `mode` is set to `dev`. <br><br>

Please note that when modifying anything in the javascript folder (including `config.js`), you need to run `npm run dev` from the `src` folder to recompile it otherwise it won't show up on the server. This is since the django template pulls the contents from a webpack bundle, not the javascript files themselves. Then s -->
Start the web application by running (from the src directory)
```sh
python manage.py runserver [PORT]
```
You may specify a port or leave it at 8000 by default.
