#update_site
git pull
git add .
git commit -m "Update site"
git push

#update_theme
git pull
git submodule update --init --recursive
cd Galileo && git pull origin latest --rebase
cd ..
git add .
git commit -m "Update theme"
git push

#update_maverick
git pull
git submodule update --init --recursive
cd Maverick && git pull origin master --rebase
cd ..
git add .
git commit -m "Update Maverick"
git push