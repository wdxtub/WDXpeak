# High Performance Web Sites

[High Performance Web Sites](http://oreilly.com/catalog/9780596529307) by Steve Souders offers 14
techniques to speed up the user experience of accessing web sites/applications and make web surfing
much faster for end users. In a way, he's like Tron - he fights for the users!

For most web pages, less than 10-20% of the end user response time is spent getting the HTML
document from server to browser. In reality, most time is spent fetching assets (JavaScript, CSS,
images, etc...), in redirects, DNS lookups, blocked requests which should be parallel, and more.

When optimizing any web site, it's critical to profile current performance and identify the
bottlenecks. Souders argues that the best bang for the buck of optimizing is in the frontend:

1. More potential for improvement in the frontend, since that's where 80-90% of the end user
   response time is spent.
2. Improvements usually require fewer resources, it usually requires updating some configuration
   files instead of major architecture changes.
3. It has been proven to work.

**The performance golden rule is only 10-20% of the end user response time is spent downloading the
HTML document. The other 80-90% is spent downloading all the components in the page.**

The rest of the book offers guidelines and techniques to reduce that 80-90%.

# Make Fewer HTTP Requests

The Performance Golden Rule reveals that 80-90% of response time is spent making additional HTTP
requests for all the components of a web page. Each request has overhead associated with it. We can
use various techniques to reduce the number of requests.

## Image Maps and CSS Sprites

An **image map** allows you to associate multiple URLs with a single image using HTML's `<map>` tag.
Example:

    <img usemap="#map1" border=0 src="/images/imagemap.gif">
    <map name="map1">
    <area shape="rect" coords="0,0,31,31" href="home.html" title="Home">
    <area shape="rect" coords="36,0,66,31" href="gifts.html" title="Gifts">
    <area shape="rect" coords="71,0,101,31" href="cart.html" title="Cart">
    <area shape="rect" coords="106,0,136,31" href="settings.html" title="Setting">
    <area shape="rect" coords="141,0,171,31" href="help.html" title="Help">
    </map>

There are some drawbacks to using image maps: defining area coordinates manually is tedious and
error-prone and it's difficult to work with any shape other than rectangles.

**CSS Sprites** let you combine images but are much more flexible. An element can use a large
background image, but only show a portion of it:

    <div style="background-image: url('a_lot_of_sprites.gif');
                background-position: -260px -90px;
                width: 26px; height: 24px;"></div>

For a navigation menu, each nav item could be its own element. Each element would use the same
background image but have different background positions.

An additional benefit of combined images are they tend to be smaller as a result of reducing image
overhead (color tables, formatting info, etc...).

## Inline Images

You can inline image data via the **data:** URL scheme, see
[RFC2397](http://tools.ietf.org/html/rfc2397).

The data is in the URL itself following the format:

    data:[<mediatype>][;base64],<data>

An example of a red star image would look like:

    <img alt="Red Star" src="data:image/gif;base64,R0lGODlhDAAMALMLAPN8ffB...=" />

It can be used anywhere a URL is specified including `<script>` and `<a>` tags. There are some major
drawbacks:

1. It's not yet supported in Internet Explorer
2. Some browsers have size limitations, FF accepts inline images up to 100K
3. base64 encoding will increase the size of the image
4. Since they're inlined, they won't be cached across different pages

A clever way to get around the caching drawback is to inline the image in an external CSS file and
then cache that CSS file. Since the stylesheet is cached, the inline image will also be cached.

## Combined Scripts/Stylesheets

In general, external scripts/stylesheets are better for performance. If you modularize your code,
however, you increase the number of HTTP requests due to separated files. To reduce load time, you
can combine your scripts and stylesheets as a build process.

Don't force every page to include script/stylesheets it doesn't need. It's worth the time to analyze
and benchmark to see which combinations of code has the best performance.

# Use a Content Delivery Network

An end user's proximity to the server affects the page's response time. Remember the golden rule, if
the application web server is closer to the user then 10-20% of the response time is reduced. If the
component web servers are closer to the end user, then you reduce the majority time.

A **Content Delivery Network (CDN)** is a collection of web servers distributed across multiple
locations to deliver content to users more efficiently.

It's most cost effective to use a CDN provider instead of owning your own CDN. Akamai is the
industry leader, CDN services include:

* Akamai
* Mirror Image
* SAVVIS
* Limelight
* Globule, CoDeeN (free)

In addition to improved response times, CDNs offer back ups, extended storage capacity, and caching.

# Add an Expires Header

Using an **Expires** header will make your components cacheable, reducing the number of HTTP
requests on subsequent page views. For HTTP 1.1, caching can be done via the **Cache-Control**
header. Usually caching is used for images, but it can be done for all components including scripts,
stylesheets, and video.

The Expires header tells the client the date/time after which the response is considered stale:

    Expires: Thu, 15 Apr 2010 20:00:00 GMT

The Cache-Control header was introduced in HTTP/1.1 to overcome limitations in the Expires header,
reducing the dependency on clock synchronization of the server and client. Cache-Control uses a
seconds delta, in this case 10 years:

    Cache-Control: max-age=315360000

This technique is known as using a **far future** expires header so clients will never have to
request the same component again. If you wish to update an image, you'll have to change its URI so
clients will fetch it again. This can be part of your build process to include timestamps or
revision numbers in the filenames.

You still want to use Expires for browsers that don't support HTTP/1.1, which is probably less than
1% of your traffic.

# Gzip Components

This rule reduces response times by reducing the size of the response itself. The transfer time
decreases when fewer packets must travel. This is the easiest technique for reducing page weight and
has the biggest impact.

Starting with HTTP/1.1, clients indicate support for compressing with the **Accept-Encoding**
header:

    Accept-Encoding: gzip, deflate

If a server sees the header, it can compress its response with one of the methods listed:

    Content-Encoding: gzip

Gzip is the most popular/effective compression method that's made freely available by the GNU
project and standardized by RFC 1952. It's worthwhile to compress your HTML documents, scripts,
stylesheets, any text response (JSON or XML). It's not worthwhile to compress images or PDFs because
they're already compressed and it would just be a waste of CPU cycles or it can potentially increase
the file size.

The cost of compression is in additional CPU overhead. You'll have to benchmark to determine which
resources should be compressed, but the general rule is you should gzip any file greater than 1 or
2K.

It gets complicated when dealing with proxies. Some proxies cache responses, but do not distinguish
between compressions. So a browser might not accept a gzipped response, but will accidentally get
one from a proxy. To fix this, the server should send back the header:

    Vary: Accept-Encoding

Which means distinguish between caches by the Accept-Encoding header.

# Put Stylesheets at the Top

**Progressive rendering** is when a page loads content progressively; it displays whatever if has as
soon as possible to give users visual feedback. The HTML page is the progress indicator for users.
Putting stylesheets at the bottom of documents will prohibit progressive rendering in many browsers.

Browsers block rendering to avoid redrawing elements, so the browser delays showing any visible
components while it waits for stylesheets to load. If your stylesheet link is at the bottom of the
page, the page will appear to load much slower with a blank white screen.

Moving all CSS to the top in the `<head>` section will solve this issue. Sounders recommends using
the `<link>` tag instead of @import, because the @import statement tends to result in the blank
white screen phenomenon.

Besides a blank white screen, there's also the **flash of unstyled content** which occurs before
browsers load the relevant CSS. Whereas IE sometimes uses the BWS, FF will tend to render with the
FOUC.

# Put Scripts at the Bottom

Whereas with stylesheets, progressive rendering is blocked until all stylesheets have been
downloaded - scripts are the opposite. Moving JavaScript to the bottom enables progressive rendering
and achieves greater download parallelization.

The HTTP/1.1 spec suggests that browsers download two components in parallel per hostname. If a
website splits its components between multiple hostnames, more components would download in
parallel. IE and FF both follow this guideline, but end users may override it in their preferences.
Many frontend engineers actually use CNAMEs (DNS alises) to split their components across multiple
hostnames instead of relying on end users to set their preferences.

Of course, splitting it too much will usually degrade performance due to overhead. Research at
Yahoo! shows using two hostnames leads to the best performance.

Parallel downloading is disabled while a script is downloading, even on different hostnames. Scripts
may use document.write to alter page content, so the browser waits to make sure the page is laid out
appropriately. Another reason is so that scripts may be executed in proper order.

# Avoid CSS Expressions

CSS expressions allow dynamic properties and are supported by IE5 and later.

    background-color: expression((new Date()).gethours()%2 ? "#fff" : "#000");

It's ignored by other browsers other than IE so developers tend to use it to get IE to behave
correctly. For example, to get min-width to work correctly in IE6:

    width: expression(document.body.clientWidth < 600 ? "600px" : "auto");
    min-width: 600px;

The frequency at which CSS expressions are evaluated make them work, but it's also why they often
have performance issues. They're evaluated when the page is rendered, when the user scrolls, resizes
the window, and even on mouse movement.

If you must use CSS expressions, you can use **One-Time Expressions** which override themselves on
load:

    p { background-color: expression(altBgcolor(this)); }
    function altBgcolor(elem) {
      elem.style.backgroundColor = (new Date()).gethours()%2 ? "#fff" : "#000";
    }

In most cases, it's usually easier to just drop the CSS expression completely. For min-width, we can
just add a JavaScript event handler to window.onresize.

# Make JavaScript and CSS External

In raw terms, inline is faster. External script/css suffer from the overhead of multiple HTTP
requests (even taking parallel downloading into consideration). External files have the benefit of
being cached which makes it more useful in the real world. Inlined script/css cannot be cached
without caching the entire page, so subsequent pages or different pages would load much slower.

The fewer page views by a user, the better it is to inline your script/css. If a user has many page
views and each page shares the same script/css, it's much better to make those external and cache
them.

There are two extremes when making these assets external. You can combine all of your script into
one file. One the user's first page view, he would download more than is necessary but subsequent
page views would load faster. The other extreme is creating a separate script or stylesheet for each
page. In this case, users would not benefit from the cached version when going from page to page.
There's also the middle case, where each page has a script/css type that's external.

The only exception where inlining is preferable is with home pages, there is often only one page
view to it per session. They also have a high demand for responsiveness (even for empty caches).

Sounders shows two techniques to get the benefits of inlining and making assets external. You can
**Post-Onload Download** resources using JavaScript. Just inline your script/css and use the onload
event to download an external version after the page has rendered. Your page will have to deal with
duplicated script in this case, which just means it can only define functions but not execute them.
There's also the **dynamic inline** technique which uses JavaScript to check the cache before
inlining script/css.

# Reduce DNS Lookups

When you type www.yahoo.com into a browser, a DNS resolver is contacted and returns that server's IP
address. It typically takes 20-120 milliseconds for browsers to look up an IP address. No downloads
can occur in this time.

Reducing the number of unique hostnames on a page will reduce the number of DNS lookups. Doing so
also reduces the number of parallel downloads. Sounders recommends a compromise of at least two but
no more than four hostnames.

Making sure your servers support Keep-Alive also reduces DNS lookups, since browsers won't do a DNS
lookup if it already has a connection to the server.

# Minify JavaScript

**Minification** is the practice of removing unnecessary characters from code to reduce its size,
thereby improving load times. **Obfuscation** is an alternative which minifies, but also renames
variables into smaller strings in an attempt to make the code harder to read. Obfuscation has 3
drawbacks: it's more complex/buggy, has higher maintenance, and makes debugging difficult.

The most popular tool for minification is [JSMin:](http://crockford.com/javascript/jsmin)

Inline script can also be minified by using whatever page generation platform (PHP, Python, Perl
CGI, etc.), there is usually a version of JSMin which can be integrated.

Gzip actually compresses more than minification, so it's probably more important to do that. It
doesn't hurt to do both.

Minifying CSS typically has less savings than JavaScript, as it usually has fewer comments and less
whitespace. The greatest saving is merging identical rules and removing unused rules, but that may
be complicated.

# Avoid Redirects

A **redirect** reroutes users from one URL to another. They're usually done for HTML pages, but can
be used for assets in a page. Redirects make your page slower.

Some 3xx status codes are:

* 300 Multiple Choices (based on Content-Type)
* 301 Moved Permanently
* 302 Moved Temporarily (aka Found)
* 303 See Other (clarification of 302)
* 304 Not Modified (not really a redirect, used for conditional GETs)
* 305 Use Proxy
* 306 (no longer used)
* 307 Temporary Redirect (clarification of 302)

301 and 302 are used most often. The URL to redirect to is specified in the **Location** header.
Despite their names, typically 301 and 302 response is not cached in practice unless additional
cache headers are applied (even the spec says it should be without an Expires/Cache-Control header!)

Redirects delay the entire HTML page from downloading and progressively rendering during the
request/response cycle.

Sounders offers some alternatives to redirects:

* redirect for trailing slash => configure your server/app to automatically add it for you on
  incoming requests
* permanent redirect to new URLs => support the old URLs via Alias or mod\_rewrite
* tracking inbound traffic => use the Referrer header
* tracking outbound traffic => use JavaScript event handlers or **Beacon**
* prettier URLs => just host your entire site on the "prettier" URL instead of redirecting to the
  "ugly" URL

# Remove Duplicate Scripts

Including the same external script twice hurts performance with unnecessary HTTP requests (IE only,
without far future cache) and wasted JavaScript execution.

Duplicate scripts occur due to team size and complexity of the site. One way to avoid it is to use
your server-side language handle generating `<script>` tags.

    <%= javascript_include_tag :cookie %>
    def javascript_include_tag(script)
      @scripts ||= [] 
      if !@scripts.include?(script)
        "<script src=\"#{script}.js\">".html_safe
      end
    end

You could even let your routine handle dependencies between scripts and versioning for far future
Expires header.

# Configure ETags

**Entity tags (ETags)** are a mechanism that servers/browsers use to validate cached components,
usually using the resource's checksum and conditional GETs.

ETags provide a more flexible mechanism for validating entities than the last-modified-date, such as
ability to make changes based on incoming headers. The problem is different servers may have
different ETags for the same resource. If the ETags don't match, the client won't get a 304 response
that it should.

Even if your components have a far future Expires header, a conditional GET request is still made
whenever the user clicks Reload or Refresh.

If-None-Match and If-Modified-Since both need to be satisfied for a 304 response so an incorrect
ETag ruins caching. It's better to use them correctly or not at all.

# Make Ajax Cacheable

Ajax requests can be passive or active. **Passive requests** occur in anticipation of a user's
future needs, like an email client getting the user's address book before any composition is made.
**Active requests** are made based on the user's current actions.

Thanks to Ajax, the user won't have to endure a complete page load, but it's still not instantaneous
because the user must wait for the HTTP response.

Many rules still apply to Ajax requests: Gzip components, reduce DNS lookups, minify JavaScript,
avoid redirects, and configure ETags. The most important, however, is to add an Expires header. Ajax
requests use the same cache headers to determine if responses should be cached or not.

Developers have to be careful not to cache private data, or only cache private data for the current
user. Sounders suggests placing the user's unique ID or username within the URL itself. He also says
the best way to ensure privacy is to use SSL, which only caches responses for the current browser
session.

Caching Ajax responses is not always as simple as adding a far future Expires header. If the user
modifies the data, the server must ensure that the cache is invalidated. A simple solution is to
embed the timestamp in the query string. Whenever the client makes an update, the timestamp would be
updated and the new resource would be fetched instead. Of course, this only works if there is only
one client and the resource isn't being shared.