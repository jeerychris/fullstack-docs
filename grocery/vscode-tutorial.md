# vscode

<https://code.visualstudio.com/docs>

# Install Portable Version

<https://code.visualstudio.com/docs/editor/portable>

Portable mode is supported on the **ZIP download** for Windows and Linux, as well as the regular Application download for macOS.

> **Note:** Do not attempt to configure portable mode on a **Windows installation**. Portable mode is only supported on the Windows ZIP archive. Note as well that the Windows ZIP archive does not support auto update.

## Enable Portable mode

### Windows, Linux

After unzipping the VS Code download, simply create a `data` folder within Code's folder:

```
|- VSCode-win32-x64-1.25.0-insider
|   |- Code.exe (or code executable)
|   |- data
|   |- ...
```

From then on, that folder will be used to contain all Code data, including session state, preferences, extensions, etc.

The `data` folder can be moved to other VS Code installations. This is useful for updating your portable Code version: simply move the `data` folder to a newer extracted version of VS Code.

# Keyboard

<https://code.visualstudio.com/docs/getstarted/keybindings>

## Keyboard rules

The keyboard shortcuts dispatching is done by analyzing a list of rules that are expressed in JSON. Here are some examples:

```json
// Keybindings that are active when the focus is in the editor
{ "key": "home",            "command": "cursorHome",                  "when": "editorTextFocus" },
{ "key": "shift+home",      "command": "cursorHomeSelect",            "when": "editorTextFocus" },

// Keybindings that are complementary
{ "key": "f5",              "command": "workbench.action.debug.continue", "when": "inDebugMode" },
{ "key": "f5",              "command": "workbench.action.debug.start",    "when": "!inDebugMode" },

// Global keybindings
{ "key": "ctrl+f",          "command": "actions.find" },
{ "key": "alt+left",        "command": "workbench.action.navigateBack" },
{ "key": "alt+right",       "command": "workbench.action.navigateForward" },

// Global keybindings using chords (two separate keypress actions)
{ "key": "ctrl+k enter",    "command": "workbench.action.keepEditor" },
{ "key": "ctrl+k ctrl+w",   "command": "workbench.action.closeAllEditors" },
```

Each rule consists of:

- a `key` that describes the pressed keys.
- a `command` containing the identifier of the command to execute.
- an **optional** `when` clause containing a boolean expression that will be evaluated depending on the current **context**.

Chords (two separate keypress actions) are described by separating the two keypresses with a space. For example, Ctrl+K Ctrl+C.

When a key is pressed:

- the rules are evaluated from **bottom** to **top**.
- the first rule that matches, both the `key` and in terms of `when`, is accepted.
- no more rules are processed.
- if a rule is found and has a `command` set, the `command` is executed.

The additional `keybindings.json` rules are appended at runtime to the bottom of the default rules, thus allowing them to overwrite the default rules. The `keybindings.json` file is watched by VS Code so editing it while VS Code is running will update the rules at runtime.

## Common questions

### How can I find out what command is bound to a specific key?

In the **Default Keyboard Shortcuts**, open `Quick Outline` by pressing <kbd>Ctrl+Shift+O</kbd>

### How to add a key binding to an action? For example, add Ctrl+D to Delete Lines

Find a rule that triggers the action in the **Default Keyboard Shortcuts** and write a modified version of it in your `keybindings.json` file:

```json
// Original, in Default Keyboard Shortcuts
{ "key": "ctrl+shift+k",          "command": "editor.action.deleteLines",
                                     "when": "editorTextFocus" },
// Modified, in User/keybindings.json, Ctrl+D now will also trigger this action
{ "key": "ctrl+d",                "command": "editor.action.deleteLines",
                                     "when": "editorTextFocus" },
```

### How can I add a key binding for only certain file types?

Use the `editorLangId` context key in your `when` clause:

```json
{ "key": "shift+alt+a",           "command": "editor.action.blockComment",
                                     "when": "editorTextFocus && editorLangId == csharp" },
```

### I have modified my key bindings in `keybindings.json`, why don't they work?

The most common problem is a syntax error in the file. Otherwise, try removing the `when` clause or picking a different `key`. Unfortunately, at this point, it is a trial and error process.