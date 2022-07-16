# bibliomathica
Library of fun mathematics

This is a personal project between myself and William Zhang. We both are passionate about math, but find that gradeschool courses take the fun away. We always wanted somewhere to go to find fun problems and resources across different domains, so hence this project was born. We are aware that Google and Youtube exist, but this is aimed to be a community maintained collection that serves as a central library. Enjoy

There are two components to this project in terms of what needs to be installed, the python dependencies and the javascript dependencies.

**Python**
First make sure you have a virtual environment installed:
```sh
pip install pipenv
```
Activate the pipenv virtual environment:
```sh
pipenv shell
```
Then run the following command from `src` to install all the required dependencies:
```sh
pipenv install -r requirements.txt
```
**Javascript**<br>
Within the src folder we are going to install a few things. First you will need `node` and `npm` (node package manager). Installing these may vary depending on your machine, on Linux run the following in the Terminal:<br>
&emsp;`sudo apt install nodejs` (the `npm` binary comes along with `nodejs`)<br>Then we will use `npm` to install `webpack`, `babel` and `react`. These can all installed with the following commands.<br>
Webpack:
```sh
npm install webpack webpack-cli --save-dev
```
Babel:
```sh
npm install --save-dev babel-loader @babel/core @babel/preset-env @babel/preset-react
```
React
```sh
npm install --save react react-dom
```
