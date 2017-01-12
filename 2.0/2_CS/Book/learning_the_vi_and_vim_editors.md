# Learning the vi and Vim Editors

A detailed guide to using Vi and Vim by Arnold Robbins. These notes are a quick summary of each
chapter.

# The vi Text Editor

vi is short for visual editor. It has an insert mode and a command mode. Commands are case
sensitive, not echoed, and do not required an "Enter".

When you open a file, vi copies it into a buffer and displays it for editing. Saving copies the
buffer contents back into the disk. Use the `vi` command to open a file for editing.

    $ vi practice

Hit `i` to enter insert mode. Hit `esc` to enter command mode. Quit vi by typing `:q` and hitting
enter. Commands prefixed with a colon are ex commands.

* `:w` writes a file
* `:wq` writes and quits
* `:!ls` lists files in current directory (! prefixes shell commands)
* `:e!` wipes edits and returns to original file
* `:q!` wipes edits and quits

# Simple Editing

The most important keystrokes let you enter insert and command mode: `i` and `esc`. In command mode,
you can move the cursor via:

* `h, j, k, l` for left, down, up, right one space
* `0` moves to beginning of line
* `$` moves to end of line
* `+` and `-` moves to beginning of next/previous line
* `w` and `b` moves forwards and backwards by words
* `W` and `B` doesn't include punctuation
* number prefixed by `G` moves to line number
* number prefixing moves by multiples (`4l` moves 4 spaces right)

Some ways to insert text:

* `i` for insert mode
* `a` to append (insert mode, cursor goes after current character)
* `I` and `A` insert mode to beginning/end of line
* `o` and `O` to insert a blank line above/below current line
* `R` for overstrike mode
* numeric prefixes can be used (`50i*ESC` inserts 50 asterisks)

Some simple edit commands:

* `c` or `C` to change character or to end of line
* `cc` to change the entire line
* `r` replace a single character then go back to command mode
* `s` and `S` substitutes a character or whole line and stays in insert mode
* `~` changes the case of a letter
* `x` to delete a single character
* `d` followed by a movement to delete up to next position
* `D` to delete to end of the line
* `dd` to delete entire line
* `y`, `yy`, `Y` works like delete, but "yanks" or "copies" characters without deleting them
* `p` or `P` to "put" or "paste" yanked or deleted characters before or after the cursor
* `J` joins two lines together
* number prefixing edit commands for multiples (`4dd` deletes 4 lines)

Combining movements with edit commands is a great way to showcase vi's power:

    cw      " changes to the end of a word
    c2b     " changes back to words
    d$      " deletes to end of the line
    4dd20Gp " delete 4 lines, move to line 20, paste deleted lines

Repeating, undoing, and redoing commands:

* `.` repeats your last command
* `u` undos your last command in case you made an error
* `U` undos commands on the same line (once you move off of it, you can no longer use uppercase U.
* `Ctrl-R` redo and undone operation

# Moving Around in a Hurry

This chapter covers movement by screen, text blocks, search patterns, and line numbers.

In normal mode, hitting `enter` will continue to move the cursor down one line. Once it hits the
bottom line, it will scroll your file. Some more efficient ways of scrolling:

* `^F` and `^B` scroll forward/backward one screen
* `^D` and `^U` scroll forward/backward half screen
* `^E` and `^Y` scroll forward/backward one line

You can also reposition the current screen without moving the cursor using `z`:

* `zEnter` moves current line to top of screen
* `z.` moves current line to middle of screen
* `z-` moves current line to bottom of screen
* Numeric prefix to use that line number instead of current (`20z.` moves cursor to line 20 and puts
  it in middle of screen)

Use `^L` to redraw the current screen. You can move within a screen:

* `H` move to top line on screen
* `M` move to middle line on screen
* `L` move to last line on screen
* it might be easier to just use line number and `G`

Some handy movement commands are:

* `^` moves to first nonblank character of current line
* `n|` moves to column n of current line
* `e` or `E` moves to end of word with or without punctuation
* `(` or `)` moves to beginning or end of sentence
* `{` or `}` moves to beginning or end of paragraph
* `[[` or `]]` moves to beginning or end of section

Use `/` to move by searches:

* `/pattern` will look for "pattern"
* `?pattern` to search backwards
* `n` or `N` to repeat searches forwards/backwards
* searching is a movement command that works with other commands (`d?move` deletes from the cursor
  to "move" pattern)

You can limit your search to the current line also:

* `fx` or `Fx` moves cursor to next/previous occurrence of x character
* `tx` or `Tx` moves cursor to right before/after next/previous occurrence
* `;` or `,` repeats command in same/opposite direction
* use numeric prefixes to skip occurrences

Use `^G` to see current line number and column number. Use a number prefix and `G` to go to a
specific line number.

# Beyond the Basics

This chapter includes extra options when starting vi, using registers for copy and deletes, and
marking places within a file.

Some options when starting vi:

* `vi +n file` opens at line number n
* `vi + file` opens at last line
* `vi +/pattern file` opens at first occurrence of pattern
* `vi -R file` or `view file` for readonly
* `vi -r` or `vi -r file` to recover a file from a previous cash

Vi lets you place yanks into registers identified by letters, so you can paste more than just the
last deletion/yank. Vi remembers the last nine deletions using numbered buffers or registers.

* `"2p` will paste the second-to-last deletion
* `"1pu.u.u` etc... will cycle through your registers

You can yank/delete text into a specific register for later recall:

* `"dyy` yanks current line into register d
* `"dP` pastes from register d
* `:registers` to see a list of all current registers

You can mark your place in a file with `m`:

* `mx` marks position with the letter x
* `'x` moves cursor to first character of line of marked position
* ``x` moves cursor to marked position
* ```` moves to exact position of previous mark or context after move
* `''` moves to beginning of line of last mark or move
* `:marks` to see a list of all current marks

# Introducing the ex Editor

ex is a line editor underlaying vi. Back then, programmers would print a single line to view it and
edit.

    $ ex practice
    "practice" 6 lines, 320 characters
    :1p
    With a screen editor you can
    :s/screen/line/
    With a line editor you can
    :vi

Some ex commands you can use for editing:

* `:p` print lines
* `:nu` print lines and line numbers
* `:d` deletes lines
* `:m` moves lines
* `:co` or `:t` copies lines
* commands work on whatever line the cursor is on. You can also prefix it with a single line number
  of line range (`:5d` deletes line 5, `:5,10d` deletes lines 5 to 10). You can also specify using
  search patterns.

Some examples:

* `160,224m23` moves lines 160-224 to follow line 23
* `23,29co100` yanks lines 23-29 and pastes them after 100

Toggle line numbers with `:set number` and `:set nonumber`. Print out lines with a range followed by
`#` like `:1,10#`.

Some special symbols you can use when specifying ranges:

* `.` represents the current line
* `$` represents the last line of the file
* `%` is the entire file
* `+` and `-` are numeric operators that can be performed on line numbers or symbols (`.,.+20` means
  next 20 lines). The dot is optional and considered default.
* `/pattern/` is valid for ranges (`/pattern1/,/pattern2/+2` goes from the first pattern to the
  second plus two lines)
* Use `;` instead of `,` to switch the current line relative to the starting location (`100;+5`
  means lines 100 to 105)

You may only want to effect lines that include a pattern or does not include a pattern:

* `:g/pattern/` are all lines including pattern
* `:g!/pattern/` are all lines not including the pattern
* `:60,124g/pattern/` all lines including pattern within lines 60-124

Ex commands can be combined with a vertical bar `|`. It works like the Unix semi-colon. Ranges need
to be specified for each command.

Some common ex commands to saving, reading, and quitting:

* `:w` writes the file
* `:w newfilename` for a new filename
* `:230,$w newfilename` only save a portion of the file
* `:340,$w >>newfilename` appends to file
* `:q` quits
* `:wq` or `:x` writes and quits
* `:read filename` or `:r filename` reads a file into the buffer
* `:e filename` opens the file in a new buffer
* `:e!` resets the current file
* `%` represents the current filename in a command (`:w %.new` saves a new file with extension
  ".new")
* `:e #` or `:b #` or `^^` switches back and forth between two buffers
* `:ls` to list current buffers
* `:b` followed by a number to switch buffers. You can also use a filename. This works great with
  `tab` for autocompletion.

# Global Replacement

The substitution command has this syntax:

    :s/old/new/

This works on the current line and works on the first occurrence of the 'old' pattern. Use the `g`
option which stands for global to affect all patterns of 'old' in the current line:

    :s/old/new/g

This command can be prefixed with a range:

    :1,$s/old/new/g
    :%s/old/new/g

For Vim, I like to use `V` to enter visual mode and highlight the lines I'd like to change. Then
just hit `:` and enter the substitution command to affect only those lines.

The `c` option lets you confirm substitutions:

    :%s/old/new/gc

Just hit 'y' and enter to confirm. Hit enter to skip.

Using the range prefix is useful for context sensitive replacements:

    :g/condition/s/old/new/g

vi uses the same pattern matching rules as grep, sed, and awk. This can be used with the `:s`, `:g`,
`/`, and `?` commands:

* `.` matches any single character except a newline
* `*` matches zero or more of previous character
* `^` matches beginning of line
* `$` matches end of line
* `\` escapes special characters
* `[]` for character sets
* `[^]` inverse character set
* `\(\)` saves pattern for later use in replacement (use `\n` where 'n' is the number for
  replacement)
* `\<` or `\>` for beginning of end of word
* `~` last search
* `[::]`, `[..]`, `[==]` can be used for character sets, multicharacter sequences, and locale
  searches

Some special characters to use in the replacement string:

* `\n` for newline
* `\` to escape special characters
* `&` entire search match
* `~` previous search match
* `\1`, `\2`, `\3`, etc... for saved patterns via `\(\)`
* `\u` and `\l` changes next character to uppercase/lowercase
* `\U` and `\L` for all proceeding characters until a `\e` or `\E` reached

# Advanced Editing

`ex` uses the `:set` command to set and unset options:

* `:set option` will set an option to true
* `:set noption` will set it to false
* `:set option=value` will set a value to a non-boolean option
* `:set option=` will unset the value
* `:set option?` for more info about the option
* `:set all` will show all available options
* `:set` shows currently set options

Use the file `~/.vimrc` or `~/.exrc` to set common options every time vi starts. An example file:

    " comments start with double quotes
    set nowrapscan 
    set wrapmargin=7
    set sections=SeAhBhChDh

Put `set exrc` in your `~/.exrc` to read an additional `.exrc` file in the current working directory
for further configuration. You can manually include configuration files using the `:so config.file`
command.

Some useful options:

* `wrapmargin` set to size of right margin for autowrap
* `ignorecase` to ignore casing in searches
* `wrapscan` to search above and below current position
* `magic` to enable or disable special characters in searches
* `autoindent`, `showmatch`, `tabstop`, `shiftwidth`, `number`, and `list` may be useful for
  programmers
* `autowrite` will automatically save to disk when you switch buffers

You can execute Unix commands from vi:

    :!command

If you want to just access the shell temporarily, use `:sh` and then exit the shell to return to vi.
You can also use Unix suspension. `Ctrl-Z` to suspend the current vi job. Use `fg` to return it back
later. If you have multiple jobs suspended, use `%jobid`. To get the list of currently suspended
jobs, use `jobs`.

vi can read the results of a command into the editor or send the contents of a file to a command:

* `:r !date` read in the date command
* `:96,99!sort` sort lines 96-99
* use `V` to enter visual mode, then use the range with a command to send it
* you can also hit `!` first, then use a movement, then type a command

vi supports text abbreviations in insert mode via `:ab abbr phrase`. Whenever you type "abbr"
followed by a nonalphanumeric character in insert mode, it will expand to "phrase". Use `:unab abbr`
to unabbreviate. Use `:ab` alone to list all abbreviations.

You can map your own key sequences to more complex sequences:

* `:map x sequence` where x is any character sequence
* `:unmap x` disables the map
* `:map` list currently mapped sequences

Vim has the convention of the "leader" key for users to define their own shortcuts. I usually set
mine to comma:

    let mapleader = ','
    map <leader>p :!git push<CR>

Some other friendly keys to start maps with are `g, K, q, ^A, ^K, ^O, ^W, ^X, _, *, \, and =`. You
can also map function keys via `#1`, `#2`, etc... If you're unsure about what a key translate to in
text, run vi and start the `:map ` ex command. Hit the key you wan to map, ex will translate the
escaped sequence for you.

Use `map!` instead of `map` to override existing maps and also have it apply to insert mode. Your
shortcut key sequence will now invoke the command instead of inserting characters to your document.

vi has a feature called "@-Functions" which let you hold commands into the copy/paste registers.
Just enter a vi command (either in normal mode or ex command) into your text, cut it into a
register, then execute via `@buffer`. For example:

1. type `cwgadfly^[`
2. `"gdd` to cut command into buffer g
3. `@g` to execute
4. Use `.` or `@@` to repeat

Some tips for editing source code:

* with autoindent enabled, Ctrl-T and Ctrl-D will add/remove a level of indentation in insert mode
* when over a bracket, hit `%` to jump to corresponding bracket
* vi supports ctags. Use the ctags command to generate one then use `:tag name` to jump to a tag. Or
  use `^]` while the cursor is over an identifier.

# Vim (vi Improved): An Introduction

Vim stands for "vi improved" and is an implementation/extension of vi written by Bram Moolenaar. It
has become so popular that the words vi and vim are almost synonymous. Many systems ship with the
command `vi` as a soft link to vim.

Vim adds features like syntax extensions, autocompletion, GUIs, scripting, plugins, session context,
and more. Use `:set compatible` to switch back and forth between vim and vi modes. If you don't
already have it, you get download it from <http://www.vim.org>.

# Major Vim Improvements over vi

Some of the major features of vim includes built-in help, initialization, motion commands, extended
regular expressions, extended undos, and customizing the executable.

To use the help system:

* `:help` starts off with basic instructions
* `:help topic` get the help page for a specific topic
* `:help t<tab>` to autocomplete/search through topics. Vim lets you `<tab>` through any ex commands
  and arguments for context sensitive autocompletion.

Vim has some extra startup and initialization options:

* `:help startup` to see your options
* `-b` to edit binary files
* `-c command` or `-cmd` runs ex command on startup
* `-C` runs in compatibility mode
* `-d` for diff mode
* `-E` use improved ex mode
* `-F` or `-A` for Farsi or Arabic modes
* `-g` use gvim
* `-m` turns off write options
* `-o` or `-O` to open files in different windows horizontal or vertical
* `-y` easy mode for beginners
* `-z` runs in restricted mode

The initialization process for vim is:

1. Runs contents of `VIMINIT` environment variable as an ex command
2. Runs user `vimrc` file in `$HOME/.vimrc`
3. If `exrc` option is set, runs `.exrc` file

Most people customize vim via their `vimrc` file. For ex commands, the initial colons may be left
off. Some relevant environment variables for vim are:

* `SHELL` or `COMSPEC` is the shell vim uses for shell commands
* `TERM` tells vim which terminal to use, usually never needs to be set
* `MYVIMRC` overrides the vimrc file location
* `VIMINIT` ex commands to run on initialization
* `EXINIT` same as VIMINIT
* `VIM` directory to vim installation for more materials
* `VIMRUNTIME` point to different vim support files like documentation

Vim provides some new motion commands:

* `n%` will go to the nth percent line in the file
* `:go n` will go to the nth character in the file
* `v` or `V` enters visual mode, where you can select text to act upon later. Movement is by
  characters or lines.

Vim also provides extended regular expressions for searches. See `:help regular-expressions` for a
full list. Here is a summary:

* `\|` for an OR as in `house\|home`
* `\+` for one or more of preceding character
* `\=` zero or one of preceding character
* `\{n.m}` n to m of preceding character
* `\{n}` n preceding characters exactly
* `\{n,}` at least n of preceding character
* `\,m}` matches 0 to m of preceding character
* negatives values may be used to match as few as possible instead of as most as possible
* `\s` or `\S` for any whitespace or inverse
* `\r` for carriage returns

# Multiple Windows in Vim

Some ways to start editing with multiple windows:

* use the `-o` or `-O` options when starting vim with multiple filenames
* use the `:split filename` or `:vsplit filename` commands
* using the `:split` or `:vsplit` without a filename will split the current document
* use `^Ws` or `^WS` to split the current file

The `split` commands has a few arguments of its own:

    :[n]split [++opt] [+cmd] [file]

* n is how many lines to open in the new window
* opt passes option information
* cmd is an ex command to run on opening the new window
* file is the filename to split

Moving your cursor from one window to another uses commands prefixed with `^W`:

* `^W-down`, `^W-j`, `^W-^J` to move to the next window down
* `^W-up`, `^W-k`, `^W-^K` to move to the next window up
* `^W-left`, `^W-h`, `^W-^H` to move to the next window left
* `^W-right`, `^W-l`, `^W-^L` to move to the next window right
* `^W-w`, `^W-^W` to cycle through windows
* `^W-t`, `^W-^T` move cursor to top leftmost window
* `^W-b`, `^W-^B` move cursor to bottom rightmost window
* `^W-p`, `^W-^P` move cursor to previous window
* `^W-r` and `^W-R` rotates window placements clockwise or counter clockwise
* `^W-x` and `^W-X` swaps current window with next, can be prefixed with count
* use `^W-` with `K, J, H, or L` to move the current window a direction and occupy the full width or
  height
* `^W-=` to resize all windows to be equal sizes
* `^W-+` and `^W--` adds or subtracts a row to the window size
* `^W-<` and `^W->` adds or subtracts a column
* `^W-|` maximizes the window size
* `:resize n` to manually set a size
* `^W-q` or `:q` to quit the current window
* `^W-c` or `:hide` to close the current window, sets the hidden option on the buffer
* `^W-o` or `:only` to close all windows except this one

Vim uses buffers to handle multiple windows. Use `:ls` or `:buffers` or `:files` to get a list of
current buffers. Some status indicators:

* `u` means the buffer is unlisted (use `:ls!` to show it)
* `%` is the current buffer in the window
* `#` is the alternate buffer
* `a` is the active buffer that's loaded/visible
* `h` is a hidden buffer
* `-` and `=` is readonly, the later meaning no permissions
* `+` is a modified buffer
* `x` is a buffer with read errors

Vim has a few special buffers:

* quickfix used to hold compile/debug errors. Can be viewed with the commands `:cwindow` or
  `:lwindow`
* help for the built-in documentation
* directory which lets you move around in a directory
* scratch is an expendable buffer for general purposes

When working with buffers, these commands are handy:

* `windo cmd` executes the cmd in all visible buffers
* `bufdo cmd` operates on all open buffers, even the invisible ones
* `:ls`, `:files`, `:buffers` list buffers, add `!` to view special ones
* `:badd file` add file to buffer list
* `:bdel`, `:bdelete` will remove buffer from buffer list
* `:b number`, `:b filename` or the longer version `:buffer arg` to edit a file. Use tab for
  autocompletion of filename. Prefix with `s` to open in a new window
* `:bn`, `:bnext`, `:bp`, `:bprev` edits the next/previous buffer. Takes a count argument.
* `:bN`, `:bNext`, `:bP`, `:bPrev` will move active buffer next or previous. Takes a count argument.

# Vim Scripts

Robbins starts off with color scheme customization:

    colorscheme desert

Stick that into your `.vimrc` to update your colorscheme. Use the command `:colorscheme <tab>` to
toggle available colorschemes.

Vim has conditional constructs:

    if cond expr
      line of vim code
    elseif some secondary expr
      another line of vim code
    else
      last line of vim code
    endif

Vim also supports the ternary operator:

    cond ? expr 1 : expr 2

Vim variables can be set using `let varname = "value"`. Variables are prefixed with a letter and a
colon. Each letter has some significance:

* `b:` variable for single vim buffer
* `w:` for single vim window
* `t:` for single vim tab
* `g:` recognized globally
* `s:` within sourced script
* `a:` a function argument
* `v:` a vim variable, only Vim should use it

Let's look at our first program:

    let currentHour = strftime("%H")
    echo "currentHour is " . currentHour
    if currentHour < 6 + 0
      let colorScheme ="darkblue"
    elseif currentHour < 12 + 0
      let colorScheme = "morning"
    elseif currentHour < 18 + 0
      let colorScheme = "shine"
    else
      let colorScheme = "evening"
    endif
    echo "setting color scheme to" . colorScheme
    colorscheme colorScheme

The last line will produce an error because `colorScheme` will be mistaken for a literal (there's no
colorscheme by that name). Instead, change the line to use `execute`:

    execute "colorscheme " . colorScheme

Vim also supports functions:

    function myFunction (arg1, arg2...)
      line of code
    endfunction
    call myFunction(arg1, arg2)

And arrays:

    let g:Favcolorschemes = ["darkblue", "morning", "shine", "evening"]
    g:Favcolorschemes[0]

Vim uses autocommands to execute commands on certain events. Some events are:

* BufNewFile - triggered when editing a new file
* BufReadPre - right before vim moves to a new buffer
* BufRead, BufReadPost - right after vim moves to a new buffer
* BufWrite, BufWritePre - right before writing to disk
* FileType - triggered after setting filetype
* VimResized - triggered when resizing a window
* WinEnter, WinLeave - window events
* CursorMoved, CursorMovedI - cursor moved in normal or insert mode

The autocmd format is as follows:

    autocmd [group] event pattern [nested] command

The events were listed above. The pattern is the file pattern for which these commands should be
executed if matched. The nested flag says whether or not this command can be nested with others. For
example:

    autocmd CursorMovedI * call CheckFileType()

Variables prefixed with `&` represents options. You can check certain options such as:

    if &filetype == ""

Autocommands can be associated with groups for quick referencing and dereferencing.

    augroup groupname
      autocommand lines
    augroup END

You can then delete autocommands:

    autocmd! [group] [event] [pattern]

A little bit more about variables. These types are supported:

* number
* string
* funcref
* list
* dictionary

There are a ton of built-in functions to help you with your scripts. Check out:

* `:help usr_41.txt`
* `:help autocmd`
* `:help scripts`
* `:help variables`
* `:help functions`

# Vim Enhancements for Programmers

Vim has a lot of features for programmers: folding, auto indenting, keyword and dictionary word
completion, tags, syntax highlighting, quickfix.

There are six ways of creating folds: manually, indentation, regular expressions, syntax, diffs, and
predefined markers. All fold commands are prefixed with `z`:

* `zA` toggle state of folds
* `zC` close folds
* `zD` deletes folds
* `zE` eliminates all folds
* `zf` creates a fold from current line to motion command
* `countzF` create fold for count lines
* `zM` set option foldlevel to 0
* `zN`, `zn` set or reset foldenable option
* `zO` opens folds
* `za` toggle state of one fold
* `zc` close one fold
* `zd` delete on fold
* `zi` toggle foldenable option
* `zj`, `zk` move cursor to start of end of next/prev fold
* `zm`, `zr` decrement or increment foldlevel
* `zo` open one fold
* folding works with visual mode also
* `:loadview` and `:mkview` to load and save folds

For programming, try `:set foldmethod=syntax`. Vim will automatically detect the correct folds for
your source code.

Vim has a few different options for autoindent which can be set like `:set autoindent`:

* `autoindent` works just like in vi, newlines start indented like the previous line
* `smartindent` recognizes basic C syntax primitives
* `cindent` recognizes C syntax almost completely
* `indentexpr` lets you define your own indent expressions

`smartindent` automatically inserts or removes indents on angle brackets { and }, any line
proceeding line beginning with keyword contained in `cinwords`, new lines preceding closed braces.

`cindent` uses the `cinkeys` to signal reevaluation of indentation, `cinoptions` to define
indentation style, and `cinwords` to signal an indent. cinkeys is a comma separate list:

    0{,0},0),:,0#,!^X^F,o,O,e

Let's break this apart:

* `0{` means if the bracket is found at the beginning of a line
* `0}` and `0)` mean the same
* `:` is for C's case statement
* `0#` another beginning of line context
* `!^F` exclamation point means the follow character is a trigger to reevaluate indentation. In this
  case, `^F` will reevaluate indentation.
* `o` covers new lines below
* `O` covers new lines above
* `e` covers the `else` keyword

The syntax rules for `cinkeys` are:

* `!` causes reevaluation on next key
* `*` reevaluate current line indentation before inserting key
* `0` beginning of line context
* `<>` contains special characters like `<Up>`
* `^` specifies control character
* `=word`, `=~word` words defining special behavior, maybe ignoring case

`cinwords` is a comma separated list, where each word signals vim to indent:

    let cinwords=if,else,while,do,for,switch

You can turn off auto indentation temporarily when you want to paste in text that's already
indented. Use `:set paste` before pasting, then turn it off with `:set nopaste`.

Vim has autocompletion commands, each start with `^X`. For example, to autocomplete filenames use
`^X-^F`. Then use `^N` to move next and `^P` to move previous.

* `^X-^L` tries to complete the whole line by looking through your file history
* `^X-^N` autocompletes keywords, defined by `iskeyword` option
* `^X-^K` autocompletes dictionary words
* `^X-^T` autocompletes by thesaurus
* `^X-^I` autocompletes using keywords in current and included files
* `^X-^]` uses tags for autocompletion
* `^X-^F` autocompletes filename in current directory
* `^X-^D` autocompletes macros (using `#define`)
* `^X-^V` autocompletes vim commands (for vim scripts)
* `^X-^U` user customizable function, calls `completefunc`
* `^X-^O` completion via omni function, user defined function that's filetype specific.
* `^X-^S` spell correcting
* `^N` combines all previous autcompletes into one, can be customized with the `complete` option

The `complete` option can customize `^N` sources. It's a comma separated list:

* `.` searches current buffer
* `w` searches other windows
* `b` searches loaded buffers
* `u` searches unloaded buffers in buffer list
* `U` searches buffers not in buffer list
* `k` searches dictionary file
* `kspell` for spelling
* `s` for thesaurus
* `i` searches current and included files
* `d` searches current and included files for macros via `#define`
* `t`, `]` search for tag completion

Vim supports ctags, a Unix program to index source code. You can generate it via `:!ctags *.[ch]`.
To output a custom tagfile, use `:!ctags -f filename *.c` and `set tags=filename`.

* `:tag name` to lookup the tag, this works well with tab autocompletion
* `:tn` and `:tp` to go to the next/prev tag for multiple matches. Can be prefixed with a count.
* `:ts [name]` to list all current matches or matches for name
* `^]` while your cursor is over an identifier to jump to it
* `^T` or `:pop` to go back to your initial location. Pop can be prefixed with a count.

One of the best features of Vim is syntax highlighting:

    :syntax enable
    :syntax on

You can force Vim to use a certain language for syntax highlighting via `:set syntax=language` One
of the best features of Vim is syntax highlighting:

    :syntax enable
    :syntax on

You can force Vim to use a certain language for syntax highlighting via `:set syntax=language`.

Vim offers quickfix, an IDE-like edit-compile-debug cycle. You can use `make` from Vim, any
compilation errors will end up in a Quickfix List window. Move your cursor over any errors and hit
`Enter` to go to it. Or you can use the command `:cnext` or `:cn`.

Some additional info about quickfix:

* `makeprg` is the option for your project's make or compile program
* `:cnext`, `:cprevious` to go to next or previous errors
* `:colder`, `:cnewer` to load in older or newer error lists. Takes count.
* `:clist` to list all current errors
* `errorformat` is an option to integrate the make program's error format with vim. Use `:help
  errorformat` for more info.

Quickfix also works with `vimgrep`. To find all occurrences of a phrase:

    :vimgrep phrase *.c *.h

Now use the regular quickfix commands to cycle through.