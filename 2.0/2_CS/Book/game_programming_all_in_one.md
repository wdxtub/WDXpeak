# Game Programming All in One

By Jonathan S. Harbour, this book covers 2D game programming using the cross platform Allegro
framework with the C language. The sample code uses Allegro 4, which is outdated. Allegro 5 has a
new, backwards-incompatible API. Since the example code uses an old version of Allegro, I'll skim
through it to learn general ideas instead of taking precise notes.

# Demystifying Game Development

This chapter is an overview of game development - it doesn't include anything technical.

Harbour says the game industry employs millions of workers, most are specialized in their own
fields. All of this is for entertainment.

There's little difference between programming for a particular console or a PC, it's all based on C
or C++. The console SDKs include libraries that you link into your program. Many companies now
produce the same games for multiple platforms.

2D games are not dead, what sets them apart are fantastic gameplay. It's best to find a niche and
use it to develop a great game.

This book focuses on the Allegro game library, originally developed by Shawn Hargreaves for the
Atari ST. Allegro abstracts the operating system so your code can compile on any supported
platforms.

# Getting Started with the Allegro Game Library

Download Allegro from <http://alleg.sourceforge.net/>. Install instructions for your OS should be on
there also. Learn how to compile Allegro programs here:
<http://wiki.allegro.cc/index.php?title=Compiling_Allegro_Programs>.

Harbour gives us a step-by-step guide on setting up several C++ IDEs with Allegro. He then gives us
an example program to compile to make sure everything works.

The first function used is:

    int allegro_init();

This initializes the library and sets the `allegro_id` information which contains information like
what version of Allegro you're using:

    extern char allegro_id[];

At the end of the main function, use `allegro_exit()` to exit allegro. After the main function, the
macro `END_OF_MAIN()` is required for cleanup. You can print out system information with:

    extern char allegro_id[];
    printf(Allegro version = %s\n", allegro_id);

# 2D Vector Graphics Programming

A **graphics primitive** is a function that draws a geometric shape. Video cards were designed to
render geometric primitives with special effects. It renders triangles made up of vertices.

**Blit** means bit-block transfer, a method of transferring a chunk of memory - usually from system
memory to the video card. The **pixel** is the smallest element on a screen.

`allegro_init` creates a global screen pointer called `screen`. It uses double buffering (render one
screen on the monitor, another off-screen, and switch between them).

The following program initializes full-screen video mode with Allegro 4:

    #include <stdlib.h>
    #include "allegro.h"

    int main(void) {
      allegro_init();
      install_keyboard();
      int ret = set_gfx_mode(GFX_AUTODETECT_WINDOWED, 640, 480, 0, 0);
      if (ret != 0) { 
        allegro_message(allegro_error); 
        return 1;
      }
      //display screen resolution
      textprintf(screen, font, 0, 0, makecol(255, 255, 255), 
                 "%dx%d", SCREEN_W, SCREEN_H);
      while (!key[KEY_ESC]);
      allegro_exit();
      return 0;
    }
    END_OF_MAIN()

`set_gfx_mode` detects the current computer's graphics settings and sets the program's window.
`allegro_message` can be used for an alert box. `allegro_error` is a global variable containing the
most recent error message. `textprintf` displays text in any video mode.

The next program draws text to the screen:

    include "allegro.h"
    int main(void) {
      char *filename = "allegro.pcx";
      BITMAP *image;
      int ret;
      allegro_init();
      install_keyboard();
      set_color_depth(16);

      ret = set_gfx_mode(GFX_AUTODETECT_WINDOWED, 640, 480, 0, 0); 
      if (ret != 0) {
        allegro_message(allegro_error);
        return 1; 
      }

      image = load_bitmap(filename, NULL); 
      if (!image) {
        allegro_message("Error loading %s", filename);
        return 1;
      }

      blit(image, screen, 0, 0, 0, 0, SCREEN_W, SCREEN_H);
      destroy_bitmap(image);
      textprintf_ex(screen,font,0,0,1,-1,"%dx%d",SCREEN_W,SCREEN_H);
      while (!keypressed());
      allegro_exit();
      return 0;
     }
     END_OF_MAIN() 

The simplest pixel drawing function is:

    void putpixel(BITMAP *bmp, int x, int y, int color)

To draw random pixels onto the screen:

    while(!key[KEY_ESC]) {
      //set a random location
      x = 10 + rand() % (SCREEN_W-20);
      y = 10 + rand() % (SCREEN_H-20);

      //set a random color
      red = rand() % 255;
      green = rand() % 255;
      blue = rand() % 255;
      color = makecol(red,green,blue);

      //draw the pixel
      putpixel(screen, x, y, color); 
    }

To draw lines use `hline` or `vline`:

    void hline(BITMAP *bmp, int x1, int y, int x2, int color)
    void vline(BITMAP *bmp, int x, int y1, int y2, int color)

Draw rectangles with:

    void rect(BITMAP *bmp, int x1, int y1, int x2, int y2, int color)
    void rectfill(BITMAP *bmp, int x1, int y1, int x2, int y2, int color)

Allegro also provides a callback feature, just use `do_line`:

    void do_line(BITMAP *bmp, int x1, y1, x2, y2, int d, void (*proc))

Your callback should have the format:

    void doline_callback(BITMAP *bmp, int x, int y, int d)

Draw circles and ellipses with:

    void circle(BITMAP *bmp, int x, int y, int radius, int color)
    void circlefill(BITMAP *bmp, int x, int y, int radius, int color)
    void ellipse(BITMAP *bmp, int x, int y, int rx, int ry, int color)
    void ellipsefill(BITMAP *bmp, int x, int y, int rx, int ry, int color)

These each have their own callback facility, just prefix each function with `do_`.

The `spline` function draws curves based on four (x,y) input points:

    void spline(BITMAP *bmp, const int points[8], int color)

Triangles can be drawn with three points:

    void triangle(BITMAP *bmp, int x1, y1, x2, y2, x3, y3, int color)

And polygons can be drawn with:

    void polygon(BITMAP *bmp, int vertices, const int *points, int color)

You can use `floodfill` to fill in random regions within your program:

    void floodfill(BITMAP *bmp, int x, int y, int color)

There are three functions for primary text output:

    void textout_ex(BITMAP *bmp, const FONT *f, const char *s,
                    int x, int y, int color, int bg)
    void textout_centre_ex(BITMAP *bmp, const FONT *f, const char *s,
                           int x, int y, int color, int bg)
    void textout_right_ex(BITMAP *bmp, const FONT *f, const char *s,
                          int x, int y, int color, int bg)

Each of these have a `printf`-like equivalent. These take a format string and variable arguments:

    void textprintf_ex(BITMAP *bmp, const FONT *f, int x, int y, 
                       int color, int bg, const char *fmt, ...);
    void textprintf_centre_ex(BITMAP *bmp, const FONT *f, int x, int y, 
                              int color, int bg, const char *fmt, ...);
    void textprintf_right_ex(BITMAP *bmp, const FONT *f, int x, int y, 
                             int color, int bg, const char *fmt, ...);

# Writing Your First Allegro Game

The first example game in this book is "Tank War", a two-player game on a single screen. The tanks
are a series of rectangles:

    void drawtank(int num) {
      int x = tanks[num].x;
      int y = tanks[num].y;
      int dir = tanks[num].dir;

      //draw tank body and turret
      rectfill(screen, x-11, y-11, x+11, y+11, tanks[num].color);
      rectfill(screen, x-6, y-6, x+6, y+6, 7);

      //draw the treads based on orientation
      if (dir == 0 || dir == 2) {
        rectfill(screen, x-16, y-16, x-11, y+16, 8);
        rectfill(screen, x+11, y-16, x+16, y+16, 8); 
      } else if (dir == 1 || dir == 3) {
        rectfill(screen, x-16, y-16, x+16, y-11, 8);
        rectfill(screen, x-16, y+16, x+16, y+11, 8); 
      }

      //draw the turret based on direction
      switch (dir) {
        case 0:
          rectfill(screen, x-1, y, x+1, y-16, 8);
          break;
        case 1:
          rectfill(screen, x, y-1, x+16, y+1, 8);
          break;
        case 2:
          rectfill(screen, x-1, y, x+1, y+16, 8);
          break;
        case 3:
          rectfill(screen, x, y-1, x-16, y+1, 8);
          break;
      } 
    }

    void erasetank(int num) {
      //calculate box to encompass the tank int left = tanks[num].x - 17;
      int top = tanks[num].y - 17;
      int right = tanks[num].x + 17;
      int bottom = tanks[num].y + 17;

      //erase the tank
      rectfill(screen, left, top, right, bottom, 0);
    }

The projectiles from tanks are also small rectangles. `fireweapon` is used to draw the bullet in the
correct direction. It looks at the pixels in front to determine if it's a hit or to keep moving it.

    void fireweapon(int num) {
      int x = tanks[num].x;
      int y = tanks[num].y;

      //ready to fire again?
      if (!bullets[num].alive) {
        bullets[num].alive = 1;
        //fire bullet in direction tank is facing
        switch (tanks[num].dir) {
          //north
          case 0:
            bullets[num].x = x;
            bullets[num].y = y-22;
            bullets[num].xspd = 0;
            bullets[num].yspd = -BULLETSPEED;
            break;
          //east
          case 1:
            bullets[num].x = x+22;
            bullets[num].y = y;
            bullets[num].xspd = BULLETSPEED;
            bullets[num].yspd = 0;
            break;
          //south
          case 2:
            bullets[num].x = x;
            bullets[num].y = y+22;
            bullets[num].xspd = 0;
            bullets[num].yspd = BULLETSPEED;
            break;
          //west
          case 3:
            bullets[num].x = x-22;
            bullets[num].y = y;
            bullets[num].xspd = -BULLETSPEED;
            bullets[num].yspd = 0;
        }
      }
    }

The `updatebullet` actually updates the bullet's rendering on the screen.

    void updatebullet(int num) {
      int x = bullets[num].x;
      int y = bullets[num].y;

      if (bullets[num].alive) {
        //erase bullet
        rect(screen, x-1, y-1, x+1, y+1, 0);

        //move bullet
        bullets[num].x += bullets[num].xspd;
        bullets[num].y += bullets[num].yspd;
        x = bullets[num].x;
        y = bullets[num].y;

        //stay within the screen
        if (x < 5 || x > SCREEN_W-5 || y < 20 || y > SCREEN_H-5) {
          bullets[num].alive = 0;
          return;
        }

        //draw bullet
        x = bullets[num].x;
        y = bullets[num].y;
        rect(screen, x-1, y-1, x+1, y+1, 14);

        //look for a hit
        if (getpixel(screen, bullets[num].x, bullets[num].y)) {
          bullets[num].alive = 0;
          explode(num, x, y);
        }

        //print the bullet position
        textprintf_ex(screen, font, SCREEN_W/2-50, 1, 2, 0,
          "B1 %-3dx%-3d B2 %-3dx%-3d", bullets[0].x, bullets[0].y,
          bullets[1].x, bullets[1].y);
      }
    }

There's an array called `key` that stores values of keys pressed. We'll use this to move the tanks.

    void getinput() {
      //hit ESC to quit if (key[KEY_ESC])
      gameover = 1;
      //WASD / SPACE keys control tank 1
      if (key[KEY_W]) forward(0);
      if (key[KEY_D]) turnright(0);
      if (key[KEY_A]) turnleft(0);
      if (key[KEY_S]) backward(0);
      if (key[KEY_SPACE]) fireweapon(0);

      //arrow / ENTER keys control tank 2
      if (key[KEY_UP]) forward(1);
      if (key[KEY_RIGHT]) turnright(1);
      if (key[KEY_DOWN]) backward(1);
      if (key[KEY_LEFT]) turnleft(1);
      if (key[KEY_ENTER]) fireweapon(1);

      //short delay after keypress
      rest(10);
    }

The `checkpath` function checks to see if the tank's pathway is clear.

    int checkpath(int x1,int y1,int x2,int y2,int x3,int y3) {
      if (getpixel(screen, x1, y1) ||
          getpixel(screen, x2, y2) ||
          getpixel(screen, x3, y3))
        return 1;
      else
        return 0;
    }

The structs that define the tanks and bullets are located in the header.

    struct {
      int x, y;
      int dir, speed;
      int color;
      int score;
    } tanks[2];

    struct {
      int x, y;
      int alive;
      int xspd, yspd;
    } bullets[2];

# Getting Input from the Player

To start detecting keyboard input, you'll need to initialize Allegro:

    int install_keyboard();

The `allegro_exit` function will handle uninitializing it, but if you need to do so before the exit
is called use:

    void remove_keyboard();

Allegro keeps track of keys pressed in a global variable:

    extern volatile char key[KEY_MAX];

Check Allegro's `keyboard.h` for constants of each key on the keyboard. A few examples are:

* `KEY_UP`
* `KEY_DOWN`
* `KEY_LEFT`
* `KEY_RIGHT`
* `KEY_SPACE`
* `KEY_LSHIFT`

The typical game loop is:

    while (!key[KEY_ESC]) {
      // do some stuff
    }

Besides using the `key` variable, you can also use buffered keyboard input which reads input via
ASCII code.

    int readkey();                // returns next ASCII code or waits
    int ureadkey(int *scancode);  // returns next Unicode key or waits

The ASCII code is actually a two-byte integer value, the low byte is the ASCII code that changes
depending on modifier keys and the high byte is the scan code regardless of modifier keys.

For demos, you can simulate key presses using:

    void simulate_keypress(int key);
    void simulate_ukeypress(int key, int scancode);
    void clear_keybuf();

To detect mouse input, you'll also need to initialize it:

    int install_mouse();
    void remove_mouse(); // optional, only if you want to disable it

The current mouse position is available via:

    extern volatile int mouse_x;
    extern volatile int mouse_y;
    extern volatile int mouse_z;  // wheel
    extern volatile int mouse_b;  // mouse button

`mouse_b` is just packed bits. Use bit masks to detect which button was pressed:

    mouse_b & 1; // left button
    mouse_b & 2; // right button
    mouse_b & 4; // center button

You can personalize the mouse cursor with:

    void set_mouse_sprite(BITMAP *sprite);
    void set_mouse_sprite_focus(int x, int y); // default is top-left
    void show_mouse(BITMAP *bmp);  // tell mouse where to be drawn
    void scare_mouse();
    void unscare_mouse();
    void position_mouse(int x, int y);
    void set_mouse_range(int x1, int y1, int x2, int y2);
    void set_mouse_speed(int xspeed, int yspeed);

# Mastering the Audible Realm

The first thing to do is detect digital sound drivers. This function returns zero if none are
available or the maximum number of voices a driver can provide:

    int detect_digi_driver(int driver_id)

You then need to reserve digital and Midi sound drivers. If you reserve too many, the quality will
drop. Pass `-1` to restore voice setting to default:

    void reserve_voices(int digi_voices, int midi_voices)

You can control the volume per voice. Pass `-1` to reset, use `0` for maximum volume without
distortion. Use `1` when panning, each time you increase the parameter by one the sound of each
voice is halved.

    void set_volume_per_voice(int scale)

After configuring the sound system, Allegro can initialize it with:

    int install_sound(int digi, int midi, const char *cfg_path)

For `digi` the default is `DIGI_AUTODETECT`, for `midi` the default is `MIDI_AUTODETECT`.

If you ever need to disable sound use:

    void remove_sound()

This gets called by default when Allegro exits. The `set_volume` function lets you set volume from 0
to 255. Use `-1` for one parameter to leave it unchanged:

    void set_volume(int digi_volume, int midi_volume)

To load a sample file in `WAV` or `VOC` format and play it:

    SAMPLE *load_sample(const char *filename)
    int play_sample(const SAMPLE *spl, int vol, int pan, int freq, int loop)
    void stop_sample(const SAMPLE *spl)
    void adjust_sample(const SAMPLE *spl, int vol, int pan, int freq, int loop)
    SAMPLE *create_sample(int bits, int stereo, int freq, int len)
    void destroy_sample(SAMPLE *spl)

The same thing for voices:

    int allocate_voice(const SAMPLE *spl)
    void deallocate_voice(int voice)
    void reallocate_voice(int voice, const SAMPLE *spl)
    void release_voice(int voice)
    void voice_start(int voice)
    void voice_stop(int voice)

To adjust the loop status:

    void voice_set_playmod(int voice, int playmode)

The available playmodes are:

* `PLAYMODE_PLAY`
* `PLAYMODE_LOOP`
* `PLAYMODE_FORWARD`
* `PLAYMODE_BACKWARD`
* `PLAYMODE_BIDIR` reverses direction on each finish

You can also control the voice volume, pitch, and panning:

    int voice_get_volume(int voice)
    void voice_set_volume(int voice, int volume)
    void voice_ramp_volume(int voice, int time, int endvol)
    void voice_stop_volumeramp(int voice)
    void voice_set_frequency(int voice, int frequency)
    int voice_get_frequency(int voice)
    void voice_sweep_frequency(int voice, int time, int endfreq)
    void voice_stop_frequency_sweep(int voice)
    int voice_get_pan(int voice)
    void voice_set_pan(int voice, int pan)
    void voice_sweep_pan(int voice, int time, int endpan)
    void voice_stop_pan_sweep(int voice)

MIDI music uses different functions. It uses the struct `midi`:

    int get_midi_length(MIDI *midi)
    int play_midi(MIDI *MIDI, int loop)
    void midi_pause()
    void midi_resume()

# Basic Bitmap Handling and Blitting

A sprite is a animated, moving object that usually interacts with the player - or it could be the
player. Usually you draw it using a graphic editing tool like Photoshop, save it in a file, then
load that image with Allegro.

    BITMAP *tank = create_bitmap(32, 32);
    clear_bitmap(tank);
    putpixel(tank, 16, 16, 15);
    blit(tank, screen, 0, 0, 0, 0, 32, 32);

`create_bitmap` allocates memory for the bitmap of `32x32` size. `clear_bitmap` actually clears the
memory space. The `putpixel` function was used previously with `screen` to draw directly to the
screen. In this case, we want to draw on the new bitmap instead. **Blit** stands for bit-block
transfer (copying memory from one location to another).

Here's the bitmap structure:

    typedef struct BITMAP {
      int w, h;              // width and height
      int clip;              // flag if clipping is turned on
      int cl, cr, ct, cb;    // clip left, right, top, bottom values
      GFX_VTABLE *vtable;    // drawing functions
      void *write_bank;
      void *read_bank;
      void *dat;             // memory for bitmap
      unsigned long id;      // for identifying sub bitmaps
      void *extra;           // points to struct with more info
      int x_ofs;             // horizontal offset
      int y_ofs;             // vertical offset
      int seg;               // bitmap segment
      ZERO_SIZE_ARRAY(unsigned char *, line);
    } BITMAP;

If your artwork is in a certain color depth, you may want to call `set_color_depth` after
`set_gfx_mode` in the initialization code. Or you can use `create_bitmap_ex` whose first parameter
is the color depth. You can get the color depth with `bitmap_clor_depth(BITMAP *bmp)`. There's also
an alternative to `clear_bitmap`, `clear_to_color(BITMAP *bitmap, int color)`.

You can create sub-bitmaps that shares memory with a parent bitmap. Any changes to the sub-bitmap
will be visible on the parent (and the reverse is true):

    BITMAP *create_sub_bitmap(BITMAP *parent, int x, int y, int w, int h);

Anything that goes beyond the boundaries of the sub bitmap will not be drawn. This is especially
useful for the `screen` for windowing effects like scrolling backgrounds.

When you're done with a bitmap, you want to free its memory with:

    void destroy_bitmap(BITMAP *bitmap);

Some functions to retrieve information for bitmaps:

    int bitmap_mask_color(BITMAP *bmp);
    int is_same_bitmap(BITMAP *bmp1, BITMAP *bmp2);
    int is_linear_bitmap(BITMAP *bmp);  // linear memory
    int is_planar_bitmap(BITMAP *bmp);
    int is_memory_bitmap(BITMAP *bmp);
    int is_screen_bitmap(BITMAP *bmp);
    int is_video_bitmap(BITMAP *bmp);

Bitmaps are actually automatically locked/unlocked every time you draw on it. It can be a
bottleneck. Instead, you can do it manually:

    void acquire_bitmap(BITMAP *bmp);
    void release_bitmap(BITMAP *bmp);
    void acquire_screen();
    void release_screen();

You can clip a bitmap so it never draws beyond a boundary:

    void set_clip(BITMAP *bitmap, int x1, int y1, int x2, int y2);

Turn it off by giving all zeros for coordinates. By default, a bitmap is clipped to its created
size.

You can load a bitmap from disk after saving it as an optimization:

    int save_bitmap(const char *filename, BITMAP *bmp, const RGB *pal);
    BITMAP *load_bitmap(const char *filename, RGB *pal);

To save a screenshot to disk:

    BITMAP *bmp;
    bmp = create_sub_bitmap(screen, 0, 0, SCREEN_W, SCREEN_H);
    save_bitmap("screenshot.pcx", bmp, NULL);
    destroy_bitmap(bmp);

Here's the prototype for the blit function:

    void blit(BITMAP *source, BITMAP *dest, int source_x, int source_y,
      int dest_x, int dest_y, int width, int height);

There are also more specialized versions of blitting:

* `stretch_blit` for scaling
* `masked_blit` for copying only solid pixels
* `masked_stretch_blit` for both

# Introduction to Sprite Programming

Game sprites came from the mythical sprite - a tiny, flying creature like a classical fairy but more
mischievous.

The first function you'll use is `draw_sprite` that draws the sprite image using transparency.
Allegro uses the color pink `(255, 0, 255)` to define transparency in an image:

    void draw_sprite(BITMAP *bmp, BITMAP *sprite, int x, int y)

This draws the entire sprite, since there's no source coordinates. A better way to do this is to
store all frames into a single image. Also, you may want to use `set_gfx_mode` to set a 16-bit color
mode instead of the default 8-bit so transparency works correctly.

To draw transformed sprites:

    void stretch_sprite(BITMAP *bmp,BITMAP *sprite,int x,int y,int w,int h)
    void draw_sprite_v_flip(BITMAP *bmp, BITMAP *sprite, int x, int y)
    void draw_sprite_h_flip(BITMAP *bmp, BITMAP *sprite, int x, int y)
    void draw_sprite_vh_flip(BITMAP *bmp, BITMAP *sprite, int x, int y)
    void rotate_sprite(BITMAP *bmp, BITMAP *sprite, int x, int y, fixed angle)
    void pivot_sprite(BITMAP *bmp, BITMAP *sprite, int x, int y,
      int cx, int cy, fixed angle)

Drawing a semi-transparent sprite requires setting the alpha blender:

    void set_alpha_blender()
    void draw_trans_sprite(BITMAP *bmp, BITMAP *sprite, int x, int y)

# Sprite Animation

Allegro 4 doesn't actually have built-in functions to handle sprite sheets or sprite animation. It
has low-level sprite routines from which you can build your own sprite handler. In this chapter,
Harbour shows us how to build one.

Here's a program that animates a cat given six image files:

    #include <stdlib.h>
    #include <stdio.h>
    #include <allegro.h> 

    #define WHITE makecol(255,255,255)
    #define BLACK makecol(0,0,0)

    BITMAP *kitty[7];
    char s[20];
    int curframe=0, framedelay=5, framecount=0;
    int x=100, y=200, n;

    int main(void) {
      // initialize the program
      allegro_init();
      install_keyboard();
      install_timer();
      set_color_depth(16);
      set_gfx_mode(GFX_AUTODETECT_WINDOWED, 640, 480, 0, 0);
      textout_ex(screen, font, "AnimSprite Program (ESC to quit)",
        0, 0, WHITE, 0);
      
      // load the animated sprite
      for (n=0; n<6; n++) {
        sprintf(s,"cat%d.bmp",n+1);
        kitty[n] = load_bitmap(s, NULL);
      }

      // main loop
      while (!keypressed()) {
        // erase the sprite
        rectfill(screen, x, y, x+kitty[0]->w, y+kitty[0]->h, BLACK);

        // update the position
        x += 5;
        if (x > SCREEN_W - kitty[0]->w) x = 0;
        
        // update the frame
        if (framecount++ > framedelay) {
          framecount = 0;
          curframe++;
          if (curframe > 5) curframe = 0;
        }

        acquire_screen();
        draw_sprite(screen, kitty[curframe], x, y);
        release_screen();
        rest(10);
      }

      allegro_exit();
      return 0;
    }
    END_OF_MAIN()

`framedelay` and `framewcount` work together to create a smooth animation. You can't just switch the
bitmap on every loop, otherwise it'd be too fast of an animation.

Next, Harbour walks us through creating a sprite handler starting with the `SPRITE` struct and
`updatesprite` function:

    typedef struct SPRITE {
      int x,y;                          // sprite position
      int width,height;                 // size of sprite
      int xspeed,yspeed;                // how many pixels to move
      int xdelay,ydelay;
      int xcount,ycount;
      int curframe,maxframe,animdir;
      int framecount,framedelay;        // animation variables
    } SPRITE;

    void updatesprite(SPRITE *spr) {
      //update x position
      if (++spr->xcount > spr->xdelay) {
        spr->xcount = 0;
        spr->x += spr->xspeed;
      }
      //update y position
      if (++spr->ycount > spr->ydelay) {
        spr->ycount = 0;
        spr->y += spr->yspeed;
      }
      //update frame based on animdir
      if (++spr->framecount > spr->framedelay) {
        spr->framecount = 0;
        if (spr->animdir == -1) {
          if (--spr->curframe < 0)
            spr->curframe = spr->maxframe;
        } else if (spr->animdir == 1) {
          if (++spr->curframe > spr->maxframe)
            spr->curframe = 0;
        }
      }
    }

Now, we need to learn how to store all frames into a single image. Here's the sprite tile algorithm:

    int x = startx + (frame % columns) * width;
    int y = starty + (frame / columns) * height;

Usually `startx` and `starty` are zero. If you decide to cache all animations into a single file,
you can use `startx` and `starty` to initialize the starting positions. Here's the function that can
grab a single frame out of an image:

    BITMAP *grabframe(BITMAP *source, int width, int height,
      int startx, int starty, int columns, int frame) {
      BITMAP *temp = create_bitmap(width,height);
      int x = startx + (frame % columns) * width;
      int y = starty + (frame / columns) * height;
      blit(source,temp,x,y,0,0,width,height);
      return temp;
    }

Note that it's up to the caller to destroy the bitmap after it's no longer needed.

# Advanced Sprite Programming

Allegro can use run-length encoding or RLE to compress sprite images. These sprites cannot be
flipped, rotated, or copied into.

    RLE_SPRITE *get_rle_sprite(BITMAP *bitmap);
    void destroy_rle_sprite(RLE_SPRITE *sprite);
    void draw_rle_sprite(BITMAP *bmp, const RLE_SPRITE *sprite, int x, int y);
    void draw_trans_rle_sprite(BITMAP *bmp, const RLE_SPRITE *sprite,
      int x, int y);
    void draw_lit_rle_sprite(BITMAP *bmp, const RLE_SPRITE *sprite,
      int x, int y, int color);

Compiled sprites actually store the machine code instructions to draw a specific image onto a
bitmap, significantly improving speed. They take up more memory than standard or compressed sprites.

    COMPILED_SPRITE *get_compiled_sprite(BITMAP *bitmap, int planar);
    void destroy_compiled_sprite(COMPILED_SPRITE *sprite);
    void draw_compiled_sprite(BITMAP *bmp, const COMPILED_SPRITE *sprite,
      int x, int y);

The easiest and most efficient collision detection is to compare bounding rectangles of two objects.
Keep these boundaries lean - they may even be smaller than the actual image to improve accuracy.

    int inside(int x, int y, int left, int top, int right, int bottom) {
      return x > left && x < right && y > top && y < bottom;
    }

Harbour then creates a function which calls `inside` four times and takes two sprites as input.
There's an alternative which uses a `border` parameter to reduce the bounding box by a certain
amount.

# Programming the Perfect Game Loop

So far we've been using `rest` to delay our game. Allegro has much better timing features. Like
other features, it needs to be activated:

    int install_timer();
    void remove_timer(); // optional, happens at allegro_exit

We've use `rest` before:

    void rest(long milliseconds);
    void rest_callback(long milliseconds, void (*callback)());

Interrupt handlers are used to run functions at specific intervals.

    int install_int(void (*proc)(), int milliseconds)
    void remove_int(void (*proc)())  // optional, happens at allegro_exit

Harbour recommends you use interrupt routines to set flags instead of any work that requires real
processing since timing is crucial.

# Programming Tile-Based Scrolling Backgrounds

Here's an example program that uses the arrow keys to scroll around the game world:

    #include <stdlib.h>
    #include "allegro.h"

    //define some convenient constants
    #define MODE GFX_AUTODETECT_FULLSCREEN
    #define WIDTH 640
    #define HEIGHT 480
    #define STEP 8
    
    BITMAP *scroll; //virtual buffer variable
    int x=0, y=0; //position variables 
    int main(void) {
      allegro_init();
      install_keyboard();
      install_timer();
      set_color_depth(16);
      set_gfx_mode(MODE, WIDTH, HEIGHT, 0, 0);

      //load the large bitmap image from disk
      scroll = load_bitmap("bigbg.bmp", NULL);

      while (!key[KEY_ESC]) {
        if (key[KEY_RIGHT]) {
          x += STEP;
          if (x > scroll->w - WIDTH) x = scroll->w - WIDTH;
        }
        if (key[KEY_LEFT]) {
          x -= STEP;
          if (x < 0) x = 0;
        }
        if (key[KEY_DOWN]) {
          y += STEP;
          if (y > scroll->h - HEIGHT) y = scroll->h - HEIGHT;
        }
        if (key[KEY_UP]) {
          y -= STEP;
          if (y < 0) y = 0;
        }

        //draw the scroll window portion of the virtual buffer
        blit(scroll, screen, x, y, 0, 0, WIDTH-1, HEIGHT-1);
        //slow it down
        rest(20);
      }
      destroy_bitmap(scroll);
      allegro_exit();
      return 0;
    }
    END_OF_MAIN()

**Tiling** is a popular technique to create backgrounds made up of tiles. It takes up little memory
compared to a full bit-mapped background. Here's an example that draws random tiles:

    void drawframe(BITMAP *source, BITMAP *dest,
        int x, int y, int width, int height,
        int startx, int starty, int columns, int frame) {
      int framex = startx + (frame % columns) * width;
      int framey = starty + (frame / columns) * height;
      masked_blit(source,dest,framex,framey,x,y,width,height);
    }
    // ...
    scroll = create_bitmap(1600, 1200);
    tiles = load_bitmap("tiles.bmp", NULL);
    for (tiley=0; tiley < scroll->h; tiley+=TILEH) {
      for (tilex=0; tilex < scroll->w; tilex+=TILEW) {
        n = rand() % TILES;
        drawframe(tiles, scroll, tilex, tiley, TILEW+1, TILEH+1,
          0, 0, COLS, n);
      } 
    }

You can save a game level using an array to represent the world. For example:

    int map[MAPW*MAPH] = {
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
      0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,
      0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    };

In this case, `2` represents grass and `0` represents stone.

# Using Datafiles to Store Game Resources

Allegro has support for datafiles to store game resources with encryption and compression. They're
similar to ZIP archive files in that they can contain multiple files of different types. It uses the
LZSS compression algorithm.

    typedef struct DATAFILE {
      void *dat;
      int type;
      long size;
      void *prop;
    } DATAFILE;

Here's example usage:

    DATAFILE *data = load_datafile("game.dat");
    draw_sprite(screen, data[PLAYER_SPRITE].dat, x, y);

Allegro comes with a `dat` script that can be used to manually compress your data into a datafile.

    dat -a -t BMP -bpp 16 test.dat back.bmp
    dat -l test.dat

The `load_datafile` loads a datafile into memory and returns a pointer. If encrypted, use the
`packfile_password` function to set the key. Use the `unload_datafile` function to free memory. You
can also use `load_datafile_object` to load a specific object instead of an array. This has the
equivalent `unload_datafile_object`.
# Introduction to Artificial Intelligence

There are several sub-fields within AI. This section is a brief introduction.

**Expert systems** solve problems usually solved by specialized humans. For example, it could ask
you a set of true/false questions to determine an answer. It uses a knowledge tree to determine that
answer.

**Fuzzy logic** expands on that by providing values in between true and false. The return value is
usually also fuzzy.

**Genetic algorithms** use something similar to real-life heredity in biology. The steps are:

1. pick population and set initial values
2. order values into a flat bit vector
3. calculate fitness of each member of population
4. keep only two with highest fitness
5. mate two to form a child

**Neural networks** imitate the workings of a brain.

**Deterministic algorithms** is a game technique that uses predetermined behaviors of objects in
relation to the universe problem. For example, you can randomly move an object left or right. Or
make a guard run towards an intruder if the intruder is within vision.

Harbour mentions **finite state machines** as a great pattern to use within your game
implementations.