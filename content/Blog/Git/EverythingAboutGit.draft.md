---
title: git cheat-sheet
date: 2019-04-17
tags: git,github
category:Blog
slug:git-cheat-sheet
author: Ashwin
summary: This post is about git
keywords: git,github
gittime: off
---
[TOC]

# Quick Refresher

## Initial setup

* Open a terminal/shell and type:

```bash
$ git config --global user.name "Your name here"
$ git config --global user.email "your_email@example.com"
```

(Don’t type the `$`; that just indicates that you’re doing this at the command line.)

optionally do:

```bash
$ git config --global color.ui true
$ git config --global core.editor nano
```

The first of these will enable coloured output in the terminal; the second tells git that you want to use nano (a user friendly text editor). You can change the highlighted section with your editor of choice!

Another way to do this is to edit the `.gitconfig` file in your `home` directory. The location of this file depends on the operating system you're using.

- Set up ssh on your computer. 

  - Look to see if you have files `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub`.

  - If not, create such public/private keys: Open a terminal/shell and type:

    ```
    $ ssh-keygen -t rsa -C "your_email@example.com"
    ```

  - Copy your public key (the contents of the newly-created `id_rsa.pub` file) into your clipboard.

  - Paste your ssh public key into your github account settings.

  - Go to your github [Account Settings](https://github.com/settings/profile)

  - Click “[SSH Keys](https://github.com/settings/ssh)” on the left.

  - Click “Add SSH Key” on the right.

  - Add a label (like “My laptop”) and paste the public key into the big text box.

  - In a terminal/shell, type the following to test it:

    ```
    $ ssh -T git@github.com
    ```

  - If it says something like the following, it worked:

    ```
    Hi username! You've successfully authenticated, but Github does
    not provide shell access.
    ```



## Start a new git repository

Your first instinct, when you start to do something new, should be `git init`. You’re starting to write a new paper, you’re writing a bit of code to do a computer simulation, you’re mucking around with some new data … *anything*: think `git init`.

### A new repo from scratch

Say you’ve just got some data from a collaborator and are about to start exploring it.

- Create a directory to contain the project.
- Go into the new directory.
- Type `git init`.
- Write some code.
- Type `git add` to add the files (see the [typical use page](https://kbroman.org/github_tutorial/pages/routine.html)).
- Type `git commit`.

The first file to create (and add and commit) is probably a ReadMe file, either as plain text or with [Markdown](https://daringfireball.net/projects/markdown/), describing the project.

### A new repo from an existing project

Say you’ve got an existing project that you want to start tracking with git.

- Go into the directory containing the project.
- Type `git init`.
- Type `git add` to add all of the relevant files.
- You’ll probably want to create a `.gitignore` file right away, to indicate all of the files you don’t want to track. Use `git add .gitignore`, too.
- Type `git commit`.

### Connect it to github

You’ve now got a local git repository. You can use git locally, like that, if you want. But if you want the thing to have a home on github, do the following.

- Go to [github](https://github.com/).
- Log in to your account.
- Click the [new repository](https://github.com/new) button in the top-right. You’ll have an option there to initialize the repository with a README file, but I suggest you  don’t do it.
- Click the “Create repository” button.

Now, follow the second set of instructions shown on the screen, “Push an existing repository…”

```bash
$ git remote add origin git@github.com:username/new_repo
$ git push -u origin master
```

Actually, the first line of the instructions will usually say

```bash
$ git remote add origin https://github.com/username/new_repo
```

But I use `git@github.com:username/new_repo` rather than `https://github.com/username/new_repo`, as the former is for use with [ssh](https://en.wikipedia.org/wiki/Secure_Shell), if you set up ssh  then you won’t have to type your password every time you push things to github. If you use the latter construction, you’ll have to type your github password every time you push to github.



## Often used commands

### Add and commit

After you’ve made some small modifications to your project and checked that they work, use `git add` to indicate that they’re ready.

```
$ git add R/modified.R man/modified.Rd
```

Then use `git commit` to add the modifications to the repository.

```
$ git commit
```

A text editor (nano if you followed this tutorial) will open; add a short message describing the changes.

To abandon your commit, exit the editor without adding text ( ctrl+x in case of nano ).

For a one-line commit message, you can just type

```
$ git commit -m "Fix such and such"
```

If you want to commit all of the modifications you’ve made, without having to explicitly “add” each file, you can skip the separate `add` and `commit` commands and just type

```
$ git commit -a
```



### Push to [github](https://github.com/)

To push committed changes to github, type

```
$ git push
```

You don’t need to do this every time. Do it after you’ve completed a batch of changes that you’re thoroughly happy with and before you move on to something else.

Once you’ve pushed a commit, it’s hard to take it away. If you’ve not pushed it yet, you *can* go back and scrap it and not have it be part of your project’s history.

### Status

You’ve made some changes to a project, but you’re not sure what. Type

```
git status
```

It’ll give you a list of files that have been changed, plus new files that haven’t been formally added.

### Diff

Exactly what changes have you made? Type

```
git diff
```

Or to see your changes to a particular file, type

```
git diff R/modified.R
```

It’ll show you which lines have been added and which have been deleted.

### .gitignore

The various files in your project directory that you’re not tracking in git should be indicated in a `.gitignore` file.

You don’t *have* to have a `.gitignore` file, but if you don’t, those files will show up every time you type `git status`.

Each subdirectory can have its own `.gitignore` file, too.

Also, you can have a global such in your home directory; I use `~/.gitignore_global`, which contains:

```
*~
.*~
.DS_Store
.Rhistory
.RData
```

You have to tell git about the global `.gitignore` file:

```
$ git config --global core.excludesfile ~/.gitignore_global
```





Huge thanks to [kbroman.org](https://kbroman.org/github_tutorial/) for his tutorials from where I have collated articles for this cheat sheet. you can check out his page for more detailed workflow. 