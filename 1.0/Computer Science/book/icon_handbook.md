# Icon Handbook

Jon Hicks is an amazing designer. His most famous work is probably the icon for Firefox. In this
book, he walks us through the theory behind icons and how to create icons.

# A Potted History of Icons

Humans used to communicate via symbols and pictures: pictographs paintings and petroglyphs carvings.
Eventually symbols came to represent abstract ideas - the difference between pictograms and
ideograms.

Isotype (International System of Typographic Picture Education) was an icon system developed by Otto
Neurath to be universal. The pictograms developed for Isotype are still used today.

The first computer icons appeared in 1974 on the Xerox Alto. The Star, a successor machine included
the first GUI and used icons for files, directories, disks, and more.

# How We Use Icons

This chapter covers our uses from a universal language to conveying emotions. It also covers when
not to use icons.

On the web, icons add visual interest to text. For software, icons can represent functions. You can
remove text instructions all together and just use icons.

Hicks uses a website navigation as an example of how to use icons poorly. In the example, the icon
and text are evenly spread apart:

    [i]   blog   [i]   portfolio   [i]   downloads   [i]   contact

But each icon is supposed to represent a navigation item. It's better to use proximity to tie the
icons together with its text:

    [i] blog     [i] portfolio     [i] downloads     [i] contact

Icons can represent what users should expect when taking an action. A play button means expect a
video. A magnifying glass means expect zooming in. A PDF icon means expect downloading a PDF.

Chat applications use status icons so users can see others' status at a glance. Status icons work
well for file editors too (unsaved, pending, uploading).

Icons can be used to convey feedback. A red X could mean a user error. A green checkmark means the
last action was a success.

Some common mistakes for using icons:

* is it being used for just decoration?
* is it repeated so often that it loses its purpose?
* are there too many icons in a small space?
* is the concept too abstract for an icon?
* is the interface too overwhelming with lots of icons?

# Favicons

Favicons are an ideal place to start because you need to achieve pixel crisp artwork and clarity at
small sizes. They're 16px by 16px and are used to represent websites. When creating an icon, you
need to answer:

1. What is the context? Think backgrounds, themes, and platforms.
2. What sizes are needed?
3. What formats are needed?

ICO files are the most widely supported. They can contain multiple bit depths and resolutions. PNG
is more convenient.

When creating your icon, it's helpful to use a pixel grid. For small icons, make sure straight edges
are kept within the grid. Anything "halfway" will appear blurred.

Some tips when designing a favicon:

* you might have to redraw your icon from scratch to fit a 16px square
* remember that your favicon will be on different backgrounds, it might be better to use a
  transparent color which changes depending on its background
* it's best not to use any perspective which requires more pixels
* if your logo won't fit into a square, just choose a portion of it
* IconBuilder is a handy application to create `.ico` files

# Metaphor

This chapter follows a client scenario. If a convention already exists, use it. If not, create a new
convention.

The first thing you need to ask when creating an icon is how to best represent that tool, function,
or direction?

To figure this out, you can break it down:

1. What is the icon for?
2. What is its context?
3. Who's it for?
4. Is there a single message? Sometimes the goal is too dispersed and needs to be focused.
5. Does it need to even be an icon?

Some tips for figuring out if a metaphor already exists:

1. Use Google's image search
2. Use <http://thenounproject.com>
3. Use <http://iconfinder.com>

If you need to start from scratch, try doing a mind map. Start with the message you're trying to
convey and then create new nodes which are related. For the "view" function, some nodes could be:
eyes, detail/close-up, sight, literal view. Each node can have something that could represent it:
actual eyes, magnifying glass, telescope, binoculars, glasses, landscape. Now ask the following
questions:

1. Would the icon be recognizable?
2. How much detail is required to make it recognizable?
3. Are there any negative connotations?

You can use combinations of pictograms to make your icon clearer. A plus sign with a document means
"New Document".

The final part is to use color. Here are some emotions evoked by different colors:

* red => importance, warm, life, love, revolution, celebration, good luck. Also stop, problems,
  danger, warning, error.
* orange => warmth, energy. Also cheap and RSS.
* yellow => joy, happiness, light, wisdom. Also warning, forbidden, cowardice, decay, secure,
  highlight.
* green => life, nature, vitality, go, growth. Also envy/madness. Technical uses include sharing and
  correctness.
* purple => royalty, cruelty, arrogance
* blue => daytime, calm, information, corporate. Also cold/corporate. Technical uses include
  selected, on, enabled.
* gray => luxury, sadness, disabled, off
* brown => comfort, nature, poverty
* black => sophistication, luxury, expensive, prosperity, death, mourning, evil, mystery, misery

# Drawing Icons

Some guidelines when drawing icons:

* Stay in context. If it's going to be used for a toolbar - draw it with the toolbar present.
* Stay in company. Don't draw each icon in isolation. Try to draw them in the same document next to
  each other to avoid inconsistencies.

Some helpful features your icon editor should support:

* vector drawing
* pixel grid
* pixel preview
* export options

The canvas size matters, especially for smaller icons. A symmetric arrow on a 16x16 canvas will have
a blunt/round pointy end. This is because the point occupies two pixel rows. Using an odd canvas
size (15x15), the pointy end will only occupy one pixel row making it pointier.

It's tempting to fill up the entire canvas with your icon. Don't, the icon weight needs to be
balanced. That's why it's important to draw them in the same document as each other.

Some tips to deal with scaling icons for multiple sizes:

* use Photoshop's smart objects or Illustrator's symbols
* keep details on a separate layer to show/hide depending on icon size

It's up to you how much detail to include. But excessive details sometimes reduce an icon's clarity
and crispness. It's a tradeoff. Try to avoid:

* excessive shadows and borders
* too much anti-aliasing
* perspective (for smaller icons)
* straight pixels that aren't crisp

If your icon uses a font, try using one that's specialized for smaller sizes like Verdana, Mini, or
Cellular (also called bitmap fonts).

Color depth is a number representing how many colors each pixel can represent. It's measured in bit
and usually called bit depth. 1-bit depth is just black and white with no grayscale. 4-bit depth was
capable of showing 16 colors. Most modern computers use 24-bit (16 million colors) or 32-bit (24-bit
color and 8-bit alpha channel). With 24-bits, each color channel RGB gets 8 bits or 256 different
options.

That's a lot of colors - but it's noticeable if a screen doesn't support as many colors during the
use of gradients, especially mobile devices. Dithering is a dotted effect to make these gradients
look better. It may make sense to include 4-bit versions with your icons for these other devices.

# Icon Formats and Deployment

Size is important. Displays have different resolutions - think retina vs regular iPhones. An icon
might look crisp on the regular iPhone but blurry on the retina display. Users can also zoom into
icons via their browsers. It's important to design icons that can scale.

For simple monochrome pictograms, vectors work great. For larger icons that require detail, you'll
need to create separate images.

Hicks recommends using the Mac app "Opacity" for creating icons of different sizes.

The most popular format for icons are PNG. If transparency is required for IE6, think about using
GIF. If it's specifically for OS X, you might want to use the TIFF format.

PNG, GIF, and TIFF were bitmap formats. Some browsers support SVG, a scalable vector format. There's
also Canvas as an alternative. PDF is supported by Quartz and is scalable for Mac applications.

For the web, you might want to use CSS3 media queries to determine the device resolution. This way,
you can display different icons depending on the resolution:

    @media="only screen and (-webkit-min-device-pixel-ratio: 1.5), only screen
            and (-o-min-device-pixel-ratio: 3/2), only screen and 
            (min-device-pixel-ratio: 1.5) {
      .icon {
        background-image: url(iconx2.png);
        background-size: 150px 40px;
      }
    }

Hicks also mentions browsers starting to support data-uris where the image is Base64 encoded and
embedded into the HTML or CSS.

A popular way to display icons is using fonts. You can use `@font-face` to declare a new "icon
font". See the Pictos icon pack for more info.

# Application Icons

Application icons tend to have the most detail and largest sizes. Its format is dependent on the
platform. Linux uses SVG, OS X uses ICNS, and Windows uses ICO.

The icon should be memorable. This is the most important trait of an application icon. Its metaphor
is still important.

Hicks walks us through the process of creating an application icon:

1. Sketching on paper.
2. Vector sketch without showing too much detail. Use basic shapes and simple gradients to get a
   concept out.
3. Draw and iterate on the detailed icon.
4. Export to the correct formats and sizes.

Application icons tend to use a lot of realism in its shading. Make sure the light source is from
one area and the perspective is consistent with other application icons. For example, OS X icons
tend to have a 9 degree rotation and are viewed as if the icon is on a desktop.

Textures tend to be realistic - leather, plastic, brushed metal. Be sure to keep your pixels crisp
for larger sizes.