# 100% Photoshop

Steve Caplin walks us through creating full scenes using only Photoshop and no photographs. Along
the way, he teaches us very cool tips and tricks.

# Essential Techniques

The book starts with a review of all the essential tools used in everyday Photoshop work. Here's a
quick summary, for a more complete intro, see notes on "Photoshop Missing Manual" or "How to Cheat
with Photoshop".

The **Move tool** is used to moving layers and selections around. The shortcut to activate it while
any other tool is currently active is holding 'Cmd'. The Auto-Select option lets you automatically
select a layer when you click on it, or just hold 'Cmd' and click with the Move tool. There are
Alignment and Distribute controls in the option bar to automatically layout layers.

The **Rectangular Marquee** and **Elliptical Marquee** are used to make selections of different
shapes. Opt-drag to expand from the center instead of from a corner. Shift-drag for equal proportion
square/circle. Hold 'Opt' to subtract from an existing selection. Hold 'Opt-Shift' to intersect.
Hold 'Spacebar' to move your selection while you're drawing it. Use Select -> Modify -> Feather to
feather out the edges.

The **Brush tool** handles painting. Use the Brush panel to set the diameter and hardness - or use
'[', ']', 'Shift-[', and 'Shift-]'.

**QuickMask** mode is used to make selections by painting. Enter QuickMask with 'Q' and exit by
pressing 'Q' again. Paint with a soft edged brush to make a feathered selection. Hit 'X' to quickly
toggle between black/white chips.

The Layers panel includes many **Locks** which can be used so you won't accidentally paint over
transparent pixels, move a layer, or resize one. Cmd- Click a layer's thumbnail to load it as a
selection. Cmd-Shift-Click to add it to an existing selection. Cmd-Opt-Click and Cmd-Opt-Shift-Click
works as expected.

**Layer Masks** are used for non-destructive editing. They mask areas of the layer and hide them.
Choose Layer -> Layer Mask -> Reveal All to add one. Now paint with black to hide and white to show
through. Gray for transparency. You can disable a mask temporarily by Shift-Clicking on its
thumbnail.

**Adjustment Layers** let you non-destructively adjust a layer's contrast, brightness, hue, and
more. All Adjustment Layers come with a mask.

**Clipping Masks** clip the visibility of the layer above so it's only visible where the two layers
overlap. Choose Layer -> Create Clipping Mask or hit 'Cmd-Opt-G' or hold 'Opt' and click on both
layers.

**Curves Adjustments** is a quick way to adjust a layer's brightness, contrast, and hue. Choose
Image -> Adjustments -> Curves or hit 'Cmd-M'.

**Layer Modes** determine how a layer is visible related to the layer beneath it. Use the Layers
panel to set it. See 'Photoshop Missing Manual' for an in depth description of each mode. Here are
the basics:

* Multiply - darkens with the layer beneath it, darker than both layers
* Screen - brighter than both layers
* Hard Light - retains highlights and shadows and hide mid tones

The **Doge and Burn** tools are used to add shadows and highlights. Caplin walks us through making a
realistic 3d sphere.

The **Cloud Filter** is horrible at making clouds, but it's great at making random textures. Set
your background/foreground chips and run Filter -> Render -> Clouds. Each time you run it, it'll
produce random texture - so feel free to run it multiple times until you get something you like.
Holding 'Opt' while running it will produce a tighter effect.

The **Noise Filter** produces random dots for texture. You can set the amount and distribution. It's
great when combined with the **Gaussian Blur Filter** which is used to soften images. The Gaussian
Blur filter is handy to prevent layers from looking too crisp and unrealistic.

Using our new knowledge of filters, let's create a wood texture:

1. Start with a solid brown layer
2. Choose Filter -> Noise -> Gaussian Noise with Monochromatic Noise
3. Set your chips to the same brown color as the background and white for the foreground. Run Filter
   -> Render -> Clouds then Edit -> Fade -> Clouds to reduce opacity to 25%
4. Run Filter -> Blur -> Motion Blur with a vertical blur of about 12 pixels
5. Use Filter -> Distort -> Wave for a grain effect with these settings: ~514 number of generators,
   10-102 wavelength (experiment), > 181 amplitude, 1% horizontal scale, and 28% vertical scale
6. That's enough for a pine-like texture. For a mahogany effect, use Filter -> Liquify. Use the
   Forward Warp, Twirl, and Bloat tools to make knots/whorls.
7. Strengthen by duplicating, desaturating with 'Cmd-Shift-U', changing to Hard Light, and lowering
   the opacity to ~10%.

Making a brick texture:

1. Start with a single black rectangle as a brick
2. Opt-drag the single brick to make copies, holding Shift to go straight. Make two rows first, then
   copy to make the entire wall
3. Filter -> Distort -> Glass to roughen the edges. Duplicate and hide for later use. Run Filter ->
   Blur -> Gaussian Blur at ~1 pixel radius
4. Filter -> Render -> Clouds and Cmd-Shift-F to fade to around 50%
5. Use Filter -> Noise -> Gaussian Noise for some more roughness
6. Copy and paste the layer into a new Channel. Return to the RGB image, create a new white layer,
   run Filter -> Render -> Lighting Effects and choose the Alpha 1 channel
7. Use Color Balance to add the brick color
8. On the black/white layer after the Glass filter, select the cement area with the Magic Wand tool.
   Run Filter -> Sharpen -> Unsharp Mask with a radius of 300 to sharpen it
9. On the black/white layer again, select some random bricks and return to the normal layer. Add the
   cement to the selection. Inverse, make a new layer above all others, set to Multiply. Fill with
   white. Now add a Drop Shadow

# Setting the Scene

This scene is an office door of a private detective. There's a lot of wood, textured wallpaper, a
wooden door, glass window, and brass doorknob.

We'll start by making a skirting board, wall crowning, and door:

1. Start with the wood texture
2. Make a selection on the top section of the wood
3. Use the Burn tool 'O' and Shift-Drag horizontally to add shading on the bottom of your selection
4. Use the Dodge tool (or hold Opt) and Shift-Drag on the top portion
5. Inverse the selection and repeat adding highlights/shade to the bottom
6. Stretch the wood horizontally and repeat the crowning vertically
7. Rotate and stretch out to cover all sides of the door
8. To make the corners, use the Lasso tool to cut out a 45 degree of each board and combine them
   together
9. Continue duplicating and mixing pieces together to form the panels of the door and complete it

The embossed wallpaper is a repeated Victorian pattern:

1. Draw the initial design with a hard-edged brush
2. Since it's symmetrical, we can make one side and copy/flip with Edit -> Transform -> Flip
   Horizontal
3. Keep duplicating and moving the design to make a grid of patterns. You can define this as a
   pattern or just copy/paste
4. Run Filter -> Stylize -> Emboss. We can add color with a Hue/Saturation adjustment

Now let's stain and age it:

1. Make a new layer set to Hard Light mode and paint a brown stain on top of it. Hard Light has a
   darkening effect for dark colors without overwriting hues
2. To make some tears, make a Layer Mask and paint with a hard-edged black brush
3. Make a new layer as a clipping mask 'Cmd-Opt-G' and paint a brown edge on any corner tears
4. Add another clipping mask layer and paint with a darker brown. Add Gaussian Noise for some
   texture
5. Finally use the Clouds filter for the brown area where there is no wallpaper. Follow it with some
   Gaussian Noise and a Gaussian Blur. Adjust colors for the plaster effect
6. Add some wooden beams behind the wallpaper tear and use a Layer Mask to make them look broken or
   torn apart
7. Paint with a shadow using a low opacity, soft edged brush on the wall behind the wallpaper

Making the 2nd wallpaper texture:

1. Select two brown tones on your color chips and run Filter -> Render -> Clouds. Add some Gaussian
   Noise and Gaussian Blur
2. Make vertical selections and Burn them to make slits. Then use the Pen tool to simulate a larger
   split filled with black
3. Use the Burn tool to add some shading and darken the interior with Dodge

Creating the door's window:

1. Start with a circle filled with blue
2. Make a vertical rectangular shape with the same width through the circle's center. Fill it with
   the same color for a window shape
3. Make thin selections around the window and remove it for its bars
4. Paint a shadow of a person on another layer and merge it
5. Make a new background layer with a flat color, merge this with the window
6. Run Filter -> Blur -> Gaussian Blur to soften
7. We'll need to add the glass texture. Run Filter -> Distort -> Glass and experiment with the
   settings until you get a good rippling effect
8. Use a Hue/Saturation Adjustment layer to turn it into a glass color
9. Make a vertical line with a gradient, duplicate it to make many, then move that layer above the
   window in Multiply mode with opacity ~10%

Making the metallic base for the keyhole:

1. Start with a gray rectangle, use Dodge/Burn tools to make it metallic
2. Select the right/bottom border and add shadows. Select the left/top border and add highlights
3. Select the inner shadow and add a faint 30% white stroke (Edit -> Stroke)
4. The keyhole is a filled black circle and rectangle. Load it as a selection and add an Outer Bevel
   with Layer Styles. Use a lot of depth to create a crisp highlight and shadow

Adding screws:

1. Make a gray circle, use Bevel and Emboss to add shading in a down direction
2. That was the hole, make the screw with a smaller gray circle and use Bevel and Emboss in an up
   direction
3. Duplicate the screw and add them to each corner
4. Make a vertical selection within the screw and delete it for the slots

Making the doorknob and hinge:

1. Make a gray circle on a new layer
2. Use the Burn tool to add shading to the right side, use the Dodge tool to add highlights to the
   left side
3. Add another small highlight on the bottom/right edge for a metallic feel
4. To make the brass effect, raise the Red midtones in curves a bit. Lower the Blue midtones a bit.
   Switch to RGB and lower the midtones more.
5. Copy/paste a thin slice from the doorknob to start the hinge. Make a long vertical section from
   the pastes. Paste a full doorknob at the top and bottom for the hinge stops.

# Deep Space

This scene is composed of a starry background, the sun, the earth, and a UFO.

Making a star brush and the starry night:

1. Select a ~12 pixel hard edged brush and choose Window -> Brushes Panel. Start customizing your
   brush
2. Increase the spacing slider
3. In Shape Dynamics, increase the Size Jitter
4. In Scattering increase the Scatter value and Count Jitter
5. Choose New Brush Preset... from the Brushes Panel to save it
6. Now fill the background and paint with your brush on a new layer

Perfecting the stars by making it smaller and more spread it:

1. To spread them out, use Free Transform and expand the background
2. Load the stars as a selection, Select -> Modify -> Contract, inverse the selection and delete
3. Add a glow with Layer Style dialog, add an Outer Glow
4. From the Layer Style dialog, lower the fill amount to make them dimmer without effecting the
   outer glow
5. To complete the effect, Caplin adds another layer of smaller stars that are closer together

Drawing Mars:

1. Make a circle selection and fill it with red (Opt-Backspace to fill selection with foreground
   color)
2. Set the background chip to black and run Filter -> Render -> Difference Clouds
3. Use Cmd-F to repeat the filter until you get the effect you want
4. Use Filter -> Distort -> Spherize to make it less flat
5. Use the Dodge/Burn tools to highlight the side facing the sun and add shading to the other side
6. Add an Outer Glow from a sampled red value for a ethereal effect

Drawing Earth:

1. Draw the initial shape, a blue circle. Most of it will fall outside the canvas. Hold Opt-Shift to
   draw from the center out and constrain to a perfect circle. Hold Spacebar while drawing to move
   it around
2. Draw green land mass using a hard edged brush
3. With the land mass selected and green/brown on color chips run Cloud filter
4. Feather the selection to soften the edges and brighten the area around the land mass for a glow
5. Use the Burn tool to add some shading away from the light source
6. For an added effect, you can paint some tiny lights in the night areas

Adding clouds to Earth:

1. Make a circle selection then run the Cloud filter and Spherize filter
2. Move the selection over the earth and reduce its opacity
3. Change the blending mode to Screen so it brightens the layer beneath
4. Add a Brightness/Contrast adjustment
5. Add a faint glow around it using the Layer Styles dialog

Drawing the Sun:

1. Start with a circle filled with yellow
2. Have the same yellow on a chip, set white as the background chip, run the Cloud filter again.
   Make sure to lock the transparency
3. To make the sun dazzle, use a large white soft-edged brush with a single dab
4. For the outer glow, duplicate the layer and run the Radial Blur filter with Zoom as the blur
   method. This effect is much softer than what can be done with a brush

Adding rays around the Sun:

1. Make a vertical document and paint some black/gray blobs of varying sizes
2. Paint between the blobs at a lower opacity, make sure there's no space
3. Run Filter -> Stylize -> Wind with the Blast method. Run it twice for each direction
4. Rotate the canvas 90 degrees then use Free Transform to increase the height and decrease the
   width
5. Run Filter -> Distort -> Polar Coordinates with Rectangle to Polar checked. This will warp the
   line into a circle
6. Run the Radial Blur filter with a Zoom effect
7. Tint this layer yellow and move it to surround the Sun layer

Building the Cosmos texture:

1. Paint a few blobs of white on a new layer. We'll stretch it out later
2. Lock the transparency and run the Clouds filter
3. Use Free Transform to stretch and rotate to an angle

Making a spiral Milky Way galaxy texture:

1. Paint with a soft brush on a new layer. Make the center thicker than the ends
2. Run the Clouds filter
3. Make a selection around the center of the layer and run Filter -> Distort -> Twirl to spin it

Making the UFO:

1. Make a circular selection and fill it with gray. Use the Dodge/Burn tools to add some texture
2. Duplicate the original, free transform a smaller circle right in the middle
3. Make two smaller circles which will be on opposite ends of your larger circle. Then duplicate and
   use Free Transform to rotate it 15 degrees until you have a group of circles on top of your ship
4. Merge all layers together, use Free Transform again to squeeze the ship vertically. Hold
   Cmd-Opt-Shift and drag a handle to add some perspective
5. Load the saucer as a selection, hold Opt and hit down four times to add an edge to it via
   duplicates. Merge the layers
6. Inverse the selection (this will select the edge only). Lock transparency with '/' and use the
   Dodge/Burn tools to add some shadows to the edge

# The Desk Drawer

The desk drawer is filled with items: an ipod, pocket watch, magnifying glass, pencil, ticket, deck
of cards, paper envelope, rubber bands, and a paper clip.

Making the drawer:

1. The draw edges are just thin pieces of wood with rounded corners. Make three edges and combine
   them
2. Use another piece of wood, darken it, and add it to the edges to create the sides
3. Use a large chunk of wood texture to make the drawer bottom

Making basic outline of an iPod:

1. Use the Pen tool to create the subtle curve of an iPod, duplicate it for all four corners. Use
   the Marquee tool for a vertical selection with the corners and fill it
2. Add some Gaussian Noise
3. Use the Burn tool to add shading to the sides, holding Shift to shade it vertically
4. Duplicate the original iPod shape, fill it with black, and shorten it vertically to create the
   screen. You can curve the top with the Warp tool
5. Add an Inner Bevel to the black screen for dimension
6. For the control, make a circle white selection and cut out a smaller circle. Add a Bevel for some
   dimension to the control
7. Finish by adding text for the menu

Making a play button:

1. Draw a square filled with a color
2. Rotate by 45 degrees to make a diamond
3. Delete half the diamond for a tall arrow
4. Use Free Transform to compress to a play button

The progress bar:

1. Make a long, horizontal white bar and select a portion to fill
2. Select the bottom half of the fill and add shading with the Burn tool
3. Select the top half and use the Dodge tool (with Shift)

The battery icon:

1. Start with a rectangle selection and stroke it with white
2. Make a smaller rectangle at the mid-right edge
3. Select a smaller rectangle inside the initial outline and fill it with white

Making a movie ticket:

1. Start by drawing a rectangle and cut out a semi-circle on both ends
2. Use the smudge tool to add a bit of smear to both sides
3. Add basic texture with Gaussian Noise (monochromatic)
4. Lock the transparency and run a horizontal Motion Blur to give it some paper texture
5. Use the Hue/Saturation dialog to give it a muted color
6. Draw the outer rectangle and text "Admit One", some dates and borders
7. Merge all the borders/text, lock transparency, change to Multiply, and run the Cloud filter. The
   white areas will be faded away

Make a pencil:

1. Draw a long rectangle that's curved on one end
2. Duplicate it and use Free Transform to squeeze it to about half its height, then lighten it and
   place it above the original. Do the same except darken it and place it below the original
3. Use Hue/Saturation with Colorize to add color
4. Use a white brush and paint a white line across where the layers join
5. Use the same wood texture as earlier, brighten it, and use Free Transform to make the tip of the
   pencil. Hold Cmd-Opt-Shift and drag the top left corner to do this
6. Use Dodge/Burn tools to add highlighting to the tip
7. Duplicate the tip, shrink it for the lead portion, and use Curves to adjust
8. Make a thin gray rectangle, add shading with the Burn tool, copy it and stretch to make it
   taller/narrower. Duplicate the edge to add dimension.
9. Curve it with Image Warp and Shear filter
10. Make a metallic effect using Curves
11. Make a large rectangle with round corners, use Dodge/Burn tools to add shading to it
12. Use Hue/Saturation to make it pink, add some Gaussian Noise
13. Put all the elements together
14. Add scratches with small, hard-edged brush the same color as the pencil
15. Add Bevel and Emboss to the scratches for an added effect

The ruler:

1. Make a slightly rounded rectangle
2. Place a piece of wood over the top using a Clipping Mask
3. Select the top/bottom thirds of the ruler, apply a 2 pixel feather, and darken
4. Tick marks can be made with duplicated vertical lines
5. Add the numbers
6. Paint with a small, hard-edged brush for scratch marks and add Bevel/Emboss

Making the pocket watch crown (twisty thing to set time):

1. Start with a gray circle
2. Make a pattern of thin vertical black lines with the circle as a clipping mask
3. Merge and run the Spherize filter
4. Lower the contrast and use Dodge/Burn tools for shading around the edges
5. Use Free Transform to squeeze it vertically

Making the pocket watch itself:

1. Start with a gray circle, use Bevel and Emboss to add dimension
2. Duplicate with the same style and shrink it slightly to form an edge. Also draw a stroked circle
   for the inner part
3. Add the top and crown of the watch
4. Make it metallic using the Curves dialog
5. Use Color Balance to add red/yellow for a gold watch
6. Make a new white layer for the watch face with some shading
7. Make two small black ticks on opposite ends, then Free Transform and rotate 30 degrees while
   duplicating for all the ticks
8. Draw a circle with the Shapes tool and write the time along the path
9. For the clock hand, draw half the shape with a Pen tool, fill it, and duplicate/flip for the
   other side. Add a circle to the bottom and add an Inner Bevel/Drop Shadow for dimension
10. Tint the watch face a pale yellow and use a soft-edged brush to highlight the glass face

Making a paper clip:

1. Draw 3 stroked gray circles. In order of size, the 1st should be top aligned with the 2nd. The
   2nd should be bottom aligned with the 3rd. The 3rd should be in between the 1st and 2nd
2. Delete half of each circle
3. Use the Marquee tool to add strokes and connect the open circles
4. Add an Inner Bevel ~ depth 220%, size 4 pixels, soften 4 pixels with gloss
5. Add further shine with Satin in Layer Styles ~ 68% opacity, 25 pixel distance, size of 29 pixels,
   Hard Light blend mode
6. Finally add a drop shadow

Rubber bands:

1. Use the Pen tool to make some shapes
2. Choose a small, hard-edged brush with mid-gray paint and hit Enter to stroke
3. Select All, hold Opt and nudge it up a few pixels for an edge
4. With the topmost layer selected, use Curves or Levels to brighten
5. Inverse selection and use Dodge/Burn to shade the edges
6. Inverse again and add a 1 pixel white stroke at 40% opacity
7. Use Hue/Saturation to change the color

Deck of cards:

1. Use the Shapes tool in Pen path mode to draw the basic outline of a card. Use the Rounded
   Rectangle shape
2. Draw a vertical blue line, hold Opt-Shift to nudge it down and make duplicates 10 pixels apart.
   Rotate it 90 degrees to make a grid
3. Rotate the grid in 45 degrees to make a diamond, delete all but the square
4. Duplicate to fill out the inner portion of the card. Select the pattern and choose Edit -> Stroke
   with a blue stroke
5. Add a Drop Shadow to your shape
6. Merge everything, select the card, and Opt-Drag to continually make copies. This will produce a
   deck of cards. Rotate a few for realism
7. Use the Burn tool (on midtones) to add some shading to the top card. This makes it look more worn
   out
8. Merge all the cards together

Create an envelope with a letter in it:

1. Draw half the envelope with the Pen tool, add a blue tint, use the Texturizer filter to add some
   texture
2. Duplicate and flip horizontally for the other half. The front flap can be made by combining the
   layers
3. Use the Burn tool to add some shading below flaps
4. Duplicate the front flap and extend the texture to make the rear flap
5. Use the Burn tool to add shading to the rear flap
6. Paint with brown at a low opacity to add some dirt
7. You can make a letter by putting some text on a layer and adding texture
8. Use the Dodge/Burn tools to paint the rear flap's area where the sticky sections is
9. Rotate the letter and place it into the envelope. Add some shading with the Burn tool

Drawing a magnifying glass:

1. Draw a black rectangle with one rounded edge
2. Lock the transparency, use a soft-edged white brush at a low opacity for highlighting to make it
   look round
3. Repeat with a smaller brush size on the bottom
4. Make the collar by drawing a small, thin round-edged rectangle and duplicating
5. Add an Inner Bevel and Contour
6. Reduce the middle four shapes and push them together
7. Draw a circle on a new layer and use Edit -> Stroke for the lens
8. Duplicate the ring and add Inner Bevel and Coutour. Duplicate another time, use Free Transform to
   make it smaller and give it depth
9. Use Dodge and Burn tools to add the lens highlight/shading

# Fantasy Art

This illustration includes a horned devil, snake-like objects, and lots of shiny metallic objects.

Whereas the Clouds filter randomly generates a new texture each time, the Difference Clouds filter
builds on the previous effect to increase/tighten.

Making the textured background:

1. Start with black/white chips and run the Difference Clouds filter a few times
2. Use Radial Blur filter with amount ~ 50 and Zoom method
3. Run a Plastic Warp
4. Tint the background with Color Balance and adjust Brightness/Contrast

Creating the face from the background:

1. Choose Filter -> Liquify to get started. Use the Forward Warp tool with a large brush size to
   push a dark region (the eyes)
2. Repeat the process for the other eye
3. Click and drag for the nose and mouth
4. Continue smearing the image to make the beard
5. When the face is complete, hit the OK button to exit

Adding polish to the eyes/teeth:

1. Make a circular selection for the pupils, feather it, and fill it red
2. Make a convincing set of teeth, don't worry about lining them up. Use a hard-edged gray brush
3. Use the Dodge tool set to Highlights to add highlights to bottom/right of each tooth
4. Switch to Burn tool and darken left side of each tooth
5. Use a Layer Mask with the Pen tool to make the teeth fit the mouth
6. Use Color Balance and Brightness/Contrast adjustment to add a blue tint and darken it a bit

Making the horns:

1. Start with a gray ellipse
2. Use the Dodge/Burn tools to add shading around the bottom edge. Add a light spot on the left side
3. Duplicate the layer and use Free Transform to shrink and move the layer upwards a bit. Rotate it
   a few degrees
4. Keep repeating the last step to build up a horn
5. Use different angles of rotations to make a random horn
6. Add gloss with the Plastic Warp filter and use Curves to make it metallic
7. Finalize with Color Balance and Brightness/Contrast

Making a hand:

1. Draw a hand shape with a mid-gray hard edged brush
2. Use Dodge/Burn tools to add shading to the fingers and a little darkness to the back of the hand
3. Add highlights to the upper part of fingers and darkness in between
4. Use the Plastic Warp filter for a shiny effect
5. Use the Smudge tool to smear the highlights down
6. Tint the hand to the color you want
7. Draw the fingernails with a hard-edged pale blue brush. Darken underneath the fingernails and add
   highlights to the top

Making snake shapes:

1. Start with a small round circle. Add shading to the bottom/left
2. Use the Smudge tool with a hard-edged brush and 100% strength. Drag up then down with different
   angles
3. Take another blob and repeat the same process until you have many snakes. Be sure to use
   different thicknesses
4. Apply the Plastic Warp filter for shiny-ness

# In the Attic

The attic scene has a brick wall background and a lot of junk. To name a few:

bowling ball, guitar, records, bike tire, tennis racket, and a broken mirror.

We'll start with forming the brick walls. Use the same brick wall we made in the Essential
Techniques chapter:

1. Copy the wall layer and align it to the existing. Use Free Transform with 'Cmd-Opt-Shift' drag a
   corner to add a corner
2. Make sure each corner brick as a white cement line (via copy/paste)
3. Use Hue/Saturation adjustment to make the wall darker
4. Add grime with a large brush, at a low opacity, set to Dissolve. Add random splatters then run a
   Gaussian Blur
5. Optionally draw horizontal lines aligned with the skewed wall to figure out where the vanishing
   point is

Making the rafters:

1. Draw the initial plan for the rafters using parallel gray rectangles and include 2 vertical
   rectangles which form a square
2. Use Free Transform to align the plan to the floor of the brick walls
3. Duplicate the rafter layers and darken. Move it down to create depth and use Free Transform to
   make up the sides
4. Select the corners between the original and duplicated rafter layers. Darken it to create corners
5. We're going to darken the entire set, so increase the contrast of the originals so they're almost
   white
6. Open the wood texture and use Free Transform to align it with the rafters. Make a Clipping Mask
   from the rafters layer and change mode to Multiply
7. Brighten the corner edges to make it less crisp

Making the wooly substance to place between rafters:

1. Paint a wiggly band of gray
2. Run a Gaussian Blur filter
3. Lock the transparency, set the chips to black/white, run the Clouds filter
4. Duplicate the layer several times, shrink it, and fit into each row
5. Merge the layers together, move left/right as necessary
6. Delete the bottom edge of each row

Making a wooden dresser:

1. Draw a rounded-corners rectangle with filled gray
2. Paste in the wood layer, using the rectangle as a clipping mask and merge
3. Use Layer Style to add a slight Bevel
4. Make 3 rectangular selections for the drawers. Make new layers, add a bevel, add a drop shadow,
   then flip horizontally
5. For the handles, make 2 gray circles. Add Bevel with Gloss Contour. Make an upside-down U shape.
   Then add a golden Color Overlay
6. Draw a gray handle with the gray circles and endpoints
7. Opt-Drag the layer styles from the circles to the handle to make it golden
8. Duplicate the two circles, make them the top layer and reduce the size
9. Duplicate and add handles to each drawer
10. Draw a curved leg for the dresser, use it as a clipping mask with the wood texture. Add some
   shading with the Burn tool
11. Copy the front and use Free Transform to make it a side
12. Duplicate the legs and move it behind the originals. Move it up and slightly to the right. Use
   the Clone tool to fill gaps
13. Use the same Hard Light procedure to add scratches and varnish used on the ruler in an earlier
   chapter

Making a draped piece of sheet:

1. Draw the outline of the sheet with light gray
2. Use the Burn tool to add shadows beneath the main folds
3. Use the Dodge tool for bright streaks above each shadow
4. Lock transparency and use Smudge tool with a soft edged brush and ~80% opacity to smear the
   shading
5. Continue smearing, add folds by smearing from within a dark area
6. Change the sheet layer opacity to ~90%
7. Duplicate and set the new layer's mode to Hard Light
8. Load it up as a selection, feather it by a few pixels, fill with black, change opacity to ~80%,
   and move it down/left for a shadow effect

Building a cardboard box:

1. Start with a plain, gray rectangle. Run the Clouds filter with different shades of gray for a
   slight mottling effect
2. Use Hue/Saturation to make it brown
3. Add vertical stripes, change the layer's mode to Diffuse, and make it brown
4. Duplicate all lines to make the spacing narrower
5. Now for the interior texture: duplicate the rectangle from step 2, paint thicker dark brown
   vertical lines
6. Merge the lines/rectangle together and run a Noise filter and Gaussian Blur
7. Back to the exterior texture: distort its perspective, duplicate and flip for the 2nd side. Add
   some shading to the front face
8. Duplicate the front face and place it in back with more shading
9. Duplicate a portion of the front and distort it to make a front flap, optionally use the Lasso
   tool to tear off edges. Add some shading to the corner where the front/top meet
10. Duplicate the flap, make it darker with more noise, rotate it for the other flap

Making scotch tape for the cardboard box:

1. Draw the tape on a new layer filled with gray. Use the Dodge/Burn tools to add shading
2. Run the Plastic Warp filter to add shine
3. Change the mode to Hard Light. Add red/yellow through Color Balance and optionally darken it

Making a mannequin:

1. Draw an outline with the Pen tool and fill with gray
2. Use Dodge/Burn to add shading on the left side and highlights on right. Use it for the breasts
   also
3. Use your favorite method to add color. Caplin uses Curves to remove blue
4. Make a new layer filled with gray, run Texturizer filter, then run Spherize set to Horizontal
   Only to make fabric
5. Place the fabric texture over the dummy layer with a clipping mask, set it to Hard Light
6. On a new layer, draw a path down the middle of the dummy and join it with the left side of the
   dummy. Fill it with gray and add an Inner Bevel. Change this layer's mode to Hard Light and use
   the dummy layer as a clipping mask
7. Draw an ellipse on the armholes/neck and paste the wood texture we have. Use Dodge/Burn tools to
   add shading

Building a guitar, starting with the body:

1. Draw half of the body using the Pen tool and fill with gray. Duplicate and flip for the other
   half
2. Add some wood texture using the layer as a clipping mask
3. Add inner shadow with a ~40% choke and size of ~200 pixels. Choose a dark brown color and set the
   mode to Multiply

The neck/bridge of a guitar:

1. Draw half the neck/bridge with the pen tool, duplicate and flip, then paste some wood texture
   with the layer as a clipping mask
2. Add a slight drop shadow to the bridge
3. Draw half the head, duplicate/flip, and paste wood texture again

Building the fretboard and enhancing the head:

1. Draw a horizontal thin rectangle in brown and add a small Inner Bevel
2. Duplicate the line several times, place them vertically apart with space decreasing a little each
   time
3. Place the lines onto the guitar neck, use Free Transform to make it line up
4. Draw a gray circle on the head, make it metallic, and paste six copies
5. Duplicate those pieces, shrink them, and place them directly above the originals for depth. These
   will hold the strings
6. Add gray circles to the neck, lock transparency, and run the Cloud filter

The center hole and rings:

1. The center hole is just a black circle
2. Make a circular selection around the hole that's wider, add a stroke
3. Repeat the process for decorative rings

The pegs on the bridge:

1. Make a gray circle
2. Add some shading with Dodge/Burn tools
3. Use Color Balance to change to an ivory color
4. Draw a black circle in the center
5. Work at a large size, but shrink them and duplicate to add to the bridge
6. Add a drop shadow to all the pegs
7. Add a thin rounded rectangle for the saddle of the guitar

Making the wounded brass string texture:

1. Draw two gray circles on a new layer
2. Use the Rectangular Marquee to make a horizontal line with rounded ends
3. Add some shading to the bottom/left and highlights to top/right
4. Shrink the piece and duplicate multiple times to form a vertical pattern
5. Use Free Transform to make it narrower and change the color to brown with Color Balance

Adding the strings:

1. Add the string to the guitar
2. Rotate it so the top hits the neck and the bottom hits a peg on the bridge
3. Duplicate and make it slightly narrower. Shearing might be easier than rotating for the middle
   strings. To shear, use Free Transform and hold Cmd while dragging the bottom center handle
4. The last two strings are thinner, not from wounded brass. Just use a line
5. Add drop shadows to the thicker strings to make it look more realistic
6. Duplicate the top portion of the strings. Free Transform to connect them to the pegs on the head

Moving the guitar into perspective:

1. Duplicate the guitar body, move it a few pixels left and fill it gray
2. Use a hard-edged brush to fill in gaps at the top/bottom
3. Paste a copy of the wood texture, run the Shear filter to add perspective
4. Darken with the Burn tool
5. Select the side and add a white stroke
6. Repeat these steps for the head/neck

Making a bicycle wheel:

1. Start with a gray circle
2. Remove two small circles at the top/bottom of the wheel and remove
3. Use Free Transform to duplicate the holes, rotated about 20 degrees, all around the wheel
4. Add an Inner Bevel to the hole with Gloss Contour, do this on alternating holes
5. Draw an inner circle and copy the layer style. Repeat for inner circles
6. Reduce the size of the hub and draw the tire circle around it, copy the layer style
7. Draw a straight line from the hub to the outer rim, copy layer style
8. Repeat at different angles to form the tire
9. To make the tire, start with a thick black circle
10. Make a tire bump on a new layer, and duplicate with Free Transform to add them all over the tire
11. Add an Inner Bevel for shine and a 3D effect

Bowling ball:

1. Make a square selection. Set chips to light/dark gray and run Cloud filter
2. Run Difference Clouds a few more times
3. Paint on a new layer with a hard edged gray brush. Set the layer to Hard Light. Add Inner Bevel
   to make the lines look like scratches
4. Add some more dabs of hard-edged brush for pits and scratches
5. Make a circular selection within the square and run Spherize filter. Inverse the selection and
   delete the outside
6. Use Dodge/Burn for shading and highlights
7. Make a hole and add Inner Bevel. The shadow/highlights should be in Screen
8. Duplicate and free transform to make all holes
9. Select the holes, contract, fill with gray, contract again and delete
10. Use Hue/Saturation to change to a color of your choice

The records:

1. Start with a black circle. Make a small hole in the middle by entering QuickMask and using Free
   Transform to scale it down
2. Apply an Inner Bevel with an N-shaped curve in Gloss Contour
3. Make a selection smaller than the record and add Gaussian Noise
4. Run Radial Blur set to Spin
5. Paint vertical white stripes with a soft edged brush and run Polar Coordinates filter set to
   Rectangular to Polar. Duplicate and rotate
6. Apply circular strokes of black rings. Select an inner portion and fill it with black
7. You can fill the inner section with a color and text
8. Use Free Transform to lay it flat and add a drop shadow
9. Duplicate to make a small stack

The light bulb:

1. Draw half the bulb and fill with gray. Duplicate and flip. Add some shading around the edge
2. Run the Plastic Warp filter
3. Lock transparency and use the Smudge tool to smear the highlights
4. Add more highlights in the center
5. Use Color Balance to add blue and green
6. On a new layer, draw the torso shape with some shading
7. Run Plastic Warp and set to Hard Light
8. Draw the filament holders on a new layer and the filament itself
9. Draw the arc beneath the bulb and add shading. The top-left and bottom-right should be shaded.
   Invert for highlights
10. Duplicate the arc to make a screw and skew it with Free Transform
11. Draw the bottom rounded portion and color it
12. Make a Curves adjustment set to Luminosity
13. The Glass layer should be Hard Light, feel free to brighten it
14. Add an outer glow

# Future Tech

We're making a futuristic scanning machine with a grip, light source, screen, fancy UI, and speaker.

First, sketch out the overall shape using Shapes tool and vector paths. Fill it with a light gray
and dark gray. Add a large Inner Bevel to give them a three dimensional feel.

The side grip:

1. Draw a series of horizontal rectangles
2. Draw a single rectangle which unites them all
3. Load as a selection, refine edge and raise smooth/feather
4. Add Inner Bevel
5. Add a Layer Mask and paint horizontal stripes to hide the bevel and layer, creating grooves
6. Disable the Layer Mask by Shift-Clicking on its thumbnail
7. Paint a vertical stripe on the right to fade it
8. Copy a section on the left, flip it to the right

Control ring that's shiny:

1. Start with a circular selection and add a thick gray stroke
2. Make a layer mask and remove two thin vertical stripes from the ring
3. Duplicate and rotate 45 degrees, repeat so until the stripes are all around
4. Load it as a selection, feather and contract it, then add a Pillow Emboss to the smaller
   selection
5. Add a dark blue color and maybe some texture using the Cloud filter
6. Select one ring segment and add an Inner Glow
7. Draw the inner circle, fill with gray and add highlights/shadows
8. Run Plastic Warp and color the inner ball with Hue/Saturation
9. Draw an ellipse at the top, feather it, paint the bottom half with a soft edged white brush

Microphone:

1. Draw one dot, select it, hold Opt-Shift and drag to duplicate to make an array of dots
2. Make a circular selection and run the Spherize filter. Inverse selection and delete the outer
   dots
3. Separate the dots into two halves and duplicate the edges to fill in between
4. Fill the dots with white and place them on a black background
5. Add an Inner Shadow to the dots layer. Optionally, use an Inner Bevel

Outer ring and lens:

1. Start with a thick gray ring on the outer layer
2. Add Inner Bevel and a U-shaped Gloss Contour to give it shine
3. Duplicate the ring, make it smaller, this time use a sawtooth (M-shaped) Gloss Contour
4. Make a gray circle behind the rings, add shadows/highlights
5. Duplicate and make it slightly smaller, rotate 180 degrees to make an inset section of lens
6. Repeat this process 3 more times
7. Make an elliptical selection on the lens but behind the ring. Make it near the top, then use a
   soft edged white brush and paint the bottom of the lens
8. Repeat for the bottom but with a green color in Hard Light mode
9. Duplicate the green layer, reduce it in size, change to magenta, and rotate it

The stereo and holes pattern:

1. Make a grid of dots, duplicate, make a selection and run Spherize filter with Horizontal only
2. Use Free Transform and squish it vertically
3. Only take the spherized dots used on your stereo. If the bottom of the stereo is round - only use
   the bottom portion of the spherized dots
4. Fill the dots with a mid-gray and add an Inner Shadow. Paste onto background

Light bar:

1. Draw a horizontal lozenge
2. Add highlights to the top and shading to the bottom. Hold Shift to constrain
3. Use Curves to make it shiny, using an up/down stepped curve
4. Merge layers and add a Hue/Saturation adjustment to color it green
5. A glow can be added with an Outer Glow layer style

# The Great Outdoors

Painting the sky:

1. Start with a black layer
2. Sketch the cloud shapes with a soft edge brush
3. Run the Ocean Ripple filter
4. Run the Glass filter
5. Select All, enter QuickMask, then paste
6. Leave QuickMask and fill selected area with gray
7. Add shading/highlights with dodge/burn tools
8. Use the Smudge tool to streak out parts horizontally

Making grass:

1. Draw a single streak of grass with a gray brush
2. Select it and choose Edit -> Define Brush Preset
3. Open the Brushes Panel and choose the newly created brush
4. Click Shape Dynamics, set Size Jitter to 100%
5. Set Angle Jitter to around 4 degrees
6. Switch to Scatter pane and drag the slider for both axes, increase count
7. Switch to Color Dyanmics and increase FG/BG jitter to 100%
8. Now just choose a FG/BG color and paint

Making the bark texture:

1. Make a rectangle selection, set chips to two browns, run Cloud filter
2. Run Fibers filter to start the bark texture
3. Duplicate and run Emboss filter for a 3D look
4. Change Embossed layer to Hard Light mode

Adding the tree trunk:

1. Sketch out the shape of the tree
2. Copy the bark, paste it onto a part of the tree and feather its selection
3. Copy and paste the bark over all sections of the tree, rotate as necessary
4. Merge and run the Liquify filter, warping as necessary
5. Use a clipping mask with the tree shape

Adding leaves to the tree:

1. Draw a single leaf's outline with gray and fill
2. Darken half the leaf to make it look like a fold down the middle
3. Paint veins with a small brush
4. Make it a custom brush, add angle/size jitter
5. Choose appropriate colors and paint the leaves onto the trees
6. Add shading/highlights with dodge/burn tools

# Still Life

This scene includes a skull, candle, books, and red cloth on a table.

Drawing the table:

1. Start with a piece of wood texture
2. Use Free Transform to move it into perspective
3. Use Curves to darken and add some red
4. Duplicate and darken to create the side
5. Paint the edge white on a new layer and reduce to 10% opacity

Make the background:

1. Use Clouds with two shades of brown
2. Since the filter creates intricate details, Caplin just uses a portion and enlarges it to cover
   the whole background
3. Darken the texture
4. Use a very large, soft brush to add a radial shading - bright at the center

Adding the red cloth:

1. Draw the basic shape of the cloth
2. Use the Burn tool to paint shadows around the edges
3. Use Dodge/Burn to approximate the folds in the middle. Paint shadows directly below the
   highlights
4. Lock transparency and use the Smudge tool to smear the highlights/shadows. Use a soft edged brush
   around 80%
5. Smear the dark edge into the cloth to create larger folds
6. Use the Burn tool to add deeper shadows beneath the folds
7. Build up with small/short smears
8. Use Hue/Saturation adjustment to make the cloth red

The skull:

1. Draw the outline of the skull and fill with gray
2. Draw eyes, teeth, and bone shapes on same layer with darker gray
3. Paint highlights on top of main bones, shadows on bottom using dodge/burn
4. Add a dab of highlights on each tooth with dodge
5. Use the Smudge tool to smear cracks onto the teeth
6. Smudge with a soft edged tip to smear shadows into the skull
7. Make small holes on a new layer with a soft edged brush set to Dissolve and 10% opacity
8. Choose Edit -> Stroke and add a 1px stroke to make the holes larger
9. Run Gaussian Blur to soften it
10. Use a small, hard-edged brush to paint tiny cracks

The skull texture:

1. Make a circular selection
2. Run the Clouds filter on two shades of gray
3. Run Emboss to get a rough, stone-like texture
4. Run Spherize for a rounded effect
5. Stretch the texture to cover the skull and use a Clipping Mask
6. Change the mode of the texture to Hard Light
7. Change colors with the Hue/Saturation adjustment

Old books:

1. Run the clouds filter on two shades of brown
2. Crisp the texture with an Unsharp Mask (400% with 6px radius)
3. Draw an upper cover layer, use Free Transform to move into perspective
4. Use the Pen tool to draw the right/bottom edge
5. Draw the spine on a new layer, fill with a darker gray
6. Place the texture above the cover, use a Clipping Mask and Free Transform
7. Do the same for the spine, squeeze if necessary
8. Darken the bottom of the spine with the Burn tool
9. Draw a curved shape which follows the spine, duplicate and fill with gray
10. Add Inner Bevel and highlights/shadows with dodge/burn
11. Change the mode to Hard Light to see through it
12. Use the polygonal lasso tool to select an area of the cover without the spine or corners. Make a
   Curves Adjustment and add red
13. Draw a single sheet of paper inside, then Opt-drag to duplicate

The candle:

1. Draw the initial shape of the candle in gray
2. Paint some drips on the sides
3. Add shadows to the bottom and edges, highlight the inside
4. Use Dodge/Burn tools to create drips from the front
5. Lock transparency and use Smudge tool to smear the drips
6. Use Hue/Saturation to make the candle white
7. Use Dodge tool set to Highlights for the inner candle - wax is supposed to be translucent. Use
   Burn tool for more shadows around the bottom

The flame:

1. Draw the basic outline in orange and fill
2. Use Dodge to add highlights to the center
3. Paint with a soft-edged white brush in the middle
4. Paint with a blue, soft-edged brush on the bottom
5. Use the Smudge tool to smear the top of the flame
6. Draw a wick with a thin brush set to Dissolve