#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip3 install pypiwin32
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Renderの無料枠では、 「Render側のシェル機能を使用することができない」 。
# そのため、Djangoのスーパーユーザー(管理ユーザー)を事前に作成するためのコマンドを定義しておく必要がある。
# https://qiita.com/kkk777/items/91a00e431d3e1d72d51e
python manage.py newsuperuser
