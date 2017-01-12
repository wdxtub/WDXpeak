# Art and Design in Photoshop

Steve Caplin teaches us art and design concepts with Photoshop walkthroughs. He starts with a goal
in mind, puts together pieces, and gives us the guidelines for which they fit.

# Typography

Serif fonts have fine lines at the end points of all their strokes. They were originally done by
Greek/Roman stove carvers. Long strokes tend to crack in the middle - the serifs prevented cracking.
Serifs add a horizontal rhythm which makes it ideal for long blocks of text.

Sans Serif literally means without serif ("sans" is Latin for without). It was designed for posters
and headlines. Overtime, designers began giving it weight variation which made it much more readable
for larger bodies of text. They take up less vertical space than serif fonts, so they're also ideal
when you need to fit a lot of text in one area.

Some tips offered:

* You don't need to use all the space on a page, whitespace is your friend
* Make headlines more appealing with sans serifs and different font families
* Make sure text columns aren't too wide
* Try drop capitals to let the reader know where paragraphs start
* Add contrast, try white on black for a single element
* Pull quotes which break apart text add contrast

Intertwining monogram letters:

1. Start with two letters as separate text objects overlapped
2. Use Layer Styles to add an outer stroke
3. Load up the top letter as a selection, expand to include most of the stroke - leave off 1px to
   exclude a white fringe, add a layer mask and paint selectively to hide areas
4. In Layer Effects make sure the Layer Mask Hides Effects option is checked
5. Once intertwined, you can set the colors you want for the fill and stroke

Font smoothing:

1. Make a type layer and load it as a selection
2. Open the Refine Edge dialog
3. Increase the Feather amount
4. To get rid of blurring, increase the Contrast amount

Caplin recommends using www.dafont.com or www.myfonts.com as a font resource.

# Principles of Design

A good rule of thumb is to always place your characters facing into an image rather than facing out.
There are exceptions to the rule though.

Adding focus to an image is a great way to draw the viewer's eyes. This can be done by surrounding
everything else in a shadow, using a Gaussian Blur, or adding a blue tint to the background.

Add diagonal elements to your images to make them more lifelike. It adds dynamism, movement, and a
sense of realism if everything isn't lined up. If you want your image to convey calmness or
stillness, then remove diagonals.

The rules of thirds dictates where your subject should be in an image. Split your image into a 3x3
grid. Your subject/focus should be where the lines meet.

If you've got a horizon in your photo, it's important to always be at the same level as your
subject's eyes. Otherwise, it'll look awkward. This is important for any horizons - including
horizontal lines leading to vanishing points.

There are always clues for perspectives. Use the shape tool to add horizontal and vertical lines in
your image and look for the vanishing point.

# Contemporary Design

Making ASCII art out of a photo:

1. Go to Preferences -> Guides, Grids & Slices. Setup gridlines with approx 12px
2. Choose View -> Show -> Grid to make it viewable. Create a new type layer and type in random 1 and
   0 characters. Adjust the size and leading until the characters fit exactly into the grid
3. Use Layer -> Rasterize to turn them into pixels, then duplicate to fill the entire canvas. Merge
   them all together to form one layer
4. Inverse the colors to be white on black text. Use Hue/Saturation to colorize the digits.
5. Choose an image with strong light and shade, increase the contrast if needed. Erase any
   background elements so only the foreground stands out.
6. Choose Filter -> Pixelate -> Mosaic to fit the grid, use same cell size as earlier
7. Optionally, use Image -> Adjustments -> Posterize to reduce gray shades
8. Change the layer mode to Multiply to show the numbers through
9. Make any perfecting tweaks using Levels or Curves for the background

Making graffiti art from a photo:

1. Turn the photo into a graphic element by turning it pure black and white using a Threshold
   Adjustment Layer
2. Use the Dodge/Burn tool to highlight/shade any areas you want
3. Use Filters -> Noise -> Median to smooth out jagged edges
4. Merge the Threshold Adjustment Layer and add a wall layer as a background
5. Use a soft edge brush set to Dissolve and the lasso tool for splatter spray
6. Use Hue/Saturation dialog with Colorize to add color
7. Optionally, use a Gaussian Blur to soften the edges

Crosshatching a photo:

1. First turn your photo grayscale, then boost the contrast to make it crisper
2. Run it through Image -> Adjustments -> Threshold
3. Draw a layer of diagonal lines (this may take a while) in QuickMask mode, the intersection of
   lines and black areas should make a crosshatch theme
4. Now do the same but flip the diagonal lines to go the other way
5. Change the top layer to Multiply mode

Creating iPod advertisements:

1. Make a selection around your subject on a white background and fill it with black
2. Draw an iPod with the shapes tool, Free Transform it and paste it into the subject's pocket
3. Make a cable with the Pen tool. Stroke it with a hard edged brush
4. Add a background and shadow

Making pixel art:

1. Zoom in to around 500%, draw the basic skewed rectangle for the outline of two buildings (2px
   right, 1px down)
2. Draw windows and duplicate them. It's easier to draw two pixels and continually copy/paste it
3. Flip the wall and connect it to make the adjacent wall. Color each sides a different shade of
   gray to take into account shading
4. To make a corner, start with an ellipse with anti-aliasing off. Add a stroke with the Stroke
   menu. Then erase all but the bottom corner
5. Add shadows at ~50% opacity

# Poster Design

Creating a Victorian playbill poster:

1. Playbills used a lot of fonts. Do the same thing with different font families and sizes. Set each
   headline to take the full width of the page
2. The cast list is in Slab Serif. Character names are left aligned and the actor/actress names are
   right aligned.
3. Photoshop doesn't support leader dots, so type them by hand "dot space dot"
4. Add texture - use a piece of stained paper placed on top with its blend mode set to Hard light
5. Change the background color from white to mid-gray to solve brightness issue

The Constructivist movement began in 1910, people decided to use art as a tool for social
development rather than decoration. Caplin shows us how to put together a Russian Revolutionary
style:

1. Start with a red diagonal polygon which takes up a good portion of the page
2. On a new layer with the red diagonal as a clipping mask, use a soft edged brush to add some
   shading to the edge. Change the mode to Dissolve to get a mezzotint effect
3. Set the background to a creamy color
4. Add a layer of architects (or any other people). Use Filter -> Sketch -> Photocopy for a screen
   printed appearance. Change the mode to Multiply to see through it. A second copy filled with
   cream color should add more color
5. Add buildings/statues in the background
6. Caplin adds text using the Kyrilla font with a drop shadow to stand out
7. Add texture to the whole poster to make it feel more worn

The Bauhaus style came from a German school of the same name, using geometric shapes in their art:

1. Start with a diagonal stripe across the poster - fill a rectangle and rotate
2. Add more elements with different colors perpendicular to the stripe
3. Add curved text. Use the Pen tool to make a path, then click with the Type tool near the curve
4. Drag the text tool marker to change orientation or direction
5. Use the shortcuts 'Cmd-Shift-&gt;' or 'Cmd-Shift-&lt;' to change font size, use the shortcuts
   'Opt-Left' and 'Opt-Right' to change kerning
6. Continue adding text and graphic elements at different angles

The Art deco period was glamorous. It highlighted travel often, which was a luxury before carbon
footprints. The low angles of their subjects made their posters seem more huge and powerful:

1. Start with a low-angle photo of a train or train model
2. The Poster Edges filter gives the photo a more hand drawn look. It reduces the number of colors
   and adds a black outline
3. Draw the rail at a straight angle first, then use the Free Transform tool to put it into place.
   Use a layer mask around the train wheels to make it look like the train is actually on top of the
   rail
4. Use a black background. Use a gradient for the night sky. Make sure the horizon lines up with the
   vanishing point of the rail. Use a small brush to paint stars one at a time
5. Draw the headlights light with the Pen tool and fill it with a yellow hue. Use a slightly
   transparent white gradient from left to right. Change its mode to Hard Light.
6. Add angular triangles into the sky with the Polygonal Lasso tool
7. Add your headline

Making a boxing promotion:

1. Paste in your subjects, preferably with boxing gloves already on
2. Desaturate both layers with 'Cmd-Shift-U'
3. Add your headlines, boxer names, nicknames, and any commentary. The fonts used were Headline One
   and Boris Black Bloxx. Add some contrast in the letters by making the first/last letters larger
4. Make the text look older. Load them as a selection, set your color chips to light/dark gray, then
   run Filter -> Render -> Clouds
5. Change the new layer to Hard Light to let you see through it
6. Add crumpled paper texture to the poster

Making a movie poster for a Western:

1. Add 3 elements to the poster: a close up of a man's face, a cowboy, and a cloudy sunset in the
   background
2. Use the Brightness/Contrast adjustment to lower brightness and increase contrast on the man's
   face. Then add a layer mask and fade it into the sunset
3. Fill in the cowboy figure with black
4. Add the movie title as the headline, use the Warp Text dialog with Arc Upper
5. Fill in the text with a gradient, orange to red
6. Using Layer Style, add a stroke, inner yellow glow, and drop shadow to the movie headline
7. Add nonsense, tiny text at the bottom to simulate movie credits
8. Add a ragged edge to the poster by using the Lasso tool on a new layer. Inverse your selection
   and cover with a white mask
9. Use a soft edge brush with black to paint inside of the jagged edges to give it an inner
   shadow/depth

Making a science fiction poster:

1. First add the layers: a space satellite, planet earth, starry background. Make sure the satellite
   overlaps the planet
2. Caplin uses the Vipnagorgialla font to add "SPACE" with a large amount of kerning onto the poster
3. Add an Outer Glow that's white from the Layer Styles. Set text color to black to give it a hollow
   feel
4. Adding a solid blue layer below the letters and turning the title's blend mode to Multiply will
   give it a better glow effect

Turning an image of Regan into a horror movie poster:

1. Darken the photo using Curves adjustments and take out a little green
2. Paint a black mask around the face using a large soft edged brush
3. Duplicate the photo layer and use the Dodge tool to shine the cheek/head
4. Use the Burn tool at midtone to set strategic darkness to the photo
5. Now add the movie title and other text

Comedy posters have to look funny, usually through the expression on the main character's face:

1. Add your character's image as a layer, zoom in to just a head/body shot, and place him in a
   comical pose
2. Use a casual font to add the movie title
3. It's common to change the text direction to match any comical puns, so if your movie is called
   "Back to Front" feel free to reverse the font direction
4. Adding contrast to part of the movie title helps
5. The remainder text should be lightweight

Making a French art movie poster:

1. Caplin starts with an image of a woman in a halter top, he uses the clone tool to remove the
   strap from her neck
2. Desaturate the image to turn it grayscale, then increase the contrast to make it look stark
3. Color the image using Color Balance to add blue/cyan. Use the gradient tool to make the top
   darker. Set the girl's layer to Screen so her hair fades into the background
4. Add an image of a man standing up. Use a large, white soft-edged brush to paint a glow behind him
   (using him as a mask). Now remove his image.
5. Now add your movie title, cast credits, etc...

Making a Film Noir poster:

1. The poster starts with two layers, an image of a woman standing and a zoomed in body/headshot of
   a man smoking a cigarette
2. Filter -> Artistic -> Poster Edges to both layers make them look hand painted
3. Boost the colors with Hue/Saturation and use Curves to darken if necessary
4. To make his shadow stronger, duplicate his layer and desaturate with 'Cmd- Shift-U'. Change the
   layer mode to Multiply so only the darks are visible, and Image -> Adjustments -> Threshold to
   turn it black/white.
5. Add a cloudy background and text

Romantic comedy poster:

1. We start with an image of an actress. Use Filter -> Blur -> Median to soften remove the actress'
   pores/wrinkles. It works like Gaussian Blur, but still keeps hard edges intact
2. Use Curves to give the image a bleached out effect, add some red/green to the image for a summery
   effect
3. Either paint out the background or cut it out
4. Now add movie title and credits

Thriller movie poster:

1. Start by making the photo look more stark. Duplicate the photo, desaturate it to grayscale, then
   set the new layer to Hard Light
2. Choose dark blue/black for your color chips and run Filter -> Render -> Clouds for a dark cloudy
   background
3. Create a hole in the glass effect with the Lasso tool. Choose white/pale blue for your color
   chips and run the cloud filter again
4. Lower the opacity of your glass to see through it and use the Dodge/Burn tools to add highlight
5. Use the Lasso tool to draw some cracks. Add some depth to the edge of the glass by nudging the
   shape of the hole and intersecting the edge
6. Add the movie headline and credits. Caplin uses the Wunderback Mix font which has a degraded
   stencil design

Making a motivational poster:

1. Start with a black background. Add a 1 pixel frame (selection, Edit -> Stroke). Add an image of
   clouds
2. Make the clouds more impressive by reducing brightness to 0 and increasing contrast to 100%. Add
   the photo of a cat and litter tray
3. Duplicate the layers and flip it vertically to create a reflection, lower the opacity of the
   reflection
4. Now add motivational text. Caplin uses the Optimus font family which is inspiring and elegant

# Works on Paper

Making a ransom note:

1. Start with a crumpled piece of paper, desaturate and brighten it. Then write each word on its own
   layer. Change the font as you go. Merge them all together when you're done.
2. Make a selection around each word with the Lasso tool, use 'Shift-Backspace' for the Fill Dialog.
   Choose "Behind" as the method.
3. Mose words should have a white background. Rotate some of them.
4. To change the font color within a selection use 'Opt-Shift-Backspace'
5. Add a drop shadow to each background with Layer Styles
6. Duplicate each word/background, make a clipping layer with scraps of paper, set the duplicated
   layer to Hard Light. Paint some glue with a hard edged gray brush
7. Use the Color Balance to add red/yellow to the glue and add a Bevel to it

Creating a medieval manuscript:

1. Choose dark/light tan colors for your color chips and run Filter -> Render -> Clouds. Keep
   repeating until you get a background you like
2. Use the Lasso tool to make selections around the top/bottom edges. Delete them to create a torn
   edge effect
3. Use the Burn tool on Midtones to add shading to the torn edges
4. Add a little more texture with Filter -> Texture -> Texturize and optionally a small drop shadow
5. Now add text. Be sure to use a medieval style font and a drop capital

Making a bank check:

1. Create a text layer of three long lines of bank text. Text warp it, rasterize, shrink it, and
   duplicate it many times to make very long lines of text. Make the background light blue
2. Add the text elements of the check: bank name, account numbers, customer's name, USD $, lines,
   etc...
3. Add a darker blue background for the main portion of the check and a white box for the amount
4. Caplin recommends writing your own text instead of using a handwriting font. Either use a tablet,
   mouse, or scan it in
5. Use the Flag option with the Image Warp tool to add perspective

Changing perspective of a flat check to a laid out wavy check:

1. Enter Free Transform, use Image Warp's Flag default
2. Use the control handles to customize the warp to be less drastic
3. Switch back to the standard Free Transform with 'Cmd-T'. Grab a corner and hit 'Cmd-Opt-Shift'
   and drag it to the center for some perspective
5. Use the Dodge/Burn tools to add highlights on the peaks and shadows in dips
6. Add shadow by using the Polygonal Lasso with a feather and fill

Making a postage stamp:

1. Make a gray rectangle on a new layer
2. Create a custom brush. Make it small, hard-edged with a lot of spacing in between strokes. This
   will be used for the stamp border
3. Press Q to enter Quick Mask mode and paint the dots along the borders holding Shift to keep
   straight. Scale with Free Transform
4. Copy the border and paste it across all sides
5. Paste an image of an important figure onto the stamp. Add the price/country code with a shadow
   and stroke. Use the Hue/Saturation Adjustment to make the stamp more monochrome
6. To make the wavy pattern, create a single wave with the Pen tool and duplicate it to make
   multiple waves.
7. Make a circle with the Elliptical Marquee tool, use Edit -> Stroke. Duplicate and shrink for an
   inner circle. Use the Type tool to type along a path
8. Add a drop shadow to the image, rotate it a bit, and add a Gaussian Blur to make it look like its
   been smudged a bit
9. Finally add the postmark with a mask. Paint out a little bit to give it a poorly inked appearance

# Books and Magazines

Making a book cover for a horror comic (Tales from the Crypt):

1. Add a yellow title on top of a red background. Caplin uses the Ray Larabie and True Crimes fonts
2. Add a stroke with Layer Styles -> Stroke. Also add a drop shadow
3. Now past in the image of a skull and office background. Use Curves to lower the brightness
4. Turn the photo into drawings with the Poster Edges filter

Creating a Victorian Periodical:

1. We'll start with a scanned image of an actual Victorian Periodical. The paper it's on is yellowed
   from age. You can remove the background by desaturating the image and increasing the brightness.
2. Add columns of text, a headline, and a subtitle
3. The drop capital Caplin uses is set in Medieval Victorian
4. Finally add your own yellow textured paper. Place it on top and set its mode to Multiply

Creating a news magazine cover like Times and Newsweek:

1. Start with a large red border and red title
2. Caplin uses a photo of Bill Clinton in the oval office for the cover. He uses the oval office as
   a background, but places Bill Clinton in front of the magazine title
3. Add the main headline text above everything else in red with a drop shadow

Creating a crime novel cover:

1. Start with a black background. Add yellow text set in True Crime font and use the Text Warp with
   the Lower Arc preset. Use a negative bend
2. Skew and rotate the title to top align it. Add a drop shadow in Normal mode so we can see it
   along the black background. Use a hard edged shadow
3. Add a background photo, use Curves to lower the brightness and add some blue. Use a black,
   soft-edged brush to add a dark cloud behind the title
4. Use the Lasso tool to select the doorway, add an outer glow, and fill it with yellow. Add a photo
   of a person in front of the door and paint him black leaving his right side intact
5. For light on the ground, use the Lasso tool to make a cone selection. Feather it by about 20
   pixels, then fill it with yellow
6. Duplicate the man, fill it with black, then use Free Transform to move it as the shadow. Use a
   Gaussian Blur to distort it
7. Add crumpled paper as texture with the Unsharp Mask for a stronger effect

Making a cover for a thriller:

1. Start with a yellow title - "Hard Just" - in Georgia Bold
2. For more impact, make both words the same large size to take up the entire width of the cover.
   Use 'Cmd-Shift-&gt;' and 'Cmd-Shift-&lt;'
3. Style with Bevel and Emboss. Add finishing touches with Satin
4. Add a wood background with a black gradient below the title
5. Add the murder weapon layer on top of the wood. Use a hard edged brush to paint some blood below
   the gun.
6. Use the Burn tool set to Highlights to darken the edges of the pool of blood. Change the blood's
   mode to Hard Light to see through it.

Making a cover for a science textbook:

1. Add vertical text on the side on top of a blue background. This acts like a band around the
   textbook.
2. Make an eclipse with a circular selection filled black. Add an Outer Glow
3. Make a new layer in screen mode filled black. Use Filter -> Render -> Lens Flare to make the Sun.
4. Move the Sun layer above the eclipse for the full effect

# Great Works of Art

Make a photo portrait look like an oil painting:

1. Select all and copy. Make a new channel and paste
2. Return to the RGB composites and choose Filters -> Render -> Lighting Effects. Use a low
   Intensity and somewhat high Ambient setting. Choose the channel you made earlier to give a bump
   map - or oil texture
3. Choose Filters -> Texture -> Texturizer for the canvas texture
4. Finally boost the contrast

Make a landscape painting from a ship and clouds:

1. Add the clouds background behind the ship. Make sure the bottom of the ship is a little bit below
   the clouds
2. Duplicate the ship and flip it vertically for the reflection
3. Make the sky more colorful. Add a new layer in Color mode above the sky and paint with tons of
   blue, yellow, red, and orange
4. Flip the sky vertically to create the water reflection. Add a short black gradient to distinguish
   between sky and water
5. Choose Layer -> Layer Mask -> Reveal All and slowly fade away the ship and clouds as it nears the
   bottom
6. Make a merged copy and run Filter -> Artistic -> Watercolor. Now run Filter -> Brush -> Strokes
   -> Splatter
7. Use the Dodge/Burn tools to highlight the sun and darken the area of the ship with no sun

Make a still painting from a still photo of fruit:

1. Start with the photo of fruit. Duplicate the layer and run Filters -> Artistic -> Dry Brush
2. Use the Burn tool on Midtones to darken the fruit a bit
3. Switch to the copy layer and run Filter -> Stylize -> Glowing Edges, then Images -> Adjustments
   -> Invert, now open the Hue/Saturation dialog and hit Colorize to change all colors to blue
4. Change the second layer's mode to Multiply
5. Duplicate the layer, set it to Color Mode, and paint blue with a soft edged brush for a shadow
   effect

Imitate Henry Matisse from a head shot:

1. Add a background of four squares. Add a shadow with black paint around your subject's head
2. Merge the layers and run Filter -> Artistic -> Fresco to make it seem more like an oil painting
3. Next, apply Filter -> Artistic -> Paint Daubs with a small, medium sharpness brush to get a 3D
   paint texture
4. Use a small Gaussian Blur to reduce the crispness
5. Make a new layer set to Hard Light. Paint with multiple translucent colors

Create a Dutch-like abstract painting:

1. Create a single vertical line first, then duplicate and rotate to create more lines all across
   the canvas
2. Make a new layer and choose a pale brown and white colors for your chips. Run Filter -> Render ->
   Clouds. Then run the Noise filter. Use Gaussian for a more natural noise filter
3. If the noise is too rough, use a Gaussian Blur to smooth it out
4. Move the texture layer behind the lines. Now fill in each square of the lines layer with
   different colors
5. Change the lines layer to Multiply so the colors darken with the texture below

Melt a pocket watch like Salvador Dali:

1. Start with two layers: a pocket watch and a table
2. Use Photoshop's Liquify filter for the melting effect. Start with the Forward Warp tool and a
   large brush to smear the watch downwards
3. Smear the top of the watch towards the table to make it look like it was laid on top of it
4. Use '[' and ']' to change brush size. Hold 'Shift' to make larger jumps. Make the perimeter of
   the watch more lumpy
5. Select the bottom portion of the watch that's hung over the table. Feather it by about 8 pixels
   and use the Curves to make it darker
6. Make a new layer above the table, hit 'Cmd-Opt-G' for a clipping mask. Now paint black with a
   soft edged brush to make a shadow

Add a horror/nightmarish theme to a portrait:

1. Use the Liquify filter and a large brush to widen the mouth like the subject is screaming
2. Use a combo of the Dry Brush and Poster Edges filter to give the painting a harder edge
3. Use the Smudge tool with downward strokes set at 80% and varying opacity
4. Continue to streak over the subject to create folds with fabric
5. Create a new layer with the Fiber filter to create a strong vertical texture. Place it above the
   portrait with Screen mode (or experiment with other modes)
6. Experiment with the Hue/Saturation and Brightness/Contrast

Make a comic scene from a plane:

1. Start with a plane on a layer
2. Make a new layer, hit Edit -> Stroke with a 5 pixel stroke, then add more strokes along contours
   with the Pen tool
3. Make a new layer between both and paint it white for highlights, green for the shadows, blue for
   the windows, and red for the propeller
4. Click the eye icon next to the Texture layer and drag it above the new shading layer. Change the
   mode to Multiply then press 'Cmd-Opt-G' to make it a clipping mask
5. Add the sky with some texture
6. Paint in fire using the Pen tool. Black is fine. Draw another flame inside the shape. This time
   fill it with red (giving it a black outline). Keep adding more flames with white and yellow.

Create abstract 3D art from dots:

1. Draw a circular ellipse and fill it with black. Hold 'Opt-Shift' and drag it 45 degrees from the
   original to make a duplicate. Select both with the Rectangular Marquee and choose Edit -> Define
   Pattern
2. Make a new layer, fill with white, then from the Layers palette choose Layer Styles -> Pattern
   Overlay
3. Turn it into a regular layer by Merging it with 'Cmd-Opt-Shift-E'
4. Duplicate the layer and hide the original. Run the Spherize filter with Horizontal Only checked
5. Scale it with Free Transform
6. Cut and reorder the layer so it looks curved into a dip in the middle
7. Now show the original layer. Use a gradient mask for a fading effect

# Any Other Business

Creating a credit card:

1. Start by typing the credit card numbers. Apply an Inner Bevel at a small size
2. Add Contour (from Bevel and Emboss) to make it more metallic
3. Now create the hologram. Make a gray, rounded rectangle with an image inside it. Merge the
   layers, desaturate, then darken the corners. Open the Curves dialog and draw a wave to make it
   more metallic.
4. Place the numbers and hologram above another larger round rectangle
5. Add the name of the bank and any other text in white. Either add another background on the card
   or draw your own

Carving in stone:

1. Start with a photograph of a stone
2. Write on it with the Type tool. Optimus Princeps is an effective font
3. Change the text color to 50% gray and set it to Hard Light
4. Choose Bevel and Emboss from Layer Styles. Set the technique to Chisel Hard. Set the direction to
   Down and increase the size
5. Make a new layer above the type, select both, hit 'Cmd-Opt-G' for a clipping mask. Make crack
   selections along the edges with the Lasso tool and fill it with a solid gray
6. Change the mode to Hard Light and copy the layer styles from the text.
7. Chip away by making shorter V-shaped selections and deleting

Making stained glass window from a photo:

1. Start with a photo of subjects on a white background. Make it seem more painted by running the
   Poster Edges filter. Make any dull colors brighter.
2. Draw a basic frame outline using the Marquee tools. Then add embossing with Layer Styles and a
   sandstone texture with the Texture filter
3. Add solid colors for the background - a green pasture, blue sky, yellow sun with the Dodge tool
   for highlights
4. Use Edit -> Stroke on each layer to add a thick black stroke
5. Keep adding strokes to your image to look like glass borders

Making a button badge:

1. Start with a circle shape with the fill color of your choosing
2. Use the Shapes tool set to Path, draw a smaller circle, switch to the Type tool and write text
   along your button
3. Hold 'Cmd' and drag the I-beam to where you want the text to start. You can duplicate this layer
   to write text at the top and bottom of the button along the same path
4. You can flip the text along the path by holding 'Cmd' and moving the I-beam to the other side
5. Select all the text, hit 'Opt-Shift-Down' to shift the baseline down to align it with the button
   edge
6. Add an Inner Bevel to the circle layer to make it more 3D. Add the max amount of Softness for a
   smooth edge. Add a drop shadow and rotate it a bit