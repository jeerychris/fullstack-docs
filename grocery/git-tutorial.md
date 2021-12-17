# Git

<https://git-scm.com/>

## Distributed

One of the nicest features of any Distributed SCM, Git included, is that it's distributed. This means that instead of doing a "checkout" of the current tip of the source code, you do a "clone" of the entire repository.

**Multiple Backups**

This means that even if you're using a centralized workflow, every user essentially has a full backup of the main server. Each of these copies could be pushed up to replace the main server in the event of a crash or corruption. In effect, there is no single point of failure with Git unless there is only a single copy of the repository.

### Any Workflow

**Subversion-Style Workflow**

![subversion-style-workflow](images/workflow-a-subversion-style.png)

**Integration Manager Workflow**

> Another common Git workflow involves an integration manager — a single person who commits to the **blessed repository**. A number of developers then clone from that repository, push to their own independent repositories, and ask the integrator to pull in their changes. This is the type of development model often seen with open source or GitHub repositories.

![github-workflow](images/workflow-github-style.png)

**Dictator and Lieutenants Workflow**

> For more massive projects, a development workflow like that of the Linux kernel is often effective. In this model, some people **lieutenants** are in charge of a specific subsystem of the project and they merge in all changes related to that subsystem. Another integrator (the **dictator**) can pull changes from only his/her lieutenants and then push to the 'blessed' repository that everyone then clones from again.

![linux-kernel-style](images/workflow-linux-kernel-style.png)

## Staging Area

Unlike the other systems, Git has something called the "staging area" or "index". This is an intermediate area where commits can be formatted and reviewed before completing the commit.

One thing that sets Git apart from other tools is that it's possible to **quickly stage some of your files and commit them without committing all of the other modified files** in your working directory or having to list them on the command line during the commit.

![staging-area](images/git-staging-area.png)

[more features][]

# git help

<https://git-scm.com/docs>

[git-immersion](file:///D:/github/git_tutorial/html/index.html)

```shell
git help help

git help -a
git help -g

git help reset
```

#  git config

global config file `~/.gitconfig`

## alias

```ini
[alias]
    hist = log --pretty=format:'%C(auto)%h %ad %an | %s%d' --date=short --decorate --graph
    co = checkout
    ci = commit
    st = status
    br = branch
    type = cat-file -t
    dump = cat-file -p
```

# gitignore

```sh
~/.gitignore
${project}/.gitignore
.git/info/exclude
```

# git revision 

https://git-scm.com/docs/gitrevisions

# git diff

```shell
# diff working set and staging area
git diff

# you staged for the next commit relative to the named <commit>, default is HEAD
git diff --cached

# diff working set and latest commit
git diff HEAD
```

# log

```
git log --grep="pattern for commit msg"
git log -S"String to find from submitted content"
```

# useful commnad

```shell
# show log with diff(-p), with number(-1)
git log -p -1
#  the overview of the change 
git log --stat --summary
git show HEAD^  # to see the parent of HEAD
git show HEAD^^ # to see the grandparent of HEAD
git show HEAD~4 # to see the great-great grandparent of HEAD

# Note that merge commits may have more than one parent:
git show HEAD^1 # show the first parent of HEAD (same as HEAD^)
git show HEAD^2 # show the second parent of HEAD

git grep "hello" v2.5
```

## github

> low speed to github.com?

replace github.com with http://www.github.com.cnpmjs.org/


[more features]: https://git-scm.com/about

# git clang-format

# git submodule

https://git-scm.com/book/en/v2/Git-Tools-Submodules

## add a project as submodule

```sh
$ git submodule add https://github.com/chaconinc/DbConnector
Cloning into 'DbConnector'...
remote: Counting objects: 11, done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 11 (delta 0), reused 11 (delta 0)
Unpacking objects: 100% (11/11), done.
Checking connectivity... done.

$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   .gitmodules
	new file:   DbConnector

$ cat .gitmodules
[submodule "DbConnector"]
	path = DbConnector
	url = https://github.com/chaconinc/DbConnector

$ git diff --cached DbConnector
diff --git a/DbConnector b/DbConnector
new file mode 160000
index 0000000..c3f01dc
--- /dev/null
+++ b/DbConnector
@@ -0,0 +1 @@
+Subproject commit c3f01dc8862123d317dd46284b05b6892c7b29bc

$ git commit -am 'Add DbConnector module'
[master fb9093c] Add DbConnector module
 2 files changed, 4 insertions(+)
 create mode 100644 .gitmodules
 create mode 160000 DbConnector
```

`pwd` not in submodule dir, no submodule related cmd will ignore submodule contents.

go to submodule dir for it's git cmd

## Cloning a Project with Submodules

```sh
```