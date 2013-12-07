# install latest jquery 1.x version into {{ project_name }} project

LIB_PATH=../{{ project_name }}/{{ project_name }}/static/lib/jquery
NAME=jquery.min.js

echo "Prepping project for html5shiv"
echo "------------------------------"
rm -rf $LIB_PATH
mkdir -p $LIB_PATH

echo "Downloading html5shiv"
echo "---------------------"
wget -O $LIB_PATH/$NAME http://code.jquery.com/jquery-latest.min.js --quiet
