::Update Theme

git pull

git submodule update --init --recursive
cd Galileo && git pull origin latest --rebase

cd ..
git add .
git commit -m "Update theme"
git push

pause