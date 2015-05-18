# Bash 入门

<!-- MarkdownTOC -->

- 删除指定文件
- shebang

<!-- /MarkdownTOC -->


## 删除指定文件

    find . -name ".Ulysses-Group.plist" -exec rm -Rf {} \;

## shebang

脚本的第一行叫 shebang，用来告知系统如何执行该脚本

    #!/bin/bash
