# Assignment 1

_Name: Da Wang, Andrew ID: dawang_

## Question 1

> Contrast an Android Project created with and without an Activity.

Normally, an Android project has one or more activities as activity is the application component which provides the window for users to interact. The fundamental method for the lifecycle of activity is `onCreate`, `onStart`, `onResume`, `onPause`, `onStop`, `onDestroy` and `onRestart`.

However, it is still possible to create an Android project without any activies. On this occasion, we often call the project a service and use `Context.startService()` or `Context.stopService()` to control the service. The fundamental method for the lifecycle of service is `onCreate`, `onStart` and `onDestroy`.

You can have multiple activities while only one of them is running forground. For service, you can only have one instance but the service can be started many times while stopped by calling stop function once.

## Question 2

> After watching video (Pranav Mistry @ MIT Labs - http://www.youtube.com/watch?v=YrtANPtnhyg) what assumptions can you make about current mobile computing replacing desktop computing. Comment on current implementation(s) and what are your assumption about how mobile computing will continue to evolve.
> 
> Use the following references:
> 1. Android 5.0 features
> 2. Google Glass
> 3. iPhone 5
> 4. iPad 3
> 5. Gaming Consoles
> 6. TV and Autoapps.

Instead of using the word "replace", I think "seperate" is a properer word for the current trend that mobile computing is "replacing" desktop computing. 

Why do we have such feelings that mobile devices are replacing desktop ones? In my opinion there are two reasons. One is that the ability of computing for mobile devices increases rapidly, much faster than the increases for desktop devices. This brings great changes for our life, for example, many things that used to be done in desktop computer can now be finished just with mobile devices. The other reason is that the mobility of mobile devices makes the ability of computing everywhere.

But this is still not enough to say "replacing". Desktop computing becomes the fundamental part of the digital world and make the mobility of mobile devices easily. The new trend is that the mobile devices show the beautiful result to the users while the desktop devices handle all the hard work behind those results.

**Android 5.0 Lollipop** and **Google Glass** can be regarded as the most significant signal for current separating process: mobile devices become the computing interface and the servers behind become the foundation. 

**iPhone 5** and **iPad 3** can be regarded as the signal for Moore's Law in mobile computing. Their performance got great improvement to make it possible for mobile devices finishing more computing works.

**Game Console** and **Smart TV** can be regarded as another kind of desktop computing but just for entertainment. Computing ability will be so popular that we can use it whenever and wherever we want just like water and electricity.

But what's next? How mobile computing will evolve in the future?

More hardware and sensor part will become as important as software for mobile computing. Based on their mobility, it is a great way to detect the enviroment and our body, or even spirit.

Also, virtual reality may also be the next generation of mobile computing as it is so interesting that it's just like opening the gate to the new world.


## Question 3

> Describe the execution lifecycle for an Android App when running on a physical Android Device.

Basically, as I mentioned in question 1, the lifecycle for an Android App is mainly related to the lifecycle of Activity and corresponding services. As it is, there are four states:

1. Active / Running state. Activity in the front, visible and active for user interaction.
2. Pause state. Partially visible, not acitve, no focus.
3. Stopped state. No long visible, may be killed by the system to free resources.
4. Destroyed / Dead state. No long exists in the memory.

Here is a nomral situation to describe the lifecycle of an Android App: 

1. User clicks the icon. Main activity -> `onCreate` and `onStart`
2. User finishs his current job and come back to the home screen. Main acitivity -> `onPause`.
3. User decides to use the app again. Main activity -> `onResume`
4. User exit the app with back button. Main activity -> `onDestroy`

For service, it is controlled by the `Context.start` and `Context.end` method which is a little different from the activity lifecycle.

