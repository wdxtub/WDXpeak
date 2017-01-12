# How to Cheat in Photoshop CS5

Steve Caplin shows us how to create realistic photomontages with Photoshop CS5. Along the way, he
teaches us a lot of time saving shortcuts and tricks. This book is full of tutorials made up of
screenshots - these notes will be much more valuable paired alongside those images.

# Selection

Caplin walks us through using Elliptical Marquee to select the hubcap of a tire and make duplicates:

1. Use the Elliptical Marquee tool, Opt-drag to expand from center outwards. Make sure you hold down
   Opt after you click.
2. Holding down Opt before dragging for subtracting from selection
3. Holding down Shift adds to the selection
4. Opt-Shift dragging will intersect with your previous selection
5. Space bar modifier lets you move just the selection as you draw it
6. To actually move the contents Cmd-drag
7. Cmd-Opt-drag make a copy and move it
8. Hold down shift to constrain movement horizontally or vertically
9. You can continue making copies with each mouse release while holding Cmd-Opt

The Lasso and Magic Wands:

1. Straightforward scenes with a solid background are easy for the Magic Wand
2. Start by clicking the white area background
3. Hold shift and click additional areas to add to your selection
4. Once you have all the background selected, invert with Cmd-Shift-I
5. Switch to the Lasso Tool and hold Shift to add anymore areas
6. Hold Opt to turn the Lasso Tool into the Polygonal Lasso Tool

QuickMask is the most powerful tool for selections in Photoshop:

1. When your selection subject and background colors are too similar, it's too hard to use the Magic
   Wand. It's also too difficult for irregular shapes for the Lasso. Press 'Q' to enter QuickMask
   mode.
2. Paint the inside of your subject with a hard edged brush, use 'X' to toggle between your
   black/white chips. You can also use the Magic Wand tool to select the middle portion and fill the
   foreground (expand if necessary).
3. Once you have the basic outline, work on the details. Lower your brush size with '['.
4. Enter 'Q' to get your marching ants and perform your action
5. You can make a soft edged selection with a soft-edged brush, use 'Shift-['
6. You can make semi-transparent selections by using a gray color

QuickMask lets you use transformation tools to augment selections. We'll use the hubcap example
again, this time the tire is at an angle:

1. Make an elliptical selection and switch to QuickMask mode
2. Enter free transform with 'Cmd-T' and move your selection to an angle
3. When you're done moving your selection over the tire, hit 'Enter' to finish

The Quick Selection tool lets you drag to create a selection:

1. Hit 'W' or 'Shift-W' until the tool is selected
2. Drag over the portion of the image you want to select. Keep dragging to add more areas, Opt-Drag
   to remove areas.
3. Use the Refine Edge dialog to see how your selection fares, hit 'Cmd-Opt-R'. Auto-Enhance to
   provide a smoother selection.
4. Switch between different background colors to see your selection in detail
5. Adjust sliders to enhance your selection

Refine Edge dialog can be used to make softer selections:

1. Start by creating a new text layer 'Hard Text' and load it as a selection
2. Bring up the Refine Edge dialog 'Cmd-Opt-R' and preview its Alpha Channel which is the last
   preview icon
3. Fix blurriness by increasing contrast (80% works well)
4. Make it round by feathering the selection, more feathering = more round
5. Hit OK when you're done to get a selection, then fill it with color

The Pen tool can be used to draw paths, shapes, or make selections:

1. To draw a straight line just click for two points, constrain by horizontal or vertical or 45
   degrees by holding shift before clicking
2. Click then drag to create a curve point, don't drag for a corner
3. The curve points have tangents called handles which can be used to edit their curvature
4. 'Opt-click' on an existing point to turn it into a corner. 'Opt-click' and drag to turn an
   existing point into a curve.
5. Click on the starting point to complete a shape
6. Hold 'Cmd' to move points with the Pen tool active. 'Opt-click' to edit points or add new ones to
   an existing path.
7. When your path is complete, hit 'Cmd-Enter' to turn it into a selection

Removing a subject from the background tends to leave a fringe - color residue from the background
due to anti-aliasing. Here's how to remove it:

1. Layer -> Matting -> Defringe works by pushing the colors of a pixels outwards but tends to be a
   bit clumsy and leaves unwanted blocks.
2. Layer -> Matting -> Remove White Matte tends to remove an unnatural dark edge on your selection.
3. Load your subject as a selection, inverse it to select the background with 'Cmd-Shift-I' and
   expand that selection by 1px to remove the fringe pixels all together.

Locking transparency lets you paint on a layer without affecting the already transparent pixels. You
can do this on the Layers panel by clicking the checkerboard icon or hitting '/' with your Layer
selected.

'Cmd-click' on a layer's thumbnail to load it as a selection. 'Shift-Cmd-click' on another layer's
thumbnail to add it to the existing selection. 'Opt-Cmd-click' to remove a layer from the existing
selection. Use 'Cmd-H' to toggle your selection to view the underlying image.

The Replace Color dialog lets you replace auto-magically replace colors in an image (Hue,
Saturation, or Brightness):

1. Choose Image -> Adjust -> Replace Color
2. The preview shows selected areas in white and non-effected areas in black
3. Use the eyedroppers to add or subtract areas on your image. Adjust the sliders to get a wider or
   more restrictive area. You can also Shift-Click or Opt-Click to add/subtract areas.

An alternative to this is using the Color Replacement Brush which lets you selectively paint on new
color (Hue, Saturation, or Brightness).

You can also select by color:

1. Select -> Color Range
2. Add/subtract areas just like how you would with the Replace Color tool
3. You can swap out large selection areas by using the Paste Inside Selected Area action, hit
   'Shift-Opt-Cmd-V'.

# Transformation and Distortion

You'll get the greatest flexibility and power with Free Transform mode:

1. Hit 'Cmd-T' to enter Free Transform
2. Drag a corner to scale the image, the opposite corner will be pinned. 'Opt-Drag' to scale in all
   directions.
3. 'Shift-Drag' to constrain the proportion
4. Position the cursor outside the bounding box and drag to rotate
5. 'Cmd-Drag' to shear the image, hold Shift while dragging to constrain to horizontal or vertical
   shearing. Dragging a corner will be a free-form shearing
6. 'Cmd-Opt-Shift-Drag' to create a perspective effect
7. 'Cmd-Shift-T' to repeat the last transformation
8. 'Cmd-Alt-Shift-T' to repeat the last transformation as a duplicate
9. At anytime you can grab the center marker and move it to manipulate future transformations

Image Warp is a special mode of Free Transform. Enter it by going into Free Transform and clicking
the Warp icon in the options bar:

1. Each corner point has two Bezier handles, drag them to create curves
2. There are control points on each side of your bounding box. Drag these to distort your image.
3. There are even more control points inside your bounding box, totaling 24.
4. You can use the control points to create a page curl effect. Add a shadow for the best effect.
5. In the options bar, you'll find a drop down with preset warps. These are handy to get you down
   the right path before you customize. Select the one you want then select Custom again to improve
   it.

Photoshop's Clone tool (aka Rubber Stamp tool) can be used to clonse portions of images:

1. Open the Clone Source panel and click Show Overlay, make sure the Clone tool is set to Sample All
   Layers in the options bar
2. Opt-Click to set the source of the clone
3. Click to mark the point where cloning begins. Undo it quickly and in the panel set the correct
   scale, angle, and offset
4. Choose a brush and start painting the cloned target

Puppet Warp uses a grid system that lets you bend, warp, and manipulate images:

1. Choose Edit -> Puppet Warp or hit 'Cmd-Opt-P'
2. Click with the Puppet Warp tool to set pins as yellow dots
3. Toggle grid visibility in the Option bar's Show Mesh box
4. Hold Option for a ring to appear around it which lets you rotate
5. Set Pin Depth for z-index of your pins
6. Hold Shift to select multiple pins and edit
7. There's also Rigid and Distort mode

Content Aware Scaling lets you resize images without distorting key elements in the image:

1. Edit -> Content Aware Scale or 'Cmd-Shift-Opt-C'
2. To protect areas, make a selection and choose Select -> Save Selection. Later when you do the
   actual scale, click the Protect pop-up in the Options bar and choose your selection.

Content Aware Fill uses information in the image to make an automatic patch:

1. Make a selection around the object to remove - the selection doesn't need to be accurate
2. Press Shift-Backspace to bring up the Fill dialog and choose Content-Aware
3. Perfect the fill with the Clone tool and Healing tool
4. You can also do Content Aware Filling from the Healing Brush. Hit 'J', brush, and choose
   Content-Aware in the options bar.

# Hiding and Showing

Clipping Masks lets you constrain the visibility of one layer with the layer below it. It won't
cover any transparent pixels. You can even do more interesting things using blend modes:

1. With a texture layer above your background, create a Clipping Mask by hitting 'Opt-Cmd-G'
2. Experiment with the blend mode of your Clipping Mask
3. Overlay lets you keep the texture while retaining the brightness/darkness values of the layer
   below. See "Photoshop Missing Manual" for an explanation on all blend modes.

Any painting tool can be used in conjunction with Layer Masks. Caplin shows us how to use the Smudge
tool to make blades of grass appear above a layer:

1. Load your subject as a selection and inverse it with 'Cmd-Shift-I'
2. Use the Smudge tool to gradually streak up some grass

Smoothing is necessary for cutouts because they look too crisp against their backgrounds:

1. Load your selection and choose Layer -> Layer Mask -> Reveal Selection
2. Open the Masks panel and increase the Feather radius
3. You can add a soft shadow with the same technique. Opt-drag to duplicate the selected layer,
   offset it, and turn it black with an adjustment.
4. Lower the opacity of your shadow

Photoshop recently added a color based masking feature:

1. Create a Layer Mask, open the Masks panel, and click the Color Range button
2. Click on colors in your layer and Invert if necessary
3. As usual, Shift-click to add and Opt-click to remove
4. Press the Mask Edge button to refine your mask

Blending is powerful in Photoshop. It lets you show/hide portions of your layers without any
brushing or selecting:

1. Double click a layer's name and choose Layer -> Layer Style -> Blending Options.
2. The bottom "Blend If" section lets you blend pixels which are in a certain color range
3. Hold down "Option" and drag to create multiple triangles on the "Blend If" configuration
4. You can use these blending options on both the top and bottom layers

# Image Adjustment

The Shadows/Highlights dialog is useful as a quick way to fix dark areas in your image:

1. Choose Image -> Adjustments -> Shadows/Highlights
2. Increase the amount setting in shadows to produce better details without affecting bright areas
3. Raise the Tonal Width setting slightly for dramatic effect. Tonal Width affects the radius to
   which your changes are made
4. If your image is too bright, lower the amount setting in shadows

Curves lets you make granular and coarse changes to color, shadows/highlights, and more with the
same dialog:

1. Choose Image -> Adjustments -> Curves or hit 'Cmd-M'. You'll see a single diagonal line
   indicating no changes have been made.
2. Click and drag upwards at the center to create a curve and raise brightness
3. Click and drag downwards for a darker image
4. Click and drag the top right point and drag it downwards to limit the brightest parts of the
   image and reduce contrast
5. You can do the same with either ends in either direction
6. Choose any color in the RGB menu to affect only that channel
7. Click once on the line to pin that point
8. The trick is you'll need to think in inverse sometimes. If you need more yellow, remove blue (you
   only have access to RGB)

An often overlooked feature is using selective colors in the Hue/Saturation adjustment dialog:

1. Choose Image -> Adjustments -> Hue/Saturation or hit 'Cmd-U'
2. Click on the "scrubber" icon at the bottom of the dialog. Adjust the triangles on the color
   sliders to only affect the colors you want
3. Cmd-drag to change the Hue without adjusting Saturation

Caplin shows us how to use multiple adjustment tools to go from a dull image to a great one with
high contrast without affecting colors:

1. Duplicate the layer and desaturate using 'Cmd-Shift-U'. The grayscale layer will show us just how
   dull an image is
2. Change the blend mode of the grayscale layer to Soft Light
3. Duplicate the layer again and sharpen the new layer (Unsharp mask, 300% at 3px radius). Use a
   layer mask to only show focus in specific areas.
4. You might want to try Hard Light instead of Soft Light which has higher contrast. Try both and
   see which works for you.

Sharpening brings back definition for soft or out-of-focus images. Caplin recommends we use the
Unsharp Mask filter for more control:

1. Start by choosing Filter -> Sharpen -> Unsharp Mask...
2. Opt-click the Cancel button to revert changes
3. Start with Amount 100%, increase up until 300% for a dull image
4. Start with a Radius of 1.0px and increase as necessary
5. Increase the threshold if you need to as the last step

Caplin walks us through using the Unsharp Mask filter on a face. With the 300% amount and 2.0px
radius, the filter is too strong affecting the skin and showing us freckles. The Threshold feature
comes into play, by raising it to 30 it will ignore the low-contrast skin and only affect the
eyes/mouth.

The Healing Brush is useful to quickly fix blemishes. It uses the area just outside of the brush and
replaces the area inside of it:

1. Select it with 'J' or 'Shift-J'
2. Opt-Click an area to get the source point
3. Paint over any blemishes to replace it
4. Use a selection to tell the healing brush what area to blend

# Composing the Scene

Caplin gives us some quick tips on positioning layers to compose a scene. In this case it's a
climber, mountain, and sky:

* Putting the climber in the middle doesn't tell a story
* Putting him at the top shows us how much he has accomplished
* At the top with less mountain and more sky amplifies this effect
* At the bottom, it shows us how much work he has in front of him
* At the bottom with more mountain amplifies the effect

Now he's using an example of a farmer and background with a fence and highway junction:

* Just placing the farmer above the background makes him look like he doesn't belong there
* Place him behind the fence and cut a portion of his pitchfork to show in front of the fence makes
  it look better
* Add shadows for the farmer and masks so blades of grass appear in front of his feet
* Finally use a Gaussian blur to blur the background to keep focus on the farmer himself

The background of an image is important. In the Last Supper, Da Vinci makes sure to keep Jesus in
the middle. The ceiling and doorway of the backgrounds are all composed to keep focus in the middle.
Caplin places a poster at a busy street intersection:

1. Placing the poster dead center is a giveaway that the photo is fake
2. Add a little tilted perspective for more realism
3. Remove any objects in the background which try to take focus away
4. Brighten the background if necessary or make it darker
5. Make the background recede further with a Gaussian Blur. Remember, hot colors do well in the
   foreground while cooler colors are best for backgrounds
6. Cartoonists like to add people to look at signs. Add a person to your photo and position him to
   look at your sign
7. Overlap the person with the sign for more realism (but just a little bit)

# Getting into Perspective

The horizon is always the same height as the eye-line of the viewer. If there are multiple adults in
your photomontage, their eye-lines should be leveled with the horizon and each other (unless
deliberately skewed).

Caplin shows us an outdoor image with many horizontal lines. The background gets smaller and smaller
because of our perspective. The point at which the lines meet is the Vanishing Point. You can draw
lines on those horizontal points. When you paste subjects into your image, make sure their eye-lines
are level (so it looks like one subject is further back than another).

Keep in mind that the Vanishing Point may be off the image. You can still use the line tool to find
it and then any additions should line up.

Use any available horizontal lines on an image to create your own perspective lines. It's useful
when adding new layers. Caplin cuts an existing door and transforms it to fit along the perspective
of a bookshelf.

Caplin walks us through duplicating a box and stacking it. The original box is below the horizon
level - we can see the top. When we stack a copy above it, the copy's top shouldn't be visible.

1. First make a copy of the box
2. Use the lasso tool to split each side of the box (top, front, and right)
3. Select the front and use Free Transform to shear it and drag it straight down to align with the
   bottom box
4. Repeat this process with the right side
5. Shear the lid and move it down, make sure it's behind the other two layers

The Vanishing Point filter lets you perform selections and other operations at a pre-determined
perspective:

1. Enter the Vanishing Point filter with 'Cmd-Opt-V'
2. Hold 'X' to zoom in, set 4 points which determine your perspective
3. A grid should show up, make sure it's aligned perfectly
4. Now use the Marquee tool to make a selection which should show at an angle now
5. Switch back to the Arrow tool and Cmd-drag the center handle to create another dimension, adjust
   it to match your picture
6. You can move items from one dimension to the next and the moved copy will adjust itself
   accordingly
7. You can also paste new items into the Vanishing Point filter automagically

# Light and Shade

Basic shadows on the wall and ground are easy to create. In this example, Caplin has a layer of a
boy in front of a wall/ground background:

1. Duplicate the boy layer, press 'D' to set chips black/white, then press 'Opt-Shift-Backspace' to
   fill the new layer black
2. Move the new layer below the actual boy layer and position it accordingly
3. Lower the opacity of the shadow layer (50% is a good start) and use the Gaussian blur filter to
   soften it (3px is a good start)
4. To move the shadow to the floor use Free Transform and position it
5. To make a shadow fade into the distance, use a layer mask with a gradient
6. Combine both techniques to make a shadow run on the ground and wall for more realism. Just make
   both shadows and combine them with masks

Ground shadows are sometimes trickier:

1. Select a portion of the bottom piece of your subject, 'Cmd-J' to make a new layer from it
2. Fill the new layer with black and edit if necessary
3. Reduce the opacity, use a Gaussian blur to soften it, and move it into place
4. Sometimes, you'll need to draw your shadow by hand. Use a soft-edged brush with low opacity
   (around 40%) and start brushing where the shadow is darkest
5. Using a larger brush, start drawing in short brush-strokes the rest

Caplin shows us how to create complex shadows using a pair of glasses as an example:

1. Check the light direction of your subject, are some areas darker than others?
2. Start with the lens selected, create a new layer and fill it with black. Hit 'Cmd-Shift-F' for
   the fade dialog and set it to around 50% opacity.
3. Inverse the lens selection to select the frames. Hold 'Cmd-Opt-Shift' and click on the layer's
   thumbnail to get an intersection
4. Split the shadow layers into three sections: front, left arm, right arm
5. Use the Free Transform to distort the front shadow and place it
6. Do the same with the two arms, but make sure you scale and rotate it as necessary so it looks
   correct coming from the light source

An indoor room can be more interesting when a light source is added - especially if it's coming from
a nine-grid window:

1. On a new layer, make a grid of white rectangles
2. Use the Free Transform to scale and distort to an angle
3. Select the pixels in this layer by Cmd-clicking the layer's thumbnail.
4. Inverse the selection and feather it by 8 pixels, make a new layer, and fill it with black. Lower
   its opacity to 50% and hide the white rectangles.
5. Use the Smudge tool or Liquify filter to adjust shadows around objects
6. Load up the light sources (those white rectangles) as selections and use the Curves tool to add
   some red to imitate light

Adding shadow adds depth to the image. In this case, we'll take a single card, duplicate it, and
create a deck of cards:

1. Load the selection, hit 'Opt-Up' to nudge it up a few pixels, inverse the selection and darken
   the edge a bit to give it some depth
2. Select the card pixels again, hit 'Opt-Cmd-D' to feather the selection, move it down a few pixels
   and fill it with black - opacity to 50% for a shadow
3. Select all, make a duplicate and move it down a few pixels for a 2nd card
4. Keep the Opt key down and continually make duplicates for a stack of cards, make sure to
   randomize their positions so it's not entirely straight
5. Tighten up the shadows in QuickMask mode with the Levels dialog. Drag the white arrow to the
   right of the slider, exit QuickMask and invert selection. Now hit Delete.

Now let's add a light source to a lamp:

1. Start by adding a shadow to the screen using a large soft-edged brush at a low opacity
2. Use the pen tool to create a rough outline of light
3. In QuickMask, use the Lasso tool to trace around the edges of the light area. Then use Gaussian
   Blur to soften the edge.
4. Exit QuickMask, on a new layer pick a pale yellow color and use the gradient tool to set
   Foreground to Transparent. The area closest to the light source should be the Foreground.
5. Use a soft-edged brush to paint an extra glow directly at the light source
6. Select an ellipse on any surface the light source is shining on and delete any shadows there so
   it will remain lit

The Dodge/Burn tools are useful to add light and shade to highlights, midtones, and shadows:

* The Burn tool darkens an image when set to Highlights
* The Dodge tool brightens an image when set to Highlights
* When set to Midtones, the Burn tool no longer loses color but still darkens
* The same holds true for Midtones Dodge - except it brightens
* When set to Shadows, both tools have an unfortunate side effect on skin tone
* The best effect is to use Midtones tools at a low opacity, then use the Dodge/Burn tools at an
  even lower opacity on Highlights

Curves Adjustments can be used to reverse shadows:

1. Make a new Curves Adjustments Layer, raise the midtone of the curve until your shadow area is as
   light as it should be. Don't worry about affecting the good highlights.
2. Every Adjustment Layer comes with a built-in mask. Use it to cover the good portions of the image
   you don't want to change.
3. If you want to adjust the masked region, just load the mask itself as a selection and add another
   Adjustment Layer.

Painting smoke:

1. On a new layer, use a soft-edged white brush with low opacity. Use many small strokes to build up
   smoke.
2. Lock the transparency of the layer, hit 'D' to reset your chips, choose Filter -> Render ->
   Clouds to add texture to your white smoke.
3. Change the smoke layer's blend mode to Multiply for a dirty look
4. Change to "Screen" for a bright smoke effect

Making fire:

1. Paint a random shape with a soft-edged white with slight variation in density
2. Use the Smudge tool to have white streaks coming from the middle
3. Lock transparency with '/' and choose Filter -> Render -> Clouds with orange and yellow chips
4. Now apply the same Clouds filter with black/white chips
5. Hit 'Shift-Cmd-F' and fade this new black/white layer and choose Linear Light

Create neon lights:

1. Create a new type layer and use a font with little thick/thin variation
2. Use Refine Edge dialog to round off corners
3. Select pixels and choose Edit -> Stroke to add a stroke
4. Now hide the original text, erase portions of the stroke for stencil effect
5. Create an inner glow by contracting your selection by a few pixels, using a Gaussian Blur, and
   filling in the selected area with white
6. Add your background, use the Burn tool (set to Midtones) on the corner areas for a tube effect
7. Create a new layer with the same selection, move it below, feather it and set the foreground
   color to the same as your neon lights for a glow effect

Turn day into night:

1. Remove the existing sky, the Background Erase tool is useful for this
2. Use a clipping mask and Curves Adjustment to lower brightness of foreground
3. Paste a night sky into your image
4. Use masks and Curves Adjustments to add yellow to windows for light sources
5. Brighten bottoms of buildings to give the street some glow

# Heads and Bodies

Making the head fit another body:

1. Cut the head off, the tricky part is the hair which the Magic Erase tool is useful for
2. Paste the new head on the image, use Free Transform to scale as necessary
3. Make a new Layer Mask and with a soft-edge brush blend the neck/head together
4. If necessary, use Curves to make sure skintone matches

The Puppet Warp tool can be used to adjust a body. In this case, Caplin shows us how to edit a
teenager to stand up straight:

1. Enter Puppet Warp mode with 'Cmd-Opt-P'
2. Click to place markers at key joints: shoulders, hands, midriff
3. Place a pin on the neck and pull it upwards, pull the shoulders down a bit
4. Every Puppet Warp will be a bit different

In the next example, Caplin removes Matt Damon from ahoto with Brad Pitt and George Clooney:

1. First make a selection of Clooney and move him to the left
2. Enter Free Transform mode and scale him as necessary so his eyeline matches
3. If his bottom edge doesn't reach the bottom edge of the photo, select a portion of his lower body
   and enter Free Transform. Scale it downwards.
4. Crop the image
5. Clooney's edge may still look too hard/crisp. You can make a selection and contract it by 1px to
   fix this or feather it.

Cutting out hair is tricky - but it's gotten easier with the Background Eraser:

1. It's often easier to make a new background layer with a solid color that complements the hair
   color. Then cut out the image loosely leaving plenty of margin for the hair.
2. Access the Background Erase tool and set it to Discontiguous mode. Set the sampling to Once since
   the background is a solid color.
3. Start erasing around the head. The crosshair picks up the sample color to erase and everything in
   the radius of the circle matching is erased.
4. Protect Foreground is useful in case you erase something by mistake. Just 'Opt-Click' the
   foreground color before erasing.
5. If necessary, use the Burn tool set to Highlights to remove any white fringe leftover on the
   hair.
6. For even more realism, lock the transparent pixels and use the Clone tool.

Cutting hair with Refine Edge:

1. Start with the Quick Selection tool and make a selection
2. Enter the Refine Edge dialog with 'Cmd-Opt-R'
3. Adjust the Radius to improve your selection. Toggle view with 'J'
4. The Decontaminate Colors checkbox blends colors of cutout with border
5. Deal with any loose strands of hair with the Edge Detection brush
6. Hold Option while brushing to remove any unwanted soft edges

Caplin walks us through ageing a person:

1. Start with the Liquify filter. Sag the jaw line, thicken the nose, and make the eyes more doleful
2. Make a new layer and set the mode to Color. Use a soft-edge brush either black or white
3. Make another layer and set to Hard Light mode. Sample colors from darker areas of the skin and
   brush with a low opacity under eyes, around cheeks, and around the mouth for shadows.
4. Remove some healthy glow of the skin with a Hue/Saturation Adjustment layer. Lower the saturation
   and mask any areas you want to keep.

Now let's reverse the ageing process:

1. Start with a Median filter (under Noise) to smooth out wrinkles. Use a mask to prevent smoothing
   on all areas.
2. Use the Healing brush to further smooth out wrinkles
3. Find a light color skin tone and set a brush to it in Color mode. Now paint over any shadows and
   redness of cheeks
4. Select the hair with a QuickMask and do a Curves adjustment to make it darker
5. Use the Liquify filter to tighten the chin and cheeks

The Liquify filter is a powerful tool for changing expressions. When you use it, be sure to make
change subtle. You can also use it to turn heads.

# Shiny Surfaces

Let's use the Plastic Warp filter to create spilled syrup out of a jar:

1. On a new layer, paint the spill in mid gray with a hard-edged brush
2. Use Dodge/Burn tools to add random shading
3. Choose Filters -> Artistic -> Plastic Warp and adjust sliders
4. Keep undoing and repeating until you get the Dodge/Burn correct
5. Changing the mode from Normal to Hard Light will make the liquid clear
6. Use a Hue/Saturation Adjustment layer to adjust the color
7. Apply a Wave Filter with a mask to get a refraction effect

Caplin walks us through making bubbles:

1. Draw a circle on a new layer in a mid-tone gray. Use the Dodge/Burn tools, the Plastic Warp
   filter, and maybe even a reflection of a window.
2. Change the layer mode to Hard Light, duplicate and scale as necessary for multiple bubbles. Merge
   each bubble with its background..
3. Apply the Spherize filter at 100%
4. Add some color with the Hue/Saturation Adjustment

Adding a water moat and dealing with reflection:

1. Draw the shape of the water on a new layer, use the Lasso at first then a hard brush to wave the
   edges
2. Duplicate the background, flip it vertically, shear as necessary
3. Make sure reflections line up with the same vanishing point
4. Lower the opacity of the reflections, around 80% works well
5. Merge the reflection and water and apply the Wave filter
6. Make elliptical selections and apply the ZigZag filter for ripples
7. Use a soft brush in Dissolve mode and paint green in low opacity for algae
8. Use a Gaussian blur to soften the algae
9. Reduce the opacity, add a new layer with green/blue paint and set the blend mode to Hard Light
   for additional color

Drawing snow and icicles:

1. Draw snow shape with a hard brush where snow sits on the ground or windowsill, use a soft brush
   to paint it alongside walls and sides
2. Add shading using Dodge/Burn tools then add texture. Start with Gaussian Noise filter, lock the
   transparency, then use a Gaussian blur to soften.
3. Use Color Balance to add a slight touch of blue
4. Paint icicles with a midtone gray and hard brush, shade with Dodge/Burn and apply the Plastic
   Warp filter. Change to Hard Light mode, duplicate and overlay it with itself for shadows.

Make it rain in the street:

1. Select the buildings, make a copy and flip it vertically. Shear it as necessary to make a
   convincing reflection.
2. Lower the transparency and add a layer mask to make puddles in the street.
3. Use the Ocean Ripple filter for the puddles, then make elliptical selection with the ZigZag
   filter for ripples.
4. Make a new layer, fill it with mid gray and set it to Hard Light. Use Gaussian Noise for texture.
   Add a Motion Blur to make it look like rain.
5. Run the Clouds filter on a new layer, set mode to Screen. Use the Curves adjustment to tweak the
   contrast

Adding a block of ice to a glass of water:

1. Draw a rough outline with a hard mid-tone gray brush and fill it
2. Use the Dodge/Burn tools for some light and shades
3. Apply the Plastic Wrap filter
4. Select the cube and contract the selection to remove the unwanted edge
5. Change the layer to hard light to make it shiny and transparent

Imitating glass refraction:

1. Load up the clear area, hide it, and select the background that will show
2. Use the Spherize filter to refract it
3. Show the glass layer again, use a soft edge brush with a layer mask to make it partially
   transparent
4. Duplicate the glass layer, delete the layer mask, choose Layer -> Layer Style -> Blending Options
   and adjust the blend if color
5. As a final touch, use a Color Balance adjustment for a blue/green tint

# Metal, Wood, and Stone

Create a metallic effect using the curve dialog:

1. Open Curves with 'Cmd-M', drag vertically upwards on the left hand side to make a steep curve
2. Further along, drag downwards. Further along more, drag upwards.
3. Continue this pattern of an oscillating graph that slowly trends upwards. Your image will begin
   looking metallic.

Using adjustment layers gives you more control:

1. Add a Curves Adjustment Layer
2. Change the blend mode to Luminosity to only effect brightness/contrast
3. Lock the transparently with '/' and apply a small Gaussian Blur to fix any pixellation
4. Paint out the mask areas that you don't want
5. Use the Dodge/Burn tool to do any touch ups

Use layer styles to make metallic text:

1. Open up the Layer Style dialog and add Inner Bevel. Optionally add a drop shadow for a 3d effect.
2. In the shading section, click Gloss Contour and change it to a bumpy map
3. Click Contour and select a curve upward shape to add reflection
4. Click Satin and add a bowl like contour for sheen. Adjust sliders
5. Use the Gradient style to turn it into gold (or copper)

The Light Effects filter is useful to add light/shade to a layer. It's especially handy with alpha
channels to simulate 3d images:

1. First make a new Alpha channel in the Channels panel. Add a faint Clouds filter to your
   background.
2. Add a slight blur to your channel. Then go back to the RGB channel and create a new layer over
   your background. Fill it with white.
3. Open the Lighting Effects filter and specify your Alpha channel. Uncheck White is High and adjust
   the slider.
4. Apply the curves technique for metallic look.

Adding rust, grime and decay:

1. Blur the artwork after it's been made to a new channel
2. Apply the lighting effects and curves from previous steps
3. Use the Hue/Saturation adjustment layer to fix color
4. Return to the Alpha channel and add some noise to it
5. Apply the Hue/Saturation adjustment again on the new layer, but use a brown color for rust
6. Now just make a mask to let the rust show through

Turning objects into wood:

1. Add a wood texture on top of your image using a clipping mask
2. Group them together with 'Cmd-G'
3. Change the blend mode to Multiply. If it's too dark use Overlay.

# Paper and Fabric

Adding dimension to money:

1. Start with a flat dollar bill
2. Use Free Transform 'Cmd-T' and press the Image Warp with the Flag preset
3. The preset is too strong, modify it to be less noticeable
4. Change the preset to Custom. Grab the corners and handles to give it a more natural distortion
5. Add shading with the Burn tool set to Highlights. Add shading to the valleys
6. Use the Free Transform to move the bill to any perspective
7. Duplicate to add a pile of bills

Add a cover to a book:

1. Take a photograph of your book with the cover inside out
2. Paste your new cover as a Smart Object and use Free Transform to place it directly onto the cover
3. Make a duplicate, set it to Hard Light mode, and Desaturate with 'Cmd-Shift- U'. Use Curves to
   add some brightness

Folding and crumpling paper:

1. Use the Image Warp or Shear filter with the anchor at the midpoint
2. Leave the top half selected, use the Burn tool with a large soft brush to add gentle shading
   above the crease line. Add shading to the top to make the paper look as if it's bending away.
3. Do the same with the bottom half
4. Use the Wave filter for the crumple effect. Number of Generators determines number of waves.
   Adjust other sliders as necessary.
5. Use Lasso tool and make irregular vertical selections. Use a large soft Burn brush to add shading
   on your selections to make crumples
6. Do the same, but with horizontal selections

Adding folds and wrinkles to fabric:

1. Curve the banner slightly with the Shear filter or Image Warp
2. Add texture with Texturize filter with Canvas setting. Use the Fade command to reduce texture
   'Cmd-Shift-F'
3. Use the Burn tool to create a fold. A medium, soft brush at 20-40% opacity is enough
4. Hold 'Option' to get the Dodge tool and draw it right above your shading in a parallel manner
5. Repeat to make multiple folds/wrinkles

Ripping and tearing paper:

1. Create tears by making ragged selections with the Lasso tool and a mask
2. Make a new layer and paint the tears with a small hard brush. Just trace it to simulate a paper
   tear
3. Fold a corner down, fill it with a neutral color and use the dodge/burn tools for shading. Use
   the Plastic Warp filter to make a glue effect
4. Add folds/creases with the dodge/burn tools like the previous tutorial

Simulate an old photo with texture:

1. Get a photo of the inside cover of an old paperback
2. Set your image to Hard Light mode with the texture layer below it
3. Duplicate the texture layer and set it above in Hard Light mode also
4. Desaturate your image and add folds/wrinkles
5. Select the image and contrast selection a bit to create a border

Red curtains with custom fibers:

1. Start with a black outline, run the Fibers filter. You can do the same to make a wood effect.
2. You can apply the same effect to a sign for some texture. If it's too strong, use the Fade dialog

Make a ribbon:

1. Draw a path with the Pen tool. Keep curves smooth and avoid tight curves.
2. Select the original, hold Option and drag to make a duplicate. Join the two paths into one to
   make the outline of your ribbon.
3. Fill it with a color and use Dodge/Burn tools for shading and highlights.
4. Make the selection again and nudge it down. Hollows should be selected and ready for more shade.
5. Use the Hue/Saturation adjustment to add color

Making tape:

1. Select a rough outline with the Lasso tool using Shift for straight lines
2. Fill the selected area with 50% transparency gray
3. Add random shading with Dodge/Burn
4. Apply the Plastic Wrap filter and change it to Hard Light mode
5. Color can be added with Color Balance

# The Third Dimension

Adding depth to a flat image of a coin:

1. Use Free Transform to lay it on its back
2. Select it and 'Opt-drag' it up, continually making duplicates
3. Select the edge, hit '/' to lock transparency, and fill it with a color
4. Use the Dodge/Burn tools to add some depth and lower its opacity

Caplin walks us through placing a sign on a jagged edged garage door viewed at an angle:

1. Select all your sign elements and Convert to Smart Object
2. Use Free Transform to match the perspective and place it onto the garage door
3. Change the blend mode to Multiply

Building a cereal box:

1. First prepare your flat artwork
2. Create a merged copy and distort the front of the box with Free Transform
3. Repeat with the side layer and place them together
4. Darken the side of the box and add shading with the Burn tool
5. Select a few pixels and brighten it to form an edge between sides

Displacement maps lets you move a layer and have it take the shape of its new surface:

1. Place your layer above the background
2. Set the layer's mode to Hard Light and reduce opacity
3. Duplicate your background and desaturate with 'Cmd-Shift-U'
4. Select the foreground and run the Displace filter
5. Try combining it with a Gaussian Blur to smooth out realism

Drawing a 3d cable:

1. Start with drawing a curve with the Pen tool and add a stroke to it
2. Select the curve and feather it
3. Nudge it vertically and inverse selection to get the bottom edge. Use Brightness and Contrast to
   darken it
4. Now do the same, except brighten the top half
5. Add shadow if necessary

Drawing a 3d pipe:

1. Start with a midtone gray rectangle
2. Use Dodge/Burn tools for highlights/shades and the Shift modifier
3. Make an elliptical selection and duplicate to create the pipe ends
4. Fill one end with a solid color gray and brighten it
5. Draw a new selection for the inside of the end and darken it to create the inner pipe effect
6. Make the pipe look more metallic with the steps from the Metal chapter

# Advanced Techniques

Caplin reminds us how to get rid of the white fringe around a selection again. After your selection
is made, contract it by 1 pixel before doing anything else.

Working with Smart Objects:

1. Start with two layers: a background, photo and some texture. The texture overlay is set to Hard
   Light mode.
2. Convert all layers into a Smart Object with Layer -> Smart Objects -> Convert to Smart Object.
   This groups them into a single layer.
3. Any Free Transforms, Image Warps, or Filters will be applied to all 3 layers
4. Applied filters will be Smart Filters. They're non-destructive and on their own layers.

Use Layer Groups and Layer Comps to add organization to your layers. Comps let you create different
versions of your document.

The Filter Gallery gives a quick preview of special effects. You can preview multiple stacked
filters.

Caplin walks us through mix and matching skies. Get the sky you want and paste it into the original
image. Use a Layer Mask for foreground elements.

Use Masks and the Curves adjustments to quickly make multiple adjustments at once with your image.

The Background Erase tool is useful to sample a point as a background and remove it from your image.
Here are some tips:

* Before starting, double click the Background layer and turn it into a regular layer. Open the
  History panel and click next to the Make Layer step to pin that point in history.
* Caplin recommends we set the tool to Sample Once so we don't accidentally sample foreground
  colors. Set the mode to Discontiguous so it will erase inside bounded areas.
* Add a new background with a strong color to check that it's fully erased. The checkered
  transparent background sometimes hides missed spots.
* Once you place your wanted background, you may notice you erased some foreground accidentally.
  Switch to the History Brush 'Y' and paint those areas with a hard edge brush to bring them back.
* Remove any fringes by painting them over with locked transparency.

Actions can be used to create keyboard shortcuts for frequent actions. Caplin walks us through
creating one:

1. Make a selection
2. Select New Action in the Actions panel. Give it a name, keyboard shortcut, then hit the Record
   button
3. Now we'll start our action, which is to contract the selection by 1px, inverse the selection, and
   delete the background.
4. Press the Stop button in the Actions panel. Your new Action can be replayed at anytime.

CS5 had some useful shortcut introductions. Dragging left/right while holding 'Ctrl-Option' with the
brush tool will resize it. Dragging it up/down will change its hardness.

The eye dropper has a sample ring now which shows the current color on top and the previous color on
bottom. Hold 'Ctrl-Opt-Cmd' with the Color Picker to get a color sampler.

# Working for Print and the Web

Resolution is the number of dots an image uses. Image resolution is usually measured by dots per
inch or dpi. For paper a higher dpi means better quality. Screens have a cap to dpi, computer
screens typically use 72dpi.

Caplin recommends these values for different media:

* 300dpi for high quality magazines
* 200dpi for newspapers or coarse paper
* 72dpi for publishing on the internet (not for print)

Most of the time you'll work in RGB mode, even if your end result is CMYK. CMYK is the color mode
for printed media. It stands for Cyan, Magenta, Yellow, and Black. It's a subtractive system where
colors are formed by reflecting light. Caplin recommends always working in RGB and even sending your
files off as RGB mode to printers. Printing services go through great lengths to make sure their RGB
to CMYK conversion works well.

Save for Web removes unnecessary elements like paths to reduce file size. You can compare images
side by side to see if the size/quality trade off is worth it. JPEGs settings range up to 12 being
the highest quality. The Save for Web dialog uses a x10 scale.

Photoshop lets you make animated GIFs using the Animation panel. Create multiple layers and add them
as frames.