# Beginning GIMP

An introduction to the GNU Image Manipulation Program or GIMP by Guillermo S. Romero.

# Getting to Know GIMP

The Toolbox window is GIMP's main window and includes most of the functions you'll be using. Its
menu bar isn't tied to any particular image. When you activate a tool, its options will be displayed
below. If you accidentally remove it, get it back with `File -> Dialogs -> Tools`.

When you edit an image, you'll get an Image window. Near the bottom left, there's a QuickMask tool
and the bottom right has the Navigation control.

GIMP usually starts with one dialog - the Layers dialog. This lets you edit, re-arrange, create, or
delete layers on your workspace. You can view more dialogs from `File -> Dialogs`. Every dialog is
movable and dockable. Menus also have a "tear-off", which lets you grab any menu and turn it into a
window of its own.

You can toggle the Menu Bar via `View -> Hide Menu Bar`. Just right-click for a context menu to get
the same menu.

Under Tool Options, be sure to change the Scaling to Cubic or Sinc. These use more CPU power, but
have higher quality.

You can customize your keyboard shortcuts with `Edit -> Keyboard Shortcuts...`.

# Improving Digital Photos

This chapter covers some basics like opening files, scaling, cropping, and saving files. I'll note
them very quickly:

1. To open a file, use `File -> Open`
2. Use `Image -> Scale Image` to scale
3. Use the Cropping tool in the toolbox for cropping
4. Use `File -> Save` to save. GIMP's file type is `XCF`

You've got a lot of options for formats. For JPEGs, there are a few quality settings with
trade-offs. Make sure you have `Show Preview` checked. Remember JPEG has lossy compression so it
loses quality every time you save. Some of the advanced options are:

* Optimize reduces file size without reducing quality, no reason not to use it
* Progressive lets users see a poor quality version when downloading the image before the high
  quality replaces it
* Smoothing, use restart markers, subsampling, and DCT method have good defaults that you shouldn't
  need to adjust
* Save EXIF data will save metadata about the image like camera information
* XMP is Adobe's metadata just like EXIF
* Comment is where you can include plaintext like your name

The Crop tool is relatively straightforward to use. Just select it from the toolbox and drag the
area to keep. There are also some additional options like cropping the current layer only, fixed
aspect ratios, or using numerical fields for cropping.

To control brightness or darkness, use `Tools -> Color Tools`. You'll have access to
brightness/contrast dialogs and the levels dialog. The levels dialog lets you choose different
channels - initially it's brightness but RGB channels are also available.

The Curves dialog is another way to adjust brightness, contrast, and colors. The horizontal bottom
bar represents input and vertical left bar represents output. Click on any spot on the line and drag
to adjust.

Some other adjustments you can make are Threshold (turns image into two tones with a given
threshold), Posterize (turns into an artistic poster), Desaturate (removes color), Invert, and Auto
(automated tools for photos). The Auto dialog can be broken down further:

* Equalize spreads the image colors out
* White Balance corrects color casts
* Color Enhance makes the colors more intense
* Normalize adjusts the exposure on underexposed images
* Stretch Contrast and Stretch HSV are like Normalize, but operate on the three color channels
  independently

The `Image -> Transform` menu lets you rotate or flip your image.

Sharpening can be done via the Sharpen or Unsharp Mask actions, both under `Filters -> Enhance`.
Unsharp Mask is very simple to use:

* Radius effects distance that sharpening works
* Amount is how strong it is
* Threshold controls smoothness

Use `Filters -> Enhance -> Red Eye Removal` to remove red eyes.

# Introduction to Layers

An image is made up of multiple layers, each on top of another. If a layer is completely opaque, it
will cover all layers underneath it. Use the Layers Dialog at `File -> Dialogs -> Layers` or
`Ctrl-L` to access them.

Some tools automatically create a new layer for you to work with, like the Text tool. Some tools
require you to select a layer before interacting with your image, like the Move tool.

GIMP comes with a few effects for layers. Drop shadows are available at `Filters -> Light and Shadow
-> Drop Shadow...`. GIMP creates a whole new layer that contains the drop shadow. This is useful,
because you can re-run the effect with different variables. Use the eye button in the Layers dialog
to toggle visibility and try out different parameters.

The chain link icon in the Layers dialog lets you link several layers together. This is useful if
layers need to stick together - like a drop shadow and its subject.

When you copy/paste, GIMP creates a new "Floating Layer". This is a historical artifact that will be
removed in future versions. Click the "New Layer" button to create a normal layer from the floating
one.

You can select multiple layers by holding down the Shift key while clicking them. Use the Align tool
to align multiple layers.

The Layer Dialog has many useful features:

* Layer Mode - the blending mode for the current layer
* Opacity - what % is transparent
* Keep Transparent - lock transparency so you can't draw on transparent portions of the layer
* Layers List - contains each layer
* Visibility Eye - toggles visibility
* Chain Link - locks two layers together
* Preview - preview of each layer
* Masks - hide portions of the layer

You can even right-click a layer for a context menu and more actions. For example, a useful one is
"Add Alpha Channel" which adds a transparency channel to the current layer. That way, erasing leaves
transparency instead of just plain white.

# Drawing

The first rule of drawing is to create a new layer. Add one with a name, width/height, and
transparent fill type.

The Pencil tool lets you draw sharp-edged lines. You can even set a brush size so the stroke is
thicker. Use `File -> Dialogs -> Brushes` for more options. If you edit a brush, it becomes a
parametric brush. You can adjust its radius, hardness, aspect ratio, angle, and spacing. Drawing
also lets you set various modes: dissolve adds randomness, behind draws behind anything already
present, color erase matches the current brush color and erases it. Use the brush tool for a
soft-edged stroke. The Airbrush tool is for fuzzier edges. The Ink Pen tool imitates a fountain pen.

The Eraser tool is like the Pencil tool, except it erases what's on the current layer. You can
configure it to be soft or hard edged.

GIMP doesn't have shape tools, but you can make any selection and fill it or stroke it. After making
a selection, choose `Edit -> Stroke Selection`. You can also use any line drawing tool. Use `Edit ->
Fill with FG Color` to fill your selection. For complicated selections, use the Bucket Fill tool.

You can even fill with patterns. A pattern is just a special type of image that's usually tile-able.
GIMP can help with this via `Filters -> Map -> Make Seamless`. An even more advanced plugin called
Resynthesizer does an even better job.

You can also fill with gradients using the Gradient Fill tool.

# Selection

To toggle your selection, use `View -> Show/Hide Selection` or `Ctrl-T`. The Select menu has a lot
of actions, like All or None (`Ctrl-A` and `Shift-Ctrl-A`) that are useful. `Select -> Invert` to
invert your selection. There's also `Select -> Float` which is similar to copy/paste, except it
keeps the pasted layer in the exact same location.

Also in the Select menu, you can:

* By Color - create a selection by color matching
* From Path - turn a vector path into a selection
* Selection Editor - edits your current selection
* Feather - makes edges fuzzier
* Sharpen - does the reverse
* Shrink and Grow
* Border - replaces a selection with a new one that follows the border
* Rounded Rectangle - to round off selections
* To Path - converts a selection to a path

Moving from the center of a selection will move the selection boundaries. Moving from the edge will
change the boundaries. Dragging with Ctrl and Alt pressed will float and move the selection.

The Magic Wand tool lets you select by similarly colored regions that are touching.

You can create a path and turn it into a selection using the Bezier Path tool. It works best if
you're zoomed in a lot. Keep adding points by clicking, when you're done Ctrl-Click on the initial
point to close the path. Hit Enter to create a selection. When you're creating a path, click and
drag a point to create a curve.

There are three modes with the Bezier Path tool: Design, Edit, and Move. By default you're in Design
- which is for adding new nodes. Switch to Edit to add/delete points. Check the Polygonal box if you
want to toggle the handles on new points. Remove a point by Shift-clicking on it in Edit mode.

The Intelligent Scissors tool works like Bezier Path tool, except it uses the image's colors as a
guide similar to the Magic Wand.

Every selection tool has four modes: Replace, Add, Intersect, Subtract. Use these to add/delete from
your selection.

QuickMask lets you use painting tools to make your selections. It can be turned on by pressing the
small button at the bottom-left corner of the image window. Paint with white to select, paint with
black to hide. Use gray for fuzzy selections.

Romero walks us through a neat trick to blur out the background of a photo. He uses Curves to darken
the background while keeping the foreground at the same lighting. Then he selects the foreground and
Gaussian Blurs the background.

You can save your selection as a channel - channels are just black/white images that represent an
aspect like QuickMask. Save a selection with `Select -> Save to Channel`. Right click a channel and
use `Channel to Selection` to convert it back to a selection.

A Layer Mask is sort of like a permanent QuickMask. It represents the alpha channel of a layer.
Right click a layer and use `Add Layer Mask` to get started. You can use `Edit Layer Mask` in the
context menu to toggle between editing the actual layer and the mask. `Show Layer Mask` shows you
the mask at full size.

SIOX or Simple Interactive Object Extraction is a new tool for automated foreground extraction.
First, draw an outline around the object. Next, draw on the object you want to extract. Stay away
from the parts you don't want. The tool will create a selection for you, hit Enter to accept.

# Erasing and Touching Up

Dodge/burn are terms from film photography. By exposing certain parts for a shorter/longer time, you
can get better details in light/dark areas.

The Dodge/Burn tool starts in dodge by default. There are three modes: Shadows, Midtones, and
Highlights. By default it's Midtones which works well in most cases. If you want to brighten a very
dark area, use Shadows. This lets you be a little sloppy with the brushing (it will only affect very
dark areas).

Opacity makes the effect more subtle. Other configurations you can adjust are Fade Out, Jitter, and
Exposure (for strength). Make sure you use one giant stroke - the tool won't re-dodge an area if you
highlight over it during a single stroke.

Burning is the opposite. Unfortunately for digital cameras, these areas are usually so saturated
they only record white. That means Burning can only be used for areas that are a little brighter.

The Smudge Tool drags a color and smudges it across your stroke. This is useful for smudging out
unwanted objects in photos.

The Clone Tool can be used for similar cases but gives greater control. Instead of a stroke, you set
a clone source and then paint onto the destination. Choose a source by holding down the Ctrl key.

The Heal Tool is similar to cloning, but it combines texture from the source layer with
color/lighting of the destination.

The Blur/Sharpen tool is like a mini blur/sharpen filter via brush.

# Filters and Effects

GIMP's effects are located in the image window's `Filter` menu or the Toolbox window's `Xtns` menu.
Filters operate on the existing image and Xtns will create new images.

Most filters are implemented via GIMP plug-ins. Whereas tools can respond to clicks in the editor,
plug-ins can only be configured via their own dialog.

Whenever you run a filter, a new action item appears in the Filter menu called `Repeat Last`. This
does exactly what it sounds like. `Re-show Last` will re-open the filter's dialog. `Reset all
Filters` will reset all dialogs.

Here's a quick overview of some filters:

* Gaussian Blur - simplest blur
* Motion Blur - blurs in a single direction
* Selective Gaussian Blur - gaussian blur that keeps edges sharp
* Tileable Blur - blur that can later be combined for tiles
* Sharpen - for sharpening images
* Unsharp Mask - advanced sharpening
* Antialias - makes jagged edges smoother
* Despeckle - removes noise from images
* Destripe - removes vertical lines left by scanners
* NL Filter - combination of smoothing, despeckle, and destripe
* Distort - category of filters creating fun effects
* Light Effects - category of filters dealing with light and shadows
* Noise - adds noise to image
* Edge Detection - creates outlines from images
* Aristic - category which turns photos into artworks
* GIMPressionist - crown jewel of filters, includes large amount of options for many artistic
  effects
* Cloud - adds cloud pattern

The Xtns menu has many scripts to create new images. This is especially useful for creating
ready-to-use buttons, logos, and images.

# Color

This chapter includes a review on color (RGB, CYMK, additive vs subtractive) and color depth (8-bit
or 256 colors, 24-bit or 8-bit per channel, 32-bit includes alpha channel).

HSV stands for Hue, Saturation, and Value. GIMP uses 0 to 360 to represent hue for degrees.
Saturation ranges from 0 to 100. Value is the brightness.

A quick way to adjust color is via `Colors -> Hue-Saturation`. Another way which deals with
shadows/highlights is `Colors -> Color Balance`.

For greatest control on adjust color, use Levels or Curves.

To change a photo to black/white, use `Image -> Mode` or `Colors -> Desaturate`.

`Image -> Mode -> Decompose` or `Filters -> Colors -> Decompose` will let you see your image in
different channels. Remember the human eye is most sensitive to the color green. Decomposing is
particular useful for creating selections. For example, get the blue channel with a Threshold and
QuickMask to select it.

`Colors -> Channel Mixer` gives complete control over colors and luminosity.

Some popular effects for photos:

* "old style" via `Filters -> Decor -> Old Photo` or `Script-Fu -> Decor -> Old Photo`
* `Colors -> Colorize` then choose a Sepia tone
* Add a new layer with fill color #a28a65, change its mode to Color

If you need to set thresholds (for example, make a picture completely black and white), use `Colors
-> Threshold`. This works great for scanned books where there's usually a shadow near the binding.

# Advanced Drawing

Some Layer Mask tricks:

* you can use a gradient from white to black to fade out a layer
* make a selection, feather it, change to a layer mask to get a faded out mask
* make it fuzzier with a Gaussian Blur on the mask

GIMP has several blend modes for layers:

* addition - adds color of both pixels
* subtract - removes color of front pixel from back pixel
* difference - absolute value of subtraction
* multiply - generally makes the image darker
* divide - generally makes the image white out
* burn/overlay - similar to multiply
* dodge/screen - similar to divide
* hard light - combination of multiply and screen
* soft light - tends to soften edges and dim colors
* darken/lighten - shows only the darker/lighter of two pixels
* grain extract - gives desaturated look
* grain merge - adds texture to the image
* hue/saturation/value - only takes one of the HSV from the front pixel, the other two are taken
  from the back pixel
* color - takes hue/saturation from front, keeps brightness from back

The easiest way to create a brush in GIMP is to copy the image and access it via "Clipboard brush"
in the Brush dialog. Brushes can be grayscale or colored. A brush is saved with the .GBR file
extension. If you save a GIMP file with multiple layers with the .GIH file extension, it becomes an
animated brush with each frame represented by a layer.

GIMP comes with its own built-in patterns. You can create your own patterns the same way you can
create a brush. The easiest is to create a "Clipboard Pattern". `Filters -> Map -> Make Seamless` is
a useful filter for creating your own patterns.

# Advanced Composition

Romero shows us how to change the color of a car:

1. select the parts of the photo you want to colorize
2. copy the selection and paste into a floating layer
3. now fill the layer with the color you want
4. experiment with layer modes, in this case Color will work nicely
5. this works with two-tone colors or gradients also
6. some modes look strange at first, experiment with the opacity

This technique loses details easily, like the fur on a squirrel. In that case, you can keep the
texture by using Grain Extract or Grain Merge modes.

Layer modes can be used to improve photos also. To brighten a dark photo, duplicate it and change
the duplicated layer's mode to Screen. Adjust the opacity until it pleases you.

Self-composing with Overlay or Hard Light will turn a flat image into one with more bright colors.
Overlay or Burn works well to see through fog or haze. You can even stack multiple layers with
Overlay.

If you're compositing two images - like texture onto an original image - Soft Light works very well.
Overlay is good if the bottom layer is dark. Use Screen for a lighter effect.

Grain Merge is great for adding texture to an image.

# Plug-ins and Scripting

GIMP's architecture makes it easy to add plug-ins and scripts. A plug-in uses the C language and
compiles with GIMP whereas scripts don't need to be compiled in.

See `Xtns -> Plug-in Browser` for the plug-ins already installed. This is also useful to search for
functionality you might not already know exists.

To find other plug-ins, you can search through GIMP's official plug-in registry at
<http://registry.gimp.org> or just do a Google search.

You can write GIMP scripts in any scripting language. GIMP has its own language called Script-Fu
which is a dialect of Scheme.