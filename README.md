What is watt
=======

Import script
-------------

`manage.py import data/consumption.csv`

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
