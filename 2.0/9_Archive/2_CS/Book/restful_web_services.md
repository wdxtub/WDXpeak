# RESTful Web Services

**Representational State Transfer** or REST, described in Roy Fielding's dissertation, is an
architecture for designing web services that emphasizes HTTP's strength and simplicity. There is no
definitive specification and an application is never said to be "REST-compliant", instead we say an
application is "RESTful" - just as you can write functional code in a language designed for object
oriented programming.

This book introduces the **Resource-Oriented Architecture**, which is a set of best practices for
developing RESTful web services. Along the way, it also describes what REST means to
clients/services and how to implement it.

# Programmable Web

Some qualities of RESTful web services are:

* they use the HTTP method to distinguish between actions
* they use the URI to distinguish between resources and components (ie. scoping information for a
  list of resources)

The web is full of data, but instead of downloading all the data at once you get a web browser and
interact with **web services** like search engines, movie databases, book databases, etc... to
retrieve data, store/search data, and perform other actions.

The programmable web works the same way, except other clients exist besides browsers (or you can
develop your own client) and instead of HTML pages you usually get an easy-to-parse XML or JSON
response.

Websites such as google.com and amazon.com are also web services. URIs are used to fetch data and
the responses are in HTML, made for human consumption instead of for a computer to parse.

More commonly known as web services are APIs which give access to data such as Amazon's S3 or
Delicious' API. Web services are also commonly used internally in distributed architectures.

This book splits web services into 3 categories:

* RESTful resource-oriented
* RPC-style
* REST-RPC hybrid

RESTful resource-oriented architectures use HTTP verbs to distinguish actions and will have URIs
designed around **resources**. A URI represents a thing and the HTTP verb that the client sends will
tell the server what to do with that particular thing.

RPC style architectures tend to convey action information in other ways than the standard HTTP
verbs. Ie. they might use the query portion of the URI:

    GET http://api.example.com/?q=DeleteUser&id=1

They may also define their own **envelope** standard instead of using HTTP. For example, all
requests may be POSTs with XML entity bodies. The server determines what to do by parsing the entity
body.

# Writing Web Service Clients

A web service client is just a specialized HTTP client that's programmed for a specific web service.
It's built to make a request and parse the response. You can use your language's standard library to
do this.

Wrappers make developing clients easier because an API is tailored to one particular service.
Instead of making raw HTTP GET/PUT requests to Amazon's S3 library, it's easier to use the
amazon-aws library.

The SOAP RPC community has WSDL, for RESTful web services there is the less widely known **WADL -
Web Application Description Language**. The developer can write a single WADL file which describes
the resources and a client API will be generated for it.

**ActiveResource** is another library that's custom made as the client library opposite to Rail's
REST support.

Ruby has **open-uri** which is easy to use but only supports GET requests and does not allow you to
set headers. The author has created his own library, **rest-open-uri** which can be used to develop
REST clients. You can also dive down into **net/http** which exposes the raw HTTP
requests/responses. On the command line, **curl** is a useful utility.

To process the response, you'll need a good XML or JSON library depending on which entity encoding
is used for the HTTP responses. There are two types of XML parses: the DOM/tree based strategy and
the SAX/pull based strategy. The DOM based libraries will parse the entire document at once while
the SAX based one will allow the programmer to define hooks to events and use the XML document as a
stream of data.

Ruby has **REXML** which is the default XML parser that supports both DOM and SAX interfaces. The
author does not recommend it because it only works with well formed documents. To handle bad markup,
the author recommends using **hpricot** available http://code.whytheluckystiff.net/hpricot/,

Here's a sample Delicious client written in Ruby:

    #!/usr/bin/ruby -w 
    require 'rubygems' 
    require 'open-uri' 
    require 'rexml/document'

    def print_my_recent_bookmarks(username, password)
      response = open('https://api.del.icio.us/v1/posts/recent', 
                      :http_basic_authentication => [username, password])
      xml = response.read  
      document = REXML::Document.new(xml)
      REXML::XPath.each(document, "/posts/post") do |e|
        # Print the bookmark's description and URI
        puts "#{e.attributes['description']}: #{e.attributes['href']}" 
      end
    end

    username, password = ARGV 
    unless username and password
      puts "Usage: #{$0} [username] [password]"
      exit 
    end
    print_my_recent_bookmarks(username, password)

# What Makes RESTful Services Different

Amazon's Simple Storage Service (S3) is an example of a popular RESTful service. S3 has an
object-oriented design. There are two concepts: buckets and objects. An object is a file and
associated metadata (like filename or permissions) and are stored in named buckets.

S3 has a simple RESTful API. The developer has access to two types of resources (the buckets and
objects mentioned above). To perform actions on those resources, developers just need to issue plain
HTTP requests. The HTTP method used will distinguish between which action:

    +-----------------+-----------------+--------------+---------------+--------+
    |                 | GET             | HEAD         | PUT           | DELETE |
    +-----------------+-----------------+--------------+---------------+--------+
    | /               | List buckets    | -            | -             | -      |
    +-----------------+-----------------+--------------+---------------+--------+
    | /{bucket}       | List bucket's   | -            | Create bucket | Delete |
    |                 | objects         |              |               | bucket |
    +-----------------+-----------------+--------------+---------------+--------+
    | /{bucket}/{obj} | Download object | Get metadata | Set value     | Delete |
    |                 |                 |              | and metadata  | object |
    +-----------------+-----------------+--------------+---------------+--------+

Some examples:

* GET / => get the list of available buckets
* PUT /nantucket => creates a new bucket named "nantucket"
* PUT /nantucket/file1 => uploads a new file named "file1"

RESTful services have obvious APIs because it follows the HTTP specs. URIs map to resources (instead
of actions) and the HTTP actions are used to distinguish between verbs (ie. create vs delete).

# Resource-Oriented Architecture

The properties of a Resource-Oriented Architecture are:

* addressability - scoping information should be kept in the URI
* statelessness - keeping application state on the client and resource state on the server
* connectedness - "Hypermedia as the engine of application state", linking resources together
* uniform interface - using the HTTP methods as they are defined in the spec

The components that make up ROA are resources, their names/URIs, their representations, and the
links between them.

A **resource** is anything that's important enough to be referenced on your web service. It has at
least one URI which is the name and address of the resource. URIs should be descriptive, have
structure (vary in predictable ways) and should contain scoping information (aka
**addressability**).

Some example URIs are:

* http://www.example.com/software/releases/1.0.3.tar.gz
* http://www.example.com/software/releases/latest.tar.gz
* http://www.example.com/search/Jellyfish
* http://www.example.com/sales/2004/Q4
* http://www.example.com/bugs/by-state/open

**Statelessness** means every HTTP request happens in complete isolation. Possible states of a
resource should be given their own URI. For example, Google handles the state of pagination in its
URI using the query string (?page=1). ROA requires that state be stored on the client side and sent
to the server on each request.

Of course that's only the case for **application state**. Application state deals with the session,
like what page a client is currently on. State that lives in the database is perfectly fine and is
called **resource state**. This is state like a user's email address, or the current state of a blog
post.

While a resource has useful information, its **representation** is what the client gets. The
representation may be in different parse-able formats including HTML, XML, or JSON. It may be in
different encodings or different languages. A client can tell the service what sort of
representation it expects using **content negotiation** (via the Accepts header), or the service
designer may place the content information within the URI. For example:

    http://www.example.com/en/search/Jellyfish.json

In most RESTful services, representations of resources are hypermedia documents which contain links
to other documents. The server guides the client's path by serving "hypermedia": links and forms
inside hypertext representation. This is the **connectedness** of ROA. An example of this is a
search engine. You start from http://google.com, enter data into a form, and get an HTML document
back full of links to explore the web.

**Uniform interface** means using the HTTP methods as they were defined in the HTTP specification.
This makes RESTful APIs, like S3's, more obvious because they all follow the same interface:

* GET to retrieve a representation of a resource
* PUT to a new URI to create a new resource
* POST to an existing URI to create a new resource
* PUT to an existing URI to modify an existing resource
* DELETE to delete an existing resource
* HEAD to retrieve only the metadata of a resource
* OPTIONS to check which HTTP methods are supported on a URI

The difference between **POST vs PUT** is subtle. GET, HEAD, PUT, and DELETE actions are supposed to
be **idempotent**. This means there's no difference between making one request vs making many. They
were originally defined as idempotent methods for faulty networks. GET and HEAD are **safe**
requests meaning they should not change any state on the server (actually, it's okay to have
side-effects like hit counters - but it shouldn't change state where it matters).

POST is not idempotent. If your request changes state and is not idempotent, that's an indication
that it should be using POST. Another subtle difference between PUT and POST can be seen from the
HTTP specification:

* PUT - used to upload data from the client to the server at a named resource
* POST - various reasons to use including uploading data from a form to be processed by some gateway
  application

Rails applications tend to map POST/GET/PUT/DELETE to Create/Read/Update/Delete, which mostly works.
Amazon uses the PUT method to create buckets/objects because the path for both actions uses an
already named resource. Naming the bucket/object occurs on the client-side (and is idempotent).
Rails applications tend to use incremental IDs in their paths which are determined on the server
side, so requests are no longer idempotent. Hence POST is commonly used.

HTTP was designed with idempotent/safe requests in mind because of unreliable network connections.
Some clients are designed to with this assumption. Web accelerator was a product which pre-fetched
links (using GET) to speed up a user's experience on the web. It was a disaster because developers
used links and GET requests to perform non-safe actions. So the product ended up changing server
state, such as deleted resources in the database.

# Read-Only Resource-Oriented Services

The author shows us how he would design a read-only ROA web service. His particular service is for
retrieving maps of locations around the universe (including other planets!).

The steps he goes through are:

1. Figure out the data set
2. Split the data set into resources, and for each resource: 1. Name the resource with a URI 2.
   Expose a subset of the uniform interface 3. Design the representation(s) accepted from the client
   4. Design the representation(s) served to the client 5. Integrate resource into existing
   resources using hypermedia links/forms 6. Consider typical course of events: what's supposed to
   happen? 7. Consider error conditions: what might go wrong?

A resource is anything interesting enough to be the target of a hypermedia link. Some examples are:

* Predefined one-off resources (like homepage or S3's home bucket)
* A resource for every object exposed through the service
* Resources representing the results of algorithms applied to the data set, such as a collection of
  objects from a search result or pagination

Representing and naming resources is similar to OOP. Whereas procedural code is split into
procedures, OOP code is split into objects. RPC-style services tend to name functions like doSearch
or subscribeFeed. RESTful services will have URIs named after nouns: /searches/jellyfish or
/subscriptions/1337;24

The 3 basic rules for URI design:

1. Use path variables to encode hierarchy: /parent/child
2. Put punctuation in path variables to avoid implying hierarchy:

     /parent/child1;child2 or /parent/child1,child2

3. Use query variables to provide input to algorithms:

     /search?query=jellyfish&start=20

You can represent your resources with a wide variety of formats ranging from XML to JSON. The author
settles on using plain old XHTML. Linked anchors are also provided in documents for connectedness:

    <!-- doctype & head -->
    <body>
      <ul class="planets">
        <li><a href="/Earth">Earth</a></li>
        <li><a href="/Venus">Venus</a></li>
      </ul>
    </body>

Using request headers to distinguish between resource representations aren't recommended. Instead,
clients can just tweak the URI to get a different representation. Conditional GETs are recommended.

When an error occurs, your service should return something in the 3xx-5xx range. Redirects are
useful to provide an alternate location. 4xx should tell the clients their error. 5xx for server
errors that clients cannot fix themselves.

# Read/Write Resource-Oriented Services

User accounts are going to be implemented as resources which you'll be able to
create/read/update/delete via the API. This will allow clients to create new user accounts straight
from their application.

When writing resources, you'll have to take authentication and authorization into account. In this
case, the author uses HTTP Basic authentication via the WWW-Authenticate header. He also uses HTTPS
to make sure passwords aren't sent in the clear.

To send data from the client to the service, clients may put their PUT or POST data in any format. A
good lightweight one is just **application/x-www-form-urlencoded** which is the standard for HTML
forms. It works well with key value pairs and looks like the query string portion of a URI:
"color1=blue&color2=green&color3=red".

The example code uses the **rest-open-uri** gem which supports POSTing/PUTing to URIs (unlike
vanilla open-uri) and is also much more easier to use than the standard net/http library which comes
along with Ruby.

Since clients determine the named resource of a user account, PUTs are used instead of POSTs. To
create a new user:

    PUT /users/{username} with a x-www-form-urlencoded body of attributes

If the user is created successfully, a 201 code can be returned with the Location header set. If the
user already exists and was updated, a 200 OK response is sent back.

If the client sends data that's not in the expected format, the service will send back a 415
Unsupported Media Type. If the client tells the service to put a resource in an impossible state,
the service will respond with a 400 Bad Request or 409 Conflict. If authentication or authorization
fails, the service will send back a 401 Unauthorized.

# Service Implementation

In this chapter, the author shows us how to go from an existing RPC-style service to a RESTful one.
He mentions the trade-offs of doing so and shows us how to implement a ROA service using Rails. The
code in this book is using an older version of Rails (v1.2.x).

Ruby and Rails both have a large base to work on. For implementation, we'll be using:

* acts\_as\_taggable plugin
* http\_authentication plugin
* atom-tools gem

The delicious API was chosen as the RPC-style service and documentation can be found here:
http://del.icio.us/help/api/

The service is available at https://api.del.icio.us/v1/ and exposes various RPCs via HTTP GET calls.
Some example functions are:

* /posts/get to search your posts by tag or date
* /posts/add to create a new bookmark for a URI
* /posts/delete to remove a bookmark

A RESTful service can be built into Rails controllers. A blog example:

* POST to /weblog would initiate a WeblogController#create Since Rails is in charge of creating the
  URI (which uses the id), a POST is used instead of a PUT. This falls inline with using POST to do
  a database append operation.
* GET to /weblog/1 to retrieve a blog post via WeblogController#read
* PUT to /weblog/1 to update a blog post via WeblogController#update
* DELETE to /weblog/1 to delete a blog post via WeblogController#destroy

RESTful controlls follow a uniform interface that fits with HTTP's already defined spec. Browsers
only support GET/POST methods, but Rails gets passed this by passing a special "\_method=PUT" or
"\_method=DELETE" parameter in the x-www-form-urlencoded body of POST requests.

The author takes the existing delicious API and starts mapping them to Rails controller/actions:

* /posts/get becomes:

    GET /users/{username}/bookmarks via BookmarksController#index

* /posts/add becomes:

    POST /users/{username}/bookmarks via BookmarksController#create

* /posts/delete becomes:

    DELETE /users/{username}/bookmarks/{md5} via BookmarksController#delete

One of the added features is that users may look at other user's bookmarks, since the paths include
the username.

The implemented service will accept multiple representations of resources from the client. A common
one being XML:

    <user>
      <name>Leonard</name>
      <email>leonard@gmail.com</email>
    </user>

There's also a form-encoded representation which works well with Rails:

    user[name]=Leonard&user[email]=leonard%40example.com

Serving representations to the client is also easy due to `ActiveRecord#to_xml and
ActiveRecord#to_json`. The only problem is there's no "connectedness", there's no concept of linking
between representations of resources. This is an easy problem to get around, just override your
method to include links to relevant resources:

    <users>
      <user>
        <name>Leonard</name>
        <bookmarks>http://example.com/users/leonard/bookmarks</bookmarks>
      </user>
      ....
     </users>

When a resource is created, the response code should be 201 Created and the Location header should
specify the URI of the resource. If a resource is updated, the response should be 200 OK (or 301 if
the location changes). When an object is deleted, a 200 OK will also be given back. Resources should
handle conditional GET when possible and send back appropriate ETag and Last-Modified headers.

If there are any unauthorized attempts, a 401 Unauthorized response should be sent back. A 409
Conflict can occur if a client attempts to create an already existing username. Other appropriate
client error codes are 400 and 404 (if a bookmark resource cannot be found). The the client sends an
incorrect representation of the resource, a 415 Unsupported Media Type will occur.

# REST/ROA Best Practices

This chapter reviews all of the previous ones and adds some advice on how to implement certain
patterns with a RESTful web service, including:

* Asynchronous Operations
* Batch Operations
* Transactions
* URI Design
* Standard features of HTTP
* Faking PUT and DELETE

HTTP has a synchronous request/response cycle, but a service can implement an **asynchronous**
operation and use standard HTTP requests/responses. Example:

1. A request is made to add a job to a queue (POST /queue)
2. A response is sent back (202 Accepted) with a Location header set where the client can check on
   the status of its job
3. Once the operation is complete, the status URI will have the full representation the client
   expects. At anytime, the client may DELETE its job prematurely.

Many of the URIs/actions we designed earlier were operations on a single resource. Services may also
expose **batch operations**. Instead of a client sending issuing a DELETE to multiple URIs, a client
can just:

    DELETE /bookmarks/sha1;sha2;sha3;sha4

Or you can expose a new resource which is a "set of bookmarks", similar to S3's notion of a bucket
containing objects. The client can just DELETE the set to delete all resources within it.

**Transactions** are a common feature of databases/ORMs that can also be exposed as a resource for
clients to work with. A client can first create a transaction, add operations to it, and then either
execute it or delete it to roll back. Here's an example of a bank transaction:

1. The client will create a transaction (POST /transactions/account-transfer)
2. Server sends back a response w/ Location:

     201 Created
     Location /transactions/account-transfer/11a5

3. Client can continue to PUT actions into the transaction:

     PUT /transactions/account-transfer/11a5/accounts/checking/11
     balance=150
     PUT /transactions/account-transfer/11a5/accounts/savings/12
     balance=250

4. At anytime, the client may DELETE the transaction resource to roll back. Or the client can commit
   the transaction with a PUT.

     PUT /transactions/account-transfer/11a5
     committed=true

5. If the transaction is valid, the server will send back the transaction:

     200 OK
     ...
     <account><id>11</id><balance>150</balance></account>
     <account><id>12</id><balance>250</balance></account>

Note the hierarchy in the paths, the accounts are rooted in the transaction path. During the
transaction, if the accounts are accessed they'll probably have their new balances. Outside of the
transaction, they should continue having their old balances. This is done with the rooted paths:

    * /accounts/checking/11 => old balance
    * /transactions/account-transfer/11a5/accounts/checking/11 => new balance

When in doubt, make it a resource.

The author offers some advice about URI designs. Use slashes to denote hierarchy, semicolons to
denote relationships in the same directory, and commas to denote relationships where order matters.
Make sure your URIs correspond to objects/resources instead of actions. Use a uniform interface via
HTTP methods to denote actions on those objects.

RESTful services should try to use the standard features that come with HTTP. **Basic
authentication** is a simple challenge/response protocol that comes along for free. A client makes a
request, gets back a 401 Unauthorized response with a challenge in the WWW-Authenticate header. The
client should make the request again with its credentials in the Authorization header. Example:

1. Client does a GET /resource
2. Server responds:

     401 Unauthorized
     WWW-Authenticate: Basic realm="Private Data"

3. Client does another GET with its credentials: Base64(USERNAME:PASSWORD)

     GET /resource
     Authorization: Basic QWxpYmFiYTpvcGVuIHNlc2FtZQ==

4. Server responds with the actual resource 200 OK

Base64 can be decoded and is not safe to send over the wire. When coupled with HTTPS, basic
authentication works well. **Digest authentication** works over normal HTTP traffic. It includes a
nonce to prevent replay attacks.

Although it's recommended to use different URIs for different representations of resources (like
English vs Spanish), the author recommends using headers for content encoding. He argues that it's
the same representation, it's just encoded differently during transit. Use the **Accept-Encoding**
and the **Content-Encoding** to determine encoding type. This goes without saying, but the
**Content-Type** and **Content-length** headers must always be set.

Services should use **HTTP caching, conditional gets, and etags** whenever possible. HTTP supports
these features via the headers:

* Last-Modified and If-Modified-Since
* ETag and If-None-Match
* Expires and Cache-Control (max-age or no-cache)

ETag can be as simple as an MD5 checksum of your representation. You might save bandwidth that way,
but you won't save any server-side processing. You can also just checksum the important data fields
of your resource (`updated_at`).

An interesting feature of HTTP is the opposite of conditional gets, instead of saving the server
from sending data back - it saves the client from sending data to the server. This is done via the
**Expect** header:

    PUT /filestore/file.txt
    Content-length: 524288000
    Expect: 100-continue

The client is asking if the server will allow it to PUT a new representation. The server makes it
decision based on headers, in this case rejecting the the request because 5MB would be too large. If
it had allowed, the response would be 100 Continue. In the case of no, it's 417 Expectation Failed.

Web browsers only support GET and POST requests. If your RESTful API needs to be exposed to a web
browser or any other client that does not support the full range of methods, you'll have to fake it.
Rails fakes it by adding a "\_method" key into the query string or entity body of an
x-www-form-urlencoded POST body. You can also fake it by using a header like
"X-HTTP-Method-Override". The author suggests using the query string/entity body method because if a
client doesn't support other HTTP methods, it probably doesn't support headers.

# Building Blocks of Services

The author has various suggestions for representation formats:

* XHTML, because it's hypermedia that's easily parsed
* XHTML w/ Microformats for more semantics
* Atom, for resources related to publishing articles/authors
* SVG for graphics
* Form-Encoded Key-Value Pairs (application/x-www-form-urlencoded)
* JSON as a lightweight serialization format (application/json)
* RDF and RDFa
* Plain old XML specific to your application (application/xml)

The uniform interface of HTTP is also re-iterated here. GET should be used as a safe way to retrieve
a resource and services should always attempt to support conditional GETs. The most common response
code for GETs are 200 OKs.

PUT should send data from the client to the server and should be idempotent. It can be used to
update the resource or create it, but the named URI should come from the client. If the client sends
inconsistent data, the server can respond with a 400 Bad Request. If the change results in a
conflict, the server may respond with 409 Conflict. If the resource is updated and available at a
different URI, use 301 Moved Permanently. Otherwise if all is successful, use 200 OK.

POST can be used to create a new resource or appending to a resource. The common response code is
201 Created with the Location header set for creation. For appending, a response code of 200 OK.

DELETE a named resource usually has the common response code of 200 OK.

There are two kinds of hypermedia: links and forms. Links and application forms implement what the
author calls connectedness and what Fieldings called "hypermedia as the engine of application
state".

**URI Templates** are currently a draft that makes simple resource forms look like links:

    https://s3.amazonaws.com/{name-of-bucket}/{name-of-object}

That's currently not a valid URI due to the curly brackets, but it is a URI template. URI templates
gives us a price way to fill in the blank portions of a URI to form new ones.

A number of HTML tags can be used as links (ie. img), but the two most common ones are `<a>` and
`<link>`. `<a>` anchors allow end users to browse the web, jumping from one document to another.
`<link>`s are used to relate one document to another, such as alternate formats or stylesheets.

`<form>` tags drive the web. They currently only support GET and POST methods, but that changes in
HTML5. They're also limited in the URIs they can express, since there's no way to fill in a template
URI given the value of inputs of the form. Instead, values are appended as part of the query string
in a GET form and are encoded in the POST body for a POST request. There are also no ways to set
HTTP headers or to use any other format other than application/x-www-form-urlencoded.

HTML5 forms support all four basic HTTP methods: GET, POST, PUT, and DELETE. There's a proposal that
would allow URI templates. HTML5 also allows two other formats for submitting forms: plain text and
XML application/x-www-form+xml.