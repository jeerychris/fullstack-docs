# Emacs

# GNU Emacs tutorial

**enter**: <kbd>Ctrl</kbd> + <kbd>h</kbd>, <kbd>t</kbd>

**Meta**, <kbd>Alt</kbd>

**end emacs session**: `C-x,C-c`

**quit a partially entered command**: `C-g`

# Emacs

# GNU Emacs tutorial

**enter**: <kbd>Ctrl</kbd> + <kbd>h</kbd>, <kbd>t</kbd>

**Meta**, <kbd>Alt</kbd>

## quit
**end emacs session**: `C-x,C-c`

**quit a partially entered command**: `C-g`

**x**quit help

**q** quit

C-v     Move forward one screenful
M-v     Move backward one screenful
C-L     Clear screen and redisplay all the text, moving the text around the cursor to the center of the screen. multiple to center, top, bottom
​		(That's CONTROL-L, not CONTROL-1.)

## Basic cursor control
```
                          Previous line, C-p
                                  :
                                  :
   Backward, C-b .... Current cursor position .... Forward, C-f
                                  :
                                  :
                            Next line, C-n
```

**summary**

```
C-f     Move forward a character
C-b     Move backward a character

M-f     Move forward a word
M-b     Move backward a word

C-n     Move to next line
C-p     Move to previous line

C-a     Move to beginning of line
C-e     Move to end of line

M-a     Move back to beginning of sentence
M-e     Move forward to end of sentence

M-<		start of text
M-> 	end

C-u 8 C-f, forward 8 lines
```

## Delete and past

```
C-BS        Delete the character just before the cursor
C-d          Delete the next character after the cursor

M-<DEL>      Kill the word immediately before the cursor
M-d          Kill the next word after the cursor

C-k          Kill cursor position to end of line
M-k          Kill to the end of the current sentence

C-w			delete selected text
M-w			copy selected text

C-y			copy last
M-y			copy cyclely
```

## undo
```
C-/		undo a command, if changed text
C-_
C-x u 	undo
```



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




# emacs help
## open emacs help
>`C-h`

## short cuts
eg, for C-x 0,
>C-h k C-x 0

>C-h c C-p

## function
>C-h f        Describe a function.  You type in the name of the function.

## Apropos
>C-h a        

Command Apropos. Type in a keyword and Emacs will list all the commands whose names contain that keyword.
These commands can all be invoked with META-x. For some commands, Command Apropos will also list a one or two character sequence which runs the same command.