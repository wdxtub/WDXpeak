# Bash 入门

<!-- MarkdownTOC -->

- 删除指定文件
- 给权限操作
- 基本操作
- 条件流程
- 表达式
- 上下文依赖
- 其他

<!-- /MarkdownTOC -->


## 删除指定文件

    find . -name ".Ulysses-Group.plist" -exec rm -Rf {} \;

## 给权限操作

    chmod 777 ./start.sh

## 基本操作

+ 脚本的第一行叫 shebang，用来告知系统如何执行该脚本 `#!/bin/bash`
+ 输出内容 `echo "Hello world!"`
+ 每一句指令用换行或分号隔开
+ 声明一个变量(不能有空格) `VARIABLE="Some string"`
+ 使用变量 `echo $VARIABLE`, `echo "$VARIABLE"`, `echo '$VARIABLE'`
+ 当赋值和 export 时，或者以其他方式使用变量时，变量名前不加 $
+ 如果要使用变量的值，则要加 $
+ 带你引号不会展开变量
+ 在变量内部进行字符串替换 `echo ${VARIABLE/Some/A}` 会把 VARIABLE 中首次出现的 Some 替换成 A
+ 内置变量 `$?`, `$$`, `$#`, `$@`

例子

    echo "Last program return value: $?"
    echo "Script's PID: $$"
    echo "Number of arguments: $#"
    echo "Scripts arguments: $@"
    echo "Scripts arguments separated in different variables: $1 $2"

+ 读取输入 `read NAME` 不需要声明新变量

## 条件流程

通常的 IF

    if [ $NAME -ne $USER ]
    then
        echo "Your name is your username"
    else
        echo "Your name isn't your username"
    fi

Bash 的 case 语句与 Java 和 C++ 中的 switch 语句类似:

    case "$VARIABLE" in
        # 列出需要匹配的字符串
        0) echo "There is a zero.";;
        1) echo "There is a one.";;
        *) echo "It is not null.";;
    esac

## 表达式

+ 格式 `echo $(( 10 + 5 ))`

## 上下文依赖

+ bash 运行时依赖上下文
+ `ls` 列出当前目录
+ `ls -l` 列出文件和目录的详细信息，指令可以带有选项
+ 前一个指令的输出可以当做后一个指令的输入。`grep` 用来匹配字符串
+ 用下面的指令列出当前目录下所有的 txt 文件 `ls -l | grep "\.txt"`
+ 重定向可以到输出，输入和错误输出。 > 会覆盖已存在的文件，>> 会以累加的方式输出文件中

例如

    python hello.py < "input.in"
    python hello.py > "output.out"
    python hellp.py >> "error.err"

+ 一个指令可用 `$()` 嵌套在另一个指令内部，如 `echo "There are $(ls | wc -l) items here."`

## 其他

循环遍历给定的参数序列:变量$VARIABLE 的值会被打印 3 次。注意 \` \` 和 $( ) 等价。seq 返回长度为 3 的数组。

    for VARIABLE in `seq 3`
    do
        echo "$VARIABLE"
    done

你也可以使用函数，定义函数：

    function foo ()
    {
        echo "Arguments work just like script arguments: $@"
        echo "And: $1 $2..."
        echo "This is a function"
        return 0
    }

更简单的方法

    bar ()
    {
        echo "Another way to declare functions!"
        return 0
    }


调用函数

    foo "My name is" $NAME

有很多有用的指令需要学习:

    tail -n 10 file.txt

打印 file.txt 的最后 10 行

    head -n 10 file.txt

打印 file.txt 的前 10 行

    sort file.txt

将 file.txt 按行排序

    uniq -d file.txt

报告或忽略重复的行，用选项 -d 打印重复的行

    cut -d ',' -f 1 file.txt

打印每行中 ',' 之前内容
