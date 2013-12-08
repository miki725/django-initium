# install latest jquery 1.x version into {{ project_name }} project

LIB_PATH=../{{ project_name }}/{{ project_name }}/static/lib/jquery
NAME=jquery.min.js

echo "Prepping project for jquery"
echo "---------------------------"
rm -rf $LIB_PATH
mkdir -p $LIB_PATH

echo "Downloading jquery"
echo "------------------"
wget -O $LIB_PATH/$NAME http://code.jquery.com/jquery-latest.min.js --quiet
