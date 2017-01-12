# Sinatra: Up and Running

A short and concise guide on creating a web app or service using the Sinatra library by Alan Harris
and Konstantin Haase.

# Taking the Stage

Sinatra is a minimalistic DSL for making websites, web services, and web apps in Ruby. It is not a
framework. It does not implement MVC.

You can build Sinatra apps in two modes: **classic** and **modular**. Classic mode is simpler, but
it adds methods to the Object namespace and won't work well if you ship the app in a gem. Modular
mode works well for shipping whole apps in gems or combining multiple Sinatra apps.

Install with:

    $ gem install sinatra
    $ gem install thin

The Thin webserver is recommended for running Sinatra apps. If Thin isn't there, Sinatra will try to
use Mongrel. If there's no Mongrel, it will default to WEBrick.

A full application in classic mode looks like this:

    require 'sinatra'

    get '/' do
      "Hello, world!"
    end

Save that into `server.rb` and run it with `ruby server.rb`. Open it by going to
`http://localhost:4567`.

Sinatra wraps around Rack, which is a modular interface to multiple webservers. The developer gets a
nice DSL to work with. Routes are written like `verb "route" do...` and get matched in a top-down
order.

If you do a `POST`, you'll get a 404 back:

    $ curl "localhost:4567" -d "foo=bar"

Now let's make a rock, paper, scissors game in the file `game.rb`:

    require 'sinatra'

    before do
      content_type :txt
      @defeat = {rock: :scissors, paper: :rock, scissors: :paper}
      @throws = @defeat.keys
    end

    get '/throw/:type' do
      player_throw = params[:type].to_sym
      if !@throws.include?(player_throw)
        halt 403, "You must throw one of the following: #{@throws}"
      end

      computer_throw = @throws.sample
      if player_throw == computer_throw
        "You tied, try again!"
      elsif computer_throw == @defeat[player_throw]
        "Nicely done; #{player_throw} beats #{computer_throw}"
      else
        "Ouch; #{computer_throw} beats #{player_throw}."
      end
    end

Now just run it with `ruby game.rb` and you can make throws like this:

    $ curl "localhost:4567/throw/rock"
    $ curl "localhost:4567/throw/paper"
    $ curl "localhost:4567/throw/scissors"

# Fundamentals

This chapter starts out with some HTTP fundamentals. See `http_the_definitive_guide.md` for more
details.

Routes are commonly defined like:

    get '/' do
      "Triggered via GET"
    end

    post '/' do
      "Triggered via POST"
    end

    put '/' do
      "Triggered via PUT"
    end

    delete '/' do
      "Triggered via DELETE"
    end

    patch '/' do
      "Triggered via PATCH"
    end

    options '/' do
      "Triggered via OPTIONS"
    end

Parameters in routes are specified with a colon and accessed with `params`:

    get '/:name' do
      "Hello, #{params[:name]}"
    end

Data from POST, PUT, or PATCH request bodies or URL query string can also be accessed via `params`.

The splat character can be used as a greedy match:

    get '/*' do
      # /foo/bar => ["foo/bar"]
      # /foo/bar/baz/bop => ["foo/bar/baz/bop"]
      params[:splat]
    end

Regular expressions may also be used:

    get %r{/(sp|gr)eedy} do
      "You got caught!"
    end

You can halt a request with `halt` which takes a response code. You can `pass` a request to the next
matching route. You can also `redirect` which defaults to a temporary redirect (use 301 for
permanent, defaults to 302).

    get '/halt' do
      halt(500) if some_condition
    end

    get '/pass' do
      pass if some_condition
    end

    get '/redirect' do
      redirect 'http://www.google.com' if some_condition
    end

    get '/redirect/permanently' do
      redirect 'http://www.google.com', 301
    end

Sinatra uses the `public` subdirectory for static files. If you have the file `static.html` in it,
the route `/static.html` will automatically direct you to the file. It will even override any `get
"/static.html"` in your app. Configure this directory like:

    set :public_folder, File.dirname(__FILE__) + '/your_custom_location'

Sinatra can use inline or external templates. Here's an example of inline:

    get '/index' do
      erb :index
    end

    __END__

    @@index
    <!DOCTYPE html>
    <html>
      ...
    </html>

For external templates, put the HTML into a file `views/index.erb`. You can change the default
subfolder using the `set :views` option. Some built in templating engines are: Erb, Haml, and
Erubis. Data can be passed into views by assigning and using instance variables.

You can also use before/after filters. Without a parameter, they'll work on all requests. They also
accept route parameters just like the HTTP verbs.

    before do
      puts "Before all requests."
    end

    before '/some/*' do
      puts "Before some requests."
    end

    after do
      puts "After all requests."
    end

    after '/some/*" do
      puts "After some requests."
    end

404s and 500s are so common, Sinatra provides helpers to handle them gracefully.

    not_found do
      content_type :txt
      "Whoops!  You requested a route that's not available."
    end

For 500s:

    configure do
      set :show_exceptions, false
    end

    error do
      content_type :txt
      "Y U NO WORK?"
    end

Use `headers` for custom response headers:

    get '/' do
      headers 'X-Custom-Value' => 'Custom HTTP header',
              'X-Custom-Value2' => 'bar'
      "Hello, World!"
    end

The `request` object has more info about incoming requests:

    get '/env' do
      content_type :txt
      request.env.map { |e| e.to_s + "\n" }
    end

    get '/methods' do
      content_type :txt
      request.methods.map { |m| m.to_s + "\n" }
    end

Some helper methods can be used to set common cache headers:

    require 'uuid'

    expires 3600, :public, :must_revalidate
    etag UUID.new.generate
    etag UUID.new.generate, :weak

Cookie based sessions look like this:

    configure do
      enable :sessions
      set :session_secret, 'your_custom_value_here' # default is random per start
    end

    before do
      content_type :txt
    end

    get '/set' do
      session[:foo] = Time.now
      "Session value set."
    end

    get '/fetch' do
      "Session value: #{session[:foo]}"
    end

    get '/logout' do
      session.clear
      redirect '/fetch'
    end

Session based cookies are cleared automatically when the browser closes. To use persistent cookies:

    response.set_cookie 'foo', 'bar'
    request.cookies['foo']
    response.delete_cookie 'foo'
    response.set_cookie 'foo', :value => 'bar', :path => '/'

Attachments can be sent downstream via `attachment` method which accepts a file path.

# A Peek Behind the Curtain

Sinatra uses some magic to handle `self`, which evaluates differently depending on whether you're in
the `Object` namespace or within a routing block:

    require 'sinatra'

    outer_self = self
    get '/' do
      content_type :txt
      "outer self: #{outer_self},\n inner self: #{self}"
    end

    $ curl "localhost:4567/"
    ...
    outer self: main,
    inner self: #<Sinatra::Application:0x0010cd8f0>

`Sinatra::Application` inherits from `Sinatra::Base`. There's also the `Sinatra::Delegator` mixin.
Methods like `get` and `post` are defined twice, once in the Delegator mixin and another in Base.
The Delegator mixin just delegates the call to Application. The mixin is what gets mixed into the
Object namespace. An app can be made without mixing into the Object namespace:

    require 'sinatra/base'

    Sinatra::Application.get('/') { 'hi' }
    Sinatra::Application.run!

Sinatra apps can be extended with extensions and helpers. Extensions exist in the Object namespace
only. Helpers exist within route blocks and views:

    # an extension
    module Sinatra
      module PostGet
        def post_get(route, &block)
          get(route, &block)
          post(route, &block)
        end
      end

      register PostGet
    end

    # a helper
    module Sinatra
      module LinkHelper
        def link(name)
          case name
          when :about then '/about'
          when :index then '/index'
          else "/page/#{name}"
        end
      end

      helpers LinkHelper
    end

    # or use helpers with a block
    helpers do
      def link(name)
        # ...
      end
    end

[Rack](http://rack.rubyforge.org) is a protocol that specifies how web servers interact with web
applications. At its core, it specifies how the application object (aka **endpoint**) responds to
the method `call`. The server (aka **handler**) calls the method with one parameter, a hash with all
relevant request information such as HTTP verb, path requested, headers, etc... The return value
should be an array with 3 items: status code, hash of response headers, body object which should
behave like an array of strings.

Here's a sample Rack application:

    module MySinatra
      class Application
        def call(env)
          headers = {'Content-Type' => 'text/html'}
          if env['PATH_INFO'] == '/'
            status, body = 200, 'hi'
          else
            status, body = 404, "Sinatra doesn't know this ditty!"
          end
          headers['Content-Length'] = body.length.to_s
          [status, headers, [body]]
        end
      end
    end

    require 'thin'
    Thin::Server.start MySinatra::Application, 4567

These low level variables are available in your Sinatra route blocks via:

* `env`
* `request`
* `response`

Rack supports chaining filters and routers in front of your application called `middleware`.
Middleware can modify requests, the env hash, the response, or even skip endpoints.

Stick this into `config.ru` the run `rackup -p 4567 -s thin`:

    MyApp = proc do |env|
      [200, {'Content-Type' => 'text/plain'}, ['ok']]
    end

    class MyMiddleware
      def initialize(app)
        @app = app
      end

      def call(env)
        if env['PATH_INFO'] == '/'
          @app.call(env)
        else
          [404, {'Content-Type' => 'text/plain'}, ['not ok']]
        end
      end
    end

    # actual configuration
    use MyMiddleware
    run MyApp

Sinatra ships with a `use` method that works like rackup's.

    require 'sinatra'
    require 'rack'

    use Rack::Runtime # middleware that sets 'X-Runtime' header

    get('/') { 'hello world!' }

You can use any `Sinatra::Application` as Rack middleware.

# Modular Applications

Before, we just `require 'sinatra/base'` and were able to make a Sinatra application. For modular
applications, it's common practice to create your own subclass of `Sinatra::Base`. Some reasons to
do this:

* avoid polluting the Object namespace
* ship your app as a gem
* allow combining multiple apps under a single process
* use apps as middleware

    require 'sinatra/base'

    class MyApp < Sinatra::Base
      get '/' do
        'Hello from MyApp!'
      end
    end

    MyApp.run! if __FILE__ == $0

To use it with rackup:

    require './myapp'
    run MyApp

We've used `set` and `configure` before to configure settings. These settings are available via the
`settings` method. `enable` and `disable` are syntatic sugar for setting an option to true or false.
`settings` is actually just a shortcut to the current application class. Actually, creating new
settings will just add instance new methods to the current application class.

    configure :development, :test do
      enable :admin_access
    end

`configure` accepts environment switches. This is controlled via the `environment` setting or the
`RACK_ENV` environment variable.

Since settings are just methods, subclassing an application will inherit its settings. It will also
inherit its routes, middleware, error handlers, extensions, and so on.

Rack also lets you mount applications on different paths with the `map` method.

    map('/example') { run MyExampleApplication }

Rack will remove the prefixed route (`/example` in this case) and store it in `env['SCRIPT_NAME']`.
From the Sinatra application's point of view, there will not be `/example`.

You can even create anonymous Sinatra applications in your `config.ru`:

    app = Sinatra.new do
      get('/') { 'Hello World!' }
    end
    run app

You can start chaining applications, just like how middleware can be chained:

    class Foo < Sinatra::Base
      get '/foo' { 'foo' }
    end

    class Bar < Sinatra::Base
      get '/bar' { 'bar' }
      use Foo
    end

`Rack::Cascade` can be used in the same fashion (pretend the line `use Foo` was removed):

    run Rack::Cascade, [Foo, Bar]

The normal Rack response is a method of three items. Rack also accepts other formats:

* `[200, {'Content-Type' => 'text/plain'}, ['ok']]`
* `[418, "I'm a teapot"]` no headers and just a string for body

`halt` accepts the format returned as Rack responses:

    halt [418, "I'm a teapot"]

Since Sinatra applications are Rack applications, they must respond to `call`. You can use this in
modular applications:

    class Foo < Sinatra::Base
      # ...
    end

    class Bar < Sinatra::Base
      get('/') { Foo.call(env) }
    end

    Bar.run!