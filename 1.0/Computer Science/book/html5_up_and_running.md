# HTML5 Up and Running

[HTML5 Up and Running](http://oreilly.com/catalog/9780596806033) by Mark Pilgrim is an informative
guide to select features from the HTML5 Specification. It's available at
@link(http://diveintohtml5.org/)

# History

Every element, attribute, feature of HTML was created by someone who decided how it should work and
wrote it all down. For example the `<img>` element:

1. Before there was a W3C, Marc Andreesen emailed his proposal for an `<img>` element with a "src"
   attribute to a mailing list.
2. People debated on it, came up with alternatives, and various implementations of it were done for
   different browsers.
3. Marc ended up implementing his original proposal in Mosaic.
4. And now we have an `<img>` element that became an HTML standard.

It's really as simple as this: we have an `<img>` element because Marc Andreesen shipped on in his
browser, and shipping code wins.

HTML has been constantly evolving. It's always been developed between browser makers, authors,
standards "wonks", and other people who just wanted to get involved.

In 1997, the W3C published the HTML 4.0 specification. They then published the XML 1.0 specification
and decided to reformulate HTML into XML instead of trying to extend HTML. That gave birth to XHTML
1.0 and XHTML 1.1.

XHTML has "draconian error handling". If served with the correct MIME type,
**application/xhtml+xml** browsers would complete break pages when there were any minor errors. So
most people ended up using the **text/html** MIME type, which was a loophole. It allowed authors to
use an XHTML syntax but keep serving it in a forgiving environment.

In 2004, the W3C branched off the What Working Group. What WG wanted to work on an evolution of the
existing HTML 4 standard to include features for modern web application developers:

* backward compatibility based on existing tech: HTML, CSS, DOM, and JavaScript
* well defined error handling (as opposed to the draconian error handling or inconsistent error
  handling implementations between browsers)
* users should not be exposed to author errors
* practical useful features
* embrace scripting
* avoidance of device specific profiling
* web forms

WHAT Working Group = **Web Hypertext Applications Technology Working Group** They called their
specification **Web Applications 1.0**

For years the W3C and What WG ignored each other, working on XHTML 2.0 and Web Applications 1.0
respectively. By 2006, Web Applications 1.0 was picking up more momentum while XHTML 2 remained
mostly unimplemented by browsers. In October 2006, Tim Berners Lee announced that the What WG and
W3C would begin working together.

Web Applications 1.0 was renamed to **HTML5**. In October 2009, The W3C shut down the XHTML2 Working
Group.

"The ones that win are the ones that ship." - Mark Pilgrim

# Feature Detection

You can start using HTML5 now, it's a collection of individual features. You can do this using
feature detection. If the current browser has a certain feature - use it, otherwise fallback.

Detection techniques fall in four categories:

1. Check for property on global object (ie. window or navigator)
2. Create an element, then check if that element has a certain property
3. Create an element, check if a method exists, call that method, and check the return value
4. Create an element, set a property and check if the value is retained

[Modenizr](http://www.modernizr.com/) is an HTML5 detection library.

# Updated and New Elements

## Doctype, Html, and Head

The new **doctype** for HTML5 is:

    <!DOCTYPE html>

The root element just needs a **lang** attribute set:

    <html lang="en">

Inside the **head** element, you'll need to specify the content type and character encoding of your
document. You may also specify any stylesheets, alternate formats, and general meta data.

    <head>
      <meta charset="utf-8" />  
      <link rel="stylesheet" href="/path/to/styles.css" />
      <link rel="alternate" type="application/atom+xml" href="/feed.xml" />
    </head>

Many of the mandatory HTML4 attributes were dropped in favor of defaults. IE, you no longer have to
specify the type="text/css" for stylesheets.

## New Semantic Elements

From the specification available at
http://www.whatwg.org/specs/web-apps/current-work/multipage/sections.html.

New elements include:

    +-----------+-----------------------------------------------------------------+
    | <section> | Represents a generic section of a document, provides thematic   |
    |           | grouping, typically with a header.                              |
    +-----------+-----------------------------------------------------------------+
    | <nav>     | Represents a section that links to other pages or parts.        |
    |           | Only major navigations are appropriate for <nav>, for example a |
    |           | footer with many links is not appropriate.                      |
    +-----------+-----------------------------------------------------------------+
    | <article> | A self-contained composition in a document, which can be        |
    |           | independently distributed.  Eg: newspaper article, blog entry,  |
    |           | user comment, or interactive widget                             |
    +-----------+-----------------------------------------------------------------+
    | <aside>   | Sections which are only tangentially related to the main        |
    |           | content of the page.  Eg: sidebars, ads, or featured quotes.    |
    +-----------+-----------------------------------------------------------------+
    | <hgroup>  | The heading of a section which groups h1-h6 elements when       |
    |           | headings have multiple levels.  Eg: subheading or taglines.     |
    +-----------+-----------------------------------------------------------------+
    | <header>  | Introductory or navigational aids.  Usually contains h1-h6 and  |
    |           | hgroup elements.  May also contain table of contents, search    |
    |           | form, or relevant logos.                                        |
    +-----------+-----------------------------------------------------------------+
    | <footer>  | Typically contains information about its ancestor such as the   |
    |           | author, links to related documents, or copyright.               |
    +-----------+-----------------------------------------------------------------+
    | <time>    | Either a time on a 24-hour clock or precise date.               |
    +-----------+-----------------------------------------------------------------+
    | <mark>    | Run of text in one document highlighted for reference.          |
    +-----------+-----------------------------------------------------------------+

Not all browsers support these elements yet. Two important questions to ask when a browser finds an
**unknown element**:

- How should this element be styled? - What should the element's DOM look like?

For non-IE browsers, you can style unknown elements:

    article { border: 1px solid red; } /* Won't be applied in IE < 9 */

Unfortunately, if IE doesn't recognize the element name, it will insert the element into the DOM as
an empty node with no children. Any actual children will become siblings.

To solve both problems in IE, just create a dummy element of the same type before you use it in the
page:

    <head>
      <!-- Now articles will be recognized! -->
      <script>document.createElement("article");</script>
    </head>

Here is the [HTML5 enabling script](http://html5shiv.googlecode.com/svn/trunk/html5.js) for IE by
Remy Sharp:
  
    <!--[if lt IE 9]> <script>
      var e = ("abbr,article,aside,audio,canvas,datalist,details," + 
               "figure,footer,header,hgroup,mark,menu,meter,nav,output," + 
               "progress,section,time,video").split(',');
      for (var i = 0; i < e.length; i++) {
        document.createElement(e[i]);
      } 
    </script> <![endif]-->

# Canvas

The `<canvas>` element is a "resolution-dependent bitmap canvas which can be used for rendering
graphs, game graphics, or other visual images on the fly."

    <canvas id="acanvas" width="300" height="225"></canvas>
    <script>
      var a_canvas = document.getElementById("acanvas");
      a_canvas.getContext("2d");  /* only supported context right now */
      a_canvas.fillRect(50, 25, 150, 100)
    </script>

Canvas support for IE7+ is available via the **excanvas library**. To detect support for canvas:

    !!document.createElement("canvas").getContext;

A sample of the API for drawing shapes:

- fillStyle property, which can be a CSS color or pattern or gradient - fillRect(x, y, width,
height) draws a rectangle - strokeStyle property is just like fillStyle - strokeRect(x, y, width,
height) draws a rectangle w/ current strokeStyle - clearRect(x, y, width, height) clears the pixels
in specified rectangle

To reset the canvas, just set its width:

    a_canvas.width = a_canvas.width;   // works even if it's the same width

Lines are drawn using **paths**:

- moveTo(x, y) moves your pencil to this coordinate - lineTo(x, y) draws a line to specified ending
point - stroke() will actually do the drawing (like finalizing in ink) this also uses the current
strokeStyle of the context

Examples:

    context.beginPath();
    context.moveTo(0, 40);
    context.lineTo(240, 40);
    context.strokeStyle = "#000";
    context.stroke();

Text may also be drawn onto the canvas:

- font property is similar to any CSS font rule, including: font style, variant, weight, size,
line-height, and font family. - textAlign property controls the alignment. Possible values are:
start, end, left, right, and center. - textBaseline controls where the text is drawn relative to the
starting point. Values are: top, hanging, middle, alphabetic, ideographic, and bottom.

Example:

    context.font = "bold 12px sans-serif";
    context.fillText("Lorem Ipsum", 248, 43);

Gradients can be created via:

- createLinearGradient(x0, y0, x1, y1) - createRadialGradient(x0, y0, r0, x1, y1, r1)

Example:

    var gradient = context.createLinearGradient(0, 0, 300, 0);
    gradient.addColorStop(0, "black");
    gradient.addColorStop(1, "white");
    context.fillStyle = gradient;
    context.fillRect(0, 0, 300, 225);

To draw an image onto the canvas:

- drawImage(image, dx, dy) where dx/dy make up the upper-left corner - drawImage(image, dx, dy, dw,
dh) scales it to dw/dh - drawImage(image, sx, sy, sw, sh, dx, dy, dw, dh) to clip and scale

Example:

    context.drawImage(document.getElementById("id-of-img-element"), 0, 0);

# Video

HTML5 defines a standard way to embed video into a web page using the `<video>` element.

## Feature Detection

To detect whether the browser supports HTML5 video or not:

    !!document.createElement("video").canPlayType;

To detect whether or not it can play a certain format:

    var v = document.createElement("video");
    v.canPlayType('video/mp4; codecs="avc1.42E01E, mp4a.40.2"');

This will return one of 3 values:

- "probably" if the browser is confident it can play it - "maybe" if the browser thinks it can play
it - "" if the browser is certain it cannot play it

## Video Containers

"AVI" and "MP4" are just container formats like how a ZIP file can contain any sort of file within
it. Container formats define how to store things in them and what kind of data is stored. Some of
the most popular formats are:

- MPEG-4 (mp4, m4v) - Flash Video (flv) - Ogg (ogv)

## Video Codecs
When you watch a video, your player is:

- interpreting the container format to find out which video/audio tracks are available and how they
are stored - decoding the video stream to display images onto the screen - decoding the audio stream
to send sound to speakers

**Codec** is a combination of "coder" and "decoder". It's the algorithm used to encode video
streams. The video player decodes a video stream to display a series of images, aka **frames** to
the screen.

Some popular video codecs are:

- H.264 (aka MPEG-4 part 10) - Theora - VP8

Some popular audio codecs are:

- MPEG-1 Audo Layer (aka mp3) - Advanced Audio Coding (AAC) - Vorbis

For cross browser reasons, you'll have to encode your video in more than one format and probably
provide a fallback mechanism for IE < 9.

- FF &gt;3.5 and Opera &gt;10.5 supports Theora video and Vorbis audio in an Ogg container - Chrome
&gt;3.0 supports supports Theora/Vorbis in an Ogg container. Also supports H.264 video and AAC audio
in an MP4 container. - Safari support anything QuickTime supports. Out of the box this does not
include Theora/Vorbis in Ogg. It does support H.264 and AAC in an MP4 container. - Mobile devices
like iPhone and Android phones support H.264/AAC in MP4. - Flash supports H.264/AAC in an MP4
container also. - IE9 will support H.264 and AAC in MP4. - IE &lt;9 have no support for HTML5 video,
you'll need to fallback to flash.

To encode ogg video, use the **Firefogg** Firefox plugin. To encode H.264, use the open source
**HandBrake** application.

## The Markup

The markup is similar to the `<img>` element:

    <video src="videofile.mp4" width="320" height="240"></video>

Your browser will center the video inside the box. It won't be scaled out of proportion.

The `<video>` element does not expose any player controls. You can do that yourself using its API:
play(), pause(), and currentTime property. There's also volume/muted properties. If you don't want
to build your own UI, you can use the browser's default with the **controls** property:

    <video src="videofile.mp4" width="320" height="240" controls></vide>

There's also the **preload** property which will begin downloading the video file and the
**autoplay** property.

A `<video>` element may have <source> children. This is useful to have more than one encoding to
support multiple browsers:

    <video width="320" height="240" controls> 
      <source src="pr6.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'> 
      <source src="pr6.webm" type='video/webm; codecs="vp8, vorbis"'> 
      <source src="pr6.ogv" type='video/ogg; codecs="theora, vorbis"'>
    </video>

The **type** attribute is important so the browser won't have to download an entire video file just
to check to see if it can play it.

Important: VIDEO FILES MUST BE SERVED WITH THE PROPER MIME TYPE!

For IE, you'll need to fallback using Flash. A recommended library to use is **FlowPlayer**.

# Geolocation

Geolocation lets you figure out where in the world the user is. Privacy is a strong concern and user
agents must not send location information to websites without the express permission of the user.

## Feature Detection

If your browser supports geolocation, there will be a geolocation property on the global navigator
object:

    !!navigator.geolocation

## Usage

The first time you ask for a user's location, the end user will decide whether or not to disclose
it. The end user gets to know which website wants to know the location, can choose to share or not
share it, and can tell the browser to remember the choice.

    navigator.geolocation.getCurrentPosition(function(position) {
      var latitute = position.coords.latitude;
      var longitude = position.coords.longitude;
      var timestamp = position.timestamp;
    });

Properties are:

- coords.latitutde (double, decimal degrees) - coords.longitude (double, decimal degrees) -
coords.altitude (double or null) - coords.accuracy (doubles in meters) - coords.altitudeAccuracy
(double in meters) - coords.heading (degrees clockwise from true north, double or null) -
coords.speed (double or null, meters/second) - timestamp (DOMTimeStamp, like Date() object)

You may also include error handling:

    navigator.geolocation.getCurrentPosition(fn_callback, error_callback);
    function error_callback(code, message) {
      /* code is a short, enumerated value */
      /* message is a string, not intended for end users */
    }

Possible error codes are:

- 1 = PERMISSION\_DENIED - 2 = POSITION\_UNAVAILABLE - 3 = TIMEOUT - 4 = UNKNOWN\_ERROR

getCurrentPosition has a third optional parameter, a PositionOptions object with three possible
properties:

- enableHighAccuracy (boolean) - timeout (long in milliseconds) - maximumAge (long in milliseconds)

## IE Support

IE does not support the geolocation API, but you can fallback onto the Gears library. **geo.js** is
an abstraction above the standards HTML5 geolocation and Gears.

# Local Storage

## Goal of Local Storage

What we want is a lot of local storage space, on the client, that persists beyond a page refresh,
and is not transmitted to the server.

Cookies were invented in the early days but it has several downsides:

- included in every HTTP request (waste of bandwidth) - could be sent unencrypted - limited to about
4KB of data

## History

IE invented "userData" to store up to 64KB of data per domain. Adobe invented the "Local Shared
Objects, or LSOs". It became known as the Flash cookie.

Brad Neuberg developed "AJAX Massive Storage System" or AMASS to interface with JavaScript. It was
later re-written into the Dojo Toolkit under dojox.storage.

In 2007, Google launched Google Gears which was an open source browser plugin aimed at providing
additional capabilities in browsers. It embedded a local SQL database and provided an API for
accessing and storing data.

The dojo team hacked away at dojox.storage to provide a unified interface to all of these plugins
and APIs.

HTML5 set out to provide a standardized API, implemented natively and constantly in multiple
browsers without relying on third-party plugins.

HTML5 Storage is actually a specification named **Web Storage**. It was once part of the HTML5
specification but was split out into its own specification due to political reasons. Certain
browsers also call it "Local Storage" or "DOM Storage".

HTML5 Storage is a way for web pages to store named key/value pairs on the client web browser.

## Feature Detection

HTML5 storage support:

- IE 8+ - FF 3.5+ - Safari 4.0+ - Chrome 4.0+ - Opera 10.5+ - iPhone 2.0+ - Android 2.0+

To detect the feature:

    ("localStorage" in window) && window["localStorage"] != null;

## Usage

Key/values are strings. If you store anything that is not a string, it will be converted to one and
you'll need to coerce that value when retrieving it.

    var foo = localStorage.getItem("bar"); /* returns null if empty */
    // ...
    localStorage.setItem("bar", foo);

Or you can use the shorter square-bracket syntax:

    var foo = localStorage["bar"];
    // ...
    localStorage["bar"] = foo;

There are also methods to remove/clear:

    localStorage.removeItem("bar");
    localStorage.clear();

And a length property and key method to get the name of a key:

    localStorage.length;
    localStorage.key(0); /* key name, useful for iterating through all keys */

The **storage** event is fired on the window object whenever setItem(), removeItem(), or clear() is
called and actually changes something. Example:

    if (window.addEventListener) {
      window.addEventListener("storage", handle_storage, false);
    } else {
      window.attachEvent("onstorage", handle_storage);
    }

    function handle_storage(e) { /* StorageEvent object */
      if (!e) { e = window.event; }
      e.key; /* String, key that was added, removed, or modified */
      e.oldValue; /* previous value or null */
      e.newValue; /* new value or null if item was removed */
      e.url; /* String, page that called the method */
    }

## Limitations

The specification suggested (should vs must) that browsers implement a 5MB limit of storage space
per origin. Although just a suggestion, most browsers implemented local storage with a 5MB limit. If
you exceed the quota, a QUOTA\_EXCEEDED\_ERR exception will be thrown.

## Beyond Key/Value

Google Gears influenced the creation of the **Web SQL Database** spec. It provides a thin wrapper
around a SQL database.

Another API that's popping up is the "Indexed Database API" aka "IndexedDB". This is more of a
client-side ORM. At the moment it's currently not implemented in any major browsers ... but maybe
one day it will be.

# Offline Web Apps

## What is it?

An offline web application is just a list of URLs pointing to HTML, CSS, JavaScript files, images,
or any other resources that may be present. The list is called a **manifest file** which is just a
text file.

Any web browsers which implement HTML5 offline applications will read this list and download the
resources locally. It will keep the local copies up to date as they change.

There's a flag in the DOM which will tell you if the user is online/offline. There are also events
that fire whenever the status changes.

## Feature Detection

Supported in Firefox, Safari, Chrome, iPhone, and Android.

To detect whether or not it's available in the current browser:

    !!window.applicationCache;

## Cache Manifest

Point the browser to the cache manifest file using the **manifest** attribute of the root element:

    <html manifest="/cache.manifest">

It must be served with the **text/cache-manifest** content type.

The first line of the file is:

    CACHE MANIFEST

Then the file is divided into three parts: explicit, fallback, and online whitelist. Each section
has a header. If no section headers are given, it means that all files listed belong to the
"explicit" section. Example:

    CACHE MANIFEST
    /clock.css
    /clock.js
    /clock-face.jpg

The web browser will download all 3 resources when it loads the cache manifest file. It will also
implicitly download the current page it's on.

Here's another example which includes the white list:

    CACHE MANIFEST
    NETWORK:
    /tracking.cgi
    CACHE:
    /clock.css

In this case, we're white listing the /tracking.cgi file so the browser never downloads and caches
it. `NETWORK:` is a section header.

The fallback section is used to define substitutions for online resources that weren't cached
successfully.

    CACHE MANIFEST
    FALLBACK:
    / /offline.html
    NETWORK:
    *

This cache manifest file works well for large sites like Wikipedia. When you visit any page that
points to a manifest, it will automatically include that page in the application cache.

'/' will match all pages not just the homepage. So if a link goes to a page you've never cached, it
will fallback to /offline.html.

'\*' has special meaning in the network section. It's the "online whitelist wildcard flag". Anything
that isn't in the appcache can still be downloaded from the original web address, as long as you
have internet connection. So while you're browsing "hypothetically offline-enabled" app online, your
browser will fetch images/videos and other embedded resources normally.

Without the wildcard, an offline-enabled app would behave strangely. It would not load any
externally hosted images or videos.

## Events

Events are fired on the window.applicationCache object:

1. When a browser hits a manifest attribute, it fires a **checking** event.
2. If your browser has never seen this cache manifest before, it fires a **downloading** event and
   then starts downloading. While downloading, it fires one or more **progress** events. After
   caching successfully, it fires a **cached** event.
3. If your browser has seen this manifest file before, it checks to see whether or not the file has
   been updated since its last time. 3a. No, it's the same => the browser fires a **noupdate**
   event. 3b. Yes, it has changed => browser fires a **downloading** event. All files will be
   re-downloaded and **progress** events are fired. Finally the browser will fire a **updateready**
   event. To hot-swap the new version without forcing a page reload, use
   **window.applicationCache.swapCache()**

If anything goes wrong, the browser will fire an **error** event. Examples:

- 404 or 410 on one of the resources - HTML page pointing to cache manifest file fails to download
correctly - failure to download one of the resources

## Browser State (from HTML5 Specification)

The **navigator.onLine** attribute will return false if the user agent is definitely offline. It
returns true if the user agent might be online.

The events **online** and **offline** are fired on the Window object when the browser changes state.

# Forms

HTML5 offers a dozen new input types and other new features for forms. All of these degrade
gracefully in older browsers. If an input type is unrecognized, browsers will treat it as a "text"
input. If an attribute is unrecognized, browsers will simply ignore it.

## New Attributes
**placeholder** is used for placeholder text on a form field. When a user focuses on a field, the
placeholder text will disappear. Example:

    <input type="text" placeholder="Search Bookmarks">

**autofocus** is used to provide focus on a particular input when the page finishes loading. Google
uses autofocus on its search field. Example:

    <input type="text" autofocus>

To detect placeholder/autofocus, create an input element and check whether or not the attribute is
in the new element:

    "autofocus" in document.createElement("input");
    "placeholder" in document.createElement("input");

## New Input Types

Having more input types is great for validation and iPhone keyboards. When the iPhone recognizes a
type, it will display the correct keyboard making it easier for users to type into the field. Some
browsers may also perform validation or render the input fields differently.

The **email** type is used for email addresses:

    <input type="email"> 

The **url** type is used for web addresses:

    <input type="url">

Numbers may be inputted via spinboxes and the **number** type:

    <input type="number" min="0" max="10" step="2" value="6">

The number type also comes with JavaScript methods:

- input.stepUp(n) - input.stepDown(n) - input.valueAsNumber

There are also sliders via the **range** type:

    <input type="range" min="0" max="10" step="2" value="6">

HTML5 includes a native datepicker via these types, only supported in Opera:

- type="date" - type="month" - type="week" - type="time" - type="datetime" - type="datetime-local"

There is also the **search** type, which Safari renders differently:

    <input type="search">

And there's a color picker via the **color** type:

    <input type="color">

As of now, only Opera 10 takes steps to include validation with these new inputs. It's part of the
specification, but no browsers have implemented validations yet.

# Microdata

Microdata is a way to extend the HTML language with additional semantics. It's tightly integrated
into the specification itself.

"Microdata annotates the DOM with scoped name/value pairs from custom vocabularies."

Microdata is about applying additional semantics to data that's already visible on your page using
name/value pairs. For most HTML elements, the property value is simply the text content of the
element. Exceptions are:

- `<meta>` uses content attribute - `<audio>`, `<embed>`, `<iframe>`, `<img>`, `<source>`, `<video>`
use src attribute - `<a>`, `<area>`, `<link>` use href attribute - `<object>` uses data attribute -
`<time>` uses datetime attribute - other elements use the text content

To declare a microdata **vocabulary** you use the **itemtype** and **itemscope** attributes.
Example:

    <section itemscope itemtype="http://.../Vocab">

The property key is specified via the **itemprop** attribute:

    <h1 itemprop="name">Mark Pilgrim</h1>

You can add microdata properties to any HTML markup. An example of microdata vocabulary can be
found: http://www.data-vocabulary.org/Person/

To add hidden values, use the `<meta>` tag. This should only be used as a last resort (eg.
geolocation data):

    <meta itemprop="latitude" content="37.4149" />

Microdata is useful to tell search engines extra information on the page. Google picks up certain
vocabularies and displays additional information in its search results: such as annotated
information about a person, organization, or a review.

Google supports microdata via the **Rich Snippets** program. You can even use the tool
http://www.google.com/webmasters/tools/richsnippets to test what Google will see on your own pages.