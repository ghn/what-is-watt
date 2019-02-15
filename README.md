What is watt
=======

Installation
------------

```
vagrant up
```

Then SSH into the box by running `vagrant ssh` and run:

```
npm install
npm run build
./manage.py runserver
```

Then point your browser to http://what-is-watt.lo/.

Front-end development
-------------

SSH into the box and run:

```
npm start
```

Then point your browser to http://what-is-watt.lo:3000/.

Heroku
------

Setup:

1. Ensure a valid `package.json` file exists
2. Install heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
3. `heroku login`
4. `heroku create`
5. `heroku buildpacks:add heroku/nodejs`
6. `heroku buildpacks:add heroku/python` (order of buildpackas is important)
7. `heroku addons:create heroku-postgresql:hobby-dev`
8. `heroku config:set SECRET_KEY=xxx`
9. `heroku config:set DJANGO_SETTINGS_MODULE=what_is_watt.config.settings.heroku`
10. Edit package.json and add the script:
   `"heroku-postbuild": "NODE_ENV=production webpack"`
11. Commit changes
12. `git push heroku master`
13. `heroku open`
