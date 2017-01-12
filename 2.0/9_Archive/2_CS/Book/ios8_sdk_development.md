# iOS 8 SDK Development

Notes on the book by Chris Adamson and Janie Clayton-Hasz. See
<https://pragprog.com/book/adios2/ios-8-sdk-development>.

# Playing Around with Xcode

Xcode 6 introduces Playground, which is a REPL built into the IDE. On the greeting window, click
"Get started with a playground" to use it.

    import UIKit
    var str = "Hello, playground"
    var myLabel = UILabel(frame: CGRectMake(0.0, 0.0, 200.0, 100.0))
    myLabel.text = str

Type your program on the left window and you'll see evaluated expressions on the right window. Click
the results and they'll expand if there are further details.

# Building Adaptive User Interfaces

Start with the UI first:

1. `File -> New -> New Project` named PragmaticTweets
2. Check out the workspace on the left (or hit `Cmd-1`)
3. Click `Main.storyboard`
4. You'll see Interface Builder and a square UI, the UI is meant to scale to any size
5. Press `Ctrl-Opt-Cmd-3` to bring up interface objects on bottom right
6. Drag a button over to your UI and rename it Send Tweet
7. Click `Run` or `Cmd-R`, try rotating the device with `Cmd-Left` or Right and notice how your UI
   doesn't scale properly
8. Use Autolayout, IB has buttons at bottom right pane that present: Align, Pin, Resolve, and
   Resizing Behavior
9. On Align tab, you can horizontally center the button. On Pin tab, you can pin the button to any
   other UI elements

Next, you'll want to connect your UI elements to code. IB does this with annotations.

1. Go to `Main.storyboard`
2. Split the editor using the buttons in top-right area, use the 2nd editor to go to
   `ViewController.swift`
3. Control-click the button and drag to the bottom area of your source code, above the last bracket.
4. In Connection, make sure Action is selected
5. Fill out `handleTweetButtonTapped` for the name and select `UIButton` for the type

You'll get a stubbed method which you can fill out:

    import Social

    @IBAction func handleTweetButtonTapped(sender: UIButton) {
      if SLComposeViewController.isAvailableForServiceType(SLServiceTypeTwitter) {
        let tweetVC = SLComposeViewController(forServiceType: SLServiceTypeTwitter)
        tweetVC.setInitialText("I just finished the first project.")
        self.presentViewController(tweetVC, animated: true, completion: nil)
      } else {
        println("Can't send tweet")
      }
    }

# Programming in Swift for iOS

Swift is compiled, strongly typed, automatically reference counting (no need to manually manage
memory), and name spaced. Classes are defined like:

    class AppDelegate: UIResponder, UIApplicationDelegater {
      // first type after colon is the parent class
      // all types after are protocols this class conforms to
    }

Swift methods look like:

    @IBAction func handleTweetButtonTapped(sender: UIButton) {
      // @IBAction means this method can be connected to a UI element
      // handleTweetButtonTapped is the method name
      // sender is a parameter of type UIButton
    }

Besides `IBAction`, there's also `IBOutlet` to indicate an instance property that exists in the UI:

    class ViewController: UIViewController {
      @IBOutlet var twitterWebView: UIWebView!
      // Control-click dragging a UI element to source code can also produce an IBOutlet
    }

For more information on Swift, see notes on Swift Programming Language.

# Testing Apps

Unit tests are built into Xcode via XCTest. There's already a PragmaticTweetsTest group in the
navigator (Command-5). Open `PragmaticTweetsTest.swift`:

    func testExample() {
      XCTAssert(true, "Pass")
    }

Testing is similar to other `xunit` style frameworks. Method names beginning with `test` will be
executed. There's a before hook via `setUp` method and after hook via `tearDown`. Run your tests
with `Command-U`.

Create a `WebViewTests.swift` file and `import PragmaticTweets` to start. Let's talk about Swift
visiblity: public is visible everywhere, internal (default) is visible within same module,
private is visible only within the class. If you test an IBOutlet, you might want to make it
public so it's viewable within your test class.

    func testAutomaticWebLoad() {
      if let viewController = UIApplication.sharedApplication().windows[0].rootViewController as?
        ViewController {
        let webViewContents = viewController.twitterWebView.
          stringByEvaluatingJavaScriptFromString("document.documentElement.textContent")
        XCTAssertNotNil(webViewContents, "web view contents are nil")
        XTTAssertNotEqual(webViewContents!, "", "web view contents are empty")
      } else {
        XCTFail("couldn't get root view controller")
      }
    }

But wait, even if your webview loads the contents on application start this test will still fail.
It's because the test runs immediately but the webview loads asynchronously. We have to wait for it
to finish before we can test it. You can utilize `XCTestExpectation` for asynchronous testing:

    func testAsynchronously() {
      let expectation = self.expectationWithDescription("a description")
      anAsynchronousMethod(callback: {
        // more assertions
        expectation.fulfill()
      })
      waitForExpectationsWithTimeout(5.0, handler: nil)
    }

Third-party frameworks to look at: OCMock and UI Automation.

# Presenting Data in Table Views

Tables are implemented with `UITableViewController`, `UITableViewDataSource`, and
`UITableViewDelegate`. The last two are protocols.

    class MyTableViewController: UITableViewController, UITableViewDataSource, UITableViewDelegate {
      override public func numberOfSectionsInTableView(tableView: UITableView) -> Int { }

      override public func tableView(_tableView: UITableView, titleForHeaderInSection section: Int)
        -> String? { }

      override public func tableView(_tableView: UITableView, numberOfRowsInSection section: Int)
        -> Int { }

      override public func tableView(_tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath)
        -> UITableViewCell {
        let cell = UITableViewCell(style: UITableViewCellStyle.Default, reuseIdentifier: nil)
        cell.textLabel!.text = "Row \(indexPath.row)"
      }
    }

Data in table views can be reloaded with `tableView.reloadData()`. It's common to call this in the
`viewDidLoad` hook of ViewControllers to load the table's initial data.

# Waiting for Things to Happen with Closures

Let's make a request to Twitter's API:

    let request = SLRequest(
      forServiceType: SLServiceTypeTwitter, 
      requestMethod: .GET,
      URL: NSURL.URLWithString("https://api.twitter.com/1.1/statuses/home_timeline.json"),
      parameters: ["count": "100"])
    request.performRequestWithHandler() {
      (data: NSData, urlResponse: NSHTTPURLResponse, error: NSError) -> Void in
      self.handleTwitterData(data, urlResponse: urlResponse, error: error)
    }

Then we can define `handleTwitterData`. Note that we used a closure to handle the HTTP request's
response after it comes back. In the example above, we used a trailing closure. That block could
also exist within the parenthesis: `request.performRequestWithHandler({...})`.

# Doing Two Things at Once with Closures

While scrolling through the table, you'll notice that images are loaded synchronously. The app's UI
runs on a single thread (known as the main thread). Since image loading occurs on it, it slows down
table scrolling. We can fix that with Grand Central Dispatch:

    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0)) {
      let avatarImage = UIImage(data: NSData(contentsOfURL: userAvatarURL))
      dispatch_async(dispatch_get_main_queue()) {
        cell.avatarImageView.image = avatarImage
      }
    }

Note that any actions manipulating UI elements must occur on the main thread, hence we're using
`dispatch_get_main_queue()` above when setting `avatarImageView.image`. The GCD function
`dispatch_get_global_queue` will determine a thread for us, we just need to pass it a priority.

The code above is buggy, it has race conditions. HTTP response for images will arrive at different
times. In our closure that sets the imageView, we'll need to double check that it's the appropriate
cell.

# Navigating Between View Controllers

In the Object Library, drag/drop a Navigation Controller (yellow circle with a blue back button)
onto the storyboard. The storyboard will have 3x scenes: original root view controller, navigation
controller, a table view controller.

Select the navigation controller, bring up Attributes Inspector (Option-Commnad-4) and check the
"Is Initial View Controller" checkbox. Control-click the navigation controller and bring up
its Connections Inspector (Option-Command-6). Set Triggered Segues -> Root View Controller to
the old view controller.

Since we only have one view, add another one from the Object Library. Control-drag from a table
view cell to the new View Controller. This indicates you want a segue from the cell to the new
view controller when the cell is tapped. The Navigation Controller automatically provides a top
navigation bar.

In `RootViewController.swift`, override:

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
      if segue.identifier == "showTweetDetailsSegue" {
        let row = self.tableView!.indexPathForSelectedRow()!.row
        let parsedTweet = parsedTweets[row] as ParsedTweet
        println("tapped on: \(parsedTweet.tweetText!)")
      }
    }

The `segue` object has a `destinationViewController` property. You can use this along with
`indexPathForSelecteRow` to get additional information from the table.

Note that you can also present the second view modally.

# Launching, Backgrounding, and Extensions

The app lifecycle:

1. iOS creates a UIApplication that will interfact with operating system
2. UIApplication has an array of `windows`, usually one per screen (in case of AirPlay there's multiple)
3. Each window has a `rootViewController` in the storyboard's initial scene
4. UIApplication also has a UIApplicationDelegate object that's informed of major events
5. When app setup is finished, the delegate's `application(didFinishLaunchingWithOptions:)` is called
6. Other events that the delegate gets include app entering background, app entering foreground,
   app resigning active or becoming active.
7. At the end, the delegate receives `applicationWillTerminate`.

To open any URLs (including a resource for another app):

    UIApplication.sharedApplication().openURL(NSURL(string: "http://..."))

Your app can declare its own URL scheme. From the File Navigator, click on the project icon, select
"PragmaticTweets" app. Under Info tab, look at "URL Types". Click the add button to enter your own
URL scheme. The AppDelegate will get called `application(openURL:sourceApplication:annotation:)`.
