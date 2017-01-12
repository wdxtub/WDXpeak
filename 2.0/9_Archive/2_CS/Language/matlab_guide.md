# Matlab 指南

## 有趣的命令

+ 在命令行敲入 `dbstop if error`。如果运行出现错误，matlab会自动停在出错的那行，并且保存所有相关变量

## MIT Matlab 2-day Tutorial

### The Basics

Calculator functions work as you'd expect:

```
>>(1+4)*3

ans =

    15
```

`+` and `-` are addition, `/` is division, `*` is multiplication, `^` is an exponent.

You can assign variables from the matlab workspace. Everything in matlab is a matrix. (If it's a scalar, it's actually a 1x1 matrix, and if it's a vector, it's an Nx1 or 1xN matrix.)

```
>>a = 3
a =

     3
```

To create a vector is pretty similar. Each element is separated by spaces, the whole vectore is in square brackets:

```
>>v = [1 3 6 8 9]
```

To create a vector of values going in even steps from one value to another value, you would use

```
>>b = 1:.5:10
```

This goes from 1 to 10 in increments of .5. You can use any increment, positive or negative, you just have to be able to get to the last thing from the first thing, using those increments. If you don't put in an increment, it assumes it's 1, so 1:5 gives you the vector [1 2 3 4 5].

To turn a row vector into a column vector, just put a ' at the end of it. (This is also how to get the transpose of a matrix.) To create a matrix, you could do something like:

```
c = [1 3 6; 2 7 9; 4 3 1]
```

The semicolons indicate the end of a row. All rows have to be the same length.

Whenever you assign a value in matlab, it will print out the entire value you have just assigned. If you put a semicolon at the end, it will not print it out, which is much faster.

### Dealing with Matrices

Once you have a matrix, you can refer to specific elements in it. Matlab indexes matrices by row and column. c(3,1) is the element in the third row, 1st column, which is 4. c(2:3,1:2) gives you the elements in rows 2-3, and columns 1-2, so you get

```
2 7
4 3
```

as a result. c(1:3,2) gives you the elements in rows 1-3, and the second column, that is, the entire second column. You can shortcut this to:
c(:,2)

literally telling matlab to use all the rows in the second column, ie, the 2nd column.

You can get a whole row of a matrix with

```
c(1,:)
```

This literally tells matlab to take the first row, all columns.

You can also refer to any matrix with only one index. It will use that index to count down the columns. c(5) will give you 7, for example.

When you have a matrix or vector (anything with more than one element) you need to do a few things to make sure all of your math does what you want it to. You can add a constant or multiply by a constant normally (const+c, const*c, etc.) If you have data in two matrices that correspond (for example, a time vector and an x position vector that has x values for each point in time), you can add and subtract those normally (it will map each element properly.)

To multiply, divide, or raise to a power when you have a matrix or vector that is acting as a set of data points, you need to use

```
.*
./
.^

```

so that matlab will multiply each element in the matrix instead of trying to do matrix multiplication or division.

Of course, it can also treat matrices as actual matrices, so you can solve something like [A]x = b where A is a matrix of coefficients, x is a column vector of the x values you want to find, and b is also a column vector just by doing

```
x = A\b
```

after you define A and b. The `\` represents "left division" (since to solve that equation you would have to divide both sides by A on the *left* side, since order is significant when dealing with matrices.).

### useful functions

Matlab has a lot of built-in functions. To use a function, just type functionname(arguments) with the appropriate name and arguments. If you create a time vector t=1:.25:6; you can get standard functions like

```
x = sin(t)
```

which returns a vector the same size as t, with values for the sin of t at all points. You can also do things like

```
s = sum(c)
```

which sums all the `columns` in a matrix c and returns a row vector of the sums.

The function `d = det(c)` takes a matrix c and returns the determinant of it. The matlab booklet has a list of many of these useful functions.

### Help and other tools

Places to get help:

+ Typing "help" at the matlab prompt gives you a list of all the possible directories matlab can find commands in (which also tells you its "search path", or a list of the directories it is looking in for commands.)
+ Typing "help directoryname" gives you a list of the commands in that directory and a short description of them.
+ Typing "help commandname" gives you help on a specific command.
+ Typing "lookfor keyword" gives you a list of commands that use that keyword. ie, "lookfor integral" lists commands that deal with integrals. It's pretty slow, choose the word wisely. You can use control-c to stop searching when you think you've found what you need.
+ Typing "doc" starts up a web browser with the Matlab on Athena home page. This includes the entire reference manual for matlab, a whole lot of other information on using matlab, and a pointer to the Matlab Primer, a good introduction to using Matlab.
+ You can get copies of "Matlab on Athena" at Graphic Arts. You can also get copies of the Matlab Primer mentioned above. (There's a small fee for copying costs on both.)
+ The matlab manual and manuals for many of the toolboxes are available in some clusters and can be borrowed from the consultants' office in 11-115.

Some Useful Tools:

+ If you accidentally reassign a function name to a variable (ie, you try saying sum = 3 and then you get errors when you try to use the sum function because it doesn't know it's a function anymore), you can restore it to its normal state using "clear functionname". You can also use clear to get rid of all variable values with "clear all".
+ `who`: will tell you all the variables you have currently defined.
+ `whos`: will tell you the variables, their sizes, and some other info.
+ `pi`: is a function of that returns the value of pi.
+ `eps`: is a function that returns Matlab's smallest floating point number. This is useful if you have a vector that might contain zeros that is going to wind up in the denominator of something. If you add eps to the vector, you aren't actually adding anything significant, but you won't run into divide by zero problems anymore.
+ `format long` & `format short`: switch between the long and short display format of numbers. Either way matlab uses the same number of digits for its calculations, but normally (format short) it will only display the first four digits after the decimal point.
+ Typing `type`: functionname for any function in Matlab's search path lets you see how that function is written.

### Plotting

The basic syntax to get a plot in matlab is

```
plot(x1,y1)
```

(The x values always come before the y values, x1 and y1 represent variables that your data is stored in.) If you type a second plot command later, it will clear your first plot. If you type `hold on` it will hold the current plot so you can add plots on top of one another (until you reset it by typing `hold off`.)

You can plot multiple values with `plot(x1,y1,x2,y2)` and you can specify the color and linetype of a plot as something like `plot(x1,y1,'w*')` to get white *'s for each data point.

To split your plot into a bunch of smaller plots, you can use the subplot command to split it up into rows and columns.

```
subplot(r,c,n)
```

will split the plot window into r rows and c columns of plots and set the current plot to plot number n of those rows and columns. For example, subplot(2,1,1) splits the plot window into two rows in a single column and prepares to plot in the top plot. Then your plot command will plot in the top plot. Then you could switch to the bottom plot with subplot(2,1,2) and use another plot command to plot in the bottom plot.

You can add titles, labels, and legends to plots.

```
title('This is a Title')
xlabel('My X axis')
ylabel('My Y axis')
legend('First Thing Plotted','Second Thing Plotted')
```

legend creates a legend box (movable with the mouse) that automatically uses the right symbols and colors and sticks the descriptions in the legend command after them.

### Printing, Saving, and Loading

Basic printing

```
>>print -Pprintername
```

You can also save to a Postscript or Encapsulated Postscript file:

```
>>print -dps filename.ps

>>prind -deps filename.eps
```

You can also save your plot as an m-file (matlab script) which should contain all the commands you need to recreate your plot later. This is about 98 percent accurate.

```
>>print -dmfile filename.m
```

You can save and load files as either text data or matlab's own data format. If you have a text file consisting of a bunch of columns of data separated by spaces or tabs, you can load it into matlab with

```
load filename.dat
```

This command will give you a matrix called filename. Then you can reassign columns of that matrix, ie

```
col1 = filename(:,1);
```

When you save data using the command

```
save filename.mat
```

, matlab will save all of your variables and their values in its own format, so that when you load it using

```
load filename.mat
```

you will have all of your variables already defined and names.

### Polynomials and Fitting

Matlab can treat a vector as a polynomial. It will assume that the numbers represent the coefficients of the polynomial going from highest-order to lowest order.

```
>>p = [1 2 2 4 1]
```

can represent the polynomial `x^4 + 2x^3 + 2x^2 + 4x + 1`. There are a number of functions that use this representation of polynomials:

```
>>roots(p)
```

gives you the roots of the polynomail represented by the vector p.

```
>>polyval(p,4)
```

gives you the value of the polynomial p when x = 4. Similarly,

```
>>polyval(p,[1:10])
```

gives you the value of the polynomial evaluated at each of the points in the vector. (It returns another vector the same size.)

You can fit polynomials to data sets using this representation and a function called curvefit.

```
>>[p, fitted] = curvefit(x,y,n)
```

fits the data in x and y to an nth order polynomial (using 1 gives you a straight line, 2 gives you a quadratic, etc), and plots both the data and the fitted curve for you. It returns p, the polynomial representing the equation of the fitted curve, and fitted, the data points you get from the curvefit for each of the x's in your data set.

You can use polyval and the fitted polynomial p to predict the y value of the data you've fitted for some other x values.

```
>>ypred = polyval(p,xvalues)
```

### Logical Conditions and Matrices

`a = [ 1 2 3 4 5 6]`

and I refer to a(a>3) I will get only the elements of a where a is greater than 3. You can combine these logical statements. Typing "help ops" will list all of the logical functions and operators you can use for this.

I can also create a second matrix the same size as a: `b = [7 8 9 10 11 12]`

and then referring to b(a<3) will give the elements of b which correspond to where a is less than 3 (that is, [7 8]).

The reason this works is because matlab logical functions are designed to return a matrix or vector of 1's and zeros. If I just typed

```
>> a>3
```

I would get [0 0 0 1 1 1] as a result. The first 3 elements are zero, because those elements are not greater than 3 (F), and the last are 1 because those elements are greater than 3 (T). Then, matlab can accept matrices like this as a way of specifying indexes for another matrix of the same size. If I just typed

```
>> a([0 0 1 0 0 1]),
```

I would get [3 6] as a result because those are the elements where 1's appear in the vector I gave as my "index" vector.

This logical indexing capability allows you to do a lot of efficient things with large matrices because you very rarely have to loop through a whole matrix in order to get only specific parts of it. Example: You have a matrix called volt with 50,000 values of voltages over time, and a corresponding matrix called t. To find the mean voltage between time 20 and time 30, you can use

```
>>mean(volt(t>20 & t<30))
```

to get the result.


### Writing Functions and Scripts

All matlab functions and scripts are plain text files that contain matlab commands. Matlab will treat any file that ends in .m as either a function or a script. It can find .m files you've written that are in your ~/matlab directory, in the directory you have cd'd into from the matlab prompt, or in a directory you've started matlab with (ie,

```
matlab /mit/2.670/Computers/Matlab/Examples
```

starts up matlab and adds that directory to the places matlab will look for .m files in.)

#### Scripts

A script is just a list of commands to be run in some order. Placing these commands in a file that ends in .m allows you to "run" the script by typing its name at the command line. You type the name of the script without the .m at the end.

#### Functions

A function is capable of taking particular variables (called arguments) and doing something specific to "return" some particular type of result. A function needs to start with the line

```
function return-values = functionname(arguments)
```

so that matlab will recognize it as a function. Each function needs to have its own file, and the file has to have the same name as the function. If the first line of the function is

```
function answer = myfun(arg1,arg2)
answer = (arg1+arg2)./arg1
```

then the file must be named myfun.m. The function has arg1 and arg2 to work with inside the function (plus anything else you want to define inside it, and possibly some global variables as well), and by the end of the function, anything that is supposed to be returned should have a value assigned to it. This particular function is just one line long, and it returns answer, which is defined in terms of the two arguments arg1 and arg2.

#### Some useful tools for functions and scripts

+ nargin
    + used within a function tells you how many arguments the function was called with.
    + You can write functions that can accept different numbers of arguments and decide what to do based on whether it gets two arguments or three arguments, for example.
+ eval
    + lets you take a string and run it as a matlab command.
    + For example, if I have to plot 20 similar data files for trials and I want to load each file and use the filename in the title, I can write a function that takes the filename as a string as an argument. To load it in the function, I can use
    + `str = ['load ' filename]`
    + to put together a command string, and
    + `eval(str)`
    + to run that command.
    + Then to use the filename in the title, I can use
    + `str = ['title(' filename ')']`
    + eval(str)
+ feval
    + evaluates a function for a given set of arguments. For example, `feval('sin',[0:pi/4:2*pi])` is the same thing as saying `sin([0:pi/4:2*pi])`. If you're dealing with a situation where you might want to specify which function to use as an argument to another function, you might use feval.

### Global Variables

When you define a variable at the matlab prompt, it is defined inside of matlab's "workspace." Running a script does not affect this, since a script is just a collection of commands, and they're actually run from the same workspace. If you define a variable in a script, it will stay defined in the workspace.

Functions, on the other hand, do not share the same workspace. A function won't know what a variable is unless the it gets the variable as an argument, or unless the variable is defined as a variable that is shared by the function and the matlab workspace, or a global variable.

To use a global variable, every place (function, script, or at the matlab prompt) that needs to share that variable must have a line near the top identifying it as a global variable, ie:

```
global phi;
```

Then when the variable is assigned a value in one of those places, it will have a value in all the places that begin with the global statement.

### Loops and Control

Sometimes, you do need to use some kind of loop to do what you need, rather than just operating on an entire matrix or vector at once.

#### While Loops

The syntax for a while loop is

```
while (some logical expression)
    do something;
    do something else;
end
```

To keep this from going on forever, you should probably be changing some variable in the logical expression within the body of the loop so that it eventually is not true.

#### For

The syntax for a for loop is:

```
FOR X = 1:N,
    A(X) = 1/(2+X-1);
END
```

You should try to avoid using i and j as counters, since you will wind up redefining i (which is intially defined as the imaginary i.)

#### If

The syntax for an if statement is

```
if (logical expression)
    matlab command
elseif (other logical expression)
    another matlab command
else
    a matlab command
end
```

(You don't need an elseif or an else, but you do need an end.)

#### break

The break command breaks you out of the innermost for or while loop you are in.

In the process of a loop, if you define an element of an vector that doesn't exist yet (the vector is smaller than the element you're trying to assign), matlab will increase the size of the vector or matrix to allow for the new element to go where you've specified. However, if you know that you're going to be assigning elements until the matrix grows to be some specific size, it's better to "preallocate" the matrix by defining it to be all zeros initially.

    matrix = zeros(rows,columns);

will do that.

### Debugging Functions

Matlab has an extensive debugger that allows you to examine what is going on inside a function when you encounter problems with it. If you type "help debug" at the matlab prompt, it will list all of the debugging commands available.

Debugging commands.

    dbstop     - Set breakpoint.
    dbclear    - Remove breakpoint.
    dbcont     - Resume execution.
    dbdown     - Change local workspace context.
    dbstack    - List who called whom.
    dbstatus   - List all breakpoints.
    dbstep     - Execute one or more lines.
    dbtype     - List M-file with line numbers.
    dbup       - Change local workspace context.
    dbquit     - Quit debug mode.

Normally, you would enter the debugger by setting a breakpoint either at the beginning of your function (dbstop in functionname) or at the point where an error first occurs (dbstop if error).

    help dbstop

lists some other ways to set a debugging stop to enter debug mode. When it "stops" at the breakpoint, you will be in the debugger. The prompt looks like K>> instead of >>. The debugger indicates the next line it will run.
When it's printed a line out, it has not yet run that line. It will run that line the next time you type "dbstep" to step down another line in the function.

Then you can examine the variables in the function, try to determine what might have the wrong value, do logical tests, and step through the function one line at a time using "dbstep" to see what the function is doing step-by-step.

### Vectorization

Matlab is written to deal with matrices and vectores. Because of that, it is much more efficient to solve problems solely by doing math on your vectors or portions of your vectors, rather than by ever needing to loop through particular elements in your vector and check their values.
You can actually check this out by timing something like taking the sine of a variable for 100 different values of the variable. The logical way to do it in matlab is to create a vector of those 100 different values, and take the sine of that vector. If you do it instead by a for loop from 1 to 100:

```
b = [some vector of 100 elements]
for n = 1:100,
    a(i) = sin(b(i));
end
```

it will take much longer. Sometimes you can't avoid using loops, but if you write your matlab scripts cleverly, you can make them much more efficient. Using logical conditions to select parts of your matrices is one way that is easy to take advantage of in vectorizing your problems.

## 语言基础

+ 变量名规则：字母引导，区分大小写
+ 保留常量：`eps`, `i`, `j`, `pi`, `NaN`, `Inf`, `i=sqrt(-1)`, `lastwarn`, `lasterr`
+ 数值型数据结构
    + 双精度数值变量
        + IEEE 标准，64位，11指数位，53数值位和一个符号位
        + -1.7x10^308 ~ 1.7x10^308
        + `double()` 函数的转换
    + 其他数据类型
        + `uint8`，常用于图像表示和处理，8位
        + `int8()`, `int16()`, `int32()`, `uint16()`, `uint32()`
+ 字符串型数据：用单引号括起来
+ 多维数组：是矩阵的直接扩展，多个下标
+ 单元数组：将不同类型数据集成到一个变量名下面，用`{}`表示
+ 结构体：`A.b`，应用也用`A.b`
+ 类与对象：可以定义重载函数
+ 定义矩阵：`A=[1,2,3; 4,5,6; 7,8,9]`
+ 复数矩阵：`B=[1+9i, 2+8i, 3+7i; 4+6i, 5+5i, 6+4i; 7+3i, 8+2i; 1i]`
+ 函数调用：[返回变量列表]=函数名(输入变量列表)
    + `[a,b,c] = myfun(d,e,f,g)`
+ 冒号表达式：`v=s1:s2:s3`
    + `v1=0:0.2:pi`
    + `v5=[0:0.2:pi, pi]`
+ 子矩阵提取
    + B = A(v1, v2)
    + 提取 A 矩阵全部奇数行，所有列：`B1=A(1:2:end, :)`
    + 提取 A 矩阵 3,2,1 行、2,3,4 列构成子矩阵：`B2=A([3,2,1],[2,3,4])`
    + 将 A 矩阵左右翻转：`B3=A(:,end:-1:1)`

## 基本数学运算

### 矩阵的代数运算

+ 矩阵表示：A 矩阵位 nxm 矩阵
+ 矩阵转置：`B = A.'` 和 `C = A'` 这两种不同
+ 矩阵加减法：`C = A + B` 和 `C = A - B`
+ 矩阵乘法：`C = A*B`
+ 矩阵除法
    + AX = B 求 X -> `X=A\B`
    + XA = B 求 X -> `X=B\A`
+ 矩阵翻转
    + 左右翻转：`B=fliplr(A)`
    + 上下翻转：`C=flipud(A)`
    + 旋转90度：`D=rot90(A)`
+ 矩阵乘方
    + A 为方阵，求 A^x：`F=A^x`
+ 点运算
    + 矩阵对应元素的直接运算：`C=A.*B`

### 矩阵的逻辑运算

+ 逻辑变量
    + 对 double 变量来说，非 0 表示逻辑 1
+ 逻辑运算(相应元素间的运算)
    + 与运算 `A & B`
    + 或运算 `A | B`
    + 非运算 `~A`
    + 异或运算 `xor(A, B)`
+ 各种允许的比较关系：>, >=, <, <=, ==, ~=, find(), all(), any()

### 基本数论运算

+ floor(): `n=floor(x)`
+ ceil(): `ceil(x)`
+ round(): `n=round(x)`
+ fix(): `n=fix(x)`
+ rat(): `[n,d]=rat(x)`
+ rem(): `B=rem(A,C)`
+ gcd(): `k=gcd(n,m)`
+ lcm(): `k=lcm(n,m)`
+ factor(): `factor(n)`
+ isprime(): `v1=isprime(v)`

## 流程控制

**for 结构**

    for i=V
        循环结构体
    end

**while 结构**

    while (条件式)
        循环结构体
    end

例子

    s=0; for i=1:100 s=s+i; end
    s=0; i=1;
    while(i<=100), s=s+i; i=i+1; end

**转移结构**

    if (条件 1)
        语句组 1
    elseif (条件 2)
        语句组 2
    ...
    else
        语句组 n+1
    end

**开关结构**

    switch 开关表达式
    case 表达式 1
        语句段 1
    case {表达式 2, 表达式 3,..., 表达式 m}
        语句段 2
    ...
    otherwise
        语句段 n
    end

**试探结构**

    try, 语句段 1,
    catch, 语句段 2,
    end

## 函数编写

    function [返回变量列表] = 函数名(输入变量列表)
        注释说明语句段，由 % 引导
        输入、返回变量格式的检测
        函数体语句

## 二维图形绘制

**二维图形绘制基本语句**

    t = t1,t2,...,tn
    y = y(t1),y(t2),...,y(tn)

构造向量：

    t=[t1,t2,...,tn]
    y=[y(t1),y(t2),...,y(tn)]

    plot(t,y)

假设有多对这样的向量或矩阵 (t1, y1), (t2, y2), ..., (tm, ym)

    plot(t1, y1, t2, y2, ..., tm, ym)

曲线的性质，如线型、粗细、颜色等，还可以使用下面的命令进行指定

    plot(t1,y1,选项 1,t2,y2,选项 2,...,tm,ym,选项 m)

+ 曲线线型：'-', '--', ':', '-.', 'none'
+ 曲线颜色：'b', 'c', 'g', 'k', 'm', 'r', 'w', 'y', '^'
+ 标记符号：'*', '.', 'x', 'v', 'hexagram', '>', 'pentagram', 'o', 'square', 'diamond', '<'

例：y = sin(tan x) - tan(sin x), x 属于 [-pi, pi]

    x = [-pi : 0.05 : pi];
    y = sin(tan(x)) - tan(sin(x));
    plot(x,y)

**图形元素属性获取与修改**

    set(句柄,'属性名 1', 属性值 1, ..., '属性名 2', 属性值 2, ...)
    v=get(句柄, '属性名')

**其他二维图形绘制语句

+ bar(x,y)
+ comet(x,y)
+ compass(x,y)
+ errorbar(x,y,ym,yM)
+ feather(x,y)
+ fill(x,y,c)
+ hist(y,n)
+ loglog(x,y)
+ polar(x,y)
+ quiver(x,y)
+ stairs(x,y)
+ stem(x,y)
+ semilogx(x,y)
+ semilogy(x,y)

## Introducing Matlab

### (1) Help and basics

    % The symbol "%" is used in front of a comment.

    % To get help type "help" (will give list of help topics) or "help topic"

    % If you don't know the exact name of the topic or command you are looking for,
    % type "lookfor keyword" (e.g., "lookfor regression")

    % When writing a long matlab statement that exceeds a single row use ...
    % to continue statement to next row.

    % When using the command line, a ";" at the end means matlab will not
    % display the result. If ";" is omitted then matlab will display result.

    % Use the up-arrow to recall commands without retyping them (and down
    % arrow to go forward in commands).

    % Other commands borrowed from emacs and/or tcsh:
    % C-a moves to beginning of line (C-e for end), C-f moves forward a
    % character (C-b moves back), C-d deletes a character, C-k deletes
    % the line to the right of the cursor, C-p goes back through the
    % command history and C-n goes forward (equivalent to up and down arrows),
    % tab command completion.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

### (2) Objects in matlab

the basic objects in matlab are scalars,vectors, and matrices...


    N   = 5             % a scalar
    v   = [1 0 0]           % a row vector
    v   = [1;2;3]           % a column vector
    v   = v'                % transpose a vector
                            (row to column or column to row)
    v   = [1:.5:3]          % a vector in a specified range:
    v   = pi*[-4:4]/4           %   [start:end] or [start:stepsize:end]
    v   = []                % empty vector


    m   = [1 2 3; 4 5 6]        % a matrix: 1ST parameter is ROWS
                        %       2ND parameter is COLS
    m   = zeros(2,3)            % a matrix of zeros
    v   = ones(1,3)             % a matrix of ones
    m   = eye(3)            % identity matrix
    v   = rand(3,1)         % random matrix with values in [0,1] (see also randn)

    load matrix_data            % read data from a file:
                        % create a file 'matrix_data' containing:
                        %   2     3     4
                        %   5     6     7
                        %   1     2     3
    matrix_data


    v   = [1 2 3];          % access a vector element
    v(3)                    %   vector(number)
                        % Index starts from 1


    m   = [1 2 3; 4 5 6]
    m(1,3)                  % access a matrix element
                        %   matrix(rownumber, columnnumber)
    m(2,:)                  % access a matrix row (2nd row)
    m(:,1)                  % access a matrix column (1st row)


    size(m)                 % size of a matrix
    size(m,1)               % number rows
    size(m,2)               % number of columns

    m1  = zeros(size(m))        % create a new matrix with size of m

    who                 % list of variables
    whos                    % list/size/type of variables


### (3) Simple operations on vectors and matrices

% (A) Pointwise (element by element) Operations:

    % addition of vectors/matrices and multiplication by a scalar
    % are done "element by element"
    a   = [1 2 3 4];            % vector
    2 * a                   % scalar multiplication
    a / 4                   % scalar multiplication
    b   = [5 6 7 8];            % vector
    a + b                   % pointwise vector addition
    a - b                   % pointwise vector addition
    a .^ 2                  % pointise vector squaring (note .)
    a .* b                  % pointwise vector multiply (note .)
    a ./ b                  % pointwise vector divide (note .)

    log( [1 2 3 4] )            % pointwise arithmetic operation
    round( [1.5 2; 2.2 3.1] )       % pointwise arithmetic operation

% (B) Vector Operations (no for loops needed)

Built-in matlab functions operate on vectors, if a matrix is given, then the function operates on each column of the matrix

    a   = [1 4 6 3]         % vector
    sum(a)                  % sum of vector elements
    mean(a)                 % mean of vector elements
    var(a)                  % variance
    std(a)                  % standard deviation
    max(a)                  % maximum


    a   = [1 2 3; 4 5 6]        % matrix
    a(:)                            % vectorized version of the matrix
    mean(a)                             % mean of each column
    max(a)                              % max of each column
    max(max(a))                 % to obtain max of matrix
    max(a(:))                   %   or...


% (C) Matrix Operations:

    [1 2 3] * [4 5 6]'              % row vector 1x3 times column vector 3x1
                                    % results in single number, also
                                % known as dot product or inner product

    [1 2 3]' * [4 5 6]              % column vector 3x1 times row vector 1x3
                                    % results in 3x3 matrix, also
                                    % known as outer product

    a   = rand(3,2)         % 3x2 matrix
    b   = rand(2,4)         % 2x4 matrix
    c   = a * b             % 3x4 matrix

    a   = [1 2; 3 4; 5 6]       % 3 x 2 matrix
    b   = [5 6 7];          % 1 x 3 vector
    b * a                   % matrix multiply
    a' * b'                 % matrix multiply


### (4) Saving your work

    save mysession                  % creates mysession.mat with all variables
    save mysession a b              % save only variables a and b

    clear all               % clear all variables
    clear a b                       % clear variables a and b

    load mysession              % load session
    a
    b


### (5) Relations and control statements

Example: given a vector v, create a new vector with values equal to v if they are greater than 0, and equal to 0 if they less than or equal to 0.

    v   = [3 5 -2 5 -1 0]       % 1: FOR LOOPS
    u   = zeros( size(v) );     % initialize
    for i = 1:size(v,2)         % size(v,2) is the number of columns
        if( v(i) > 0 )
            u(i) = v(i);
        end
    end
    u

    v   = [3 5 -2 5 -1 0]       % 2: NO FOR LOOPS
    u2  = zeros( size(v) );     % initialize
    ind = find( v>0 )           % index into >0 elements
    u2(ind) = v( ind )


### (6) Creating functions using m-files:

Functions in matlab are written in m-files. Create a file called 'thres.m' In this file put the following 4 lines:

    function res = thres( v )
    u   = zeros( size(v) );     % initialize
    ind = find( v>0 )           % index into >0 elements
    u(ind)  = v( ind )



    v   = [3 5 -2 5 -1 0]
    thres( v )              % call from command line



### (7) Plotting

    x   = [0 1 2 3 4];          % basic plotting
    plot( x );
    plot( x, 2*x );
    axis( [0 8 0 8] );

    x   = pi*[-24:24]/24;
    plot( x, sin(x) );
    xlabel( 'radians' );
    ylabel( 'sin value' );
    title( 'dummy' );
    gtext( 'put cursor where you want text and press mouse' );

    figure;                 % multiple functions in separate graphs
    subplot( 1,2,1 );
    plot( x, sin(x) );
    axis square;
    subplot( 1,2,2 );
    plot( x, 2.*cos(x) );
    axis square;

    figure;                 % multiple functions in single graph
    plot( x,sin(x) );
    hold on;                        % hold on tells matlab to write on top
    plot (x, 2.*cos(x), '--' );     % of the current plot
    legend( 'sin', 'cos' );
    hold off;

    figure;                 % matrices as images
    m = rand(64,64);
    imagesc(m)
    colormap gray;
    axis image
    axis off;

### (8) Working with the Images and the Matlab Image Processing Toolbox

    [I,map]=imread('trees.tif');            % use as it is, Matlab has pre-stored images

    figure
    imshow(I,map)                           % display it as indexed image w/colormap

    I2=ind2gray(I,map);                     % convert it to grayscale

    figure
    imagesc(I2,[0 1])                       % scale data to use full colormap
                                            %  for values between 0 and 1
    colormap('gray')                        % use gray colormap
    axis('image')                           % make displayed aspect ratio proportional
                                            %  to image dimensions

    I=imread('football.jpg');               % read a JPEG image into 3D array

    figure
    imshow(I)
    rect=getrect;                           % select rectangle
    I2=imcrop(I,rect);                      % crop
    I2=rgb2gray(I2);                        % convert cropped image to grayscale
    imagesc(I2)                             % scale data to use full colormap
                                            %  between min and max values in I2
    colormap('gray')
    colorbar                                % turn on color bar
    impixelinfo                             % display pixel values interactively
    truesize                                % display at resolution of one screen pixel
                                            %  per image pixel
    truesize(2*size(I2))                    % display at resolution of two screen pixels
                                            %  per image pixel

    I3=imresize(I2,0.5,'bil');              % resize by 50% using bilinear
                                            %  interpolation
    I3=imrotate(I2,45,'bil','crop');        % rotate 45 degrees and crop to
                                            %  original size
    I3=double(I2);                          % convert from uint8 to double, to allow
                                            %  math operations
    imagesc(I3.^2)                          % display squared image (pixel-wise)
    imagesc(log(I3))                        % display log of image


