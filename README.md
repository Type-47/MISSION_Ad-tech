# MISSION_Ad-tech

pipenv shell   ###---仮想環境に入るコマンド
django-admin startproject simple_project .   ###---simple_projectという名前のプロジェクトを作った
tree   ###---参考サイトに書いてあったコマンドだが，使えなかった
python3 manage.py migrate   ###---マイグレーション．意味はまだ調べてない...
python3 manage.py runserver   ###---サーバー起動．出力されたアドレスにブラウザでアクセスして確かめる

~~~

~~~

pipenv install djangorestframework
vi simple_project/settings.py
python3 manage.py startapp api
vi simple_project/settings.py
vi simple_project/urls.py
vi api/urls.py


curl "http://127.0.0.1:8000/api/" -d'{"userid":"0000", "time":"0:00:00", "referrer":"none", "count":"999"}'
>>>{"detail":"Method \"POST\" not allowed."}   ###---


