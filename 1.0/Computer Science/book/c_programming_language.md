# C Programming Language

A concise introduction to the C programming language by Brian W. Kernighan and Dennis M. Richie. The
book is written for a reader without any programming experience, but these notes assume prior
experience.

# A Tutorial Introduction

Kernighan and Ritchie start off with a "Hello World" program:

    #include <stdio.h>
    main() {
      printf("hello, world\n");
    }

To actually compile and run it:

    % cc hello.c
    % ./a.out

A C program consists of **functions**, **statements**, and **variables**. This example uses the
special `main` function where program execution starts. Every program needs this function. The
`#include` statement tells the compiler to include information about standard input/output.

`"hello, world\n"` is called a **character string** or **string constant**. It's a sequence of
characters.

This next program prints a Fahrenheit-Celsius conversion table:

    #include <stdio.h>
    /* print Fahrenheit-Celsius table
       for fahr = 0, 20, ..., 300 */
    main() {
      int fahr, celsius;
      int lower, upper, step;

      lower = 0;    /* lower limit of temp scale */
      upper = 300;  /* upper limit */
      step = 20;    /* step size */

      fahr = lower;
      while (fahr <= upper) {
        celsius = 5 * (fahr-32) / 9;
        printf("%d\t%d\n", fahr, celsius);
        fahr = fahr + step;
      }
    }

Text between `/*` and `*/` are comments and can include newlines.

The first two lines of the main function are **declarations** that announces variables. The type
`int` means the variables are integers. The range and size of `int`s and `float`s depend on the
machine you're using. Some other types:

* `char` single byte character
* `short` short integer
* `long` long integer
* `double` double-precision floating point

There's also **arrays**, **structures**, and **unions** which are data structures made up of basic
types or **pointers** to them.

To get a more accurate table, the authors switched the program to use floats instead of ints. A
decimal point is also used to indicate constants are floats and not ints:

    celsius = (5.0/9.0) * (fahr-32.0);

C will implicitly convert an integer to floating point if the operation involves another floating
point. However, it doesn't hurt to be explicit with decimal points.

Formatting for the `printf` function:

* `%d` print a decimal integer
* `%6d` print a decimal integer, at least 6 characters wide
* `%f` print a floating point
* `%6f` print a floating point, at least 6 characters wide
* `%.2f` print a floating point, 2 characters after decimal point
* `%6.2f` print a floating point, at least 6 characters wide and 2 after decimal

The program can be shortened using a `for` statement instead of the `while`:

    for (fahr = 0; fahr <= 350; fahr = fahr + 20)
      printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));

It's bad practice to bury "magic numbers". We deal with this by defining a **symbolic name** or
**symbolic constant**:

    #define name replacement text

Any occurrence of the "name" will be replaced by the "replacement text".

    #define LOWER 0
    #define UPPER 300
    #define STEP 20
    // ...
    for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
      printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));

At its simplest, input/output functions use `getchar()` to get a character from the keyboard and
`putchar(c)` to print a character to the string. `getchar` returns a single character typed from the
keyboard. You can use this to write a program to copy files:

    int c = getchar();
    while (c != EOF) {
      putchar(c);
      c = getchar();
    }

Notice that `getchar` returns the distinctive EOF value for "end of file". We also use the `int`
type instead of `char` because EOF might be too big of a value to store into a `char`.

Arrays in C are declared like this:

    int ndigit[10];  // an array of 10 integers

Subscripts start with zero, so `ndigit[0]` accesses the first element.

`if/else` statements are formatted like:

    if (condition1)
      statement1
    else if (condition2)
      statement2
    else
      statement3

Multi-line statements can be surrounded with brackets. The `else if` and `else` are both optional.

Let's write a `power` function that computes `x^y`:

    int power(int m, int n);

    // main function goes here

    int power(int base, int n) {
      int p = 1;
      for (int i = 1; i <= n; ++i)
        p = p * base;
      return p;
    }

First, we declared our function at the top. This announces it like a variable so we can use it
without the compiler complaining. It's called a **function prototype**. Parameter names don't need
to match, in fact they're optional. But they're still good for documentation.

A function definition has the following format:

    return-type function-name(parameter declarations, if any) {
      declarations
      statements
    }

**Parameters** are variables named in the parenthesized list of a function, sometimes called
**formal arguments** or **actual arguments**. These parameters are passed by value - they're local
copies.

The most common use for arrays in C are character arrays or strings. They're terminated with a null
byte or `\0`:

    h e l l o \n \0
    0 1 2 3 4  5  6

The `%s` format for `printf` expects this null byte to be there and uses it for formatting strings.
When arrays are parameters in functions, they're passed by reference. If you modify it, you modify
the original variable.

So far, we've used **local variables** which exist when the function is called and disappears when
the function exits. They're also called **automatic variables**. These must be explicitly set or
else they will contain garbage.

C also supports **external variables**, globally accessible by any functions. These retain their
values even when functions exit. They must be defined outside a function and declared inside each
function that wants to access it (either implicitly or explicitly).

    #include <stdio.h>
    int global_counter;

    main() {
      extern int global_counter;
      // ...
    }

The keyword `extern` is used to declare it as external to the function. The prefix may be omitted if
the variable was declared in the same file before usage.

# Types, Operators, and Expressions

Variable names are made of letters, digits, or hyphens. The first character must be a letter.

The data types available are `char`, `int`, `float`, and `double`. There are also `short`, `long`,
`signed`, and `unsigned` qualifiers. See `<limits.h>` or `<float.h>` for actual sizes and limits.

    short int sh; // int is optional
    long int counter;

You've seen integer constants before, they're just numbers. Float constants use a decimal point or
exponent (`1e-2`). Constants can be suffixed with `u` or `U` for unsigned. They can also be suffixed
with `l` or `L` for long. For example: `123ul`.

A leading zero specifies octal, a leading `0x` specifies hexadecimal.

A **character constant** is just an integer written as one character in single quotes like `'x'`.
It's stored as a numerical value according to the machine's character set.

String constants are concatenated at compile time:

    "hello, " "world" == "hello, world"

**Enumeration constants** are lists of constant integers:

    enum boolean { NO, YES };

The first element has value 0, following elements are incremented by 1. They can receive explicit
values:

    enum escapes { NEWLINE = '\n', TAB = '\t' };

We've already covered variable declaration. You can also initialize variables at the time you
declare it. Automatic variables without explicit initialization have undefined values. External and
static variables are initialized to zero by default.

The binary arithmetic operators are: `+`, `-`, `*`, `/`, and `%`. The logical operators are: `>`,
`>=`, `<`, `<=`, `==`, `!=`, `&&`, and `||`.

There are also unary increment and decrement operators: `++` and `--`.

C sometimes does implicit type conversions from narrower to wider types, like ints to floats. chars
may be used in arithmetic expressions, since they're just narrow ints. Logic expressions may use
integers, true just means non-zero.

Longer integers are converted to shorter ones by dropping excess high-order bits.

Explicit type conversion can be coerced with a unary **type cast**:

    (type name) expression

C provides operators for bit manipulation: `&` AND, `|` OR, `^` exclusive OR, `<<` left shift, `>>`
right shift, `~` one's complement.

AND is often used to mask off bits, while OR is used to turn bits on. The shift operators will shift
bits by a given number of positions. `x << 2` shifts x by two positions. New bits are zero.

The **assignment operator** is an abbreviated way to combine binary operators with an assignment. `i
= i + 2` becomes `i += 2` and works with most binary operators.

Conditional expressions may also use the **ternary operator** `?:`:

    expr1 ? expr2 : expr3

# Control Flow

An **expression** becomes a **statement** when it's followed by a semicolon. The semicolon is a
statement terminator. Braces are used to group declarations and statements together into a compound
statement or **block**, syntactically equivalent to a single statement.

We've already seen the if-else statement in earlier examples. Conditional expressions evaluate any
non-zero values as true.

    if (condition)
      statements
    else if (condition)
      statements
    else
      statements

There's also the **switch** statement:

    switch (expression) {
      case const-expr: statements
      case const-expr: statements
      default: statements
    }

Constant expressions need to be an integer value (remember that characters are integer values also).

C supports while loops:

    while (expression)
      statement
 
And for loops:

    for (expr; expr; expr)
      statement

The first expression is the initializer, the second is the condition to stop, and the third is the
step expression. Each are optional.

There's also the **do-while loop**:

    do
      statement
    while (expression)

It's valuable when the statement needs to be executed at least once. The keyword **break** allows
you to exit early from any loops or switch statement. The keyword **continue** exits the current
block, but continues to the next iteration of the loop.

For completeness, the authors mention the **goto statement**. It's not normally used in practice,
but is provided:

    for ( ... )
      for ( ... ) {
        if (disaster)
          goto error:
      }
    ...
    error:
      /* clean up the mess */

The label follows the same naming convention as variables and has the scope of a function.

# Functions and Program Structure

Functions break a large program into smaller chunks. A function needs to be defined or declared as a
prototype before being used in a file. We've already seen what a function definition looks like:

    return-type function-name(argument declarations) {
      declarations and statements
    }

Many parts are optional, here's the minimal function:

    dummy() {}

The **return statement** is used to return a value from a function to its caller:

    return expression;

There's an implicit conversion to the return type if needed. Parentheses around the expression are
optional.

Compiling multiple source files will create object files. If you need to, you can recompile a single
file to produce an executable, just pass along the generated object files:

    % cc main.c getline.c strindex.c
    % cc main.c getline.o strindex.o
    % ./a.out

The default return type of a function is an integer. If it's something else, it needs to be
explicitly declared. Function declarations can even be made local to another function:

    main() {
      double atof(char []);
    }

Functions are considered external, you cannot have a function local to another one. Variables are
external if it's defined outside of any function.

The **scope** of a variable is the part of the program in which it may be used. The scope of an
external variable or function is from the point it's declared (or defined) to the end of the file
being compiled. If it's being used before it's defined, an `extern` declaration is required.

    extern int sp;
    extern double val[];

The lines above declare the variables for usage, but they do not reserve any storage space for them.
There should be only one definition among all files, other files contain the `extern` declaration to
access it.

A **header file** uses the file suffix `.h` and usually contains declarations for functions or
variables for central access. For example, a `calc.h` header file might look like:

    #define NUMBER '0'

    void push(double);
    double pop(void);
    int getop(char []);
    int getch(void);
    void ungetch(int);

Whereas the implementation file will look like:

    #include <stdio.h>
    #include <ctype.h>
    #include "calc.h"

    int getop() {
      ...
    }

The **static** declaration limits the scope of the variable to the source file it's in during
compilation. External static means it's external so multiple functions can access it, but it's still
limited in scope to a single source file. It can be applied to functions also.

    static char buf[BUFSIZE];
    static int bufp = 0;
    static ing getch(void) { ... }

It can also be applied to local variables within a function. Unlike automatics, they remain in
existence after the end of the function.

The **register** declaration tells the compiler that the variable is in heavy use and should
consider storing it in the CPU register:

    register int x;

The scope of a variable can be limited by any curly brackets, such as following if statements (not
just functions). You can override a variable name when the program name enters a new scope:

    int x;
    f(double x) { ... }

Automatic and register variables have garbage values for implicit initialization. External and
static variables are initialized to zero. You can initialize an array using curly brackets:

    int days[] = {31, 28, 31, 30};

C functions may be used recursively (calling itself). Be sure to declare the function so it can call
itself.

The C preprocessor is an initial step in compilation. We've used this before with `#include` and
`#define`. For file inclusion, use quotes to include a relative file and use angle brackets for
system libraries.

Macros can be defined with arguments:

    #define max(A, B) ((A) > B) ? (A) : (B))

They can be undefined with `#undef`. If a parameter name is preceded by a `#` in the replacement
text, the preprocessor will use a quoted string.

Some other useful preprocessor statements are `#if`, `#elif`, `#else`, and `#endif`. This can be
used for conditional inclusion:

    #if !defined(HDR)
    #define HDR
    #endif

# Pointers and Arrays

A **pointer** is a variable that contains the address of a variable. The unary `&` operator gives
the address of an object:

    p = &c;

The unary `*` operator is the **dereferencing** operator. Applied to a pointer, it accesses the
object the pointer points to.

    int x = 1, y = 2, z[10];
    int *ip;      /* ip is a pointer to int */
    ip = &x;      /* ip now points to x */
    y = *ip;      /* y is now 1 */
    *ip = 0;      /* x is now 0 */
    ip = &z[0];   /* ip now points to z[0] */

Both `*` and `&` have higher precedence than arithmetic operators.

Since C passes arguments by values in functions, we can use pointers and addresses to implement a
swap function:

    void swap(int *px, int *py) {
      int temp;
      temp = *px;
      *px = *py;
      *py = temp;
    }

Pointers and arrays have a strong relationship. Any array subscripting can be done with pointers.
`int a[10]` creates an array with ten spaces:

    a: [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
        0  1                       9

Let's assign a pointer to point to the first element, then assign another variable to the
dereferenced pointer:

    int *pa = &a[0];
    int x = *pa;

By definition, `pa + 1` points to the next element. So we can iterate along the array using pointer
arithmetic:

    *(pa + 1) == a[1]
    *(pa + 2) == a[2]

In fact, an array is just a pointer to the first element. C just converts the subscript syntax into
pointer arithmetic for you:

    a == pa
    a[i] == *(a+i)

The only difference is that a pointer is a variable, whereas an array is not. We can do `pa = a` and
`pa++`, but we can't do `a = pa` and `a++`.

Passing an array to a function is just passing a pointer to the first element, so it's pass by
reference. You can modify the original contents.

    f(int *arr) { ... }
    f(int arr[]) { ... }

It's easy to create subarrays using pointer arithmetic also:

    f(a + 2)
    f(&a[2])

The author illustrates memory management by writing two functions: `alloc(n)` and `afree(p)`.
`alloc` returns a pointer to `n` consecutive bytes which must be released so it can be re-used later
on. They must be called in order of a stack (last-in, first-out).

`malloc(n)` and `free(p)` use the heap so they don't require the same stack ordering.

`alloc` and `afree` uses `allocbuf`, the buffer that stores your data. There's a limit on its size.
If it's not large enough to allocate more memory, `alloc` returns zero. If it's large enough,
there's a pointer called `allocp` which points to the current position in the stack. It gets
incremented and `alloc` returns the pointer. `afree(p)` just sets `alloccp` back to `p` so memory
can be re-used.

    #define ALLOCSIZE 10000 /* size of available space */
    static char allocbuf[ALLOCSIZE]; /* storage for alloc */
    static char *allocp = allocbuf;  /* next free position */

    char *alloc(int n) {  /* return pointer to n characters */
      if (allocbuf + ALLOCSIZE - allocp >= n) {  /* it fits */
        allocp += n;
        return allocp - n; /* old p */
      } else      /* not enough room */
        return 0;
      }
    }

    void afree(char *p) { /* free storage pointed to by p */
      if (p >= allocbuf && p < allocbuf + ALLOCSIZE)
        allocp = p;
    }

Strings are just a null-byte terminated character sequence. A variable holding a string is a `char
*`.

    char amessage[] = "now is the time";
    char *pmessage = "now is the time";

The difference is the array is just big enough to hold the sequence of characters plus `\0`.
`amessage` contents can be modified and it will always refer to the same storage. `pmessage` is a
pointer, it can point somewhere else but you cannot modify the contents (C has undefined behavior).

The `main` function actually takes two arguments, an argument count and an array of strings.
`argv[0]` is the name of the program. `argv[argc]` is a null pointer.

    main (int argc, char *argv[]) {
      int i;
      for (i = 0; i < argc; i++) {
        printf("%s", argv[i]);
      }
    }

You can even have pointers to functions. These can be assigned, passed around, or returned from
functions.

    int (*compare)(void *, void *)
    int* comparep(void *, void *)

`compare` is a pointer to a function that has two `void *` arguments and returns an `int`.
`comparep` is a function that returns a pointer to an int. The parentheses are required.

Let's look at some more complicated declarations:

* `char **argv` pointer to char sequence
* `int (*daytab)[13]` pointer to `array[13]` of int
* `void *comp()` function returning pointer to void
* `void (*comp)()` pointer to function returning void
* `char (*(*x())[])()` function returning pointer to array of pointer to function returning char
* `char (*(*x[3])())[5]` `array[3]` of pointer to function returning pointer to `array[5]` of char

# Structures

**Structures** are collections of one or more variables grouped together for convenience.

    struct point {
      int x;
      int y;
    };

In this case, `point` is the **structure tag** which is an optional name. The variables inside are
called **members**. A struct declaration defines a type:

    struct { ... } x, y, z;  // x, y, z are all structures

If no variables follow, then the declaration reserves no space. It just acts as a template. The tag
can be used later to declare a variable.

    /* declaring and using structures */
    struct point pt;
    struxt point maxpt = {320, 200};

    maxpt.x == 320;
    maxpt.y == 200;

    /* nested structures */
    struct rect {
      struct point pt1;
      struct point pt2;
    };
    struct rect screen;
    screen.pt1.x = 100;

    /* returning structures from functions */
    struct point makepoint(int x, int y) {
      struct point temp = {x, y};
      return temp;
    }

    /* passing structures to functions */
    struct rect canonrect(struct rect r) {
      struct rect temp;
      // ...
      return temp;
    }

If the structure is large, it's more efficient to pass a pointer:

    struct point *pp = &apoint;
    pointfn(pp);
    (*pp).x; // access a member

Pointers to structures are frequently used so there's a shorthand notation to access members:

    pp->x == (*pp).x;

The `->` operator has high precedence along with `.`, `()` function calls, and `[]` subscripts.
They're used before arithmetic operators.

There's a operator `sizeof` which returns a `size_t`. This is just an unsigned integer value that
represents the size of an object or type:

    sizeof object
    sizeof typename

C provides `typedef` for creating new data types:

    typedef int Length;

Now `Length` is a synonym for `int`. It can be used in declarations, casts, etc...

     Length len, maxlen, *lengths[];

     typdef char *String;
     String p, lineptr[MAXLINES];

This becomes very handy for `structs` so you don't have to type the keyword `struct` when declaring
new ones:

    typedef struct tnode {
      char *word;
      int count;
      struct tnode *left;
      struct tnode *right;
    } Treenode;
    Treenode node = {"test", 1, &left, &right};

**Unions** are like structures, but they hold objects of different types/sizes at different times in
the same storage space:

    union u_tag {
      int ival;
      float fval;
      char *sval;
    } u;
    union-name.member;
    union-pointer->member;

If storage is precious, you may want to pack objects into a single machine word using bit flags. The
most compact way is to use one-bit flags in a single char or int. First, define bit masks in powers
of 2:

    #define KEYWORD  01
    #define EXTERNAL 02
    #define STATIC   04
    // or
    enum { KEYWORD = 01, EXTERNAL = 02, STATIC = 04 };

To turn on the flags use the OR bit operator:

    flags |= EXTERNAL | STATIC;

To turn off the flags:

    flags &= ~(EXTERNAL | STATIC);

To check if a flag is on or off:

    flags & EXTERNAL
    flags & STATIC
    flags & (EXTERNAL | STATIC)  // checks both at once

Besides bit flags, you may also want to use **bit fields**:

    struct {
      unsigned int is_keyword : 1;
      unsigned int is_extern  : 1;
      unsigned int is_static  : 1;
    } flags;

`flags` is a table containing three 1-bit fields now. It can be used just like a regular struct.
Here we used 1 as the bit width. The special width `0` will force alignment to the next word
boundary. Fields are implementation dependent.

# Input and Output

We've already used `getchar(void)` and `putchar(int)`. This works using standard input and output.
For a Unix environment, a program gets input and puts output in several ways:

    prog < infile
    otherprog | prog

    prog > outfile
    prog | anotherprog

We've also used `int printf(char *format, arg1, arg2, ...)` for formatted output. Here are some
basic printf conversions:

* `d,i` decimal number
* `o` unsigned octal number
* `x,X` unsigned hexadecimal number
* `u` unsigned decimal number
* `c` single character
* `s` character sequence
* `f` double
* `e,E` double exponent for smaller/larger numbers
* `g,G` double
* `p` void pointer, implementation dependent representation
* `%` escapes percents

Notice that `printf` is a varargs functions. To declare one:

    void functionname(char *fmt, ...)

The `...` means any number of arguments and types may be used. `<stdarg.h>` contains macros that
help step through variable argument lists. `va_list` will declare a variable to use that refers to
each argument. `va_arg` returns one argument, a step at a time. `va_end` does cleanup. `va_start`
will initialize your first argument. Here's an example of our own `printf` style function:

    void minprintf(char *fmt, ...) {
      va_list ap;
      char *p, *sval;
      int ival;
      double dval;

      va_start(ap, fmt);
      for (p = fmt; *p; p++) {
        if (*p != '%') {
          putchar(*p);
          continue;
        }
        switch (*++p) {
        case 'd':
          ival = va_arg(ap, int);
          printf("%d", ival);
          break;
        case 'f':
          dval = va_arg(ap, double);
          printf("%f", dval);
          break;
        case 's':
          for (sval = va_arg(ap, char *); *sval; sval++)
            putchar(*sval);
          break;
        default:
          putchar(*p);
          break;
        }
      }
      va_end(ap);
    }

The input version of `printf` is `int scanf(char *format, ...)`. This function reads characters from
standard input. The variable argument list should each be a pointer and is where the input gets
stored.

`<stdio.h>` includes a struct called `FILE`. You can use this to read/write file contents.

    FILE *fp = fopen("filename", "rw");  // the mode can include r, w, b, or a
    getc(fp);      // get a single character
    putc('C', fp); // print a single character

Standard input/output are actually just file pointers. They can be accessed via `stdin`, `stdout`,
or `stderr`. Some other useful functions are:

    int fscanf(FILE *fp, char *format, ...)
    int fprintf(FILE *fp, char *format, ...)
    char *fgets(char *line, int maxline, FILE *fp)
    int fputs(char *line, FILE *fp)
 
If an error occurs in your program, you may want to print to `stderr` and then exit the program with
a status code:

    fprintf(stderr, "There was an error");
    exit(2);  // 0 signals all is well, non-zero usually means an error

Some string functions the authors mention that are useful: `strcat`, `strncat`, `strcmp`, `strncmp`,
`strcpy`, `strncpy`, `strlen`, `strchr`, `strrchr`. Some character functions: `isalpha`, `isupper`,
`islower`, `isdigit`, `isalnum`, `isspace`, `toupper`, `tolower`. For command execution use
`system`. You can find documentations for any of these functions via their man page.

`malloc` and `calloc` obtain blocks of memory dynamically:

    void *malloc(size_t n)            // for object of size n
    void *calloc(size_t n, size_t s)  // for array of n objects of size s

Each returns a pointer to the beginning of the block or NULL on any errors. The pointer must be
casted. Use `free(p)` to free the space pointed to by a pointer.

Some useful math functions: `sin`, `cos`, `atan2`, `exp`, `log`, `log10`, `pow`, `sqrt`, `fabs`,
`rand`.

# The UNIX System Interface

All input/output on a Unix system is done by reading or writing to files. This includes peripheral
devices like keyboards. A **file descriptor** is sort of an ID to represent files. Unix and programs
use this to read/write.

At the lowest level of read/write, there are these two functions:

    int n_read = read(int fd, char *buf, int n);
    int n_written = write(int fd, char *buf, int n);

To open a file:

    int fd = open(char *name, int flags, int perms);

The flags can be one of: `O_RDONLY`, `O_WRONLY`, or `O_RDWR`. You can create a file with:

    int fd = create(char *name, int perms);

To remove a file, you **unlink** it. You can remove a file with:

    unlink(char *name);