# django_LiveBooks
Django Local Library Tutorial

# Using venv
It's a better practice to use venv (virtual environment). It simplifies the creation of the requirements.txt file.

```
source venv/bin/activate
```
# Hosting Django App

- [Railway](https://railway.app/) 

# Install Python packages using requirements.txt
```
python -m pip install -r requirements.txt
```

# Install Railway cli (Ubuntu)
```
sudo curl -fsSL https://railway.app/install.sh | sudo sh
```

# Deploying on Railway
Populate static files
```
python manage.py collectstatic
```
Commit changes
```
git add -A
git commit -m 'Some message'
git push
```

Update Railway server
```
railway up
railway logs
```

# HTML, CSS and JavaScript code

# Download Icons

- [Font Awesome](https://fontawesome.com/)
- [Feather Icons](https://feathericons.com/)
- [Octicons](https://octicons.github.com/)

# Download Images
https://www.pexels.com/

# References
[CLI Railway](https://docs.railway.app/develop/cli)
[MDN Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
[Heroku/Django deploy: why am I getting an error 500 with successful deploy and static collection?](https://stackoverflow.com/questions/53694341/heroku-django-deploy-why-am-i-getting-an-error-500-with-successful-deploy-and-s)
