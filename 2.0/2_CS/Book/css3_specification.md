# CSS3 Specification

Notes on the working draft of CSS3. Includes a rough overview of grammar, values/units, media,
selectors, cascading/inheritance, box model, positioning, inline box model, text/font, form/table
elements, columns, math, and media queries.

# Grammar

### Identifiers
CSS **identifiers** must start with a letter and consist of alphanumeric characters, a dash, or
underscore. They cannot start with a dash followed by a number. They are commonly used as attribute
values, but may also represent keywords like values or properties.

Keywords with the first character being a dash are reserved for vendor specific use.

Valid Examples:

* class-name
* id\_Name1
* -vendor-specific

Invalid Examples:

* 0class-name
* -0id\_name

### Case Sensitivity
CSS is case insensitive except for parts dealing with your document. For example, type and attribute
selectors depend on the document.

DIV[ID=body] would match `<div id="body">` in HTML, but would not match in XHTML.

### Structure
A **selector** is used to match elements in a document.

    div > div.child ~ div#sibling

A **declaration** consists of a **property** followed by a colon (:), followed by a **value** (or
multiple values).

    font-weight: bold;
    color: red;

The properties are "font-weight" and "color". The values are "bold" and "red".

Declarations can be grouped together and separated with a semi-colon (;) to form a **declaration
block**:

    { font-weight: bold; color: red }

A **rule set** is a selector followed by a declaration block:

    div > div.child { font-weight: bold }

Rule sets are also called **statements**. A statement can be either a rule set or an **at rule**:

    div { color: red }  
    @import "main.css"

A **comment** is any text that appears between the characters `/*` and `*/`

### Invalid Grammar
Given an invalid declaration (due to an unknown property or illegal value), the User Agent will
ignore it. Other declarations within the declaration block will still apply.

Given an invalid selector, the User Agent will ignore the entire rule set.

    div > div.child {
      font-weight: bold; /* still applies */
      invalid: rule; 
    }

    div & div.child { /* this entire rule is ignored */
      font-weight: bold;
      color: red;
    }

# Values

### Lengths
There are two types of length units: **relative** and **absolute**. Relative units are:

* em => relative to font-size property of element on which it is used
* ex => relative to x-height of a font
* px => relative to pixels of viewing device

Example usage with an `h1`:

    /* h1 is 20% greater than font-size of h1 font */
    h1 { line-height: 1.2em } 

Absolute units are:

* `in` => inches
* `cm` => centimeters
* `mm` => millimeters
* `pt` => points (in CSS 2.1, 1pt == 1/72in)
* `pc` => picas (1pc == 12pt)

### Percentages
Percentage values are always relative to another value, eg. a property of an ancestor element or the
width of a containing block.

    p { line-height: 120% } /* 120% of font-size */
    div { width: 50% } /* half as wide as parent container */

### URIs, see [RFC3986](http://www.ietf.org/rfc/rfc3986)
Uniform resource identifiers are specified with the `url` keyword followed with the uri in
parenthesis. Quotes are optional, but if left off some characters may need to be escaped with
backslashes such as parentheses, commas, whitespace, single quotes, and double quotes.

    div { background: url(http://www.kaching.com/images/logo.png) }
    div { background: url(/images/logo.png) }
    div { background: url("/images/logo.png") }

### Counters
Counters are used to add generated content such as those found in ordered lists.

    p { counter-increment: par-num }
    h1 { counter-reset: par-num }
    p::before { content: counter(par-num, upper-roman) ". " }

### Colors
The color keywords are: aqua, black, blue, fuchsia, gray, green, lime, maroon, navy, olive, orange,
purple, red, silver, teal, white, and yellow.

Colors can also be specified with a hash/RGB in hex, or rgb(values).

    div { color: red }
    div { color: #f00 } /* #rgb, digits are replicated */
    div { color: #ff0000 } /* #rrggbb */
    div { color: rgb(255, 0, 0) } 
    div { color: rgb(100%, 0%, 0%) }

# Media Types
CSS can be used to specify presentation on different forms of media: screen, paper, speech
synthesizer, braille, etc...

Use an at-rule to specify the media target for a style sheet:

    @import url("fancyfonts.css") screen;
    @media print { /* style sheet goes here */ }

Or you can specify your target using the media attribute of the `<link>` element:

    <link rel="stylesheet" 
          type="text/css" 
          media="print, handheld" 
          href="foo.css">

Recognized media types:

* all
* braille
* embossed (paged braille printers)
* handheld
* print
* projection
* screen
* speech
* tty (terminals, fixed-width characters)
* tv (low resolution, sound available)

These media groups contain multiple media types, see the spec for more info:

* continuous, paged
* visual, audio, speech, tactile
* grid, bitmap
* interactive, static
* all

# Selectors

Selectors are pattern matching rules which determine which style rules apply to which elements in
the document tree.

### Summary
    +-----------------+--------------------------------------------+-------------+
    | Example         | Meaning                                    | Category    |
    +-----------------+--------------------------------------------+-------------+
    | *               | Matches any element                        | Universal   |
    +-----------------+--------------------------------------------+-------------+
    | E               | Matches any E element (i.e., an            | Type        |
    |                 | element of type E)                         |             |
    +-----------------+--------------------------------------------+-------------+
    | E F             | Matches any F element that is              | Combinator  |
    |                 | a descendant of an E element               |             |
    +-----------------+--------------------------------------------+-------------+
    | E > F           | Matches any F element that                 | Combinator  |
    |                 | is a child of an element E                 |             |
    +-----------------+--------------------------------------------+-------------+
    | E + F           | Matches any F element immediately          | Combinator  |
    |                 | preceded by a sibling element E            |             |
    +-----------------+--------------------------------------------+-------------+
    | E ~ F           | Matches any F element preceded by a        | Combinator  |
    |                 | sibling element E                          |             |
    +-----------------+--------------------------------------------+-------------+
    | E:class         | Matches element E when                     | Pseudo-class|
    |                 | E satisfies psuedo-class                   |             |
    +-----------------+--------------------------------------------+-------------+
    | E:class(val)    | Psuedo-class selectors                     | Pseudo-class|
    |                 | may also take arguments                    |             |
    +-----------------+--------------------------------------------+-------------+
    | E[foo]          | Matches any E element with the "foo"       | Attribute   |
    |                 | attribute set (whatever the value)         |             |
    +-----------------+--------------------------------------------+-------------+
    | E[foo=warning]  | Matches any E element whose "foo"          | Attribute   |
    |                 | attribute value is exactly equal to        |             |
    |                 | warning                                    |             |
    +-----------------+--------------------------------------------+-------------+
    | E[foo~=warning] | Matches any E element whose "foo"          | Attribute   |
    |                 | attribute value is a list of               |             |
    |                 | space-separated values, one of which       |             |
    |                 | is exactly equal to "warning"              |             |
    +-----------------+--------------------------------------------+-------------+
    | E[lang|=en]     | Matches any E element whose "lang"         | Attribute   |
    |                 | attribute has a hyphen-separated list      |             |
    |                 | of values beginning (from the left) w/ en  |             |
    +-----------------+--------------------------------------------+-------------+
    | E[foo^=warning] | Matches any E element whose "foo"          | Attribute   |
    | E[foo$=warning] | attribute exactly starts with, ends with,  |             |
    | E[foo*=warning] | or contains the value "warning".           |             |
    +-----------------+--------------------------------------------+-------------+
    | E.warning       | Language specific. (In HTML,               | Class       |
    |                 | the same as E[class~=warning])             |             |
    +-----------------+--------------------------------------------+-------------+
    | E#myid          | Matches E element with ID equals "myid"    | ID          |
    +-----------------+--------------------------------------------+-------------+

See [browser support](http://www.quirksmode.org/css/contents.html) for each selector.

Note for attribute selectors, the value must be in quotes if it does not qualify as a CSS identifier
(starts with an alphabet character and is made up of alphanumeric characters, dashes, and/or
underscores).

### Syntax
Selectors may be grouped together into a comma-separated list:

    h1 { font-size: 10pt }
    h2 { font-size: 10pt }
    h3 { font-size: 10pt }
    /* is equal to */
    h1, h2, h3 { font-size: 10pt }

### Selector types
A **simple selector** is either a **type selector**, **universal selector**, **attribute selector**,
**id selector**, or **pseudo-class selector**.

A sequence of selectors is made up of simple selectors separated by **combinators**.

### Psuedo Classes
Psuedo classes permit selection based on information outside of the document tree or that cannot be
expressed by other selectors.

**Dynamic pseudo classes** classify elements on characteristics other than those from the document
tree.

* :link, :visited
* :hover, :active, :focus, :enabled, :disabled, :checked
* :target
* :lang(en)

**Structural pseudo classes** classify elements based on information found in the document tree.

* :root
* :nth-child(2n+1), :nth-child(odd), :nth-child(-n+6)
* :nth-last-child, :nth-of-type, :nth-last-of-type
* :first-child, :last-child, :only-child, :only-of-type, :empty
* :not(selector)

### Pseudo Elements
**Pseudo elements** create abstractions about the document tree beyond those specified by the
document language.

* p::first-line { text-transform: uppercase } /\* formats first line \*/
* ::first-letter, ::before, ::after

### Specificity
A selector's **specificity** is used to determine which declarations apply to which elements in case
of collisions.

A selector's specificity is calculated as follows:
1. count the number of ID selectors in the selector (= a)
2. count the number of class selectors, attributes selectors, and pseudo-classes in the selector (=
   b)
3. count the number of type selectors and pseudo-elements in the selector (= c)
4. ignore the universal selector

Selectors inside the negation pseudo-class are counted like any other, but the negation itself does
not count as a pseudo-class.

Now concatenate the numbers a-b-c (aka a\*100 + b\*10 + c). Higher specificity takes higher
precedence. In case of equal specificities, the rule set which occurs later in the stylesheet will
be applied.

    *               /* a=0 b=0 c=0 -> specificity =   0 */
    li              /* a=0 b=0 c=1 -> specificity =   1 */
    ul li           /* a=0 b=0 c=2 -> specificity =   2 */
    ul ol+li        /* a=0 b=0 c=3 -> specificity =   3 */
    h1 + *[rel=up]  /* a=0 b=1 c=1 -> specificity =  11 */
    ul ol li.red    /* a=0 b=1 c=3 -> specificity =  13 */
    li.red.level    /* a=0 b=2 c=1 -> specificity =  21 */
    #x34y           /* a=1 b=0 c=0 -> specificity = 100 */
    #s12:not(foo)   /* a=1 b=0 c=1 -> specificity = 101 */

# Cascading and Inheritance

### Values
A user agent goes through a few steps to calculate values for properties:

1. **Computed values** can be calculated without the user agent rendering the document, for example
   absolute 'px' or other lengths.
2. **Used values** can only be calculated by formatting the document, for example an element's 50%
   width of parent element.
3. **Actual values** are what the user agent actually renders. If an author specifies decimal
   pixels, a the actual value might be an integer because of browser limitations.

### Inheritance
**Inheritance** occurs when an element inherits a property value from its parents. Each property
will define whether it is inheritable in the spec.

    <div style="color:red">Hello <b>World</b></div> /* <b> will be red */

A property can be declared with an **inherit** value explicitly, which can also be used on
properties that are not normally inherited.

    <div>Hello <b>World</b></div>
    /* CSS */
    div { color: red }
    b { color: inherit }

### @import rule
You can import style rules from another style sheet. You can also specify media dependent import
rules.

    @import "mystyle.css";
    @import url("mystyle.css");
    @import url("mystyle.css") projection, tv;

### Cascading
**Cascade** means a succession of stages or operations or processes or units.

In the context of CSS, it means the order in which style rules override one another. At the highest
level, there is the **origin** of the style sheet:

- author => this is the author of the css file or website - user => this is the user viewing the
document/css file - user agent => this is the user's browser

CSS from the author is common. Sometimes, users define their own style rules for documents they
view. This is the case for accessibility (larger fonts). The user agent defines its own default
rules, such as default properties to present a document (h1, h2, ul, li, p, etc...).

Rules may also be marked as **!important**. A declaration marked as !important will override other
declarations on the same element that are not marked.

    p { font-size: 10pt !important } /* this rule will be enforced */
    p.class { font-size: 9pt }

The cascading order concerning origin and important declarations is:

1. user agent declarations /\* lowest precedence \*/
2. user normal declarations
3. author normal declarations
4. author important declarations
5. user important declarations /\* highest precedence \*/

For each origin/important section, the rules are then sorted by specificity. If the specificity of
two rules match, the latter declaration will be used.

# Layout

### Box Model
The box model describes how rectangular boxes are generated for elements and how those boxes are
laid out according to the visual formatting model.

Each box has a content width/height, inset padding, a border, and margin.

The **margin** properties are margin-(top|right|bottom|left) or just the shortcut margin. Example:

    div { margin-top: 20px }
    span { margin-right: 10% }
    p { margin: 2px 5px 3px 1px }

When two adjoining vertical margins of block boxes appear, **margin collapse** occurs - the maximum
value is used as the total margin between both boxes. If the content area, border, and padding of a
block box equal to 0 then the top and bottom margins of that box will collapse. Margins of inline
boxes do not collapse.

A **padding** property also exists, which pads the inset area of the box.

    div { padding-top: 20px }
    span { padding-right: 10% }
    p { padding: 2px 5px 3px 1px }

The **border** properites are:

- border-(top|right|bottom|left)-width and border-width which can be set to
    an absolute length (ie. 1px) or to thin, medium, or thick.
- border-(top|right|bottom|left)-color and border-color - border-(top|right|bottom|left)-style and
border-style - or just the shorthand border (ie. border: 1px solid #000)

The **width** property sets the content width of the box - not the total width (which is equal to
horizontal margin + left/right borders + horizontal padding + content width).

    div { width: auto } /* default, takes up 100% of containing block */
    div { width: 50% }
    div { width: 200px }
    span { width: 30px } /* ignored, inline elements shrink-to-fit */

The **height** property sets the content height of the box. Example:
    div { height: 200px }

### Inline Box Model
In an inline formatting context, boxes are laid out horizontally, one after the other. The boxes may
be aligned vertically in different ways: their bottoms or tops may be aligned, or the baselines of
text within them may be aligned. The rectangular area that contains the boxes that form a line is
called a **line box**.

Inline elements cannot have a set width, but its containing line box's width is determined by its
own containing block and the presence of floats. The height of a line box by its line-height
property and vertical-align properties. The white-space above and below text are known as
**leading**.

When the total width of inline elements on a line is less than the width of the line box, their
horizontal alignment is determined by the **text-align** property.

When inline elements of varying heights occur in the same line, its vertical alignment is determined
by the **vertical-align** property.

If an inline box exceeds the width of a line box, it is split into several boxes (and wrapping
occurs).

### Visual Formatting Model
The **viewport** is the viewing area on the screen - usually a browser window. When the spec
mentions **containing block**, it is usually the element's parent, but is not always the case. For
instance, the containing block for an absolute positioned element is the closest positioned
ancestor.

Each element in the document tree generates zero or more boxes according to the box model. The
layout of these boxes are then determined by their:

- box dimensions and type - position scheme (normal flow, float, and absolute positioning) -
relationship between elements in document tree - external information (ie. viewport size)

Block boxes are laid out vertically, the top edge of the following element will touch the bottom
edge of the previous element.

Inline elements are laid out horizontally, until horizontal space runs out - then a line wrap
occurs. Inline elements are grouped together to form a **line box**, which have different properties
than block boxes.

### Positioning
There are 3 positioning schemes:

- normal flow - floats - absolute positioning

If an element is **floating**, it goes as far as it can in the floated direction and as high as it
can without passing the boundaries of its containing block. Sibling elements are said to flow past
it (unless a clear declaration is specified). Generated boxes of floated elements have a
shrink-to-fit width if its width is set to auto.

    div { float: left }
    div { float: right }
    p { clear: left } /* or right or both */
    div { float: none } /* default value, can be used to override a declaration */

In **absolute positioning**, a box is explicitly offset with respect to its containing block. The
containing block is an ancestor box that is positioned or the viewport if that does not exist. The
properties top, right, bottom, and left can be used to set the offset (and optionally width/height).
If the width is set to auto, an absolute positioned element has a shrink-to-fit width.

    div.outer { position: relative }
    div.inner { position: absolute; left: 20px; top: 30px; }
    .inner.off { left: auto; } /* default value */

### Table Visual Formatting
Formatting for tables can be done on non-table elements by changing their display properties:

- table => table or inline-table - tr => table-row - tbody => table-row-group - thead =>
table-header-group (if contains > 1 row, only applies to first) - tfoot => table-footer-group - col
=> table-column - colgroup => table-column-group - caption => table-caption

When other elements are placed where table elements are expected, a corresponding table container
will be generated. For example, a table cell may be generated to contain an unexpected P tag.

Table cells may belong to two contexts: rows and columns. The following properties belong to column
and column-group elements:

    border, background, width, and visibility

**Captions** may be used to annotate a table with additional info. table-caption elements have the
**caption-side** property which will let you place the caption above or below the table:

    caption { caption-side: top; } /* default */
    caption { caption-side: bottom; }

Each row box occupies one row of grid cells and each column box occupies one or more columns of grid
cells. A row group occupies the same cells as its rows, and the same holds true for column groups.
Cells may span several rows or columns (which is usually the case for missing `<td>`'s).

Tables are made up of layers to determine which element's properties have higher precedence (ie.
borders or backgrounds). In order of bottom to top:

1. table
2. column groups
3. columns
4. row groups
5. rows
6. cells (have highest precedence)

There are two **table width algorithms** which is set by the **table-layout** property.

    table { table-layout: auto } /* default */
    table { table-layout: fixed }

The fixed table layout is the faster of the two, the width of each column is determined:

- A column element with a value other than 'auto' for the 'width' property sets the width for that
column. - Otherwise, a cell in the first row with a value other than 'auto' for the 'width' property
determines the width for that column. If the cell spans more than one column, the width is divided
over the columns. - Any remaining columns equally divide the remaining horizontal table space (minus
borders or cell spacing).

In the automatic table layout, the width of the table is determined by the width of its columns.

# Fonts and Text

### Font Properties
The properties which apply to fonts are:

- font-family - font-style - font-variant - font-weight - font-size

The values for **font-family** are a comma separated list of families (specific and generic). The
generic options are:

- serif - sans-serif - cursive - fantasy - monospace

Families given early in the list have highest priority. Authors are encouraged to use a generic
family as the final value.

    p { font-family: Gill, Helvetica, sans-serif; } 

**font-style** values may be normal (default), italic, or oblique. Oblique characters still use the
same font family but are slightly skewed. Italic characters may use a different font (that are still
skewed).

The **font-variant** property lets authors style their text so that lowercase letters use the same
style as uppercase ones (although slightly smaller).

    p { font-variant: small-caps; }
    p { font-variant: normal; }  /* default */

**font-weight** specifies the weight (or boldness) of characters. Values may be: normal | bold |
bolder | lighter | 100 - 900 (in steps of 100).

    p { font-weight: 400; } /* same as normal */
    p { font-weight: 700; } /* same as bold */

**font-size** specifies the size of characters. Values may be absolute, relative, a length, or a
percentage. Absolute sizes are:

- xx-small - x-small - small - medium (default) - large - x-large - xx-large

Relative sizes are calculated based on the size of the parent element:

- larger - smaller

Examples:

    p { font-size: larger; }
    p { font-size: 1.5em; }
    p { font-size: 150%; }

There is also a shorthand **font** property whose value:

    [[ <'font-style'> || <'font-variant'> || <'font-weight'> ]? <'font-size'> 
    [ / <'line-height'> ]? <'font-family'> ] | caption | icon | menu | message-box
    | small-caption | status-bar | inherit

Examples:

    p { font: bold italic 12px/1.5em Helvetica, sans-serif; }

This property will reset any property not explicitly given a value to its initial value.

### Text Properties
These properties affect the visual presentation of characters, spaces, words, and paragraphs:

- text-indent - text-align - text-decoration - letter-spacing - word-spacing - text-transform -
white-space

The **text-indent** property is used to indent the first line of text in a block, inline-block, or
table cell element. Example:

    p { text-indent: 12px; }

The **text-align** property is used to justify text in block level elements. Values for it are:
left, right, center, and justify. Examples:

    p { text-align: left; } /* default in ltr languages */
    p { text-align: right; } /* default in rtl languages */

The **text-decoration** property may be used to decorate text and applies to all elements. Values
include:

- none (default, has no decoration) - underline - overline - line-through - blink

**letter-spacing** and **word-spacing** specifies the spacing (or kerning) between letters and words
respectively. The default value for both these properties is normal. Other possible values are
lengths (eg 1px, 1.5em, 20%).

**text-transform** controls capitalization effects of an element's text.

- none (default, does nothing) - capitalize (uppercase first character of each word) - uppercase -
lowercase

**white-space** declares how white space is handled inside elements.

- normal: default, does nothing - pre: prevents UAs from collapsing white space, preserves line
breaks - nowrap: collapses white space as normal, but suppresses line breaks - pre-wrap: prevents
collapsing white space, preserves line breaks,
    and also adds line breaks as necessary to fill line boxes
- pre-line: UAs may collapse white space

# Forms and UI Elements

These properties affect the visual presentation of UI elements which users may interact with.

The **cursor** property specifies the type of cursor to be displayed when the cursor is hovered over
that element. If applies to all elements.

- auto (default value, UA determines) - crosshair - default (default platform dependent cursor) -
pointer (indicates link) - move - {e,ne,nw,n,se,sw,s,w}-resize - text - wait - progress - help -
`<uri>` (eg. p { cursor: url(dinosaur.png); }

The **outline** property are used to make visual objects stand out. They differ from borders in two
ways: they don't take up space and may be non-rectangular. Properties are:

- outline-width (values are border-widths) - outline-style (values are border-styles) -
outline-color (values are colors) - outline (a shorthand property to specify the above 3)

Example:

    p { outline: 1px dotted #000; }