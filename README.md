# sshri
SSHRI website
## Deploy to github
Generate: pelican -s pelican.conf.py ./path/to/posts -o /path/to/output
1. Manually  push output to master </br>
git add /path/to/output/* </br>
git commit -am "Your Message" </br>
git push origin master </br>
2. Push to gh-pages </br>
pip install gh-imports </br>
pelican -s pelican.conf.py .  </br>
ghp-import output </br>
git push origin gh-pages </br>

#### 3. Put the following into .git/hooks/post-commit:
pelican -s pelican.conf.py . && ghp-import output && git push origin gh-pages

#### 4. Extract  site in ./docs folder rather than output
pelican -s pelican.conf.py ./path/to/posts -o ./docs
On  git server website from root /docs
