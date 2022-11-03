### Start app ( worker ):
```bash
heroku login
```
```bash
heroku create monitoring-sites-bot
```
```bash
heroku ps:scale worker=1
```
```bash
git commit

git push heroku master
```
```bash
heroku logs --tail
```

### Add and change env variables to prod:
```bash
heroku config:set URLS="site-1.com site-2.com"

heroku config:edit DELAY
```

### Destroy app ( worker ):
```bash
heroku destroy monitoring-sites-bot --confirm monitoring-sites-bot
```
```bash
heroku logout
```

### Local development:
>Use ./app/.env file
```bash
git clone <URL>
cd <THIS_DIR>
virtualenv .
source bin/acrivate
pip install -r requirements.txt
python3 app/bot.py
```
