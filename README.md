# Locale Date/Times

A work in progress playground to visualise different Python methods of displaying dates and times.  Currently just babel, but strftime and others may get added.

## Usage

```shell
pip install -r requirements.txt
flask run
```

* http://127.0.0.1:5000 - date and time in en_GB
* http://127.0.0.1:5000/short - short date and time in en_GB
* http://127.0.0.1:5000/long - long date and time in en_GB

For all of these you can pass a url parameter locale:

* http://127.0.0.1:5000/?locale=ckb_IQ - date and time in ckb_IQ
* http://127.0.0.1:5000/short?locale=cy_GB - short date and time in cy_GB
* http://127.0.0.1:5000/long?locale=hi_IN - long date and time in hi_IN

## TODO

* ability to display multiple formats / multiple locales on a single page
* make it pretty
* include some documentation
