::Update Theme

set https_proxy=http://127.0.0.1:1080
git pull

git submodule update --init --recursive
cd Kepler && git pull origin latest --rebase

cd ..
git add .
git commit -m "Update theme"
git push

pause