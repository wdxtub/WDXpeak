# Developing Backbone.js Applications

An introduction to Backbone.js by Addy Osmani.

# Introduction

This chapter introduces what MVC is (Model-View-Controller pattern) and how Backbone is a MV*
framework. Some reasons to use Backbone:

* it provides minimal set of data structuring and UI primitives
* it scales well
* no performance drawbacks
* vibrant community
* mature library

Features of Backbone:

* contains these core components: model, collection, view, router. This makes up the MV*
* supports event-driven communication between models/views
* supports data bindings via events or KVO (via separate library)
* offers support for RESTful interfaces
* has extensive event system
* instantiates prototypes with `new`
* agnostic about templating frameworks (Underscore's microtemplating is default though)
* clear/flexible conventions for structuring applications

# Backbone.js Basics

Here's the boilerplate HTML used for a Backbone application:

    <!DOCTYPE HTML>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Title</title>
    </head>
    <body>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
      <script src="http://documentcloud.github.com/underscore/underscore-min.js"></script>
      <script src="http://documentcloud.github.com/backbone/backbone-min.js"></script>
      <script>
        // your code here      
      </script>
    </body>
    </html>

Models extend from Backbone.Model:

    var Todo = Backbone.Model.extend({
      initialize: function() { ... },
      defaults: {
        title: '',
        completed: false
      }
    });
    var todo1 = new Todo();
    var todo2 = new Todo({
      title: "This is a test",
      completed: true
    });

    // get/set with Model.get() and Model.set()
    todo2.get("title");
    todo2.set("title", "New title");
    todo2.set({title: "Newer title", completed: false});

    // get/set attributes with `.attributes` or use `silent: true` to hide events
    todo2.attributes.title = "Newest title";
    todo2.set({"title": "Newest title 2"}, {silent: true});

    // listen to events with Model.on()
    initialize: function() {
      this.on("change", function() { ... });
      this.on("change:title", function() { ... });
    }

Backbone supports validation which are run when `save()` is called or when `validate: true` is
passed with the `set()` method.

    // returns nothing if valid, otherwise returns error value
    validate: function(attrs) {
      if (!attrs.name) {
        return "I need your name"; // also triggers `invalid` event and sets `model.validationError`
      }
    }
    Person.unset("name", {validate: true}); // false

Collections are an array of models:

    var TodosCollection = Backbone.Collection.extend({
      model: Todo
    });
    var todos = new TodosCollection([a,b]);
    todos.add(c);

    var todo = todos.get(2); // get by id
    todos.remove([a,b]);

    TodosCollection.on("add", function(todo) { ... });
    TodosCollection.on("remove", function(todo) { ... });

Note that there's also `once`, `listenTo`, and `listenToOnce` for event binding. Besides
adding/removing, you can also reset/refresh entire collections at once. Reset doesn't fire any add
or remove events. A single reset event is fired instead. Use `trigger` to manually fire events.

Collections also inherit most of Underscore's methods. See `underscore.js`'s api for more details.

To interact with a backend:

    var TodosCollection = Backbone.Collection.extend({
      model: Todo,
      url: '/todos'
    });
    todos.fetch(); // sends HTTP GET to /todos, same can be done for solo models
    todo.save(); // sends HTTP PUT
    todos.create({title: "Test"}); // sends HTTP POST
    todo.destroy(); // sends HTTP DELETE
    todo.save({a: 1}, {patch: true}); // sends HTTP PATCH with partial attributes

This uses Backbone.Sync API which in turn uses jQuery's $.ajax(). If your server doesn't support
PUT/DELETE methods or application/json requests, you can turn them off:

    Backbone.emulateHTTP = false;
    Backbone.emulateJSON = false;

All fetch, save, create, destroy methods delegate to `Backbone.sync`, which can be hooked into:

    Backbone.sync = function(method, model, options) { ... }

Views contain presentation logic of model's data to user. Binding `render()` to a model's `change()`
event is the same as 2-way binding.

    var TodoView = Backbone.View.extend({
      tagName: 'li',

      // Cache the template function for a single item.
      todoTpl: _.template("An example template"),

      events: {
        'dblclick label': 'edit',
        'keypress .edit': 'updateOnEnter',
        'blur .edit':   'close'
      },

      // Rerender the titles of the todo item.
      render: function() {
        this.$el.html(this.todoTpl(this.model.toJSON()));
        this.input = this.$('.edit');
        return this;
      },

      edit: function() {
        // executed when todo label is double-clicked
      },

      close: function() {
        // executed when todo loses focus
      },

      updateOnEnter: function( e ) {
        // executed on each keypress when in todo edit mode,
        // but we'll wait for enter to get in action
      }
    });

    var todoView = new TodoView();
    console.log(todoView.el); // logs <li></li>

Views can also have an optional `tagName` and `className`. If the element already exists on the
page, set the `el` property to its selector like `el: '#footer'`. Properties can be passed in during
construction like: `new TodosView({el: $('#footer')})`.

Backbone Views cache the jQuery element as `$el`. In this case it's `todoView.$el`.
`todoView.$(selector)` is equivalent to `$(todoView.el).find(selector)`.

`render()` is what gets called when Views render its element. Returning `this` is useful for making
views re-usable later on:

    render: function() {
      this.$el.html(this.model.toJSON());
      return this;
    }

Backbone Routers are used to connect URLs to your application.

    var TodoRouter = Backbone.Router.extend({
      routes: {
        "about": "showAbout",
        "todo/:id": "getTodo",
        "*other": "defaultRoute"
      },

      showAbout: function() {...},
      getTodo: function(id) {...},
      defaultRoute: function(other) {...}
    });

Use Backbone.history to handle `hashchange` events:

    var router = new TodoRouter();
    Backbone.history.start(); // now go to /#about or /#todo/1

    // route event is triggered on Backbone.history and the actual router
    Backbone.history.on('route', ...);
    router.on('route', ...);

To programmatically trigger route changes:

    Backbone.navigate("todo/"+id);

# Modular Development

Modules may be arriving via the ES6 modules proposal, but until them there's AMD and RequireJS.
RequireJS implements the Asynchronous Module Definition Specification. Its format looks like:

    define(
      module_id
      [dependencies]
      definition function
    );

    define(['foo', 'bar'],
      function(foo, bar) {
        var myModule = {
          doStuff: function() { ... }
        }
        return myModule;
      }
    );

To use RequireJS:

    <script data-main="app.js" src="lib/require.js"></script>
    
    // in app.js you configure how RequireJS loads the rest of your app
    require.config({
      baseUrl: "app",
      paths: {
        'underscore': 'lib/underscore' // shortcuts for shims below
      },
      shim: {
        'lib/underscore': {exports: '_'}
        'lib/backbone': {deps: ['lib/underscore', 'jquery'], exports: 'Backbone'}
      }
    });

    // for any library that doesn't support AMD
    require('lib/backbone', function(Backbone) { ... });

So your file containing a model would use:

    // in models/mymodel.js
    define(['underscore', 'backbone'], function(_, Backbone) {
      var myModel = Backbone.Model.extend({...});
      return myModel;
    });

# Jasmine, QUnit, and SinonJS

Jasmine offers BDD for your front-end code. An example spec:

    describe('Something', function() {
      var number = 1;

      beforeEach(function() {
        this.numberTwo = 2;
      });

      it('should do something', function() {
        expect(number).toEqual(1);
        expect(this.numberTwo).toEqual(2);
      });
    });

Jasmine also supports an `afterEach`.

QUnit is another testing framework that is composed of three files:

1. HTML structure for displaying results
2. `qunit.js` for the test framework
3. `qunit.css` for styling results

All can be downloaded via the QUnit website. Here's an example HTML file:

    <!DOCTYPE html>
    <html>
    <head>
        <title>QUnit Test Suite</title>
         <link rel="stylesheet" href="qunit.css">
         <script src="qunit.js"></script>
         <script src="app.js"></script>
         <script src="tests.js"></script>
    </head>
    <body>
        <h1 id="qunit-header">QUnit Test Suite</h1>
        <h2 id="qunit-banner"></h2>
        <div id="qunit-testrunner-toolbar"></div>
        <h2 id="qunit-userAgent"></h2>
        <ol id="qunit-tests">test markup, hidden.</ol>
    </body>
    </html>

Assertions in QUnit:

    ok(state, message) // passes if state is truthy
    equal(actual, expected, message) // comparison assertion
    notEqual(actual, expected, message)
    expect(amount) // number of assertions expected to run within each test
    strictEqual(actual, expected, message) // less coercion
    deepEqual(actual, expected, message) // uses ===

A basic test looks like:

    module('First module', setup: function() {}, teardown: function() {});
    test('Our first QUnit test', function() {
      ok(true, 'the test succeeds');
    });

    module('Second module', setup: function() {}, teardown: function() {});
    test('Our second QUnit test', function() {
      ok(!false, 'the test succeeds');
    });

To test DOM elements, create a `<div id="qunit-fixture"></div>` element in your HTML. This element
is automatically reset after each test.

SinonJS is a mocking/stubbing/spy library that's useful for creating fake API servers that our
applications can talk to.