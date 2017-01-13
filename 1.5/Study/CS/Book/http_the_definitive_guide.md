# HTTP, The Definitive Guide

The Hypertext Transfer Protocol is used to communicate over the Web. [HTTP, The Definitive
Guide](http://oreilly.com/catalog/9781565925090) is an informative guide on this protocol. The
authors are very knowledgeable about HTTP and have covered almost the entire specification (along
with additional HTTP-related information) in an easy to read format.

# HTTP: The Web's Foundation

## Overview of HTTP
### Servers and Clients
Web browsers, servers, and other web apps all talk to each other via the Hypertext Transfer
Protocol.

HTTP uses reliable data-transmission protocols that guarantee that your data will not be damaged or
scrambled in transit.

**Servers** store data, **clients** send HTTP requests to servers. Servers return the requested data
in HTTP responses.

Web servers host are said to host **resources**, which can range from text files, HTML files,
images, movies, or even dynamic content.

HTTP tags each object being transported through the Web with a data format called a **MIME type -
Multipurpose Internet Mail Extensions**. It was originally designed for emails, but it worked so
well that HTTP adopted it. When a client gets back an object with the MIME type, it will usually
know how to deal with it.

Example MIME types:

- text/html - text/plain - image/jpeg - image/gif - video/quicktime - application/vnd.ms-powerpoint

### URIs and URLs
A **URL - uniform resource locator** describes a resource's location. It tells precisely where a
resource is located and how to access it. Most URLs have 3 main parts:

- the scheme (http://) - server's Internet address (www.joes-hardware.com or 192.168.1.1) - path to
specific resource on server (/specials/saw-blade.gif)

A URL is a kind of **URI - uniform resource identifier**, which act like the postal addresses of the
Internet. Another kind of URI is the **URN - uniform resource name**. A URN is a unique name for a
particular piece of content, independent of where the resource currently resides.

    urn:ietf:rfc:2141

URNs are still experimental and not yet widely adopted.

### HTTP Messages
An **HTTP transaction** consists of a **request** command and a **response** result. The
communication happens with formatted blocks of data called **HTTP messages**.

There are different types of requests called **HTTP methods**, which tells the server what action to
perform. For example (incomplete):

- GET, send named resource form server to client - PUT, store data from client into a named server
resource - DELETE, delete named resource from a server - POST, send client data into a server
gateway application - HEAD, send just the HTTP headers from the response for the named resource

Every HTTP response comes back with a three-digit numeric **status code** that tells the client if
the request succeeded or if other actions are required. For example (incomplete):

- 200; OK. Document returned correctly - 302; Redirect. Go someplace else to get the resource. -
404; Not Found. Can't find this resource.

HTTP also sends a textual "reason phrase" with each numeric status code. It's included only for
descriptive purposes.

HTTP messages are plain text, line-oriented messages. Example request/response:

    +---------------------------------+--------------------------+
    | Request                         | Response                 |
    +---------------------------------+--------------------------+
    | GET /test/hi-there.txt HTTP/1.0 | HTTP/1.0 200 OK          |
    | Accept: text/*                  | Content-Type: text/plain |
    | Accept-Language: en,fr          | Content-length: 19       |
    |                                 |                          |
    |                                 | Hi!  I'm a message!      |
    +---------------------------------+--------------------------+

Messages consist of 3 parts:

- **start line**, first line of message indicating what to do or what happened. - **header fields**,
name/value pairs per line. - **body**, optionally following a blank line after the headers. Unlike
the other parts, the body can contain arbitrary binary data.

Messages use **Transmission Control Protocol (TCP)** connections to move from place to place. HTTP
is an application layer protocol, it leaves the details of networking to **TCP/IP**. TCP provides:

- error free data transportation - in order delivery - unsegmented data stream

### Behind The Scenes
HTTP is layered over TCP which is in turn layered of IP:

1. HTTP: application layer
2. TCP: transport layer
3. IP (Internet Protocol): network layer
4. Network-specific link interface: data link layer
5. Physical network hardware: physical layer

Before an HTTP client sends a message to the server it establishes a TCP/IP connection using an IP
address and port number. Browsers usually retrieve the IP address using a **hostname**, example:
www.netscape.com. Hostnames are converted to IP addresses through the **Domain Name Service** or
DNS.

The steps of a typical transaction are:

1. Browser extracts server's hostname from URL
2. Browser converts server's hostname into server's IP address
3. Browser extracts port number from URL (or defaults to 80)
4. Browser establishes TCP connection with web server
5. Browser sends an HTTP request to server
6. Server sends HTTP response back to browser
7. Connection is closed and browser displays the document

### Other Components
Some other architectural components of the web include:

- proxies: HTTP intermediaries that sit between clients/servers - caches: HTTP storehouses that keep
copies of pages close to clients - gateways: special servers that connect to other applications -
tunnels: special proxies that blindly forward HTTP communications - agents: semi-intelligence web
clients that make automated requests

A **proxy** sits between the client and server, receives all the client's HTTP requests and relays
it to the server (maybe modifying them). They're often used for security. They can filter
requests/responses; for example to detect viruses or filter adult content.

**Caches** are a special type of proxy server that keeps copies of popular documents for performance
reasons. A client can download a document much more quickly from a nearby cache than from a distant
web server.

**Gateways** are servers that act as intermediaries for other servers. They often convert HTTP
traffic to another protocol.

**Tunnels** are HTTP applications that blindly relay raw data between two connections. HTTP tunnels
are often used to transport non-HTTP data over one or more HTTP connections. One popular example is
to carry SSL encrypted traffic through an HTTP connection.

**Agents** are client programs that make HTTP requests on the user's behalf. For example: web
browsers are a kind of HTTP agent.

## URLs and Resources
### Syntax and URL components
Breaking down the URL http://www.joes-hardware.com/seasonal/index-fall.html:

- The first part (http) is the URL **scheme** that tells the web client how to access the resource.
In this case, it says use the HTTP protocol. - The second part (www.joes-hardware.com) is the
**host** and tells the client where the resource is hosted. - The third part
(/seasonal/index-fall.html) is the **resource path** and tells the client what particular local
resource on the server is requested.

URLs can point to any resource on the Internet, from an email account:

    mailto:president@whitehouse.gov

to files available through FTP:

    ftp://ftp.lots-o-books.com/pub/complete-price-list.xls

Most URLs adhere to this nine-part general format:

    <scheme>://<user>:<password>@<host>:<port>/<path>;<params>?<query>#<frag>

    +-----------+--------------------------------------------+-----------------+
    | Component | Description                                | Default         |
    +-----------+--------------------------------------------+-----------------+
    | scheme    | which protocol to use                      | none            |
    +-----------+--------------------------------------------+-----------------+
    | user      | username some schemes require for auth     | anonymous       |
    +-----------+--------------------------------------------+-----------------+
    | password  | password for auth                          | <email address> |
    +-----------+--------------------------------------------+-----------------+
    | host      | hostname or dotted IP address of server    | none            |
    +-----------+--------------------------------------------+-----------------+
    | port      | port number server is listening on         | scheme-specific |
    +-----------+--------------------------------------------+-----------------+
    | path      | local name for resource on server          | none            |
    +-----------+--------------------------------------------+-----------------+
    | params    | name/value pairs                           | none            |
    +-----------+--------------------------------------------+-----------------+
    | query     | also used to pass params                   | none            |
    +-----------+--------------------------------------------+-----------------+
    | frag      | name for piece of the resource, not passed | none            |
    |           | to the server (only used by client)        |                 |
    +-----------+--------------------------------------------+-----------------+

Some servers require a username/password before you can access data. If none is given a default
value of 'anonymous' is given for the username. Browsers will also send a default password (IE sends
"IEUser" and Netscape Navigator sends the password "mozilla").

URLs also have a **params** component which is a list of name/value pairs. They provide applications
with any additional info that is needed to access the resource. For example, the FTP protocol allows
you to define the transfer mode to be text or binary:

    ftp://prep.ai.mit.edu/pub/gnu;type=d

The path component may be divided into **path segments** separated by the "/" character. Each
segment can have its own params component:

    http://www.joes-hardware.com/hammers;sale=false/index.html;graphics=true

Everything to the right of a '?' character is the **query** component:

    http://www.joes-hardware.com/inventory-check.cgi?item=12731&color=red

The query string has no required format except that some characters are illegal. By convention, most
gateways expect the query string to be formatted as name/value pairs separated by the "&" character.

**Fragments** allow clients to divide the resources into sections, for example a chapter in a large
HTML document. Clients don't pass fragments to servers, after your browser gets the entire resource
from the server it will use the fragment to display the part of the resource you're interested in:

    http://www.joes-hardware.com/tools.html#drills

### Shortcuts and Relative URLs
URLs come in two flavors: **absolute** and **relative**. A relative URL is interpreted relative to
another URL, called its **base**. For example, if your resource location is:

    http://www.joes-hardware.com/tools.html

And inside the document there was an anchor:

    <a href="./hammers.html">hammers</a>

It will be interpreted relative to the base "/tools.html" on joes-hardware.com:

    http://www.joes-hardware.com/hammers.html

Relative URLs may also infer the scheme:

    ://www.joes-hardware.com/hammers.html

### Encoding and Character Rules
URLs are permitted to contain only characters from a relatively small, universally safe alphabet in
order to be portable and readable. There are also escape mechanisms so that URLs may be complete.

An encoding scheme was devised to represent characters in a URL that are not safe. It represents
unsafe characters by an "escape" notion, consisting of a percent sign (%) followed by two
hexadecimal digits that represent the ASCII code of the character.

Some characters have special meaning inside of a URL, are not defined by the US-ASCII printable set,
or are discouraged due to confusing some Internet gateways and protocols:

- % escape token for encoded characters - / delimiting splitting up path segments in path component
- ' reserved in the path component - " reserved in the path component - \# reserved for fragment
delimiter - ? reserved as query string delimiter - ; reserved as params delimiter - : reserved to
delimit scheme, user/password, and host/port - $,+ reserved characters - @&= special meaning in
context of some schemes - {}|\^~[]‘ unsafe handling by various agent - &lt;&gt;" should be encoding
because they often have special meaning - 0x00 to 0x1F, 0x7F restricted non-printable characters -
&gt; 0x7F don't fall within 7-bit range of US ASCII set

Once all unsafe characters have been encoded, the URL is in a **canonical form** that can be shared.

### Common Schemes
Some popular schemes:

- http, conforms to general URL format - https, twin to http scheme but uses SSL to provide
encryption. Its default port is 443. - mailto, refers to email addresses. It's got a different
format because it behaves differently (it does not refer to objects that can be accessed directly).
Documented in internet RFC822. - ftp, File Transfer Protocol which follows the general format:
`ftp://<user>:<password>@<host>:<port>/<path>;<params>` - rtsp, rtspu are identifiers for
audio/video media resources via the Real Time Streaming Protocol. - file, denotes files directly
accessible on given host machine by local disk - telnet, access interactive services with the
general format: `telnet://<user>:<password>@<host>:<port>/`

### Future and URNs
The **Internet Engineering Task Force (IETF)** have been working on a new standard, **uniform
resource names (URNs)**. Whereas URLs represent a location, URNs represent a name. So even if a
given resource moves, if you have its name you should still be able to find it (similar to domain
names vs IP addresses).

URNs have been around for a while but have not been heavily adopted yet. URLs are currently the
standard and will be for a while.

## HTTP Messages
### How Messages Flow
Messages are blocks of data send between HTTP applications. Their direction is described to be
**inbound**, **outbound**, **upstream**, or **downstream**.

**Transactional** direction are said to be inbound and outbound. Messages travel inbound to the
origin server and when their work is done, they travel outbound back to the user agent.

All messages flow downstream, regardless of whether they are requests or responses. The sender of
the message is upstream of the receiver.

All HTTP messages are either **request** or **response** messages. Requests carry an action to a web
server. Response carries results back to a client.

The format of a request message:

    <method> <request-URL> <version>
    <headers>

    <entity-body>

And the format of a response message:

    <version> <status> <reason-phrase>
    <headers>

    <entity-body>

### Start Line
All messages begin with a start line which says what to do or what happened. The start line for a
request is the `<method> <request-URL> and <version>`. Response start lines contain the `<version>
<status> and <reason-phrase>`.

Version number appear in both request/response message start lines. They are in the format HTTP/x.y
where x is the major version and y is the minor version. They're provided to help applications speak
HTTP to each other.

### Headers
HTTP header fields add additional information to request/response messages, they're name/value
pairs. For example:

    Content-length: 19

The spec defines several header fields, applications are also free to invent their own headers.
They're classified into:

- General, can appear in both request/response - Request, provides additional info about the request
- Response, provides additional info about the response - Entity, describes body size, contents, or
the resource itself - Extension, new headers not defined by spec

The syntax is simple: a name, followed by a colon, followed by optional whitespace, followed by the
field value, followed by CRLF (Carriage Return Line Feed).

Long header lines can be made readable by breaking them into multiple lines, preceding each extra
line with at least one space or tab character:

    HTTP/1.0 200 OK
    Content-Type: image/gif
    Server: Test Server
      Version 1.0
    Content-Length: 8572

For a complete list of headers defined in the spec, see the HTTP/1.1 specification or Appendix C of
this book. Here's a general overview:

* General Headers
- Connection: allows clients/server to specify options about connection - Date: timestamp for
message - MIME-Version: MIME version sender is using - Trailer: set of headers in trailer of message
encoded - Transfer-Encoding: what encoding was performed on message for transport - Upgrade: new
version or protocol that sender would like to upgrade to - Via: shows what intermediaries message
has gone through
* General Caching Headers
- Cache-Control: pass cache directions with message - Pragma: another way to pass directions not
specific to caching
* Request Headers
- Client-IP: IP address of client - From: email address of client's user - Host: hostname and port
being sent to - Referrer: URL of document that contains current request URI - UA-Color: capabilities
of client machine's display - UA-CPU: type/manufacturer of client's CPU - UA-Disp: info about
client's display capabilities - UA-OS: name/version of client's OS - UA-Pixels: pixel information
about client's display - User-Agent: tells server name of application making request
* Accept Request Headers
- Accept: what media types are okay to send - Accept-Charset: what charsets are okay -
Accept-Encoding: what encodings are okay - Accept-Language: what languages are okay - TE: what
extension transfer codings are okay
* Conditional Request Headers
- Expect: list of server behaviors that client requires - If-Match: only get if entity tag matches -
If-Modified-Since: only get if resource has been modified since - If-None-Match: get if entity tags
supplied do not match - If-Range: get conditional range of document - If-Unmodified-Since: get if
not modified since date - Range: request a specific range of resource
* Security Request Headers
- Authorization: client supplied data to authenticate itself - Cookie: used to pass a token to
server - Cookie2: note version of cookies a requestor supports
* Proxy Request Headers
- Max-Forwards: max # of times a request should be forwarded - Proxy-Authorization: auth data for
proxy - Proxy-Connection: options for proxy connection
* Response Headers
- Age: how old response is - Public: list of request methods server supports - Retry-After:
timestamp to try again if resource is unavailable - Server: name/version of server's application
software - Title: for HTML documents, title of document - Warning: more detailed warning message
than reason phrase
* Negotiation Response Headers
- Accept-Ranges: type of ranges server will accept - Vary: list of headers server looks at
* Security Response Headers
- Proxy-Authenticate: list of challenges for client from proxy - Set-Cookie: sets cookie on client
side - Set-Cookie2: similar to Set-Cookie - WWW-Authenticate: list of challenges for the client from
server
* Entity Headers
- Allow: lists of request methods allowed on this resource - Location: tells client where entity is
really located (redirect)
* Content Headers
- Content-Base: base URL for resolving relative URLs within body - Content-Encoding: encoding
performed on body - Content-Language: natural language best used - Content-Length: length or size of
body - Content-Location: where resource is actually located - Content-MD5: MD5 checksum of body -
Content-Range: range of bytes entity represents of entire resource - Content-Type: type of object
that this body is
* Entity Caching Headers
- ETag: entity tag associated with this resource - Expires: timestamp for when this resource will no
longer be valid - Last-Modified: timestamp when this entity changed

### Entity Body
Entity bodies are what HTTP was designed to transport, they can carry many kinds of digital data:
images, video, plain text, HTML, software apps, etc...

### HTTP Methods
Methods help tell the server what to do in an HTTP request:

    +---------+---------------------------------------------------+----------------+
    | Method  | Description                                       | Body Required? |
    +---------+---------------------------------------------------+----------------+
    | GET     | Gets a document from the server                   | No             |
    +---------+---------------------------------------------------+----------------+
    | HEAD    | Gets just the headers for a document              | No             |
    +---------+---------------------------------------------------+----------------+
    | POST    | Send data to server for processing                | Yes            |
    +---------+---------------------------------------------------+----------------+
    | PUT     | Store the body of the request on the server       | Yes            |
    +---------+---------------------------------------------------+----------------+
    | TRACE   | Trace the message through proxy servers to server | No             |
    +---------+---------------------------------------------------+----------------+
    | OPTIONS | Determine what methods can operate on a server    | No             |
    +---------+---------------------------------------------------+----------------+
    | DELETE  | Removes a document from the server                | No             |
    +---------+---------------------------------------------------+----------------+

Not all servers implement all seven methods and HTTP was designed to be extensible so servers may
implement their own request methods called **extension methods**.

To be compliant with HTTP v1.1, a server only needs to implement the GET and HEAD methods for its
resources.

HTTP defines a set of **safe** methods (ie. GET or HEAD) meaning no action should occur as a result
of an HTTP request that uses GET or HEAD. They're meant to distinguish unsafe methods from
end-users, ie. as a result of a request your credit card may be charged.

HTTP was designed to be extensible and some additional methods are in common use that are not
declared in the spec, for example the WebDAV extension that supports publishing content to servers:

- LOCK allows users to lock a resource - MKCOL allows user to create a resource - COPY facilitates
copying resources - MOVE moves a resource on a server

It's best to be tolerant of extension methods, since HTTP applications could run into extension
methods that it does not understand. Proxies should forward them and end servers should response
with a 501 Not Implemented status code. "Be conservative in what you send, be liberal in what you
accept."

### Status Codes
Status codes tell the client what happened in HTTP responses:

    +---------------+---------------+---------------+
    | Overall Range | Defined Range | Category      |
    +---------------+---------------+---------------+
    | 100-199       | 100-101       | Informational |
    +---------------+---------------+---------------+
    | 200-299       | 200-206       | Successful    |
    +---------------+---------------+---------------+
    | 300-399       | 300-305       | Redirection   |
    +---------------+---------------+---------------+
    | 400-499       | 400-415       | Client error  |
    +---------------+---------------+---------------+
    | 500-599       | 500-505       | Server error  |
    +---------------+---------------+---------------+

Current versions of HTTP define only a few codes for each category. The specification will add more
status codes in the future, but developers may decide to extend the current protocol with their own
status codes. In that case, you should treat it as a general member of the class whose range it
falls into.

**Reason phrases** also come along with status codes. Whereas status codes are for machines, reason
phrases are a textual explanation of the status that's meant for humans. The spec does not provide
any hard rules for what reason phrases should look like.

100-199 are informational status codes:

    +------+---------------------+-------------------------------------------------+
    | Code | Reason              | Meaning                                         |
    +------+---------------------+-------------------------------------------------+
    | 100  | Continue            | Initial part of request received, client should |
    |      |                     | continue sending requests                       |
    +------+---------------------+-------------------------------------------------+
    | 101  | Switching Protocols | Server is changing protocols to one             |
    |      |                     | in "Upgrade" header                             |
    +------+---------------------+-------------------------------------------------+

For clients to use the 100 status code, it must send a request with an Expect header with the value
100-continue.

200-299 are successful status codes:

    +------+-----------------+----------------------------------------------------+
    | Code | Reason          | Meaning                                            |
    +------+-----------------+----------------------------------------------------+
    | 200  | OK              | Request is OK, body contains requested resource    |
    +------+-----------------+----------------------------------------------------+
    | 201  | Created         | For unsafe requests, ie. PUT has created resource  |
    |      |                 | with Location header containing specific reference |
    +------+-----------------+----------------------------------------------------+
    | 202  | Accepted        | Request accepted, but no action performed yet      |
    +------+-----------------+----------------------------------------------------+
    | 203  | Non-Auth        | Headers did not come from origin server            |
    |      | Information     |                                                    |
    +------+-----------------+----------------------------------------------------+
    | 204  | No Content      | Response has start line and status, but no body.   |
    |      |                 | Eg. update browsers without redirecting/refreshing |
    +------+-----------------+----------------------------------------------------+
    | 205  | Reset Content   | Eg. clear any HTML form elements on current page   |
    +------+-----------------+----------------------------------------------------+
    | 206  | Partial Content | Partial range successful, expecting more.          |
    +------+-----------------+----------------------------------------------------+

300-399 are redirection status codes. They tie heavily with the Location header which should tell
clients where to go to next:

    +------+--------------------+--------------------------------------------------+
    | Code | Reason             | Meaning                                          |
    +------+--------------------+--------------------------------------------------+
    | 300  | Multiple Choices   | Multiple redirect choices, preferred in          |
    |      |                    | Location header                                  |
    +------+--------------------+--------------------------------------------------+
    | 301  | Moved Permanently  | Resource moved, use new URL                      |
    +------+--------------------+--------------------------------------------------+
    | 302  | Found              | Like 301, but is temporarily moved and client    |
    |      |                    | should continue using the old URL                |
    +------+--------------------+--------------------------------------------------+
    | 303  | See Other          | Redirect response for POST for created resource  |
    +------+--------------------+--------------------------------------------------+
    | 304  | Not Modified       | If client sends conditional headers, such as the |
    |      |                    | If-Modified-Since, server responds without body  |
    +------+--------------------+--------------------------------------------------+
    | 305  | Use Proxy          | Resource must be accessed through proxy          |
    +------+--------------------+--------------------------------------------------+
    | 307  | Temporary Redirect | Like 302, used for backwards compatibility       |
    +------+--------------------+--------------------------------------------------+

400-499 are client error status codes:

    +------+--------------------+-------------------------------------------------+
    | Code | Reason             | Meaning                                         |
    +------+--------------------+-------------------------------------------------+
    | 400  | Bad Request        | Client has send malformed request               |
    +------+--------------------+-------------------------------------------------+
    | 401  | Unauthorized       | Client requires authorization                   |
    +------+--------------------+-------------------------------------------------+
    | 402  | Payment Required   | Not used                                        |
    +------+--------------------+-------------------------------------------------+
    | 403  | Forbidden          | Request refused by server                       |
    +------+--------------------+-------------------------------------------------+
    | 404  | Not Found          | Server cannot find requested URL                |
    +------+--------------------+-------------------------------------------------+
    | 405  | Method Not         | Request made with unsupported method. Should    |
    |      | Allowed            | include Allow header with supported methods     |
    +------+--------------------+-------------------------------------------------+
    | 406  | Not Acceptable     | Client's "Accept" header has no available       |
    |      |                    | option for server                               |
    +------+--------------------+-------------------------------------------------+
    | 407  | Proxy Auth Req.    | Proxy requires authentication                   |
    +------+--------------------+-------------------------------------------------+
    | 408  | Request Timeout    | Client taking too long to send request          |
    +------+--------------------+-------------------------------------------------+
    | 409  | Conflict           | Server is afraid conflict of resource may arise |
    +------+--------------------+-------------------------------------------------+
    | 410  | Gone               | Similar to 404 but permanent                    |
    +------+--------------------+-------------------------------------------------+
    | 411  | Length Required    | Client needs to send Content-Length header      |
    +------+--------------------+-------------------------------------------------+
    | 412  | Precondition       | Client included an Expect header and conditions |
    |      | Failed             | cannot be met by server                         |
    +------+--------------------+-------------------------------------------------+
    | 413  | Request Body       | Client's entity body larger than what server    |
    |      | Too Large          | can or wants to process                         |
    +------+--------------------+-------------------------------------------------+
    | 414  | Request URI        | Same as 413, but with request URI               |
    |      | Too Long           |                                                 |
    +------+--------------------+-------------------------------------------------+
    | 415  | Unsupported Media  | Client sends an entity of content type that the |
    |      | Type               | server does not support                         |
    +------+--------------------+-------------------------------------------------+
    | 416  | Requested Range    | Requested range is invalid                      |
    |      | Not Satisfiable    |                                                 |
    +------+--------------------+-------------------------------------------------+
    | 417  | Expectation Failed | Request's Expect header cannot be satisfied     |
    +------+--------------------+-------------------------------------------------+

500-599 are server error status codes. This occurs if the client sends a valid request, but the
server itself has an error:

    +------+---------------------+-------------------------------------------------+
    | Code | Reason              | Meaning                                         |
    +------+---------------------+-------------------------------------------------+
    | 500  | Internal Server     | Server encounters error                         |
    |      | Error               |                                                 |
    +------+---------------------+-------------------------------------------------+
    | 501  | Not Implemented     | Client makes request beyond server's capability |
    +------+---------------------+-------------------------------------------------+
    | 502  | Bad Gateway         | Server acting as proxy/gateway encounters error |
    +------+---------------------+-------------------------------------------------+
    | 503  | Service Unavailable | Server temporarily cannot service request       |
    +------+---------------------+-------------------------------------------------+
    | 504  | Gateway Timeout     | Similar to 408, except response is from gateway |
    +------+---------------------+-------------------------------------------------+
    | 505  | HTTP Version        | Server does not support client's HTTP version   |
    |      | Not Supported       |                                                 |
    +------+---------------------+-------------------------------------------------+

## Connection Management
### TCP Connections
TCP gives HTTP a **reliable bit pipe**. Bytes stuffed in one side will come out the other side
correctly and in the right order. TCP sends data in little chunks called **IP packets}} or IP
datagrams. HTTP is a top layer over TCP, HTTPS inserts a TSL/SSL layer over TCP.

HTTP messages are streamed through an open TCP connection which is chopped up into **segments** and
transported across the internet in IP packets. Each TCP segment contains an IP packet header, TCP
segment header, and a chunk of data.

The IP header contains the source/destination IP addresses, the size, and other flags. The TCP
segment header contains TCP port numbers, TCP control flags, and numeric values used for data
ordering/integrity checking.

Computers may have multiple TCP connections open concurrently, TCP keeps these connections straight
through **port numbers**. Four values of a TCP connection define it:

    <source-IP-address, source-port, destination-IP-address, destination-port>

### Delays, Bottlenecks, and Clogs
Here's an example of an HTTP transaction:

1. DNS lookup
2. Connect
3. Request
4. Process
5. Response
6. Close

Unless the client or server is overloaded or executing complex resources, most HTTP delays are
caused by TCP network delays.

Some TCP-related delays affecting HTTP programmers are:

- TCP connection setup handshake - TCP slow-start congestion control - Nagle's algorithm for data
aggregation - TCP's delayed acknowledgement algorithm for piggybacked acknowledgements - TIME_WAIT
delays and port exhaustion

The initial handshake is broken up into three steps:

1. client requests new TCP connection, sends a small TCP packet (40-60 bytes) with the "SYN" flag
   set which means it's a connection request.
2. server accepts, sends back TCP packet with "SYN" and "ACK" flags set indicating connection
   request is accepted.
3. client sends acknowledgement back to server (usually TCP allows client to send data along also,
   ie. the HTTP request data). This time it's just the "ACK" flag that's set.

The **SYN/SYN+ACK handshake** creates a measurable delay when transactions do not exchange much data
and the handshake becomes the main overhead. HTTP allows reuse of existing connections to eliminate
the impact of the TCP setup delay.

Internet routers are free to destroy packets if overloaded so TCP implements its own acknowledgement
scheme to guarantee data delivery. Each packet gets a sequence number and data-integrity checksum.
The receiver of each segment returns an acknowledgement back to the sender. If the sender doesn't
receive the acknowledgement, it will conclude the packet was destroyed/corrupted and resend the
data. Acknowledgements are small an may "piggyback" on outgoing data packets heading in the same
direction.

To increase the chances of piggybacking, many TCP stacks implement a **delayed acknowledgement**
where they're stored in a buffer for a certain time window (ie. 100-200 milliseconds) looking for
something to piggyback on. If it cannot find one, an acknowledgement packet will be sent on its own.

Unfortunately for the request/reply behavior of HTTP, it's hard to find other packets headed in the
reverse direction. It's usually best to turn the delayed acknowledgement feature off.

TCP connections "tune" themselves over time, initially limiting the max speed and increasing it to
prevent sudden overloading/congestion of the Internet. This is called the **TCP slow start**.
Because tuned connections are faster, HTTP allows reuse of existing connections.

Since each TCP packet carries flags/headers (at least 40 bytes), network performance can be degraded
when sending large numbers of packets containing small amounts of data as opposed to a small number
of packets with large amounts of data. **Nagle's algorithm** attempts to bundle up large amount of
TCP data before sending a packet. It will only allow small packets if all others have been
acknowledged. This causes a problem with HTTP, since small messages may not fill a packet and
waiting for an acknowledgement may take a while when considering delayed acknowledgements. HTTP
applications often disable Nagle's algorithm by setting the **TCP\_NODELAY** parameter on their
stacks, but you must ensure that you won't write large chunks of data that will create a small
flurry of small packets.

TCP performance delays can add up if connections are managed naively, ie. in serial transactions. If
a web page has 3 embedded images and each transaction requires a new connection, that's 4 connection
delays.

### Optimizations like Parallel, Keep-Alive, and Pipelined Connections
The **Connection** header carries 3 different types of tokens:

- HTTP header field names relevant for only this connection - Arbitrary token values, describing
options for this connection - The value "close", indicating the connection will be closed when done

HTTP header field names listed in the Connection header must not be forwarded, this is known as
**protecting the header**.

Several techniques are available to improve HTTP connections:

- Parallel connections, concurrent requests across multiple TCP connections - Persistent
connections, reuse TCP connections to eliminate delays - Pipelined connections, concurrent requests
across shared TCP connection - Multiplexed connections, interleaving chunks of requests/responses

**Parallel connections** allow a browser to perform multiple transactions in parallel, for example
loading 3 embedded images at the same time. If any of these individual requests aren't taking up the
entire bandwidth limit and the delays are overlapped, using parallel connections will be faster.
They are not always faster though, ie. if the client's bandwidth is scarce. In practice browsers do
use parallel connections but limit it (often to 4).

An application that initiates an HTTP request to a server will likely have more requests to the same
server in the near future, called **site locality**. HTTP allows devices to keep TCP connections
open after transactions complete, called **persistent connections**. Using persistent connections
will avoid the slow setup cost and the slow-start phase.

There are two types of persistent connections: HTTP/1.0+ "keep-alive" and the modern HTTP/1.1
"persistent" connections.

Keep-alive handshaking is deprecated but still commonly used. Clients will send the header
"Connection: Keep-Alive" and servers will respond with the same header if they accept. It comes
along with a Keep-Alive header, which has an estimation of how long the connection is alive for
(timeout) and an estimate of how many more transactions the server is likely to keep the connection
alive for

    Connection: Keep-Alive
    Keep-Alive: max=5, timeout=120

HTTP/1.1 phased out support for keep-alive connections, replacing them with persistent connections.
HTTP/1.1 assumes all connections are persistent unless otherwise indicated. HTTP/1.1 applications
have to add a "Connection: close" header to indicate a connection should close after transaction is
complete.

For both cases, servers are free to close any persistent connection they deem idle or if they become
overloaded. Clients should be prepared to retry requests that they think failed, unless it may have
repeated side effects. All requests should have a correct Content-Length header so servers can
distinguish between requests.

HTTP/1.1 permits optional **request pipelining** over persistent connections, an optimization over
keep-alive connections. Multiple requests can be enqueued before the response arrives.

### Do's and Don'ts for Managing Connections
Any HTTP client, server, or proxy can close a connection at any time. Each HTTP response should have
an accurate Content-Length header. When a client/proxy receives a response that terminates due to
connection closing, they can match the Content-Length to determine the correctness of length.

HTTP applications have to be ready to handle unexpected closes. Clients can reopen connection and
retry requests, unless the transaction has side effects. A transaction is **idempotent** if it
yields the same results regardless of whether it is executed once or many times. Implementors can
assume these methods are idempotent: GET, HEAD, PUT, DELETE, TRACE, and OPTIONS. Clients should not
pipeline non-idempotent requests (such as POSTs).

# HTTP Architecture

## Web Servers
Web servers come in all flavors, shapes, and sizes but they all receive HTTP requests for resources
and serve content back to the clients. They perform several common tasks:

1. setup connection
2. receive request
3. process request
4. access resource
5. construct response
6. send response
7. log transaction

High performance servers support thousands of simultaneous connections. **Single-threaded** servers
process one request at a time until completion. This is easy to implement but causes serious
performance problems, is only appropriate for low-load servers and diagnostic tools.

**Multiprocess and multithreaded** servers dedicate multiple processes/threads to process requests
simultaneously. The threads/processes may be created on demand or in advance. Many servers put a
limit on the max number of threads and processes to make sure it doesn't consume too much memory or
resources.

In a **multiplexed** architecture, all connections are simultaneously watched for activity. When a
connection changes state a small amount of processing is performed. Work is done on a connection
only when there is something needs to be done; threads/processes are not tied up waiting on idle
connections.

Some systems combine multithreading and multiplexing architectures.

Servers support different kinds of resource mapping, the simplest uses the request URI to name a
file on the server's filesystem. The root folder is usually called the **document root** or
**docroot**.

**Virtually hosted** servers host multiple sites on the same web server, giving each site its own
distinct document root. It maps to document roots using the IP address or hostname in the URI or
Host header.

Servers can also map URIs to dynamic resources - programs that generate content on demand. A whole
class of specialized servers that do this are called **application servers**.

Servers also provide support for **server-side includes**, if a resource is flagged the server will
do additional processing on its contents before sending them to the client.

Web servers will construct a response message to send back to the client. If the generated response
includes a body, it will usually also contain:

- Content-Type header, describing the MIME type of the body - Content-Length header, size of body -
actual message body content

## Proxies
Proxies sit between clients and servers and act as "middlemen," shuffling HTTP messages back and
forth between the parties. HTTP proxy servers act as both web servers and we clients.

Proxies dedicated to a single client are **private proxies**, shared across numerous clients are
called **public proxies**. Here are a few examples of how proxies may be used:

- child filter to block access to adult content - document access control for audit trail - security
firewall - web cache that maintains local copies of popular documents - surrogate or reverse
proxies, which receive real requests but then initiate communication with other servers to locate
requested content - transcoder proxies will translate data representations (ie. GIF to JPEG) -
anonymizer proxies will provide privacy by removing identifying characteristics such as client IP
address or cookies

Proxies can be cascaded in chains called **proxy hierarchies**, messages are passed from proxy to
proxy until they reach the **origin server** and are then passed proxy to proxy until they reach the
client.

Proxy servers in a hierarchy are assigned **parent** and **child** relationships and the next
**inbound** (closer to the server) is called the parent and the next **outbound** (closer to the
client) is called the child.

These relationships can be dynamic, ie. a proxy which load balances might pick different parents
based on the current level of workload.

There are 4 common ways to cause client traffic to get to a proxy:

- modify the client (popular browsers support proxy configuration) - modify the network, called
**intercepting** proxy, without the client's knowledge or participation (ie. the corporate content
filter) - modify the DNS namespace (ie. surrogates or reverse proxies) - modify the web server to
redirect client requests to a proxy

Clients, such as modern web browsers, have multiple ways of configuring proxies:

- manual configuration - browser pre-configuration (maybe a distributor already did it for you) -
proxy auto-configuration (PAC), if you provide a URI to a JavaScript PAC file, the client will fetch
it and configure it - WPAD proxy discovery will detect automatically a configuration server

The original HTTP specification did not take into account proxies and virtual hosts, so http
requests did not have to contain the absolute URI. Now, requests to servers/proxies are identical
except requests to proxies require the absolute URI so proxies know where the origin server is.

This also created a problem with virtual hosts, most servers will require either an explicit
absolute URI from a proxy or that the request includes the "Host" header to determine which virtual
host to use.

Proxies should take into account that they might not receive the full absolute URI because sometimes
they remain invisible to the client. Generally:

- if a full URI is provided, use it - if partial and Host header is present, use the Host header -
otherwise, determine the origin server in another way (ie. surrogates usually know the real server's
address) or return an error message

The **Via** header lists information about each intermediate node, each time a message passes
through a proxy the node must be added to the end of the list. The list is a comma-separated list of
**waypoints**, each representing an individual proxy server or gateway hop. Example:

    Via: 1.1 cache.joes-hardware, 1.1 proxy.irenes-isp.net

The **Server** response header describes the software of the origin server. Proxies should take
extra care not to overwrite this header.

HTTP/1.1's **TRACE** method lets you trace a request message through a chain of proxies, observing
what proxies the message passes through and how each proxy modifies the request message. When it
reaches the origin server, the entire message is reflected back to the sender. You can use the
**Max-Forwards** header to limit the number of hops for TRACE and OPTIONS requests.

The **OPTIONS** method lets you discover supported functionality of a server. Using an asterisk as
the URI pertains to the entire server's supported functionality, or the request can inquire about a
particular resource. Example:

    OPTIONS * HTTP/1.1
    OPTIONS http://www.joes-hardware.com/index.html HTTP/1.1

The response will include header fields with various optional features, for example the **Allow**
header which specifies which methods are allowed:

    Allow: GET, HEAD, PUT

## Caching
Web caches are HTTP devices that automatically keep copies of popular documents. They have the
following benefits:

- reduce redundant data transfers - reduce network bottlenecks - reduce demand on origin servers -
reduce distance delays

Requests that arrive at a cache that can be served an available copy of the resource is called a
**cache hit**. If the cache must forward it to the origin server to retrieve and copy a resource,
it's called a **cache miss**.

Caches must check the origin server to check if their copies are still up to date, these checks are
called HTTP **revalidations**. Special requests may be made so they don't have to re-download the
entire content. A cache may do a GET with the **If-Modified-Since** header set. If the cache's copy
is still valid, it will usually get a **304 Not Modified** response. This is called a **revalidate
hit** or **slow hit**. On a **revalidate miss**, the origin server will send back the full content
in a normal 200 response.

The **cache hit rate** is the fraction of requests that are served from the cache, sometimes called
the **document hit rate**. Some people prefer the **byte hit rate** because it's more accurate of
overall data traffic.

Web browsers often have **private caches** which don't need much horsepower or storage space.
Private caches serve only one client. **Public caches** are shared among multiple clients and are
often called **proxy caches** or **caching proxy servers**. In practice, caches are often deployed
in hierarchies. Smaller caches are often closer to the client while larger caches are closer to the
origin server. Some networks have **cache meshes** which talk to each other to determine cache
hits/misses.

HTTP lets an origin server attach an expiration date using the **Cache-Control** and **Expires**
header. These headers dictate how long content should be viewed as fresh and eliminate the need for
freshness or revalidation checks. Example:

    +-----------------------------------------+------------------------------------+
    | Expires                                 | Cache-Control                      |
    +-----------------------------------------+------------------------------------+
    | HTTP/1.0 200 OK                         | HTTP/1.0 200 OK                    |
    | Date: Sat, 20 Jun 2002, 14:30:00 GMT    | Date: Sat 20 Jun 2002 14:30:00 GMT |
    | Content-type: text/plain                | Content-type: text/plain           |
    | Content-length: 11                      | Content-length: 11                 |
    | Expires: Fri, 05 Jul 2002, 05:00:00 GMT | Cache-Control: max-age=484200      |
    |                                         |                                    |
    | Lorem Ipsum                             | Lorem Ipsum                        |
    +-----------------------------------------+------------------------------------+

HTTP/1.0+'s Expires and HTTP/1.1's Cache-Control do the same thing but Cache-Control is preferred
because it uses relative time. Absolute dates depend on computer clocks being set correctly.

If the copy has expired, it does a revalidation. If the content has changed, a full response is made
with another Cache-Control header max-age set. If the content has not changed, a 304 Not Modified
response with a later max-age will be returned.

**Conditional Methods** allows clients to make a request and have the server send back an object
body only if the document is different from the copy in the cache. HTTP defines 5 conditional
request headers, the 2 most useful for cache revalidation are:

* If-Modified-Since: `<date>`
* If-None-Match: `<tags>`

If-Modified-Since was described earlier. **If-None-Match** headers use **entity tags** also known as
**ETags**, which are arbitrary labels attached to the document. They might contain a serial number,
version name, a checksum, or another fingerprint of the document content. ETags are set using the
**ETag** header in the response (value in quotes). An example transaction:

    GET /announce.html HTTP/1.0
    If-None-Match: "v2.6"
    ====
    HTTP/1.0 304 Not Modified
    ETag: "v2.6"

Requests may send several etag values, meaning the client has each copy of the document with those
specific tags:

    If-None-Match: "v2.4","v2.5","v2.6"

ETags support **strong validation** and **weak validation**. When a strong validation etag changes
for a document, it means the resource should be re-downloaded. When a weak validation etag is a
cache hit, it just means the documents are semantically equivalent. There could have been a minor
change, such as a spelling fix. Weak ETags are prefixed with a W/, example:

    ETag: W/"v2.6"
    If-None-Match: W/"v2.6"

Caches may be controlled, in decreasing order of priority a server can:

- add Cache-Control: no-store header to response - add Cache-Control: no-cache header to response -
add Cache-Control: must-revalidate header to response - add Cache-Control: max-age header to
response - add Expires date header to response

The no-store and no-cache headers prevent caches from serving unverified cached objects:

    Cache-Control: no-store
    Cache-Control: no-cache
    Pragma: no-cache

A response marked "no-store" forbids a cache from making a copy, caches would typically delete its
object and forward the response to its client. A "no-cache" response can actually be stored in the
local cache storage but it cannot be served without first revalidating the freshness with the origin
server. The Pragma: no-cache header is included in HTTP/1.1 for backward compatibility with
HTTP/1.0+.

Caches may be configured to serve stale (expired) objects, a response may have the Cache-Control:
must-revalidate header set to explicitly require a revalidation.

Clients may use Cache-Control request headers to tighten or loosen expiration constraints:

- Cache-Control: max-stale, cache is free to serve stale document - Cache-Control: max-stale=S -
Cache-Control: min-fresh=S, the document must still be fresh for at least S seconds in the future -
Cache-Control: max-age=S, cache cannot return a document that has been cached for longer than S
seconds - Cache-Control: no-cache, client won't accept cached resource unless it has been
revalidated. Also "Pragma: no-cache". - Cache-Control: no-store, cache should delete every trace of
document - Cache-Control: only-if-cached, client wants a copy only if it's cached

HTML 2.0 defined the `<meta http-equiv>` tag which lets HTML authors define HTTP headers without
editing server config files, example:

    <meta http-equiv="Cache-Control" content="no-cache">

Unfortunately, servers aren't guaranteed to parse HTML files and send these HTTP headers. Some
browsers do apply cache headers, but you should not depend on the client.

## Integration Points: Gateways, Tunnels, and Relays
### Gateways
**Gateways** speak HTTP on one side and a different protocol on another. They're interpreters and
are labeled in the format `<client-protocol>/<server-protocol>`.

* HTTP/FTP
* HTTPS/HTTP

**Server-side gateway** and **client-side gateway** describe what side the conversion is done for.
Server-side is HTTP/\* and client-side is \*/HTTP.

As an example, take the request:

    GET ftp://ftp.irs.gov/pub/00-index.txt HTTP/1.0
    Host: ftp.irs.gov

The request would follow this timeline:

    client => ..http req.. => HTTP/FTP gateway => ..ftp req.. => FTP server

The most common form of gateway is the **application server** that combines the destination server
and gateway into a single server. The first popular API for application gateways was the **Common
Gateway Interface (CGI)**, although more sophisticated interfaces for connecting web servers to
applications exist now (eg. Sinatra, Rails, Django, etc...)

For CGI, when a request comes to a server a new process is spawned and the query is handed off to
that running process. The CGI program will dynamically form a response for the client. **FastCGI**
attempts to solve the startup cost of spawning a new process for each request by keeping the program
running as a daemon.

Although CGI provides a clean protocol for developers, server extension APIs are available for
performance or plugging in additional behaviors.

The Internet community have also developed a set of standards/protocols to allow web applications to
talk to each other, most often called **web services**. Web services exchange information using XML
over SOAP or other agreed upon data formats and APIs.

### Tunnels
**Web tunnels** let you send non-HTTP traffic through HTTP connections, allowing other protocols to
piggyback on top of HTTP. The most common reason to use tunnels are to embed non-HTTP traffic into
an HTTP connection to send it through firewalls that only allow web traffic.

Tunnels are established via the HTTP CONNECT method. It's not specified by HTTP/1.1 specification
but is widely implemented. The CONNECT method asks a tunnel gateway to establish a TCP connection
and blindly relay data.

CONNECT requests' start line contain the hostname and port number instead of a path. Example:

    CONNECT hone.netscape.com:443 HTTP/1.0
    User-agent: Mozilla/4.0

### Relays
**HTTP relays** are simple HTTP proxies that don't fully adhere to the specification but process
enough HTTP to establish connections and then blindly forward bytes.

They should be deployed with great caution because they don't fully understand HTTP (ie. causing
keep-alive connections to hang because they don't properly process the Connection header).

## Web Robots
**Web robots** are automated user agents that act without human interaction. Some examples include:

- stock-graphic robot that repeatedly issues GETs to get stock data - a web census robot that crawls
the web to figure out its scale and evolution - search engine crawlers that collect documents and
index them - comparison shopping robots that gather and parses web pages to form catalogs

When a robot recursively follows web links it's called a **crawler** or **spider**. The initial set
of URLs it starts visiting is the **root set**. Crawlers need to do simple HTML parsing to extract
links and convert relative URLs to their absolute form. They need to be careful to not get stuck in
a **cycle** to avoid infinite loops, delays, and server overload. They also need a good data
structure to store their trail in (which pages they've already visited) and checkpoints to save
their progress to disk. Crawlers may attempt to **canonicalize** URLs into a standard form to detect
duplicates.

It's possible for malicious webmasters to create crawler traps, such as a web app that dynamically
generates links that point to the same web app. Or having a subdirectory be a soft link to its own
parent directory, creating an infinite loop. Or webmasters may do so unintentionally (ie. a calendar
app that has an infinite amount of "next month" links). Robots can avoid these and other
cycles/loops by:

- canonicalizing URLs - using breadth-first-search instead of depth-first-search - throttling page
visits - limiting URL size - URL/site blacklist - pattern detection - content fingerprinting - human
monitoring

It's polite to tell servers if you're a robot by setting some basic headers:

- User-Agent: name-of-robot - From: email address of robot's administrator - Accept: tell server
what media types are okay to send back to prevent wasted cycles, ie most robots are only interested
in text - Referrer: provide URL of document containing current request URL

Since robots can make tons of requests, it makes sense to use conditional requests so only fresh
content is downloaded.

The community understood the issues that robots could/did cause so they created **Robots Exclusion
Standard** but it's often referred to as **robots.txt**. If a robot follows this standard, it will
request the robots.txt file from the web site before accessing any other resource from that site. It
will check to see if it has permission to access any particular resource. If the response is:

- 2XX status, the robot must parse and follow the exclusion rules - 404, no exclusion rules exist
for this site and the robot is free to fetch any resources it finds - 401 or 403, access to this
site should be regarded as completely restricted - 503 temporary failure, robot should defer visits
until it can retrieve file - 3xx redirect, follow the redirection to find exclusion rules

robots.txt files have 3 types of lines: comments, blank, and rules. Rule lines are key/value pairs
just like HTTP headers:

    User-Agent: slurp
    User-Agent: webcrawler
    Disallow: /private

A robot will find the group of rules that match its User-Agent (or * wildcard) and follow those
rules. Disallow/Allow lines are used for permissions. When a URL is requested, a robot looks for the
first line that matches it and follows that rule. If none match, it's assumed that the resource is
allowed.

Standard HTTP protocols are used for caching robots.txt so that robots don't have to fetch the file
every time a request for a resource is made.

Guidelines/etiquette for robots can be found at: http://www.robotstxt.org/wc/guidelines.html

## HTTP-NG
**HTTP: The Next Generation (HTTP-NG)** was a proposal that addressed:

- complexity - extensibility - performance - transport dependence (use something else besides TCP/IP
stack)

The HTTP-NG working group proposed modularizing the protocol into 3 layers:

- message transport layer, focused on delivering opaque messages between endpoints. This layer would
support various substacks. - remote invocation layer, defines request/response functionality where
client can invoke operations on server resources. - web application layer, provides most of the
content-management logic. All of the HTTP methods/header parameters are defined here.

The HTTP-NG team concluded that it's too early to bring the HTTP-NG proposals to the IETF for
standardization. At this time, no major HTTP-NG effort is underway.

# Identification, Authorization, Security

## Client Identification and Cookies
HTTP started as an anonymous, stateless, request/response protocol. Client identification was born
out of necessity. Some mechanisms to identify users:

- HTTP headers that carry identity - Client IP address tracking - User login for authentication -
Fat URLs - Cookies

Some headers commonly used for identification are:

- From, user's email address - User-Agent, user's browser software - Referrer, page user came from
by following link

In practice, few browsers send the user's email address in the From header (think of the spam
mail!). The User-Agent is useful for customizing content specifically for browsers and their
attributes, but doesn't help identify the user. The Referrer header is also insufficient.

Early web pioneers tried using the IP address as a form of identification. Unfortunately, it had
some weaknesses:

- client IP describes the computer being used, not the user - ISPs dynamically assign IP addresses
to users when they log in - firewalls often obscure the user's IP address - proxies/gateways
typically open new TCP connections

A web server can explicitly ask a user to log in with a username/password. HTTP includes a built-in
mechanism to pass username information to web sites using the **WWW-Authenticate** and
**Authorization** headers. Once logged in, browsers continually send these headers on each request
so users can stay logged in.

URLs modified to include user state information are called **fat URLs**. The first time a user
visits a site, a unique ID is generated and stored into subsequent URLs. Some problems include:

- ugly URLs - can't share URLs - breaks caching - extra server load - escape hatches, too easy to
lose your unique id - not persistent across sessions

**Cookies** are the best current way to identify users and allow persistent sessions. They were
first developed by Netscape but are now supported by all major browsers. A **session cookie** is a
temporary cookie that is deleted when the user exits the site. A **persistent cookie** live longer
on disk and survives browser exits and computer restarts.

Cookies are an arbitrary list of name=value information and are set via the Set-Cookie or
Set-Cookie2 HTTP response headers. Cookies are sent to the server on each request. Because the
browser is responsible for storing cookie information, it's known as **client-side state**.

Some parts of a cookie are:

- domain - allh, whether all hosts or specific host gets the cookie - path, path prefix in the
domain associated with the cookie - secure, should be sent only on SSL connections - expiration,
expiration date - name - value

In general, a browser sends to a server only those cookies that the server generated. An example to
set a cookie with the domain attribute:

    Set-cookie: user="mary17"; domain="airtravelbargains.com"

When visiting www.airtravelbargains.com or specials.airtravelbargains.com, the request will have the
following header:

    Cookie: user="mary17"

There are two versions of cookies, the most widely used one being Netscape's original cookie
standard:

- http://home.netscape.com/newsref/std/cookie\_spec.html - http://www.ietf.org/rfc/rfc2965.txt

Version 0 (Netscape) cookies look like this:

    Set-cookie: name=val [; expires=date] [; path=p] [; domain=d] [; secure]
    Cookie: name1=value1 [; name2=value2] ...

    +------------+--------------------------------------------------------------+
    | Attribute  | Description                                                  |
    +------------+--------------------------------------------------------------+
    | name=value | Mandatory name/value pairs                                   |
    +------------+--------------------------------------------------------------+
    | expires    | Expiration date in format: Weekday, DD-Mon-YY HH:MM:SS GMT   |
    |            | GMT only, if it's not specified then cookie will expire when |
    |            | user's session ends.                                         |
    +------------+--------------------------------------------------------------+
    | domain     | Restrict cookie to only this hostname. Uses current hostname |
    |            | by default.                                                  |
    +------------+--------------------------------------------------------------+
    | path       | Restrict cookie to this particular/other paths that          |
    |            | starts with this value.  Defaults to current path.           |
    +------------+--------------------------------------------------------------+
    | secure     | Whether or not to send this cookie on non-SSL connections.   |
    +------------+--------------------------------------------------------------+

Version 1 (RFC 2965) is an extension that uses the Set-Cookie2 and Cookie2 headers and offers
backwards compatibility but is not completely supported. Some features:

- descriptive text with each cookie to explain its purpose - support forced destruction of cookies
on browser exit - max-age in relative seconds instead of absolute dates - control cookies by port
number - Cookie header carries back the domain, port, and path filters - version number - $ prefix
in cookie header distinguishes additional keywords from usernames

## Basic Authentication
HTTP provides a native **challenge/response** framework for authentication. The four phases are:

1. Request, GET on resource with no authentication.

       GET /family/jeff.jpg HTTP/1.0

2. Challenge, WWW-Authenticate header sent back with 401 Unauthorized response indicated user needs
   to provide username/password.

       HTTP/1.0 401 Authorization Required
       WWW-Authenticate: Basic realm="Family"

3. Authorization, client makes a GET request and sends the Authorization header with a hashed
   username/password.

        GET /family/jeff.jpg HTTP/1.0
        Authorization: Basic YnJpYW4tdG90dHK6T3ch

4. Success, Authentication-Info header is optionally set with additional info. Original resource
   gets sent back.

        HTTP/1.0 200 OK
        Content-type: image/jpeg

Clients will then continue sending the Authorization header on subsequent requests for
authorization.

Web servers group protected documents into **security realms**, each realm can have different sets
of authorized users.

**Basic authentication** is the most prevalent HTTP authentication protocol. The browser will send a
scrambled base-64 representation of the username and password joined by a colon, ie.
base46encode("username:password"). This also helps prevent administrators from accidentally viewing
usernames/passwords while administering servers (but is not useful for malicious intruders).

Basic authentication sends the username/password across the network in a form that can trivially be
decoded. Even if the username/password were encoded more securely, it would not prevent replay
attacks. It offers no protection against proxies or intermediaries that act as middlemen and can
leave the headers intact but modify the rest of the message. It's also vulnerable to
spoofing/phishing.

It can be made secure by combining it with encrypted data transmission (such as SSL) to conceal the
username/password.

## Digest Authentication
**Digest authentication** was developed as a compatible, more secure alternative to basic
authentication. In particular:

- it never sends passwords across the network in the clear - prevents capturing and replaying
authentication - optionally can guard against tampering with message contents

Digest authentication is not the most secure protocol possible, many needs are better suited with
TLS or HTTPS.

Instead of sending the password in clear text, a fingerprint or **digest** of the password is sent.
The client and the server both know the digest, so they can verify if it's correct or not. Digests
are one-way (ie. MD5 or SHA1), so malicious users cannot revert it into a plaintext password.

To prevent replay attacks, the server can pass a special **nonce** token to the client which changes
frequently. The client appends this token to the password before computing the digest. Nonces are
passed from server to client in the WWW-Authenticate challenge and Authentication-Info response
header.

RFC 2617 suggests this hypothetical nonce formulation:

    BASE64(time-stamp H(time-stamp ":" ETag ":" private-key))

Requests/responses may also digest the message body to prevent man-in-the-middle attacks which take
the authorization headers and change the message body.

## Secure HTTP
### Overview
Previous authentication techniques worked well to identify/authenticate users in a friendly
community, but they aren't strong enough to protect important transactions from a hostile community.
For secure transactions, we combine HTTP with digital encryption technology. It needs to provide:

- server auth, clients need to know they're talking to the real server - client auth, servers need
to know they're talking to the real user - integrity of data - encryption - efficiency - ubiquity -
administrative scalability - adaptability - social viability

**HTTPS** is the most popular secure form of HTTP. When using it, HTTP request/response data is
encrypted before being sent across the network. It works by providing a transport-level
cryptographic security layer, either **Secure Sockets Layer (SSL)** or its successor **Transport
Layer Security (TLS)** underneath HTTP.

Most of the encoding/decoding happens in the SSL layer, so web servers don't need to change much to
use them:

- HTTP, application layer - SSL or TLS, security layer &lt;--- layer inserted for HTTPS - TCP,
transport layer - IP, network layer - Network interfaces, data link layer

### Digital Cryptography Primer
**Ciphers** are algorithms for encoding text to make it unreadable. The original message is called
**plaintext** or **cleartext**. After the cipher is applied to the message it's often called a
**ciphertext**.

**Keys** are numeric parameters that change the behavior of ciphers, in case the cipher algorithm
and/or message fell into the wrong hands.

**Symmetric-key cryptosystems** are algorithms that use the same key for encoding and decoding. The
sender and receiver have a shared secret (key) that they both use for encoding/decoding messages.
Some popular symmetric-key cipher algorithms are DES, Triple-DES, RC2, and RC4.

It's important that the key stay secret because in many cases the cipher algorithm and ciphertext
are public knowledge. A good algorithm will force the enemy to try every possible key value
possible, called a **brute force** or **enumeration attack**.

The number of possible key values depends on the number of bits in the key and how many of the
possible keys are valid. An 8-bit key would have 2^8 or 256 possible values. 40-bit keys are
considered safe enough for small, noncritical transactions. 128-bit keys are considered very strong
for symmetric-key cryptography.

Shared keys are an administrative nightmare, if there are N nodes and each node has to talk securely
with all other N-1 nodes, there are roughly N^2 total keys. It may also be difficult to securely
transmit shared keys.

**Asymmetric-key cryptosystems** are algorithms that use different keys for encoding and decoding.
Public-key cryptography uses two asymmetric keys, one for encoding messages and another for decoding
the host's messages. The encoding key is publicly known to the world but only the host knows the
private decoding key.

A popular asymmetric cipher is **RSA** which has many libraries that you can use. It's still
difficult to crack even if the attacker has:

- the public key - a piece of intercepted ciphertext - a message and its associated ciphertext

Public-key cryptography algorithms tend to be computationally slow. In practice, mixtures of both
symmetric and asymmetric schemes are used. For example, it's common to use public-key cryptography
to setup a secure channel and send over a shared private key to encrypt further messages.

**Digital signatures** are checksums that verify that a message has not been forged or tampered
with. Because only the author has the author's top-secret private key, only the author can compute
these checksums - acting as a personal "signature" from the author. If a malicious assailant
modified the message in-flight, the checksum would no longer match. Signatures are often generated
using asymmetric, public-key technology.

**Digital certificates** are identifying information, verified and signed by a trusted organization.
Some forms of identification are harder to forge (ie. passports) so we can trust them more than
something relatively easy to forge (ie. a business card).

Basic digital certificates commonly contain:

- subject's name (person, server, organization, etc.) - expiration date - certificate issuer (who is
vouching for the certificate) - digital signature from the certificate issuer

### HTTPS Details
HTTPS combines the HTTP protocol with a powerful set of symmetric, asymmetric, and certificate-based
cryptographic techniques, making HTTPS very secure but also very flexible and easy to administer.

In normal, nonsecure HTTP, the scheme prefix of the URL is http. In the secure HTTPS protocol, the
scheme prefix of the URL is https. If a browser encounters the http scheme, it opens a connection to
a server on port 80 (default) and sends plain-old HTTP commands. If the URL has an https scheme, the
browser opens a connection to the server on port 443 (default) and then "handshakes" with the
server, exchanging some SSL security parameters with the server in a binary format, followed by the
encrypted HTTP commands.

SSL traffic is a binary protocol, which is why it uses a different port so servers won't mistaken
binary traffic on port 80 as junk and close connections.

In HTTPS, the client first opens a connection to port 443, then the client and server initialize the
SSL layer, negotiating cryptography parameters and exchanging keys. When the handshake completes,
the initialization is done, and the client can send request messages to the security layer. These
messages are encrypted before being sent to TCP.

The SSL handshake consists of:

- exchanging protocol version numbers - select a cipher that each side knows - authenticate the
identity of each side - generate temporary session keys to encrypt the channel

Clients no longer typically have certificates, but servers still do. Server certificates typically
show the organization's name, address, server DNS domain name, and other information.

SSL is a complicated binary protocol, thankfully, several commercial/open source libraries exist to
make it easier to program SSL: OpenSSL http://www.openssl.org

# Entities, Encodings, and Internationalization
## Entities and Encodings
HTTP uses headers to ensure that messages can be identified, unpacked, and arrives complete:

- Content-Type and Content-Language to identify - Content-Length and Content-Encoding to unpack -
Content-MD5 checksums to make sure it's complete and accurate

HTTP messages are crates and entities are cargo:
    HTTP/1.0 200 OK
    Server: Netscape-Enterprise/3.6
    Date: Sun, 17 Sep 2000 00:01:05 GMT
    Content-type: text/plain                   <--.
    Content-length: 18                         <----- Entity
                                               <---.
    Hi! I'm a message!                         <--.

Entity headers are:

* Content-Type, the kind of object carried by the entity
* Content-Length, the length/size of the message in bytes
* Content-Language, language of object
* Content-Encoding, any transformation performed on object
* Content-Location, alternate location
* Content-Range, if partial entity define which pieces included
* Content-MD5, checksum of contents
* Last-Modified, date which content was created/modified on server
* Expires, date/time which entity will become stale
* Allow, request methods are legal on this resource
* ETag, unique validator for caching
* Cache-Control, how this document can be cached

The Content-Type header field describes the MIME type of the entity body, a standardized name that
describes the underlying type of media. Common ones are:

- text/html - text/plain - image/gif - image/jpeg - audio/x-wav - model/vrml -
application/vnd.ms-powerpoint - multipart/byteranges - message/http

The Content-Type header also supports optional parameters, ie. charset:

    Content-Type: text/html; charset=iso-8859-4

HTTP supports **multipart bodies** which are usually used in form submissions and range responses.
Multipart bodies are multiple messages sent as a single one where each component has headers/body.
For example, a multipart form will allow you to send different content types (useful for file
upload):

    <form enctype="multipart/form-data" method="post">
      <input type="text" name"filename" />
      <input type="file" name="filedata" />
    </form>

    Content-Type: multipart/form-data; boundary=AaBo3x
    --AaBo3x
    Content-Disposition: form-data; name="filename"
    Random
    --AaBo3x
    Content-Disposition: file; filename="imagefile.gif"
    Content-Type: image/gif
    ... binary ..

The content body may also be encoded, useful for compressing or encrypting:

1. Server generates original response with Content-Type and Content-Length.
2. Server encodes body, message still has the same Content-Type but changes Content-Length to be the
   new length value. It adds Content-Encoding.
3. Receiver gets encoded message, decodes it, obtains original.
  
    HTTP/1.1 200 OK
    Content-Length: 6096
    Content-Type: image/gif
    Content-Encoding: gzip
    [...]

Some common content-encoding tokens are gzip, compress, deflate, and identity. Identity means no
encoding was done, which can be assumed if Content-Encoding header is missing.

Clients can tell servers which encodings they support with the Accept-Encoding header:

    GET /logo.gif HTTP/1.1
    Accept-encoding: gzip;q=0.5, compress;q=1.0, *;q=0
    [...]

The Q parameter indicates quality factor, 0 meaning the client does not want and 1 meaning highest
preference.

## Internationalization
HTTP supports many languages and alphabets. Servers need to tell clients the alphabet and languages
of each document so the client can properly unpack it. These are set using the Content-Type and
Content-Language headers. Clients must also tell servers which languages/encodings to use by sending
the Accept-Charset and Accept-Language headers. Example:

    Accept-Language: fr, en;q=0.8
    Accept-Charset: iso-885901, utf-8

The charset tells you how to convert from entity content bits into characters in a particular
alphabet. They're standardized in the MIME character set registry and maintained by IANA
(http://www.iana.org/assignments/character-sets).

Bits to character conversion happens in two steps. First, the bits are converted to a numbered
character in a particular coded character set. Then the character code is used to select an element
in the set (determined by the character encoding). Internationalized character systems isolate
semantics (letters) from the presentation (graphical forms). HTTP only concerns itself with
transporting the character data and associated language/charset labels. If an incorrect character
set is given, the client will render characters incorrectly.

The combination of the character encoding and character set is called a **MIME charset**, which are
used by HTTP in the Content-Type and Accept-Charset headers. Some common ones are: us-ascii,
iso-8859-\*, utf-8.

If no charset is given in the response headers and the client cannot infer a character encoding from
the document, it assumes iso-8859-1.

Character Set Terminology:

* character is an "atom" of writing (letter, numeral, punctuation mark, etc...). The **Universal
  Character Set** aka **Unicode** has named many characters in many languages, which are often used
  to conveniently/uniquely name them.
* glyph is a graphical shape to represent a character.
* coded character is a unique number assigned to a character.
* coding space is a range of integers used for character code values.
* code width is the number of bits in each character code.
* character repertoire is a particular working set of characters
* coded character set maps numeric character codes to real characters
* character encoding scheme is an algorithm to encode numeric codes into bits and vice-versa.

Interestingly, HTTP messages (headers, URIs, etc.) use US-ASCII. iso-8859 uses an extra bit and is a
superset of ASCII. It's not large enough to hold all characters so it uses specialized sets for
different regions. iso-8859-1 aka Latin1 is the default charset for HTML. Universal Character Set
(UCSD) is a worldwide standards effort to combine all world's characters into a single coded
character set (Unicode).

UTF-8 is a variable-length encoding that is backwards compatible with US-ASCII. The first byte tells
the length of the encoded character in bytes and subsequent bytes contains six bits of code value.
The first byte will set as many 1 bits as there are bytes in the character, followed by a 0 flag.

Examples:

* 0ccccccc (ascii compatible, 7 bits of code value)
* 110ccccc 10cccccc (110 = 2 bytes)
* 1110cccc 10cccccc 10cccccc (1110 = 3 bytes)

**Language tags** are standardized strings that name languages. Examples:

* fr = French
- en = English - de = German - en-US = US English

URIs don't provide much support for internationalization, they're comprised of a subset of US-ASCII
characters. URI characters have 3 categories:

* unreserved, may be used in any part of the URL
* reserved, have special meanings in many URIs, shouldn't be used in general
* escape, safely insert reserved and other unsupported characters

The two hexadecimal digit characters in an escape sequence represent the code for a US-ASCII
character. HTTP applications should unescape URIs only when the data is needed, otherwise just
forward them as is. HTTP applications should ensure that no URIs are unescaped twice. Escape values
should fall into US-ASCII range only (0-127). Sorry, no international characters.

HTTP messages may only contain US-ASCII character set, but not all applications follow the spec.
Date formats are specified in the spec for legal GMT formats. Once again, applications should be
aware that not all clients/server follow the spec.

## Content Negotiation and Transcoding
**Content negotiation** methods allow clients/servers to determine which **variant** of a resource
to serve/receive (ie. French vs English versions).

There are 3 categories:

* **client-driven** Client makes request, server sends choices back, client chooses. Easy to
  implement but adds latency.
* **server-driven** Server examines client's request headers and decides what version to serve. If
  decision is not obvious though, the server must guess.
* **transparent** An intermediate device (ie. proxy) does request-negotiation on client's behalf.
  Offloads negotiation from server, no latency, but no formal spec.

An example of client-driven is sending back an HTML document with links to each variant of the
document. Or responding with a 300 Multiple Choices response.

We've seen examples of Server-Driven negotiation using the Accept, Accept-Language, Accept-Charset,
and Accept-Encoding request headers. Servers can also match up responses with other client request
headers, such as User-Agent (knowing what technology the client's browser supports).

When serving variants of documents, the server must take caching into consideration. You don't want
to serve a cached French copy of the document to a German viewer. Cache proxies use the "Vary"
header, a server will list the headers it takes into account when responding. Caches must match up
the request headers with those listed in "Vary" for a hit.

If the server doesn't have a document available that matches the client's request, it may
**transcode** its existing document into something the client wants: HTML => WML, high-res =>
low-res, colored image => black/white image.

# Content Publishing and Distribution

## Web Hosting
**Web hosting** is the storing, brokering, and administering content resources. **Dedicated
hosting** refers to a client having his/her own dedicated web server for their site. **Shared
hosting** or **virtual hosting** occurs when two or more people share the same physical machine to
host separate sites.

An oversight in HTTP/1.0 assumed that every site would be unique to one physical machine, so the
host information wasn't given in requests making virtual hosting impossible. Enhanced HTTP/1.0 and
HTTP/1.1 now require the full URL. For backwards compatibility, web hosts may also give each virtual
site its own IP Address or determine which site based on the Host header.

Mirrored server farms exist to duplicate/serve content. There is a **master origin server** and
**replica origin servers**. A simple way to implement this is with a switch, with the outside world
talking to the switch and the switch delegating between each servers. All together, this is usually
called a **server farm** and is used to:

* prevent downtime
* handle traffic spikes
* provide redundancy for network outages or losses

A **content distribution network** or CDN is a network that distributes specific content so it may
be served faster or more reliable. Distributing content usually brings it closer to end users,
reducing latency.

## Publishing Systems
**Web Distributed Authoring and Versioning (WebDAV)** adds collaboration to web publishing by
extending HTTP. Some new HTTP methods:

* PROPFIND retrieves the properties of a resource
* PROPPATCH sets 1+ properties on 1+ resources
* MKCOL creates collections
* COPY copies resource/collection
* MOVE moves resource/collection
* LOCK locks 1+ resources
* UNLOCK unlocks 1+ resources

WebDAV also modifies the existing methods: DELETE, PUT, and OPTIONS. It uses XML to provide extra
information on how to handle data and formatting complex rules (hierarchies, multiple resources,
selective application, etc...). The schema is defined in the specification RFC 2518.

Some headers introduced are:

* DAV to communicate WebDav capabilities of the server
* Depth to specify recursive depth of an action
* Destination to assist COPY or MOVE
* If defines a set of conditionals for a locked resource
* Lock-Token used by UNLOCK method
* Overwrite option used by COPY/MOVE
* Timeout request header specified by client

WebDAV supports **exclusive write locking** and **shared write locking** of a resource/collection.
The state is set with LOCK/UNLOCK. Example:

    LOCK /ch-publish.fm HTTP/1.1 
    Host: minstar 
    Content-Type: text/xml 
    Content-Length: 201

    <?xml version="1.0"?> 
    <a:lockinfo xmlns:a="DAV:">
      <a:lockscope><a:exclusive/></a:lockscope> 
      <a:locktype><a:write/></a:locktype> 
      <a:owner><a:href>AuthorA</a:href></a:owner>
    </a:lockinfo>

For more information about WebDav, refer to:

* http://www.ietf.org/rfc/rfc2518.txt?number=2518
* http://www.ietf.org/rfc/rfc3253.txt?number=3253

## Redirection and Load Balancing
HTTP messages often travel through many different network tools, including: HTTP redirection, DNS
redirection, anycast routing, policy routing, IP MAC forwarding, IP address forwarding, the Web
Cache Coordination Protocol (WCCP), Intercache Communication Protocol (ICP), Hyper Text Caching
Protocol (HTCP), Network Element Control Protocol (NECP), Cache Array Routing Protocol (CARP), and
Web Proxy Autodiscovery Protocol (WPAD).

Redirections occur to:

* perform HTTP transactions reliably
* minimize delay
* conserve network bandwidth

Most redirection setups work together with load balancing to deliver content faster and spread
incoming messages across multiple servers.

General redirection methods are:

* HTTP redirection, initial request goes to 1st server which sends back a redirect response to
  chosen server
* DNS redirection, DNS server decides which IP address to send back for hostname
* Anycast addressing, several servers use same IP address and masquerades as a backbone router.
* IP Mac forwarding, a network element reads packet's destination and perhaps re-routes it
* IP Address forwarding, layer-4 switch evaluates a packet's destination port and perhaps changes
  the IP address to proxy or mirrored server

Proxy/cache redirection techniques:

* Explicit browser config, client is configured to talk to a nearby proxy/cache
* Proxy auto-configuration (PAC), client retrieves a PAC file which will configure it to talk to a
  nearby proxy/cache
* Web Proxy Autodiscovery Protocol (WPAD), asks config server for PAC file
* Web Cache Coordination Protocol (WCCP), router evaluates packet's destination and redirects them
  as necessary
* Internet Cache Protocol (ICP), proxy cache query group of sibling caches for requested content
* Cache Array Routing Protocol (CARP), protocol that allows caches to forward a request to a parent
  cache
* Hyper Text Caching Protocol (HTCP), proxy caches can query a group of sibling caches for requested
  content

DNS round robin is a common and simple redirection technique. One hostname may represent more than
one IP address/physical machines for load balancing.

    % nslookup www.cnn.com
    Name:      cnn.com
    Addresses: 207.25.71.5, 207.25.71.6, ... more ip addresses ...
    Aliases:   www.cnn.com

Most clients just use the first address, so servers usually rotate addresses. Most clients will also
cache the DNS lookup, so it doesn't work well for a single client. It does a good job for multiple
clients.

Browsers can be configured to talk to a proxy instead of the server. The proxy can them determine
which server to send the request to.

## Logging and Usage Tracking
Logging is useful for tracking errors and/or to generate statistics. Most commonly logged fields of
requests/responses are: HTTP method, version, URL, status code of response, size of
request/response, timestamp, referrer and user-agent header values.

There's a **Common Log Format** which logs these fields: remotehost, username, auth-username,
timestamp, request-line, response-code, response-size. Example:

    209.1.32.44 - - [03/Oct/1999:14:16:00 -0400] "GET / HTTP/1.0" 200 1024 
    http-guide.com - dg [03/Oct/1999:14:16:32 -0400] "GET / HTTP/1.0" 200 477 
    http-guide.com - dg [03/Oct/1999:14:16:32 -0400] "GET /foo HTTP/1.0" 404 0

The **Combined Log Format** adds two additional fields: Referrer and User-Agent header values.