# django_local_library
Django Local Library Tutorial

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

# References
[CLI Railway](https://docs.railway.app/develop/cli)
[MDN Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
[Heroku/Django deploy: why am I getting an error 500 with successful deploy and static collection?](https://stackoverflow.com/questions/53694341/heroku-django-deploy-why-am-i-getting-an-error-500-with-successful-deploy-and-s)