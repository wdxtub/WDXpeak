# Tmux: Productive Mouse-Free Development

This is a short handbook on [tmux](http://tmux.sourceforge.net) by Brian Hogan. These notes are
mostly just cheat sheets that cover the commands on Linux. You can always grab a full cheat sheet in
tmux with `C-b ?`.

# Learning The Basics

Install tmux using your OS's package manager.

    $ sudo apt-get install tmux  # ubuntu
    $ sudo pacman -Ss tmux       # arch
    $ sudo emerge tmux           # gentoo

Start and quit tmux is easy:

    $ tmux
    $ exit

Tmux works with **sesions**, **windows**, and **panes**. A session is usually tied to a project but
you can create sessions for anything. A window is like a terminal tab. Windows can have multiple
panes on them, for example have an editor running on the left and a REPL on the right.

For working with sessions:

* `tmux new-session` creates new session without name, shorcut is `tmux new` or just `tmux`
* `tmux new -s development` creates seeion called "development"
* `tmux new -s development -n editor` creates session and names first window "editor"
* `tmux attach -t development` attaches session named development

Keyboard shortcuts that are used often:

* `C-b d` detaches from session leaving it on the background
* `C-b :` enter command mode
* `C-b c` creates new window
* `C-b 0..9` switches to window
* `C-b w` shows selectable list of windows
* `C-b ,` prompt to rename window
* `C-b &` closes current window
* `C-b %` splits window vertically
* `C-b "` splits window horizontally
* `C-b o` cycles through panes
* `C-b q` momentarily show pane numbers
* `C-b x` closes current pane
* `C-b Space` cycles through pane layouts

# Configuring tmux

When tmux starts, it reads `~/.tmux.conf` for configuration. You can automatically run commands or
bind/unbind keys.

* `set -g [setting] [value]` to globally set settings
* `set -g prefix C-a` sets new key combo for Prefix key
* `setw -g [setting] [value]` to set a window setting
* `source-file [file]` to load a coniguration file
* `bind [key] [command]` to bind a key to run a command
* `bind -r [key] [command]` to bind a repeatable command where the Prefix only has to be hit once
* `set -g repeat-time [ms]` how long tmux waits for repeated combos
* `unbind [key]` to unbind a key combo
* `display [text]` displays text on status line

Use `C-b ?` to see what commands exist.

A useful setting is to set the base index to 1 for windows, otherwise the first window is 0: `set -g
base-index 1`. Do the same with panes `setw -g pane-base-index 1`.

Bind a shortcut to refresh your config: `bind r source-file ~/.tmux.conf \; display "Reloaded!"`.
You can run multiple commands by splitting them with `\;`.

Make sure your session is working with 256 colors. To test it:

    $ wget http://www.vim.org/scripts/download_script.php?src_id=4568 -O colortest
    $ perl colortest -w

And validate that each line is a different color. To configure your terminal, add this line to your
`.bashrc` or `.zshrc`:

    [ -z "$TMUX" ] && export TERM=xterm-256-color

Then add this to `.tmux.conf`:

    set -g default-terminal "screen-256color"

Tmux lets you configure the UI, from colors to adding to the status bar. Run this script to figure
out which colors you have:

    for i in {0..255} ; do
      printf "\x1b[38;5;${i}mcolour${i}\n"
    done

Some things you can change:

    set -g status-fg color
    set -g status-bg color
    setw -g window-status-fg color
    setw -g window-status-bg color
    setw -g window-status-attr color
    setw -g window-status-current-fg color
    setw -g window-status-current-bg color
    setw -g window-status-current-attr color
    set -g pane-border-fg color
    set -g pane-border-bg color
    set -g pane-active-border-fg color
    set -g pane-active-border-bg color
    set -g message-fg color # command line for tmux
    set -g message-bg color
    set -g message-attr color
    setw -g monitor-activity on/off
    setw -g visual-activity on/off

You can configure your status lines with:

    set -g status-left "string"
    set -g status-left-length num
    set -g status-right "string"
    set -g status-right-length num
    set -g status-utf8 on
    set -g status-interval seconds
    set -g status-justify centre

For the `"string"` portion, these variables are available:

* `#H` hostname of localhost
* `#h` hostname of localhost without domain
* `#F` current window flag
* `#I` current window index
* `#P` current pane index
* `#S` current session name
* `#T` current window title
* `#W` current window name
* `##` literal #
* `#(shell-command)` first line of shell output
* `#[attributes]` color or attribute change

For example on attributes:

    set -g status-left "#[fg=green]Session: #S #[fg=yellow]#I"

# Scripting Customized tmux Environments

This chapter is all about setting up tmux so projects are tied to sessions and resuming a project
should be as easy as a single command.

Here's an example script:

    tmux has-session -t development
    if [ $? != 0]
    then
      tmux new-session -s development -n editor -d
      tmux send-keys -t development 'cd ~/devproject' C-m
      tmux send-keys -t development 'vim' C-m
      tmux split-window -v -t development
      tmux select-layout -t development main-horizontal
      tmux send-keys -t development:1.2 'cd ~/devproject' C-m
      tmux new-window -n console -t development
      tmux send-keys -t development:2 'cd ~/devproject' C-m
      tmux select-window -t development:1
    fi
    tmux attach -t development

Stick that into an executable file like `~/development` and run it to start your editor and REPL.

Instead of a shell script, you can stick it into a `app.conf` file and have tmux execute it. Just
remove all the `tmux` prefixes and add `source-file ~/.tmux.conf` at the top. To run it:

    $ tmux -f app.conf attach

`tmuxinator` provides a nicer way to do this for each of your projects. Configuration is done in
YAML and the files are stored in a central location.

    $ gem install tmuxinator
    $ tmuxinator open development
    # ... edit config ...
    $ tmuxinator devproject
    # ... runs the config ...
    $ tmuxinator open devproject
    # ... lets you do further edits ...

# Working With Text and Buffers

Some tmux commands:

* `C-b [` to enter copy mode
* `C-b ]` pastes current buffer contents
* `C-b =` lists paste buffers and pastes selected buffer

When you're in copy mode, use these keys:

* `Space` to start highlighting
* `Enter` during highlight to copy
* `h`, `j`, `k`, `l` to move around
* `w`, `b` for movement by words
* `f`, `F` to next/previous occurrence of character
* `C-b`, `C-f` to go up/down a page
* `g`, `G` to jump to top/bottom of buffer
* `?`, `/` to start searching

Some handy tmux commands to use:

* `show-buffer` displays current buffer
* `capture-pane` to capture entire pane
* `list-buffers` lists all paste buffers
* `choose-buffer` lets you choose content
* `save-buffer [filename]` to save to a file

On Linux, it's useful to get `xclip` which can integrate the command line and system clipboards.

    $ sudo apt-get install xclip

Now some bindings to work with xclip:

    bind C-c run "tmux save-buffer - | xclip -i -sel clipboard"
    bind C-v run "tmux set-buffer \"$(xclip -o -sel clipboard)\"; tmux paste-buffer"

# Pair Programming with tmux

You can create a new user account on a computer for others to ssh in and share a tmux session. You
can also use tmux sockets for a second user to connect to your tmux. The third way is to setup a
cheap third party machine to share.

If you create a new user, just create a session and have that user attach it:

    ted123$ tmux new-session -s pairing
    barney$ tmux attach -t pairing

You can also create grouped sessions so each user can independently create windows and stay on their
own:

    ted123$ tmux new-session -s groupedsession
    barney$ tmux new-session -t groupedsession -s mysession

Tmux works with sockets:

    ted123$ tmux -S /var/tmux/pairing
    barney$ tmux -S /var/tmux/pairing attach

# Workflows

* `C-b !` turn a pane into a new window
* `join-pane -s 1` joins window #1 into current window
* `join-pane -s 1.0` joins window #1, pane #0 into current window
* `move-window -s sessionname:1 -t newsession` moves windows

Some tmux commands lets you execute shell commands also:

    $ tmux new-sesion -s servers -d "ssh deploy@burns"
    $ tmux split-window -v "ssh dba@smithers"
    $ tmux attach -t editor

When sessions are created this way, they exit when the process ends. Use these keys to move between
sessions:

* `C-b (` move left
* `C-b )` move right
* `C-b s` list of sessions

When you're done with a session:

    $ tmux kill-session -t sessionname

Set the default shell:

    set -g default-command /bin/zsh
    set -g default-shell /bin/zsh

Or run tmux by default by sticking this at the end of `.bashrc` or `.zshrc`:

    if [[ "$TERM" != "screen-256color" ]]
    then
      tmux attach-session -t "$USER" || tmux new-session -s "$USER"
      exit
    fi