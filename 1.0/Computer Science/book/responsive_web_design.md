# Responsive Web Design

Ethan Marcotte coined the term "Responsive Web Design", it's a bag of useful techniques to optimize
our web pages to different screen sizes. In this book, he shows us how to do it.

# Our Responsive Web

The web inherited a lot of terms and techniques from other media. We start with a blank canvas (from
painting). There's typography just like print design. More recently, there has been an explosion of
devices - each with a different screen size. Our web pages tend to have horrible UI on smaller
sizes.

Marcotte mentions how a company has produced a glass wall that's initially transparent but becomes
opaque when many people enter the room. The glass wall is responsive, it knows when privacy is
needed.

Our web pages can also be responsive. There are three ingredients:

1. A flexible, grid-based layout
2. Flexible images and media
3. Media queries

# The Flexible Grid

This chapter includes a lot of tips on how to create a fluid design.

Typesetting should be flexible. This means setting a base size for the `body` and using `em` for
font sizes instead of `px`.

    body { font-size: 100%; }  /* browser default of 16px */
    h1 { font-size: 1.5em; }   /* 24px (1.5 * 16) */

This formula comes in handy:

    target / context = result

In this case, we our target is `24px`. The context is the `body`'s font size, which is `16px`. So,
we use `1.5em`.

For layout, use percentages instead of fixed pixels.

    .blog { width: 93.75%; }  /* 900px (% of 960px) */

I noticed that the author tends to use percentages for flexible widths and `em` for flexible height.
This makes sense, since height is tied to typesetting.

Context is usually the size of the containing element. Sometimes, it can be the element itself -
such as padding. This makes sense when you think about the box model.

# Flexible Images

Whereas the last chapter was on layout and text, this chapter is about images and other media. These
also need to scale correctly depending on viewport size.

    <div class="figure">
      <img src="robot.jpg" alt="" />
    </div>

    .figure { width: 48%; }

If the image is too large for its containing element, its overflow will just show and break the
layout. Well, technically it doesn't break the layout.

You have two options:

1. use `max-width:100%` to scale the image
2. use `overflow:hidden` to hide the extra parts

This works well for more than just `img`:

* img
* embed
* object
* video

This works for most browsers except IE6 and below. If you have to support these browsers, you can
use `width:100%` which always matches the width of the container or use JavaScript.

For background images, you could use the CSS3 property `background-size`. Unfortunately, browser
support is limiting. Scott Robbin has created a jQuery plugin called Backstretch which works very
well.

# Media Queries

Fluid layouts and flexible images will get your site very far, but sometimes your design will just
break on smaller/larger resolutions. You can use media queries to change your layout accordingly
(for example, turning a two-column layout into a single-column).

Media queries is a CSS3 feature born from media types. You've seen media types before. They're
especially handy for print stylesheets:

    <link rel="stylesheet" href="..." media="all" />
    <link rel="stylesheet" href="..." media="screen" />
    <link rel="stylesheet" href="..." media="print" />

    @media print {
      /* css goes here */
    }

The media query adds a query component, letting you target specific characteristics like size:

    @media screen and (min-width: 1024px) {
      /* css targets screens 1024px and wider */
    }

Some properties to target:

* width - width of display area like browser viewport
* height - height of display area
* device-width and device-height
* orientation - portrait or landscape
* aspect-ratio
* device-aspect-ratio
* color - bit depth

The most common one you'll use is `max-width` and `min-width`. Now you can change your layout
depending on the browser viewport size! You can add CSS rules which override older ones
conditionally.

Another feature to use is the `meta` element with `viewport`. Apple's iPhone was the first to
support it, but many other devices have followed:

    <meta name="viewport" content="width=320" />

This forces the iPhone browser to render the page with a `320px` width. By default, it shows a width
of `980px` but scaled down to the device size.

    <meta name="viewport" content="initial-scale=1.0,width=device-width" />

The above will force the device to render at the device width without zooming in or out.

Media queries are supported by most browsers except IE8 and below. Luckily, developers have created
JavaScript alternatives that you can use. A full featured one is called `css3-mediaqueries.js`. A
more lightweight one is called `respond.js` <https://github.com/scottjehl/Respond> which just
supports `min-width` and `max-width`. You'll also need to add a CSS comment in your stylesheets so
media queries can be parsed:

    @media screen and (max-width: 768px) {
      ...
    }/*/mediaquery*/

# Becoming Responsive

Content is king. Sometimes you'll even want to switch your content depending on the device. For
example, a mobile user might be more interested in a restaurant's location/hours than the menu. Of
course, that's just an assumption.

Many developers advocate creating the site for mobile users first. Often time, they're left as an
after thought. This way, you create a focused site that's optimized for mobile users before adding
more content for desktop users.

Some of the sizes you should target:

* 320px for smaller screens like iphones
* 480px for smaller screens like iphones in landscape
* 600px for smaller tablets
* 768px for larger tablets like ipads
* 1024px for larger tablets like ipads in landscape
* 1200px for desktop browsers