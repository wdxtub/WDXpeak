# Programming iOS8

A complete guide to creating iOS8 apps with Swift. By Matt Neuburg.

# Views

UIWindow is the top of the view hiearchy:

    let w = UIWindow(frame: UIScreen.mainScreen().bounds)

The application lifecycle handles creating and retaining the window. UIApplicationMain creates an
app delegate, whose window property is assigned and remains for the lifetime of an app. You
typically don't add views manually, instead you obtain a view controller and assign it to the window's
`rootViewController` property. If you're using the main storyboard, this will be done automatically
for it and is the storyboard's initial view controller.

The window has a root view which is the `rootViewController`'s `view` property. There's only one.
The window's `makeKeyAndVisible` method makes the app's interface visible.

The creation of window for an app with a main storyboard:

1. Info.plist UIMainStoryboardFile will indicate if storyboard exists
2. UIApplicationMain creates UIWindow, sets its frame, and assigns app delegate's `window`
3. UIApplicationMain also creates storyboard's initial view controller and assign `rootViewController`
4. App delegate's `application:didFinishLaunchingWithOptions:` is called
5. UIApplicationMain calls `makeKeyAndVisible` which causes the controller to load its view from
   the nib file.

The creation of window for an app without main storyboard:

1. All Xcode app templates have a main storyboard, so you'll have to manually remove it
2. Create Single View Application template, edit target, in General select "Main" in the Main
   Interface field and delete it
3. Delete Main.storyboard and ViewController.swift from the project
4. Delete contents of AppDelegate.swift
5. Creating/configuring window must be done by you in code, AppDelegate is a good place:

    class AppDelegate: UIResponder, UIApplicationDelegate {
      var window: UIWindow?
      func application(application: UIApplication,
           didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool {
        self.window = UIWindow(frame: UIScreen.mainScreen().bounds)
        self.window!.backgroundColor = UIColor.whiteColor()
        self.window!.makeKeyAndVisible()
        return true
      }
    }

To access the window:

* all UIView instances have a `window` property, this is nil if it's not in the interface though
* UIApplication.sharedApplication().delegate!.window!
* UIApplication.sharedApplication().keyWindow is more voalitile because the app creates temporary
  windows, so the previous line is preferred

If you used storyboard, you can use Interface Builder to create view controllers and other subviews.
You can also use the view controller's `viewDidLoad` method to add subviews:

    override func viewDidLoad() {
      super.viewDidLoad()
      let mainview = self.view
      let v = UIView(frame: CGRectMake(100,100,50,50))
      v.backgroundColor = UIColor.redColor()
      mainview.addSubview(v)
    }

If you didn't use storyboard, you can assign `rootViewController` and add subviews in the app
delegate:

    func application(application: UIApplication,
         didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool {
      // ... create/assign window ...
      self.window!.rootViewController = UIViewController()
      let mainview = self.window!.rootViewController!.view
      v = UIView(frame: CGRectMake(100,100,50,50))
      v.backgroundColor = UIColor.redColor()
      mainview.addSubview(v)
      self.window!.makeKeyAndVisible()
      return true
    }

View hierarchies are similar to layout in HTML/CSS. Subviews are drawn above their superviews. Later
siblings are also drawn above their earlier siblings. Interface Builder has "Send to Front/Back" and
"Send Forward/Backward" to manipulate ordering. Or it can be done in code. Properties/methods to know:

* `clipsToBounds` property should be set if you want to clip a child's views to its parent's bounds
* `superview` to access the parent
* `isDescendantOfView:`
* `tag` numeric value
* `viewWithTag:` to access it by numeric value
* `addSubview:`
* `removeFromSuperview`
* `didAddSubview:`, `willRemoveSubview:`, `didMoveToSuperview:`, `willMoveToSuperview:`,
  `didMoveToWindow:`, `willMoveToWindow:`
* `insertSubview:atIndex:`, `insertSubview:belowSubview:`, `insertSubview:aboveSubview:`,
  `exchangeSubviewAtIndex:withSubviewAtIndex:`, `bringSubviewToFront:`, `sendSubviewToBack:`
* remove all subviews: `for v in view.subviews as [UIView] { v.removeFromSuperview() }`
* `hidden` property to make visible/invisible
* `backgroundColor` property
* `alpha` property for transparency
* `opaque` property hints to the drawing system for optimizations, set to true if it will always be
  opaque for more efficient drawing (not handled automatically, your job to set it)

# Drawing

# Layers

# Animation

# Touches

# View Controllers

# Scroll Views

# Table Views

# iPad Views

# Text Controls and Views

# Web Views

# Other UIKit Views

# Modal Dialogs

# Audio

# Video and AV Foundation

# Music Library

# Photo Library

# Address Book

# Calendars

# Email, SMS, and Social

# Maps

# GPS
