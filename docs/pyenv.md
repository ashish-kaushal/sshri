# docs
## pyenv and pelican

### Software Install and Setup
  python-3.6.3 pelican Markdown typogrify ghp-import2 *Note*: ghp-import can require removal of cryptography pip package
  
#### Install pyenv
  `$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv` <br> 
  `$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile` <br>
  `$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile` <br>
  `$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile` <br>
#### Install latest verion of python 
  `$ pyenv install --list` <br>
  `$ pyenv install 3.6.6` <br>
#### Create workspace directory
  I just create directory, named pelican, and put all the pelican projects in there. I set the local version for that
  directory to latest version of python. You can setup virtualenv if that is easier for you. <br>
  `$ cd pelican` <br>
  `$ pyenv local 3.6.6` <br>
  
#### Working with pelican 
  If existing project then create a branch to hold the source
  `$ git checkout -b docs` </br>
  `$ git branch --list` # check active branch </br>
  
  Create pelican project
  `$ pelican-quickstart`
  
  Add files in content folder, this is your main source folder. Add articles in markdown (md) format, you can use md editors
  available online for creating nice md files.
  `$ vim page1.md`
  
### Deploy
  #### local
  For whatever the source files and images added, first create output files i.e. html in output directory
  by doing </br>
  `$ pelican content -o output -s pelicanconf.py` </br>
  `$ make html` </br>
  `$ ./develop_server.sh start` </br>
  checkout site at localhost:8000 or you can provide new port after start in ./develop_server e.g. </br>
  `$ ./develop_server.sh start 8080` </br>
   
   #### git
   All seems well use ghp-import to do the magic </br>
  `$ ghp-import output` </br>
  Discard for older version of ghp-import ** `$ git push git@github.com:organization/project.git gh-pages:master` </br>
  **`$ ghp-import -p output` </br>

  Reference: 
  1. http://docs.getpelican.com/en/3.6.3/tips.html
  2. https://help.github.com/articles/user-organization-and-project-pages/
  3. https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/
  4. https://help.github.com/articles/user-organization-and-project-pages/
