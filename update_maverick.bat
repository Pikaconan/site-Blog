::Update Maverick

set https_proxy=http://127.0.0.1:1080
git pull

git submodule update --init --recursive
cd Maverick && git pull origin master --rebase

cd ..
git add .
git commit -m "Update Maverick"
git push

pause