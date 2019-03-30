# The vscode python tutorial

<https://code.visualstudio.com/docs/python/python-tutorial>

## the vscode python extension

## python interpreter

# `vscode` folder

## `code .`

> use code open a folder, vscode make this a workspace. and create  `.vscode` automatically

- setting.json
    workspace scope vscode setting
- keybinding.json
 
- launch.json
    if use debug

# pip

<http://www.pianshen.com/article/5331129106/>

the python package installer, use PyPI(The Python Package Index), the standard repository of software for the python programming language.

## help 

```shell
D:\python\hello>pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
```

```shell
D:\python\hello>pip help install

Usage:
  pip install [options] <requirement specifier> [package-index-options] ...
  pip install [options] -r <requirements file> [package-index-options] ...
  pip install [options] [-e] <vcs project url> ...
  pip install [options] [-e] <local project path> ...
  pip install [options] <archive url/path> ...

Description:
  Install packages from:

  - PyPI (and other indexes) using requirement specifiers.
  - VCS project urls.
  - Local project directories.
  - Local or remote source archives.

  pip also supports installing from "requirements files", which provide
  an easy way to specify a whole environment to be installed.

Install Options:
  -r, --requirement <file>    Install from the given requirements file. This option can be used multiple times.
  -c, --constraint <file>     Constrain versions using the given constraints file. This option can be used multiple times.
  --no-deps                   Don't install package dependencies.
  ```


# Use a virtual environment

A best practice among Python developers is to avoid installing packages into a **global interpreter environment**, as we did in the previous section. You instead use a **project-specific virtual environment** that **contains a copy of a global interpreter**. Once you activate that environment, any packages you then install are isolated from other environments. Such isolation reduces many complications that can arise from conflicting package versions.

## Django Tutorial in Visual Studio Code

<https://code.visualstudio.com/docs/python/tutorial-django>
<https://docs.djangoproject.com/en/2.1/intro/tutorial01/>

Django is a high-level Python framework designed for rapid, secure, and scalable web development. Django includes rich support for URL routing, page templates, and working with data.

