# janken

* https://daeudaeu.com/django-janken/
* https://render.com/docs/deploy-django
* https://qiita.com/kkk777/items/91a00e431d3e1d72d51e


### Render.com
* Pythonの実行バージョンを指定
    * https://render.com/docs/python-version


### 対応策
* https://qiita.com/kkk777/items/91a00e431d3e1d72d51e
以下の対応をしなくても上記で良さそう。

* https://stackoverflow.com/questions/45228395/error-no-module-named-fcntl

> I got the same error when trying to run my flask app using gunicorn.
```gunicorn --bind 127.0.0.1:5000 predict:app```
The issue is that 'fcntl' is not available on windows. The alternative that can be used, as suggested by Alexey Grigorov in Ml bookcamp, is the 'waitress' package.
```pip install waitress```
Then write in the command prompt the following command.
```waitress-serve --listen=127.0.0.1:5000 predict:app```
For those still looking for the answer.

* https://stackoverflow.com/questions/11087682/does-gunicorn-run-on-windows
> Basically all you have to do is replace the gunicorn call with:
```waitress-serve --listen=*:8000 myapp.wsgi:application```
For typical apps this will give you the same result as running gunicorn. :) Good luck!


### 起動
```
python manage.py runserver
```
* アクセス先
http://localhost:8000/janken/signup/（旧）
