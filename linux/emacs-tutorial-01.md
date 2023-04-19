# Emacs

# GNU Emacs tutorial

emacs tutorial from emacs official:`Ctrl+h, t`

**Meta**, `Alt`

**end emacs session**: `C-x,C-c`

`C-g`

1. quit a partially entered command
2. no responding, comand runs too long

help: `C-h, ?`

**x** quit help

**q** quit

C-v     Move forward one screenful
M-v     Move backward one screenful
C-L     Clear screen and redisplay all the text, moving the text around the cursor to the center of the screen. multiple to center, top, bottom
​		(That's CONTROL-L, not CONTROL-1.)

## overview

```
1. cursor control
                          Previous line, C-p
                                  :
                                  :
   Backward, C-b .... Current cursor position .... Forward, C-f
                                  :
                                  :
                            Next line, C-n

C-f     Move forward a character
C-b     Move backward a character

M-f     Move forward a word
M-b     Move backward a word

C-n     Move to next line
C-p     Move to previous line

C-a     Move to beginning of line
C-e     Move to end of line

M-a     Move back to beginning of sentence, dot for sentence
M-e     Move forward to end of sentence

M-<	start of text
M-> 	end

M-r   runs the command move-to-window-line-top-bottom

2. numeric argument, repeat count normally

C-u 8 c-n
meta-8 c-n

3. emacs stops responding
C-g

4. windows
C-x 0		delete-window
C-x 1		delete-other-windows
C-x 2		split-window-below
C-x 3		split-window-right

C-x o		other-window

C-x 4		ctl-x-4-prefix
C-x 4 C-f	find-file-other-window
C-x 4 C-o	display-buffer
C-x 4 .		xref-find-definitions-other-window
C-x 4 0		kill-buffer-and-window
C-x 4 a		add-change-log-entry-other-window
C-x 4 b		switch-to-buffer-other-window
C-x 4 c		clone-indirect-buffer-other-window
C-x 4 d		dired-other-window
C-x 4 f		find-file-other-window
C-x 4 m		compose-mail-other-window
C-x 4 r		find-file-read-only-other-window

5. insert and delete

5-1. delete:
<back>      character
C-d
Alt-back      word
ALT-D
C-k         kill to the end
A-k

5-2. mark, kill and paste
      the difference between del and kill, kill is for paste
c-space     set-mark
c-w         kill-region
c-y         paste
M-y         paste, but cycle to previous kill

c-x space   rectangel-mark-mode

6. undo
c-/
c-_
c-x u

7. files
      minibuffer

c-x c-f     find-file, create new file when no
c-x c-s     save-buffer

8. buffers
c-x c-b     list-buffers
c-x b       switch-to-buffer
c-x s       save-some-buffers

9. extending the command set
      C-x   Character extend
      A-x   Name command extend

A-x replace-string

10. auto save
      crash, autosaved with #filename#
A-x recover-this-file

11. echo area

 -:**-  TUTORIAL       63% L749    (Fundamental)

12. mode
Major mode
A-X text-mode

minor mode
A-x auto-fill-mode
    c-x f	set-fill-column 70
    A-q		fill-paragraph

13. searching
c-s		isearch-forward
c-r		isearch-backward

backspace, during searching

14. windows, frames
c-l         recenter-top-bottom
c-x 2       split-window-below
c-A-v	    scroll-other-window
c-x 0	    delete-window
c-x o	    other-window
c-x 1	    delete-other-windows
c-x 4	    ctl-x-4-prefix
c-x 4 c-f   find-file-other-window
c-x 4 b	    find-buffer-other-window

15. MULTIPLE FRAMES

On graphical displays, what Emacs calls a "frame" is what
most other applications call a "window".  Multiple graphical frames
can be shown on the screen at the same time.  On a text terminal, only
one frame can be shown at a time.

c-x 5 2	      	new
c-x 5 0		close

16. RECURSIVE EDITING LEVELS
mode line: [(Fundamental)] instead of (Fundamental)

>> Type M-x to get into a minibuffer; then type <ESC> <ESC> <ESC> to
   get out.

```

## emacs help

help key, `c-h` or `f1`

C-h ?           help-for-help

```
a PATTERN   Show commands whose name matches the PATTERN (a list of words
              or a regexp).  See also the ‘apropos’ command.
b           Display all key bindings.
c KEYS      Display the command name run by the given key sequence.
C CODING    Describe the given coding system, or RET for current ones.
d PATTERN   Show a list of functions, variables, and other items whose
              documentation matches the PATTERN (a list of words or a regexp).
e           Go to the *Messages* buffer which logs echo-area messages.
f FUNCTION  Display documentation for the given function.
F COMMAND   Show the Emacs manual’s section that describes the command.
g           Display information about the GNU project.
h           Display the HELLO file which illustrates various scripts.
i           Start the Info documentation reader: read included manuals.
I METHOD    Describe a specific input method, or RET for current.
k KEYS      Display the full documentation for the key sequence.
K KEYS      Show the Emacs manual’s section for the command bound to KEYS.
l           Show last 300 input keystrokes (lossage).
L LANG-ENV  Describes a specific language environment, or RET for current.
m           Display documentation of current minor modes and current major mode,
              including their special commands.
n           Display news of recent Emacs changes.
o SYMBOL    Display the given function or variable’s documentation and value.
p TOPIC     Find packages matching a given topic keyword.
P PACKAGE   Describe the given Emacs Lisp package.
r           Display the Emacs manual in Info mode.
s           Display contents of current syntax table, plus explanations.
S SYMBOL    Show the section for the given symbol in the Info manual
              for the programming language used in this buffer.
t           Start the Emacs learn-by-doing tutorial.
v VARIABLE  Display the given variable’s documentation and value.
w COMMAND   Display which keystrokes invoke the given command (where-is).
.           Display any available local help at point in the echo area.

C-a         Information about Emacs.
C-c         Emacs copying permission (GNU General Public License).
C-d         Instructions for debugging GNU Emacs.
C-e         External packages and information about Emacs.
C-f         Emacs FAQ.
C-m         How to order printed Emacs manuals.
C-n         News of recent Emacs changes.
C-o         Emacs ordering and distribution information.
C-p         Info about known Emacs problems.
C-s         Search forward "help window".
C-t         Emacs TODO list.
C-w         Information on absence of warranty for GNU Emacs.
```

## emacs info

info, manage with emacs help system

c-h m       describe-mode info-mode

```
Info mode provides commands for browsing through the Info documentation tree.
Documentation in Info is divided into "nodes", each of which discusses
one topic and contains references to other nodes which discuss related
topics.  Info has commands to follow the references and show you other nodes.

h       Invoke the Info tutorial.
q       Quit Info: reselect previously selected buffer.

Selecting other nodes:
<mouse-2>
        Follow a node reference you click on.
          This works with menu items, cross references, and
          the "next", "previous" and "up", depending on where you click.
RET     Follow a node reference near point, like <mouse-2>.
n       Move to the "next" node of this node.
p       Move to the "previous" node of this node.
^,u       Move "up" from this node.
m       Pick menu item specified by name (or abbreviation).
          Picking a menu item causes another node to be selected.
d       Go to the Info directory node.
<,t       Go to the Top node of this file.
>       Go to the final node in this file.
[       Go backward one node, considering all nodes as forming one sequence.
]       Go forward one node, considering all nodes as forming one sequence.
TAB     Move cursor to next cross-reference or menu item.
C-M-i   Move cursor to previous cross-reference or menu item.
f       Follow a cross reference.  Reads name of reference.
l       Move back in history to the last node you were at.
r       Move forward in history to the node you returned from after using l.
L       Go to menu of visited nodes.
T       Go to table of contents of the current Info file.

Moving within a node:
SPC     Normally, scroll forward a full screen.
          Once you scroll far enough in a node that its menu appears on the
          screen but after point, the next scroll moves into its first
          subnode.  When after all menu items (or if there is no menu),
          move up to the parent node.
DEL     Normally, scroll backward.  If the beginning of the buffer is
          already visible, try to go to the previous menu entry, or up
          if there is none.
b       Go to beginning of node.

Advanced commands:
s       Search through this Info file for specified regexp,
          and select the node in which the next occurrence is found.
S       Search through this Info file for specified regexp case-sensitively.
C-s, C-M-s      Use Isearch to search through multiple Info nodes.
i       Search for a topic in this manual’s Index and go to index entry.
,       (comma) Move to the next match from a previous i command.
I       Look for a string and display the index node with results.
M-x info-apropos        Look for a string in the indices of all manuals.
g       Move to node specified by name.
          You may include a filename as well, as (FILENAME)NODENAME.
1 .. 9  Pick first ... ninth item in node’s menu.
          Every third ‘*’ is highlighted to help pick the right number.
c       Put name of current Info node in the kill ring.
M-n     Select a new cloned Info buffer in another window.
C-u C-h i       Move to new Info file with completion.
C-u N C-h i     Select Info buffer with prefix number in the name *info*<N>.
```


# emacs manual, more detail

## Delete and paste

## undo


## file
```
C-x C-f		open a file
C-x C-s		save file
```



## buffer
```
C-x C-b		buffer list
C-x b
```



## search and replace
```
C-s			forward search, inc
C-r			backward
M-x replace-string:
```



## windows
```
C-x 1		delete other windows
C-x 2		split horizontally
C-x o		goto another window
ESC C-v		scroll another screen, without leave the cursor
C-x 4 C-f 	filename	new bottom window
C-x 4 b 	new Buffer window

M-x make-frame, delete-frame:
```

## general idea
```
C-x
M-x
```
