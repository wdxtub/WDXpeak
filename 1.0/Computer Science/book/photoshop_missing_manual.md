# Photoshop CS5: Missing Manual

Lesa Snider has written a complete guide to Photoshop CS5 for beginners in this missing manual. It
covers most of the features available in Photoshop which is a good foundation for users to build
upon. It also covers some techniques used to solve common problems (ie. correcting color/lighting).

# Photoshop CS5 Guided Tour

Photoshop comes with a few different views, use 'Window -> Application Frame' to toggle between
them. There's the classic floating-window frame and the new application-frame which has one window.

The application frame consists of:

* Tools panel - list of tools available in Photoshop
* Application bar - minimize, maximize, etc...
* Options bar - options for current active tool you're using
* Document tabs - work on multiple documents at once
* Live Workspaces - configure placement of panels
* Panels - commonly used features in Photoshop
* Document window - the actual image you're working with

It's easier to select tools using keyboard shortcuts. Some tools actually have more than one kind,
for example the Gradient or Sold fill. Hit 'G' once to select the tool or hit 'Shift-G' to cycle
between types.

Below the tools are color chips, one for foreground and one for background. Hit 'X' to toggle
between the two.

Use 'Cmd-Option-Z' to undo actions or 'Cmd-Shift-Z' to redo actions. If you need to undo every
action since opening this file, use 'File -> Revert'.

# Opening, Viewing, Saving Files

Use 'Cmd-N' to create a new document. You'll then input the size, resolution, and color profile.
Most of the time this will be RGB. Be sure to set the correct background contents also (most of the
time this will be transparent).

To save a file use 'File -> Save' or 'Cmd-S'. Use 'File -> Save As' or 'Shift-Cmd-S' to save as a
different filename or format.

* JPEG is a good format which takes up little space at the price of quality
* GIF is popular for animations, transparent backgrounds, or images which use little colors
* PNG has true transparency, a wide range of colors, and higher quality images

It's always a good idea to save your document as PSD so you can edit it later. When you're satisfied
with your changes, you can export it to the file type you want.

**Raster** images are made up of pixels of colors. **Vector** images are made up of points and
paths. Vector images can be scaled without any loss of quality.

Use 'File -> Open' or 'Cmd-O' to open an existing document. You may also open documents as Smart
Objects using 'File -> Open as Smart Object' which will let you edit them non-destructively.

The 'File -> Open Recent' menu option is useful so you won't have to dig through your filesystem.

Zoom in and out with 'Cmd-+' and 'Cmd -' (or use your scrollwheel). To zoom to a specific area, use
the Zoom tool. Use 'Cmd-1' to zoom/dezoom to the actual size of the document (100%). Use 'Cmd-0' to
zoom to fit the screen. Hold the 'H' key to get a aerial view of your document to move around. Open
the Navigator panel to zoom into specific locations.

The Application Frame will let you organize your documents via cascading, stacking, etc... in case
you have multiple documents open.

Use 'Cmd-R' to toggle the document rulers. You can configure which units to use in the Units & Rules
preferences. Click on the horizontal/vertical ruler to create a guide and use the Move tool (V) to
move them. Use 'View -> Snap to -> Guides' so objects will snap to guides while you're moving them.
To hide the guides use 'Cmd-;', delete a guide by dragging it back to its ruler, and delete all
guides with the menu option 'View -> Clear Guides'.

'View -> Show -> Grid' to see the document grid. To configure it, go to 'Photoshop -> Preferences ->
Guides, Grids, and Slices'.

Photoshop has a Ruler tool to measure the distance between two objects. It's grouped with the
eyedropper (Shift-I).

# Layers & Nondestructive Editing

**Destructive** editing means you're changing your original image. **Non-destructive** editing means
you're not changing the original image and can go back at anytime. To do non-destructive editing,
you use **layers** - a set of transparencies stacked on top of each other to form a whole image.

* Image layers - pixel based
* Type layers - used for text
* Shape layers - creates vector-based shapes
* Fill layers - changes or adds color to an image
* Adjustment layers - adjusts the layers below it
* Smart Objects - a container which imports an external source
* 3D/Video layers - for importing video or other special sources

Right-click on a portion of your image to get a list of layers in the area that you clicked. When
you do actions in Photoshop, it only affects the currently selected layer. The highlighted layer in
your Layer panel is the current active layer.

Hit 'Shift-Cmd-N' to create a new layer. Use 'Option-[' to select the layer below the current one
and 'Option-]' to select the layer above. Hold down 'Shift' while doing layer movements to select
multiple layers. Use 'Option-.' and 'Option-,' to select the first/last layers. Use 'Cmd-Option-A'
to select all layers except the locked background. To move the selected layer, use 'Cmd-[' and
'Cmd-]'. To move the selected layer all the way to the top/bottom use 'Shift-Cmd-[' and
'Shift-Cmd-]'.

To duplicate a layer, use 'Cmd-J' or option drag a layer. To delete it, press the 'delete' key or
use the trash icon in the Layers panel. 'Cmd-C' and 'Cmd-V' will only copy/paste from the current
selected layer.

You can do **transformations** on a layer such as resize, rotating, etc... Just select the layer and
hit 'Cmd-T'. While dragging handles, hold 'Option' to expand in multiple directions. Hit 'Return'
when you're done.

To move a layer perfectly vertical/horizontal, hold down the 'Shift' key while you're moving it.
Holding 'Shift' while using the arrow keys will move it 10 pixels either way.

Photoshop attempts to align layers by snapping them to boundaries of other layers of guides that you
set. To see these boundaries, use to Move tool (V) and turn on the 'Show Transform Controls'
checkbox in the Options bar.

You can link two or more layers so that they don't separate. For better protection from accidental
edits, you can also lock down layers by clicking on the lock icon in the Layers panel. There are 4
types of locks:

* Lock transparent pixels
* Lock image pixels
* Lock position
* Lock all

You can organize your layers into groups. Click the folder icon in the layers panel to create a new
group. Or select your layers first and hit 'Cmd-G'.

Layer comps are snapshots of your work, they can be used to create different versions to show to
other people. Choose 'Window -> Layer Comps' to edit your layer comps.

Sometimes you'll need to **rasterize** a layer, which changes it from vector base to pixels based.
To do this, just choose 'Layer -> Rasterize'.

You can merge layers if you know you'll never want to change them. Use 'Layer -> Merge Down' or
press 'Cmd-E'. You can also hide the ones you don't want to merge and use 'Layer -> Merge Visible'
or 'Shift-Cmd-E'.

Stamping is a safer version of merging because the resulting operation produces a new layer. The
keyboard shortcuts are 'Cmd-Option-E' and 'Shift-Cmd-Option-E'.

**Blending** refers to how one layer interacts with the colors on another layer for the areas they
intersect. There's more about it in Chapter 7.

**Masks** are like masking tape used for painting. They cover areas that you don't want to effect
(or vice-versa). Some layers come with them automatically. To add it, click on the circle icon in
the Layers panel.

Painting with black will conceal and white will reveal. Use 'B' to choose the brush tool and use the
'X' shortcut to toggle quickly between two color chips. Use the left bracket '[' or right bracket
']' to change your brush size. 'Ctrl-Option-drag' will change your brush hardness.

For more options, use the Masks panel to edit a mask's opacity/density, feathering, or edge. You can
also add/subtract to a mask using color ranges from this panel.

**Styles** can be added to layers to add pre-made effects. Some styles include:

* outer/inner shadows
* inner/outer glows
* inner bevel
* pillow emboss
* satin
* color/gradient overlay
* pattern overlay
* stroke (borders)

Just select a layer and click on the 'Add a layer style' button at the bottom of the Layers panel to
add one. Option drag a style to move it from one layer to another. Ctrl-click a style to see other
options (disable, copy, delete...)

# Selections

Selections let you perform actions on a certain portion of your image or layer, including:

* filling in with a solid color or gradient
* adding an outline
* moving it around
* resize or transforming
* creating a mask

When a selection is made, the view on your screen is called **marching ants**. You'll see these
marching ants surrounding the area you selected.

Some shortcuts for selections are:

* Select all with 'Cmd-A'
* Deselect with 'Cmd-D'
* Reselect with 'Cmd-Shift-D' or just use undo
* Inverse selection with 'Cmd-Shift-I'
* Load layer as selection by Cmd-clicking the layer's thumbnail image
* Select all layers with 'Cmd-Option-A'
* Deselect layers with 'Select -> Deselect Layers'
* Similar layers will select all of the same layer types 'Select -> Similar'

Hit 'M' to get the Marquee tool and 'Shift-M' to cycle between them. You can use the options bar to
add/subtract from a selection or you can use keyboard shortcuts:

* Hold 'Shift' to add to a selection
* Hold 'Option' to subtract from a selection
* Hold 'Shift-Option' to intersect with a selection

**Feathering** means making the border of your selection more transparent so it blends it better.
**Anti-alias** smooths the color transition at the border. Use the **Style** option to restrain to a
fixed size or aspect ratio.

You can use the shape tool to make a selection (or mask). Just create a shape and 'Ctrl-click' on
the add mask icon. This will create a vector mask, which you're free to resize without losing any
quality.

Photoshop also includes tools to select by colors. Use the **Quick Selection** tool (W) by dragging
it across your picture. You can change the brush size to get better results.

The **Magic Wand** (Shift-M) is great for pulling an image out of its solid color background,
whereas the Quick Selection tool is more suited at selecting objects. Just click once to use the
Magic Wand. A tolerance value of '0' will select pixels with exactly the same color. Tolerance can
go up to 255.

You can expand on your selection by choosing 'Select -> Grow' or 'Select -> Similar' in the menu.
Grow will only select the pixels adjacent to your current selection, whereas similar will select all
similar pixels in the image.

'Select -> Color Range' is more fine tuned and can select partial pixels (using opacity). If you're
trying to select adjacent pixels, use the Localized Color Clusters setting. You can use the 'Cmd'
key to switch temporarily between the image and its selection preview.

The **Background Eraser** and **Magic Erasers** are useful to erase using colors. Use 'Shift-E' as a
keyboard shortcut. The Background Eraser has a brush size which will only affect that area, but only
colors similar to the pixel under your crosshair. The Magic Eraser doesn't have a brush size,
instead it uses a wand similar to the magic wand. For these tools, it's best to duplicate your
layers before you start destructive work.

To select irregular shapes, use the **Lasso** tools (L). The regular lasso lets you draw a selection
freeform, the polygonal lasso is useful for selecting polygon shapes where you can identify points.
The Magnetic Lasso will attempt to guess the curves of your selection using the color of pixels.

When you're finished making a selection, you can refine it further using 'Cmd-Option-R' or 'Select
-> Refine Edge'. You can tweak options, Adobe recommends doing it in this order:

* Smart Radius to automatically determine soft/hard edges
* Radius is the size of the selection
* Refine Radius to fine-tune your selection even more
* Erase Refinements if too much background is included
* Smooth to make your edges look less jagged
* Feather to blur the edges
* Contract to sharpen the edges
* Shift Edge to make your selection smaller (tighten it)
* Decontaminate Color to prevent **edge halos**, which will attempt to replace the edge colors with
  other colors nearby
* Output To to determine what to do with the result

To create a border selection, use 'Select -> Modify'. Transform a selection by choosing 'Select ->
Transform Selection'.

You can also paint selections with brushes using **Quick Mask Mode**. After making a selection,
press 'Q' to toggle Quick Mask Mode.

Choose 'Select -> Save Selection' to save it for another time. Choose 'Select -> Load Selection' to
reload it.

To add a **Stroke** to an image, make a selection and then choose 'Edit -> Stroke'.

# Control Colors with Channels

**Channels** are storage containers for all of your image's color information. Eyes are sensitive to
different wavelengths which produces different colors.

**Additive color system** works by adding light to create colors - all it takes is red + green +
blue. The absence of light is black. Monitors use this system to display colors. When all 3 lights
overlap, you see white.

**Subtractive color system** uses a combination of light that's reflected ( which you see) and light
that's absorbed (which you don't see). This is how printed color works using cyan + magenta + yellow
+ black, all of which absorb light. The paper the ink is printed on is a reflective surface.

Cyan ink absorbs red light and reflects green/blue light back to you, creating the cyan color. A mix
of all cyan/magenta/yellow absorbs most of the primary colors - reflecting back dark brown.

To find out whether you're in RGB or CYMK mode, choose 'Image -> Mode'. In RGB mode, your image
stores its color information in red/green/blue channels. You can actually see the grayscale
representation in the **Channels panel**. The lighter areas represent a large amount of that
particular color, whereas black areas represent the absence of that color.

There are 3 types of channels: composite, color, and alpha. Composite is all colors mixed together.
**Alpha channels** are for saved selections. They get their name from alpha compositing - combining
a partially transparent image with another image for special effects. The same technology lets you
save your selections for later use. They're sometimes referred to as **channel masks**.

Photoshop stores alpha channels are a grayscale representation of your selection. Black is the
unselected portion, lighter areas are the selected portions. Click on 'Create new channel' button to
create one and paint with a white brush to select an area. Or make a selection and choose 'Select ->
Save Selection'.

To reload your alpha channel as a selection, 'Cmd-click' on the thumbnail or click the 'Load as
selection' button.

You can also use channels to help you make your selections, here we'll remove the blue background
from an image:

1. Make sure your image is in RGB mode, choose 'Image -> Mode'
2. Find the channel where your channel is the darkest (absent of this particular color), use
   'Cmd-3,4,5' to quickly cycle through channels
3. Duplicate the channel so your original won't be destroyed
4. Adjust the channel's Levels to make what you want to keep black and what you want to remove white
   (the background) by choosing 'Image -> Adjustments -> Levels' or 'Cmd-L'
5. Using the white eyedropper, click the gray background to make it white
6. If necessary, touch up with black/white paint
7. Load the channel as a selection
8. Invert the selection by choosing 'Select -> Inverse' or 'Cmd-Shift-I'
9. Hide your new channel and turn on the composite channel
10. Add a layer mask, which will use the current selection as a mask

You can lighten/darken a channel temporarily to make a difficult selection. Select a channel, make a
copy of it, then choose 'Image -> Apply'. Choose either 'Screen' to lighten or 'Multiply' to darken.

# Cropping, Resizing, and Rotating

**Cropping** means eliminating distracting elements in an image by cutting away unwanted bits around
the edges. Press 'C' to get the crop tool and drag it across the screen to crop your image. CS5
includes a grid so you can crop your image according to the golden ratio. The darkened portion is
called the shield. Use the square handles to resize the box. Hit 'Enter' to crop.

In the options bar, set the 'Hide' option to hide the shield area instead of deleting it when doing
a crop. Just grab the layer with the Move Tool (V) to move the cropped area back into view. You can
also set a specific size.

While you're adjusting the crop handles, you can hold the 'Option' key to expand equally in all 4
directions.

Cropping can be done with selections by choosing 'Image -> Crop' after making a selection. 'Image ->
Trim' is handy if you don't know the exact dimensions of the crop, it can base its dimensions on
transparent/color pixels.

'File -> Automate -> Crop' will automatically crop and straighten photos based on its edges (useful
when scanning photos).

**Pixels** are the smallest unit in a **raster** image. They have no pre-determined size.
**Resolution** determines how small/large a pixel is. It's helpful to think of resolution as pixel
density - it's measured in terms of pixels per inch or **PPI**. More PPI means smaller pixels, which
results in a smoother image. Printers can modify its output, so a high resolution image will look
much better than a lower resolution one. Monitors have a cap on its resolution, that's why an 85 ppi
image looks identical to an 850 ppi image.

To resize an image, choose 'Image -> Image Size' or hit 'Cmd-Opt-I':

* Scale Styles determines if Photoshop should scale any layer styles like drop shadows
* Constrain Proportions locks the aspect ratio
* Resample Image is key to changing resolution without changing image quality. **Resampling** is the
  process Photoshop uses to resize your image by adding or subtracting pixels.

Resampling is useful for images meant for monitors, you can lower the resolution without harming
image quality. The methods available are:

* Nearest neighbor looks at the closest neighboring pixel and copies it, it's useful to small file
  size (but has lowest image quality)
* Bilinear averages the colors directly above/below and to the sides, its only advantage over the
  next 3 methods is that it's fast
* Bicubic is similar to bilinear, but it uses 2 pixels to each side
* Bicubic Smoother will blur the new and old neighboring pixels to create a smoother effect. Adobe
  recommends this for making images larger
* Bicubic Sharper is similar to Bicubic but will soften the pixel's edges, Adobe recommends it for
  making images smaller

If your image will be displayed on the web, you can compress it by choosing 'File -> Save for Web &
Devices'.

To resize the canvas, choose 'Image -> Canvas Size' or 'Cmd-Opt-C'.

Photoshop added a neat feature called **Content Aware Scale** which allows you to scale selected
areas of your images while keeping other areas intact. This is useful for scaling backgrounds
without effecting people in photos:

1. Hit 'Q' to go into Quick Mask mode
2. Press 'B' for brush and 'D' to set to black/white
3. Paint with the area you want to protect with the black brush
4. Press 'Q' to exit quick mask and 'Cmd-Shift-I' to invert selection
5. Save as alpha channel and deselect
6. Choose 'Edit -> Content Aware Scale' or 'Cmd-Opt-Shift-C'
7. From the option's bar Protect menu, choose 'Alpha 1'
8. Grab the handle and resize it

**Transformers** let you resize, rotate, flip, skew, and distort images. They're available in the
menu, but just 'Edit -> Free Transform' will let you do all available transformations (or hit
'Cmd-T').

* Scale by dragging a handle, hold 'Option' to resize in all directions
* Rotate by hovering over a handle until it turns into a curved cursor and drag
* Skew/slant by holding 'Cmd-Shift' while dragging one of the sides
* Distort by holding 'Cmd' while dragging a corner
* Alter Perspective by holding 'Opt-Cmd-Shift' and dragging a corner
* Warp by using the option bar 'Switch between free transform/warp'
* Flip/rotate can be done via the menu with preset numbers

Apply a transformation again by choosing 'Edit -> Transform -> Again'.

# Combining Images

The easiest way to combine images is to copy the area you want and paste it into another image. You
can do this with 'Cmd-C' and 'Cmd-V'. To copy from all available layers use 'Shift-Cmd-C'. To paste
it in the exact location it was in the old document, use 'Shift-Cmd-V'. Paste into a selection with
'Opt-Shift- Cmd-V'. You can use the 'Paste Outside' option to get an automatic layer mask from your
selection.

Fade two layers together by placing one above the other and using the Eraser tool with a soft brush.
A better, non-destructive approach would be to use a layer mask with the soft brush. The smoothest
transition can be made with a gradient mask.

**Blend modes** define how one layer interacts with another layer. Photoshop has a few different
methods for you to use. You can set a layer's blend mode from the Layers panel. It's helpful to
think of colors on a layer being made up of 3 parts:

* Base color that you start out with that's already on the image
* Blend color of another layer you're putting on top or brushing with
* Result after mixing the base/blend colors

Photoshop categorizes its blend mode based on the mode's neutral color - the color that causes no
particular change.

The blend modes are (use Shift-Opt prefix):

* Normal - shows the pixels on top which blocks bottom pixels (N)
* Dissolve - turns semi-transparent pixels into spray of dots (I)
* Darken Modes will darken or **burn** your image, white is neutral * Darken - keeps the darkest of
  the base/blend colors and combines (K) * Multiply - increases the base color by the blend color
  (M) * Color Burn - darkens by increasing contrast, useful for intensifying dull backgrounds in
  photos (B) * Linear Burn - combo of Multiply/Color Burn, darkens by decreasing brightness which
  produces the darkest colors. Great for grungy, textured collages (A)
* Lighten Modes will lighten or **dodge** your image, black is neutral * Lighten - keeps the
  lightest of the base/blend colors and combines (G) * Screen - multiplies the opposite of the blend
  and base colors like bleach, useful for when images are too dark or underexposed (S) * Color Dodge
  - decreases contrast, tends to turn light pixels solid white and dark pixels on your image stay
  the same (D) * Linear Dodge - increases brightness, combination of screen/color dodge (W) *
  Lighter Color - compares base/blend and keeps lightest pixels
* Lighting Modes do darkening and lightening to increase contrast, and have a neutral of 50% gray *
  Overlay - color > 50% gray ? color * base : color * 1/base (O) * Soft Light - equivalent of
  shining a soft light, making bright areas brighter and dark areas darker (F) * Hard Light -
  similar to Overlay but uses Multiply/Screen for dark/light pixels respectively (H) * Vivid Light -
  applies Color Burn/Dodge to dark/light pixels respectively (V) * Linear Light - applies Linear
  Burn/Dodge to dark/light pixels (J) * Pin Light - applies Lighten/Darken (Z) * Hard Mix - reduces
  range of colors to look flat like a cartoon (L)
* Hue Modes relate to color and luminance (brightness) values, they're extremely practical to
  intensify, change, or add to colors * Hue - keeps lightness/saturation of base colors and adds the
  hue of the blend color. Useful for changing object's color without changing how light/dark it is
  (U) * Saturation - keeps luminance and hue of base color and picks up the saturation of the blend
  color. Useful to increase an image's color intensity (T) * Color - keeps luminance of base color
  and picks up hue/saturation of blend, useful for colorizing a grayscale image (C) * Luminosity -
  keeps base color's hue/saturation and uses blend's luminance, useful for sharpening an image or
  when using curves/levels adjustments (Y)

There are also blending options in the Layer Style dialog box that are useful for editing
backgrounds. Double-click a layer's thumbnail in the Layers panel to access it.

The "Blend if" section has two gradients with sliders. Each slider lets you make pixels transparent
based on its brightness - the left slider being the shadows and right slider represents the
highlights.

You can auto-align layers with 'Edit -> Auto-Align Layers', which lets you align multiple photos
into a panorama or make collages. 'Edit -> Auto-Blend' will blend those images together to make the
panorama more realistic.

Clone an image with the Clone Stamp tool:

1. Open both images, source and target
2. Press 'S' for Clone Stamp tool then open Clone Source panel
3. 'Opt-click' the area you want to copy
4. Create a new layer in the target
5. Paint to clone the item

**Displacement maps** is a grayscale image that Photoshop will warp onto the curvature of another
image. This is useful for placing textures onto skin or other objects:

1. Find the channel with the greatest contrast on your subject
2. Duplicate and send to new document named 'Map'
3. Use 'Filter -> Blur -> Gaussian Blur' on the displacement map just a bit so the map is smooth
4. Save map and close file
5. Go back to original document and turn composite channel on
6. Select the subject's are you want the map on
7. Invert with 'Cmd-Shift-I'
8. Feather the edges slightly
9. Save selection with 'Select -> Save Selection'
10. Place the map onto the face
11. Choose 'Filter -> Distort -> Displace', use the Map document from step 2
12. Load the face selection with 'Select -> Load Selection'
13. Add a layer mask to areas you don't want to show
14. Change the map's blend mode to 'Multiply'

# Draining, Changing, Adding Color

**Desaturating** means draining the color for your image. In Photoshop, use 'Image -> Adjustments ->
Desaturate' to turn your image black/white.

The get a less flat black/white image, use the Black/White Adjustment layer which lets you set
different types of contrast:

1. Open your image
2. Open the Adjustments panel, click the Black/White Adjustment layer icon
3. Move the various sliders until you have a nice image
4. Optionally add a tint (like a fake Sepia)

All Adjustment Layers come with a mask, if you want to have an area with color cover that area with
black paint in the mask. Fading a color to black/white is as simple as using a gradient on that
mask.

A high contrast black/white image has no gray in it. To create one:

1. Open the Adjustments panel, click the Threshold icon (rectangle with diagonal black stripes)
2. Drag slider to right to make shadows more black. Drag slier to left to make highlights more
   white.
3. Press 'O' for the Burn/Dodge tool to edit your image's darkness/brightness
4. Merge the layer/adjustment. Use `Filter->Blur->Gaussian blur` for softer edges
5. Optionally, create a new color layer - bright red - move it to top
6. Set that layer's blend mode to Darken

To change colors in Photoshop, use the Hue/Saturation adjustment mask:

1. Select the area you want to change - skip if you want to change everything
2. Create a Hue/Saturation adjustment mask
3. To change color, change the hue slider left or right
4. To adjust intensity, change the saturation slider left or right
5. To adjust brightness, change the lightness slider left or right

You can target specific colors instead of replacing the entire image or selection:

1. Add the Hue/Saturation adjustment layer
2. Use the Target Adjustment tool - it's a hand with two arrows
3. Use the eye droppers at the bottom to edit your thresholds
4. You can edit with eye droppers or via sliders. The dark gray on the slider represents hues which
   will completely change. The light gray represents hues which will partially change

A single dialog way to change color is 'Image -> Adjustments -> Replace Color'. Select your
threshold with eye droppers then adjust with sliders.

Snider recommends the Selective Color Adjustments layers as an easy and powerful way to replace
colors:

1. Add a Selective Color adjustment layer - square divided by 4 triangles
2. In the adjustment dialog, choose a color to adjust
3. Use the sliders to adjust their RGB or CYMK values

The destructive Match Colors command will attempt to match the colors of one image with another:

1. Open your source and target images in RGB mode
2. In the target, choose Image -> Adjustments -> Match Color
3. Select the source document
4. Adjust image options

The Photo Adjustment Layer is handy to do slight changes to colors like warming a photo:

1. Click the Photo Filter icon - it looks like a camera with a circle above it
2. Select from a list of 20 presets or turn on the color option
3. Use the Density slider to adjust - it's just intensity

The Posterize Adjustment Layer removes most of the colors. It's not that useful, but it's fun to
play with to make photos look like cartoons.

The Invert Adjustment Layer will invert colors for you.

Variations will add a quick tint to black/white photos:

1. Choose Image -> Adjustments -> Variations
2. Choose one of the colored previews
3. Re-click previews to add more intensity, adjust with right panel

The Color Balance Adjustment Layer is just like Variations, except it's non-destructive and uses
sliders instead of previews.

To paint color onto a black/white image:

1. Add a new layer for paint
2. Set the paint layer's blend mode to Color
3. Grab the brush tool and paint

The Gradient Map Adjustment Layer adds a gradient to your image. It uses the highlights and shadows
to determine where to place the gradient:

1. Set color chips to black/white (D) and add the Gradient Map Adjustment layer
2. Click the gradient preview to open the Gradient Editor
3. Edit the gradient's color stops
4. Change the layer's blend mode to Color to only affect hue

# Correcting Color/Lighting

**Shadows** are created when light is blocked. **Highlights** represents the lightest or brightest
parts of your image. **Midtones** are what fall between the two extremes.

To use Photoshop's auto-correction tools, you'll need to do some setup:

1. Choose Window -> Adjustments, then the Levels icon (fire with 3 triangles)
2. Option-Click Auto button to open the Auto Color Correction Options
3. Choose Find Dark & Light Color algorithm
4. Turn on Snap Neutral Midtones checkbox
5. Set target shadow color by entering 10 in each RGB field
6. Set Clip field to 0.10 percent
7. Set target midtone by entering 133 in each RGB field
8. Set target highlights by entering 245 in each RGB field
9. Turn on "Save as Defaults" and click OK

**Color cast** means your photo is flat with a single color - like everything looks green. If your
photo is flat or has color cast, try the Auto Color tool. Photoshop hunts down shadows, highlights,
and midtones and changes them to the targets you set. It works well for oversaturated images. Choose
Image -> Auto Color or "Shift-Cmd-B".

The Variations adjustment is also handy to fix color casts. Just choose Image -> Adjustments ->
Variations and pick a preview.

The Color Balance tool will shift colors to be on opposites sides of the color wheel. It's available
as a layer: choose Color Balance from Adjustment panel. Or choose Image -> Adjustments -> Color
Balance or 'Cmd-B' for the destructive version.

Photo Filter will add tints to your photo. Use the opposite tint to remove color casts. Image ->
Adjustments -> Photo Filter or use the Adjustment layer.

Photoshop has some tools to automagically fix lighting issues also:

* Auto Tone adds more contrast to brighten your image. Use 'Shift-Cmd-L' or click the Levels/Curves
  button on the Adjustments panel then Option-Click the Auto button. Choose Enhance Per Channel
  Contrast and click OK.
* Auto Contrast will adjust your contrast without affecting colors. It's useful for a little boost
  in contrast - but will keep flat images flat. Use 'Opt-Shift-Cmd-L' or use the Adjustment panel's
  Levels button, Opt-Click Auto, and choose Enhance Monochromatic Contrast algorithm.
* Shadows/Highlights will quickly darken shadows and lighten highlights. It's referenced later.
* Equalize will turn your highlights white and shadows black. Choose Image -> Adjustments ->
  Equalize.
* Dodge/Burn tools will let you darken/lighten using a brush
* Brightness/Contrast adjustment tools will adjust the brightness/contrast. Leave the legacy
  checkbox off, the new algorithm will detect which areas to brighten. Access it from your
  Adjustment panel (looks like the sun) and adjust the settings.

Shadows/Highlights is the most useful and is for when your camera doesn't have flash or it failed to
go off. Choose Image -> Adjustments -> Shadows/Highlights. Use the advanced options:

* Set amount slider to 20 to 35% to avoid noise
* Leave tonal width to 50%, which tells Photoshop which shadows to adjust. A low number means
  Photoshop will only adjust the darker shadows.
* Increase Shadows section's Radius slider to 250 to 300 px. This algorithm works by analyzing the
  surrounding pixels of shadows. This setting tells Photoshop how big the neighborhood is.
* Set Color Correction to 0 to prevent messing with colors
* Leave Midtone Contrast at 0
* Leave the black clip and white clip set to 0.01%
* Click 'Save as Default'

To get better results, Snider recommends running the Shadows/Highlights adjustment in Lab mode.
Switch to it temporarily with Image -> Mode -> Lab Color. Don't flatten or rasterize. Choose Window
-> Channels and select the lightness channel. Now run the Shadows/Highlights adjustments. Switch
back to RGB with Image -> Mode -> RGB.

**Level** adjustments change intensity levels of your shadows, midtones, and highlights to fix
lighting problems, increase contrast, or even balance color in your image.

A **histogram** is a visual representation of information about your image. Look at one with Window
-> Histogram. It looks like a mountain range. The width represents tonal range (range between
lightest and darkest pixels). The height represents how many pixels are at that particular
brightness.

Create a Level Adjustment layer by clicking the histogram icon in the Adjustments panel. Adjust the
shadows, midtones, and highlight sliders to their min/mid/max positions to adjust contrast. The
sliders at the bottom are for pure white/black pixels. You can also use the Levels eyedroppers to
determine shadows/highlights.

Use Window -> Info to see data about your image. Mouse over any part of your image to see the exact
color value.

By curving a diagonal line on a grid, you change the brightness of all pixels in your image. To
create a Curves Adjustment layer, click on the Curves button (looks like an S) on the Adjustments
panel. The diagonal line represents your curve. You can place 14 points on it which you can then
drag upwards or downwards to change the brightness of your image.

Use the Vibrance Adjustment layer to intensify your image's colors. It usually doesn't completely
destroy skin tone. The Vibrance slider works well but the Saturation slider tends to be over-kill.

You can also make colors pop using Lab/blend mode:

1. Choose Image -> Mode -> Lab Color
2. Duplicate your layer with 'Cmd-J'
3. Choose Image -> Apply Image
4. Change Blending popup menu to Soft Light
5. In Channel popup, select the one that looks best
6. If necessary, lower the channel's opacity
7. Switch back to RGB, choose Image -> Mode -> RGB

# Photoshopping People

The **Spot Healing Brush** (J) will look at the pixels outside the cursor's edge and blend them with
the pixels inside. It's useful to get rid of moles or pimples. Press the [ or ] keys to resize your
brush. The Mode option determines which blend mode to use. Type tells Photoshop which pixels to use.
Content Aware Fill is an amazing tool which can remove unwanted power lines or people from photos.

The **Healing Brush** is similar, but instead of looking for pixels directly outside of the cursor
you need to give it a sample point. Option click with the brush to set a sample point. Then mouse
over the bad skin and brush away.

The **Patch** tool works like the Healing Brush but is better for removing piercings, tattoos, or
highlights/shadows. You draw an outline over a large area, click inside the area, and drag it to a
sample point to use.

The **Clone Stamp** can get rid of sweat shines. Press 'S' to activate, choose a soft edge brush and
Darken blend mode in the options bar. Lower the opacity to 20-30 percent. Set sample popup to all
layers. Option click to get a sample point. Now brush away the sweat shine.

Fix flabby chins by selecting it with the lasso tool, Filter -> Distort -> Pinch it. Enter 100 in
the amount field. You can follow the same steps with the Liquify filter to pull in bulges.

Any parts of your image can be selected and used with the Free Transform tool. This is useful for
slimming or expanding.

Use the **Gaussian Blur** filter to smooth out freckles. Create a new layer with a mask to just get
the face. Lower the layer's opacity and apply the Gaussian Blur filter (Filter -> Blur -> Gaussian
Blur). Use these same steps with the Easy Glamour Glow filter for a face glow effect.

You can imitate the dodge/burn tools by creating a new layer, setting its blend mode to Soft Light
and painting with 50% gray. It's a non-destructive way to lighten images (and reduce wrinkles).

A quick way to enhance eyes is to lighten them and change their blend mode to Screen. Add an empty
Adjustment layer with mask around your subject's eyes. Set the blend mode. You can intensify the
effect by duplicating the layer. Adjust by lower opacity.

Use the **Red Eye** tool (part of the healing brush set) to remove red eyes.

# Art of Sharpening

If your image came from a digital camera or scanner, it needs sharpening. Sharpening improves your
photo's focus.

You can sharpen with the Sharpen, Sharpen Edges, Sharpen More filters. Snider advises that these
give no control and you shouldn't use them.

Smart Sharpen lets you pick the settings. This one is recommended. Unsharp Mask used to be the gold
standard but Smart Sharpen has mostly replaced it.

Sharpening is a destructive process, so be sure to:

* resize your image first
* reduce any noise first (Filter -> Noise -> Reduce Noise), the settings are:

Strength - increase if you have a lot of color or grayscale noise Preserve Details - to protect
details in your image at the expense of noise Reduce Color Noise - increase to reduce color noise
even more Sharpen Details - combines sharpening, resist using it (use Smart Sharpen) Remove JPEG
Artifacts - if you're dealing with a compressed JPEG

* sharpen your image on a duplicate layer
* change the sharpened layer's blend mode to Luminosity
* sharpen your image a little bit, multiple times

The unsharp mask is easy to use:

1. Either duplicate a layer or create a smart object: Filter -> Convert for Smart
2. Choose Filter -> Sharpen -> Unsharp Mask
3. Change layer's blend mode to Luminosity

Some options in sharpening:

* Amount determines how much lighter/darker to turn light/dark pixels
* Radius determines how many pixels Photoshop will look at
* Threshold controls how different neighbor pixels have to be for edges

Some general guidelines:

* Soft stuff like flowers or babies don't need much sharpening. Amount should be around 150%, Radius
  to 1, and Threshold to 10.
* Portraits need little sharpening, to make eyes stand out you can set Amount to 75%, Radius to 2,
  and Threshold to 3.
* Objects, landscapes, and animals are tough to sharpen because there aren't any real edges. Try
  Amount 120%, Radius 1, and Threshold 3.
* Max sharpening for buildings, cars, or anything with edges: Amount 65%, Radius 4, Threshold 3.
* Everyday sharpening: Amount 85%, Radius 1, Threshold 3
* Sharpening for Web (or downsized image): Amount 200%, Radius 3, Threshold 0

The smart sharpen filter is a bit more difficult to use:

1. Create a duplicate layer
2. Choose Filter -> Sharpen -> Smart Sharpen
3. You'll have tons of options including:

* Remove what kind of blurs to reduce. Gaussian is basic and what Unsharp
     Mask uses.  Lens should be picked in image has a lot of noise.  Motion if
     your subject in the photo was moving and blurry.
* Angle - if you used Motion Blur, set the angle the blur is occurring at * More Accurate - more
precise sharpening at a time cost * Fade Amount - reduce amount of sharpening on shadows/highlights
* Tonal Width - control which highlights/shadows to sharpen

Use a mask to sharpen only a portion of a layer.

# Painting in Photoshop

Snider starts by teaching us the basics of color theory, the foundation of painting in Photoshop.

A color scheme refers to any group of colors. A color wheel is a tool that helps you pick a good
scheme. There are primary colors (RGB or CYM), secondary colors, and tertiary colors. Secondary
colors are made by combining primary colors. Tertiary colors are made by combining a primary and
secondary.

A color is actually made up of three things: Hue, Saturation, and Brightness. Hue just means the
"color" itself, like red or green. Saturation is the intensity of the color. A highly saturated hue
is vivid, whereas the less saturated is dull and gray. Brightness is how light or dark a color is.
100% brightness is white, 0% brightness is the absence of light (or black).

You usually select a base color first when selecting a color scheme. For more tips on color
combinations, see notes on Non Designer's Design Book.

The Eyedropper tool (I) can be used to grab the exact color on an image. CS5 introduced an even more
accurate Sample Ring. Click once to set your foreground chip to that color. Option-Click to set your
background chip.

Snider recommends the Kuler and Panetone Matching System extensions.

You can store your frequently used colors in the Swatches panel, choose Window -> Swatches to
activate. Hover over an empty panel and click on it to set the panel to your foreground chip. Click
a swatch to set your foreground chip. Cmd-Click to set your background chip. Finally, delete it by
Opt-Clicking.

The Color panel is a more concise way to pick your colors. Choose Window -> Color to activate it.

The Brush (B) tool has tons of options:

* Tool presets let you save settings to re-use them
* Brush Preset picker has built-in brushes
* Brush Panel lets you customize your brushes in CS5
* Mode is the blend mode similar to layers. It contains two extra ones:

Behind mode lets you brush behind the current layer and Transparent mode
* Opacity controls transparency of your strokes
* Flow controls how much paint to place onto your layer per stroke
* Airbursh option makes your brush behave like a spray can

CS5 saw the introduction of the Mixer Brush - it lets you brush over a previous stroke to mix colors
just like real life.

Snider walks us through a quick tutorial for painting:

1. Create an empty document and new layer
2. Select a small, hard-edge brush and set the foreground chip to dark gray
3. Sketch your drawing, don't worry about details which will be added later
4. Lower the sketch's opacity to 40%
5. Create a new layer for your refined drawing
6. Clean up your drawing until you're happy with it
7. Create a new layer and fill it with the color you'll use most
8. Grab a large, round, textured brush at 25% and start painting to add dimension to your background
   color (think different brightness of blues)
9. Create a new layer with a large 25% opacity brush and paint your subject
10. Keep creating new layers and painting more, refining at each step
11. Finalize your painting by adding texture - use funky-edged brushes or even add a background
   photo and set the painting's blend mode to Overlay

You can load more brushes by opening the Brush menu in the Options bar with the Brush tool selected.
Choose "Faux Finish Brushes" or any other types from the popup menu.

The Brush panel gives you amazing customization abilities. Choose Window -> Brush. The categories
are:

* Brush Tip Shape - lets you edit the Size, Flip X, Flip Y, Angle, Roundness, Hardness, or Spacing
  (amount of space between brush marks when you stroke)
* Shape Dynamics - natural/realistic vs solid/perfect brush marks. Size Jitter and Control controls
  how much the size of brush marks vary. Angle Jitter and Control controls angle variation and
  Roundness Jitter/Control is roundness variation.
* Scattering - create random marks around your brush as you stroke. Scatter and Control is how much
  to distribute your marks. Count and Count Jitter/ Control are used to color the numbers of marks.
* Texture - apply a repeating pattern to your brushstroke which makes it look textured. You'll have
  to load most of them (explained below). Invert will invert light/dark points so a repeating stroke
  will act differently. Scale controls the size of the pattern. Texture Each Tip to apply the
  texture to each brush mark within the stroke rather than replacing. Mode for blend mode. Depth
  controls how much paint seeps into the texture.
* Dual Brush - combine two brush tips. Mode for blend mode. Diameter controls the size of the tip.
  You can also control Spacing, Scatter, and Count.
* Color Dynamics - controls variety of color within your strokes. There's Foreground/Background
  Jitter Control, Hue Jitter, Saturation Jitter, Brightness Jitter, and Purity.
* Transfer - these are the extra customizations you can make. There's Opacity, Flow, Wetness, and
  Mix.
* Some other options are Noise for random textures onto tips, Wet Edges, Airbrush, Smoothing, and
  Protect Texture.

Load textures by clicking the down array inside the Texture preview in your Brush panel.

Some suggested customizations by Snider are:

* Round, hard-edged: 25% opacity, 0% spacing, Size Jitter = Pen Pressure for shading, blocking in
  color, and sketching
* Rough-edged: 25% opacity, 0% spacing, Maybe Flow Jitter = Pen Pressure for shading, adding
  texture, making hair
* Rough brush: 30% opacity, 0% spacing, Angle Jitter = 20%, Control = off for adding texture and
  shading
* Small dot brush: 30% opacity, 0% spacing, Size Jitter = Pen Pressure, Opacity = Pen Pressure for
  making hair, shading
* Round rough-edged brush: 100% opacity, 20-25% spacing, Size Jitter = Pen Pressure, Opacity Jitter
  and Flow Jitter = Pen Pressure for shading/block coloring
* Textured round brush: 30% opacity, 0% spacing, Flow Jitter = Pen Pressure for adding texture and
  shading
* Textured round brush: 100% opacity, 0% spacing, Size Jitter = Pen Pressure, Flow Jitter = Pen
  Pressure for sketching, creating line art, and adding fine details
* Scattered spot brush: 70% opacity, 25% spacing, Scatter = 20%, Size Jitter = Pen Pressure,
  Opacity/Flow Jitter = Pen Pressure for adding texture

You can create a new brush by:

1. Creating a 300x300 document
2. Making a paint dab with 100% black and gray paint. The black paint will be completely opaque and
   the gray paint will be semi-transparent
3. Use a Rectangular Marquee to select the dab
4. Choose Edit -> Define Brush Preset
5. Create a new document and grab the Brush tool (B)
6. In the options bar, select your new brush from the Brush menu and open the Brush panel
7. Customize and save your brush

# Drawing with Vector Tools

Photoshop lets you set down points to make a path, which can be used to create vector objects
(lines, circles, squares, other shapes). These objects are then infinitely tweak-able. You can use
vector tools to add new elements to your image, create precise selections, or create precise masks.

Photoshop has three drawing modes:

1. Shape Layers - Any click will create a new Shape Layer, when you finish laying out your shape its
   foreground will be filled. It works with the Pen and Shape tools. It's useful for adding shapes
   to images.
2. Paths - In this mode, Photoshop turns whatever you draw into an empty outline. You can use it to
   create selections or new shapes, but Photoshop won't automatically create a new layer and fill it
   for you. New paths will exist on the Paths panel.
3. Fill Pixels - Only works with shape tools. It's like the Shape Layer tool, but it automatically
   rasterizes the new layer.

With the Pen tool you create **anchor points** and **control handles**. Two anchor points make up a
line. Control handles are used to create curves. There are two types of anchor points: Smooth and
Corner. A smooth curve is round whereas a corner is a square corner without control handles. Click
and immediately let go to create a corner anchor point, drag for smoothness.

Once you're done setting anchor points, hit Esc or Cmd-Click to exit. Use the Direct Selection tool
(Shift-A) to drag any of the anchor points. Use the Convert Anchor Point tool (Shift-P) and drag on
any anchor point to convert it.

Some tips:

* Exaggerate curves by dragging one side of the control handle in the opposite direction of the
  path.
* The length of the control handle determines the depth of the curve.
* To create an open path, just hit Esc. To create a close path, hover your mouse above the first
  anchor point and click.
* You can add a control handle to anchor points by Opt-Clicking.

You can only have one working path at a time. Save your path using the Paths panel. Hit Return to
hide the gray line so you don't accidentally edit it.

All shape tools work the same, here are the steps to draw a line:

1. Select the Line tool (Shift-U)
2. The options bar (and disclosure menu) should have options specifically for the shape. For a line,
   that includes arrowheads and width/weight.
3. Pick a line color
4. Click where you want the line to start, drag to where it ends
5. You can double-click on the Shape Layer's thumbnail in the Layers panel to edit its color

Once you've created a shape, you can edit it like any other paths. Use the Direct Selection tool to
move anchor points. Use the Pen tool to add or subtract points. Use Free Transform or layer styles
or special effects. For other shapes you'll need to drag diagonally. Hold Shift while dragging for
perfect proportions.

Every new shape creates a new layer. If you want to use the existing layer, use the Option bar's
Add, Subtract, Intersect, and Exclude buttons.

To add a point, hover over an existing path with your Pen tool and click where there are none. Or
you can use the Add Anchor Point tool. To delete a point, hover over it with the Pen tool until a
minus sign appears. Or use the Delete Anchor Point tool.

The Direct Selection tool turns your cursor into a white arrow and lets you select a single point.
The Path Selection tool turns your cursor black and lets you select entire paths. Once selected:
Option drag to copy it, hit Delete to delete it, align it with alignment toolset, combine it using
Options toolbar, or resize it with Free Transform.

Once you have a path, you can add a stroke to it. Just create a new layer then choose Stroke Path
from the Paths panel's menu. Or activate the tool you want to use for stroking (Brush usually) and
then click the Stroke Path button.

You can also fill in a path. Create a new layer then choose Fill Path from the Paths panel's menu.
The higher the number in the Feather Radius field, the softer/more transparent the edge. Anti-alias
will make the edge harder.

You can also make a selection from a Path. Just choose Make Selection from the Path panel's menu. Or
click Load path as selection button - which skips the dialog. Or Cmd-Click the path's thumbnail in
the Paths panel.

If you drag an image layer over a shape layer with a vector shape on it, you can create a **clipping
mask**. Just choose Layer -> Create Clipping Mask.

For a regular vector mask, create your vector shape first. Use the Paths drawing mode. Then
Cmd-click the layer you want to add a mask to and select "Add a layer mask". The mask is now
infinitely resizable.

# Artistic Text

Snider warns us about some typography offenses:

* Overusing decorative fonts
* Using too many fonts per design
* Setting whole sentences in capital letters
* Underlining text that's not a hyperlink
* Centering large bodies of text
* Misusing straight vs smart (curly) quotation marks
* Misusing hyphens, en dashes, and em dashes. Hyphens combine words, en dashes are a substitute for
  to as in 10AM-11AM (Option-hyphen on Mac), em dashes are for abrupt changes in a sentence
  (Shift-Option-hyphen)
* Creating ellipses with periods. Three periods have too much space in between, instead use Option-;
  on a Mac

A **Glyph** is a unique graphical representation of a character. A collection of glyphs is called a
**typeface**. A **font** is a specific typeface, size, style, and weight. Times New Roman is a
typeface, Times 14-pt bold is a font.

There are three font formats: PostScript, TrueType, OpenType. PostScript is the oldest and will work
with almost any printer. TrueType was developed by Microsoft/Apple and is the most common format
today. TrueType fonts on Windows can be used on Macs, but not vice-versa. OpenType was developed by
Microsoft and Adobe, it's the most compatible on all systems and a single file can contain more than
65,000 glyphs. It's not supported by older printers though.

There are too many font categories to list out, but Snider introduces us to these four:

* Serif - these have little lines (serifs) extending from the main stroke that looks like feet to
  help lead the eye from one character to the next. They're great for large bodies of text due to
  high legibility. Glyphs tend to have a thick/thin stroke with transitions.
* Sans serif - these are missing serifs and usually have a uniform stroke. They display well at
  small sizes and are ideal for headlines or web copy.
* Slab serif - these have serifs, are usually thick, and have a uniform stroke. Use them to attract
  attention like headlines.
* Decorative - this category is for distinctive, eye-catching fonts.
* Scripts - designed to look like they were hand written.

There are several font **styles** like bold, semi-bold, italic, or condensed. When they're included
in the font it's known as native. Photoshop can fake a style for you, just set the style in the
Character panel. It usually looks fine on screen but is horrible for printing.

Choose Photoshop -> Preferences -> Type -> Edit to preview your fonts in the font selection drop
down.

All font lives on a **Type Layer**. Select the Horizontal Type Tool (or Vertical) by hitting 'T'.
Click anywhere to start typing. Clicking creates an initial point and the text is called Point Text.
To create a newline hit return, to end your typing hit enter. You can also create Paragraph Text,
just drag a box or Option-Click with the type tool. You set a boundary and Photoshop will
automatically fit your text.

Move your text by placing your cursor outside the type layer, wait for it to turn into a move
cursor, then drag it. Or hold Cmd while dragging inside the Type layer.

If you keep the Type tool activated, you can select text by double clicking or click and dragging.
To load your text as a selection, Cmd-click on the thumbnail in the Layers panel. Loading as a
selection lets you apply styles, effects, and other common layer edits.

While you're editing, hold Cmd to get resize handles. This lets you dynamically resize your type
layer. With the Type layer activated, use Cmd-T to begin a Free Transform.

Photoshop includes a Type Mask tool which lets you type characters to create a mask. When you're
done typing, just hit Enter to create a selection. You're not limited to horizontal or vertical.
Create a path with the Pen tool, then select the Type tool and click along the path to type with it.
You can type within a Shape by doing the same (wait until your cursor turns to an I-beam with
surrounding dots).

The options bar lets you format:

* Type Tool Preset Picker - presets of saved font preferences. You can make a new preset by
  selecting your options then clicking the disclosure triangle on this tool.
* Text Orientation
* Font Family
* Font Style - native styles for the font family you selected
* Font Size - use Photoshop -> Preferences -> Units & Rulers to switch units
* Anti Aliasing - use none on small text to make it clean/sharp and strong or smooth on larger text
* Alignment
* Text Color
* Create Warped Text
* Character Panel - advanced formatting options

**Leading** (rhymes with "bedding") controls the amount of blank space between two lines of text.
**Kerning** refers to the amount of space between a pair of letters. **Tracking** is the space
between all letters in a word. Adjusting tracking is useful to fit words into a space. Text's
**baseline** is the invisible line where letters sit. Changing it via a **baseline shift** will make
some characters appear higher or lower.

Photoshop includes two auto-kerning methods in the Character Panel: Metrics and Optical. Metrics
kerning uses the letter pairs to determine kern amount. Optical adjusts kern based on the
characters' shape.

Horizontal/Vertical Scale can be used to scale your characters. All/Small Caps lets you capitalize
all letters. Super and Subscript will shift the baseline and point size of selected characters.
Language will adjust your text with a spell check and hyphenation.

Fractional Widths is turned on by default, which rounds characters widths. Adobe recommends you turn
this option off for smaller text (under 20pt) to give it more breathing room.

System Layout turns off Fractional Widths and anti-aliasing to render text the same way your OS
renders it. No Break will force Photoshop to reflow words so a particular word won't break with a
hyphen. Reset Character will reset your formatting options (just in case).

The paragraph panel has fewer options:

* Justification
* Indentation
* Margin after paragraphs
* Hyphenate

Snider mentions how headers should have more spacing above it than below. This follows the rule of
proximity to relate headers to its paragraphs.

A really neat trick is adding multiple strokes to text:

1. Type your text in a new Type layer
2. Make it a selection and open Layer Styles
3. Check the Stroke section, and open the Gradient editor
4. Give it 2 or more colors in the gradients as solid chunks

You can use a photo or filter to add texture to text:

1. Add the text in a new Type layer (make sure you have a white background on the layer below)
2. Load the text as a selection and create a mask
3. Choose Filter -> Distort -> Ocean Ripple or Filter -> Sketch -> Torn Edges

It's useful to convert your type into a vector shape for further editing. To do this, select Layer
-> Type -> Create Work Path or "Convert to Shape".

# Filters

If you convert a layer into a Smart Object, you can make filters run on their own layer - sometimes
known as a **Smart Filter**. Not all filters run on Smart Objects (like Extract and Liquify). For
these, you'll need to duplicate your layer before running to avoid destructiveness. To use a Smart
Filter just choose Filter -> Convert for Smart Filters with your layer selected.

Copy a filter by Option-dragging them from one layer to another.

The categories of filters are:

* Artistic - make your image resemble paintings or cartoons
* Blur
* Brush Strokes - to create traditional fine art effects
* Distort
* Noise - add or remove grains
* Pixelate
* Render - deals with lighting
* Sketch - adds a bit of texture to your image
* Stylize - high contrast artistic filters (like making a sketch from an image)
* Texture

Make a Lens Blur:

1. Open image and locate Channels panel
2. Create a new alpha channel
3. Use Brush tool to paint with 50% opacity on area you want focused
4. Turn off alpha visibility and select RGB channel
5. Open Layers panel and duplicate original layer
6. Choose Filter -> Blur -> Lens Blur
7. Change Depth Map source to Alpha 1
8. Turn on Invert
9. Adjust Radius slider

Add a jagged frame:

1. Select where you want the frame to surround
2. Add a layer mask, select it
3. Choose Filter -> Brush Strokes -> Spatter

Add snowflakes in the foreground:

1. Create a new layer filled with black
2. With black layer selected, choose Filter -> Convert for Smart Filters
3. Change blend mode to Screen (ignores black)
4. Choose Filter -> Sketch -> Graphic Pen
5. Set Stroke Direction to Vertical, Length of 5, Light/Dark Balance of 90
6. Choose Filter -> Gaussian Blur with radius of 1.5

Convert a photo into a pencil sketch:

1. Add a black/white adjustment layer
2. Choose Filter -> Convert for Smart Filters
3. Chose Filter -> Stylize -> Find Edges
4. Open the filter's blending options, change to Hard Mix with opacity 85%
5. Choose Filter -> Blur -> Gaussian Blur with radius of 2
6. Change Gaussian layer's blend mode to Lighten

One of the fast filters is to create a darkened edge effect:

1. Filter -> Convert for Smart Filters
2. Filter -> Lens Correction
3. On Custom tab, adjust Amount and Midpoint

# Photoshop and the Web

This chapter is all about keeping your file sizes down and image quality up. You can do this by:

* Adjusting the image's dimensions properly
* Deciding on which file format to use
* Compressing the file

Snider recommends these dimensions:

* 800x600 for design or photo sample that won't be printed
* 640x480 for emailing a photo
* 320x240 for sending a gallery of photos
* 100x133 for thumbnails or headshots

Sometimes it's easier to resize images visually instead of with dimensions:

1. Open image and zoom in/out until it looks right on the screen
2. Make a note of the zoom percentage
3. Open Image Size dialog (Cmd-Option-I) or choose Image -> Image Size
4. Change width/height to zoom percentage values
5. Choose Bicubic Sharpener from Resample Image popup for best quality
6. Click OK

Snider recommends these formats:

* JPEG for photos
* GIF for images with solid blocks of colors or animations
* PNG for images with transparent backgrounds or high quality images

The Save for Web & Devices dialog is for saving and compressing images at the same time. It also
gives you previews so you can monitor file size and quality.

1. Choose File -> Save for Web & Devices
2. Click the 4-Up tab
3. Click the preview window and choose a file format
4. Adjust quality and color settings "Dither method and amount" if your image contains colors that
   old monitors cannot display, this will fake the colors with dithering. A high dither amount
   produces more accurate color; the tradeoff is larger file size. Usually Diffusion is the best
   method which simulates with a random pattern.
5. Make sure convert to sRGB is turned on (for Windows monitors)
6. Edit the Copyright and Contact Info
7. You can edit (remove) colors using the Color Table
8. Click Save

You can create an animating GIF:

1. Add a layer for each frame
2. Choose Window -> Animation
3. Keep adding new frames by clicking the "Add Frame" icon at the bottom
4. Select each frame, then set it to only show the layer you want
5. Press play to preview, save when done

Creating a favicon:

1. Create a 64x64 image with 72 resolution
2. Place your artwork into the document
3. Use Free Transform if needed
4. Resize document to 16x16
5. Sharpen image if needed
6. File -> Save As and select ICO