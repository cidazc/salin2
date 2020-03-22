# express-locallibrary-tutorial

## How to set up
1. Install nodejs: https://github.com/nvm-sh/nvm
1. Install mongodb: https://www.mongodb.com
1. Clone the repo: `git clone https://github.com/carlaraya/express-locallibrary-tutorial`
1. Copy .env.example to same directory (root dir). Name it .env
1. Install dependencies: `npm install`
1. Populate database: `node populatedb.js`
1. Run dev server: `npm run serverstart`
1. Done!!!

## Git Help

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

*running*
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
