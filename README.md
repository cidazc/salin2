# Salin2
I made a translation app for filipino languages before but it failed, now I am redoing it.


**to install git**

installing git, open terminal

```
sudo apt-get install git
```




**to start your repository**

do this if you made a repo and you are gonna put it to github
```
git init
git add .
git commit
git remote add origin git@github.com:username/new_repo
git push -u origin master
```

do this if someone else started the repository
```
git clone https://github.com/carlaraya/express-locallibrary-tutorial
```
**to add all the files with change**
```
git add .
```

**to add a comment to the files you changed**
```
git commit -m "Your comment goes here"
```

**to push your changes to the master**
```
git push origin master
```

**to make a branch unit_test**
```
git checkout -b unit_test
```

**to switch to branch unit_test**

first add and commit the changes with
```

git add .
git commit -m "I am finalizing this branch and switching to branch unit_test"
```

then go to another branch
```
git checkout unit_test
```

**case 1 if you have changes in master and you want to merge it with unit_test**

```

git checkout master
git pull
git checkout unit_test
git merge master
```


**to reset local changes made to branch unit_test**

resetting mistakes made to one branch

```
git reset
git pull origin unit_test
```

**to install django**
install python 3
```
sudo apt-get update
sudo apt-get install python3.6
```
install pip3
```
sudo apt-get install python3-pip
```


```python -m pip install Django
```
***to install nodejs for npm for angular***

```
sudo apt install nodejs
```

***to install npm for angular***

this is installed when you install nodejs


**to install angular**
```
npm install -g @angular/cli
```

*running*
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
