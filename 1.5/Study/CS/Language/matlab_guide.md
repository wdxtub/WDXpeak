# Matlab 指南

<!-- MarkdownTOC -->

- 语言基础
- 基本数学运算
    - 矩阵的代数运算
    - 矩阵的逻辑运算
    - 基本数论运算
- 流程控制
- 函数编写
- 二维图形绘制
- Introducing Matlab
    - (1) Help and basics
    - (2) Objects in matlab
    - (3) Simple operations on vectors and matrices
    - (4) Saving your work
    - (5) Relations and control statements
    - (6) Creating functions using m-files:
    - (7) Plotting
    - (8) Working with the Images and the Matlab Image Processing Toolbox

<!-- /MarkdownTOC -->

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
