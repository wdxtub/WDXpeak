# Learning Cocos2D

This book is a hands-on guide to making 2D iOS games using Cocos2D, Box2D, and Chipmunk by Rod
Strougo and Ray Wenderlich.

These notes won't include the full guide. I'll try to highlight the important aspects of Cocos2D
without the full game code. Also, I'm only reading the chapters on Cocos2D and a quick introduction
to the Box2D physics engine.

Purchase the book here: <http://cocos2dbook.com/book/>. It's good!

# Hello, Cocos2D

**Cocos2D** is a 2D game engine for iOS, you can get it at <http://www.cocos2d-iphone.org>.

1. Download cocos2d and unzip the download
2. `cd cocos2d-iphone`
3. `sudo ./install-templates.sh`
4. Restart Xcode

Now let's make a "Hello, World!" application using Cocos2D:

1. Launch Xcode and select File > New Project
2. Choose Cocos2D template
3. Name the project CCHelloWorld
4. In the Scheme dropdown, select the project and iOS simulator
5. Click Run

Let's render an image:

1. Drag the SpaceCargoShip directory from the provided resources into the CCHelloWorld project.
   Select "Copy items into destination group's folder".
2. Open HelloWorldScene.m and add these lines to the init method:

    CCSprite *spaceCargoShip = [CCSprite spriteWithFile:@"SpaceCargoShip.png"];
    [spaceCargoShip setPosition:ccp(size.width/2, size.height/2)];
    [self addChild:spaceCargoShip];

Click run to see the space ship. Move the ship around with this code:

    id moveAction = [CCMoveTo actionWithDuration:5.0f
                                        position:ccp(0, size.height/2)];
    [spaceCargoShip runAction:moveAction];

Cocos2D games are made up of a few components:

* `CCDirector` - director runs the scenes
* `CCScenes` - one scene gets run at a time, for example one with a menu and the next with some
  gameplay
* `CCLayer` - each scene consists of one or more layers composited on top of one another. For
  example: one background and another for characters
* `CCSprite` - layers have sprites which are objects displayed on screen, like a single character or
  paddles and a ball.

Cocos2D objects have a shorthand method called `node`:

    [CCScene node]
    // equivalent to...
    [[[CCScene alloc] init] autorelease];

# Hello, Space Viking

Let's make a new Space Viking game:

1. Open Xcode and "Create a New Xcode Project"
2. Choose Cocos2d template
3. Enter "Space Viking" as name of product and Create
4. Download the resources at <http://www.informit.com/store/product.aspx?isbn=9780321735621>.
5. Drag the Images directory into the SpaceViking project and choose "Copy items into destination
   group's folder". Choosing this option makes a hard copy in your project instead of using a link
   to existing files

Let's make a background:

1. Right-click on the Classes and choose "New File"
2. From iOS -> Cocoa Touch Class, choose "Objective-C class"
3. For the subclass field, enter CCLayer
4. Save as file BackgroundLayer.m

    // BackgroundLayer.m
    - (id) init {
      if (self = [super init]) {
        CCSprite *backgroundImage;
        if (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad { // ipad
          backgroundImage = [CCSprite spriteWithFile:@"background.png"];
        } else {
          backgroundImage = [CCSprite spriteWithFile:@"backgroundiPhone.png"];
        }
        CGSize screenSize = [[CCDirector sharedDirector] winSize];
        [backgroundImage setPosition:
          CGPointMake(screenSize.width/2, screenSize.height/2)];
        [self addChild:backgroundImage z:0 tag:0];
      }
      return self;
    }

Cocos2D includes utility functions `convertToGL` and `convertToUI` to deal with UIKit's coordinate
system (origin at upper left) and OpenGL ES coordinate system (origin at bottom left). Cocos2D uses
OpenGL ES coordinate system.

Create a GameplayLayer class that subclasses CCLayer. We're going to add a viking to the scene. Add
a `CCSprite *vikingSprite` instance variable in the interface:

    // GameplayLayer.m
    - (id) init {
      if (self = [super init]) {
        CGSize screenSize = [CCDirector sharedDirector].winSize;
        self.isTouchEnabled = YES;
        vikingSprite = [CCSprite spriteWithFile:@"sv_anim_1.png"];
        [vikingSprite setPosition:
          CGPointMake(screenSize.width/2, screenSize.height*0.17f)];
        [self addChild:vikingSprite];
        if (UI_USER_INTERFACE_IDIOM() != UIUserInterfaceIdiomPad) {
          [vikingSprite setScaleX:screenSize.width/1024.0f];
          [vikingSprite setScaleY:screenSize.height/768.0f];
        }
      }
      return self;
    }

Now we have a background and viking layer. We need to connect these layers to a scene and connect
that scene to the director. Create the GameScene class and have it inherit CCScene:

    // GameScene.m
    - (id) init {
      if (self = [super init]) {
        [self addChild:[BackgroundLayer node]];
        [self addChild:[GameplayLayer node]];
      }
      return self;
    }

Open SpaceVikingAppDelegate.m. We need to use our scene instead of the default HelloWorldScene:

1. `#import "GameScene.h"` add this near the top
2. Uncomment the section to enable iPhone 4 retina display
3. Change the call to `[HelloWorld scene]` to `[GameScene scene]`

At this point we've rendered a viking and the background. Let's add movement. The author uses an
open source joystick class called SneakyInput. Right-click the project, select 'Add > Files', select
the JoystickClasses directory, and add (make sure "copy items into destination" is checked).

You'll need to add some imports and instance variables to GameplayLayer:

    // add to GameplayLayer.h
    #import "SneakyJoystick.h"
    #import "SneakyButton.h"
    #import "SneakyButtonSkinnedBase.h"
    #import "SneakyJoystickSkinnedBase.h"

    SneakyJoystick *leftJoystick;
    SneakyButton *jumpButton;
    SneakyButton *attackButton;

GameplayLayer needs to initialize the joystick and buttons:

    // add to GameplayLayer.m
    - (void) initJoystickAndButtons { // call in init
      CGSize screenSize = [CGDirector sharedDirector].winSize;
      CGRect joystickBaseDimensions = CGRectMake(0, 0, 128.0f, 128.0f);
      CGRect jumpButtonDimensions = CGRectMake(0, 0, 64.0f, 64.0f);
      CGRect attackButtonDimensions = CGRectMake(0, 0, 64.0f, 64.0f);
      CGPoint joystickBasePosition, jumpButtonPosition, attackButtonPosition;

      if (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad) {
        CCLOG(@"Positioning joystick/buttons for ipad");
        joystickBasePosition = ccp(
          screenSize.width*0.0625f,
          screenSize.height*0.052f);
        jumpButtonPosition = ccp(
          screenSize.width*0.946f,
          screenSize.height*0.052f);
        attackButtonPosition = ccp(
          screenSize.width*0.947f,
          screenSize.height*0.169f);
      } else {
        CCLOG(@"Positioning joystick/buttons for iphone/itouch");
        joystickBasePosition = ccp(
          screenSize.width*0.07f,
          screenSize.height*0.11f);
        jumpButtonPosition = ccp(
          screenSize.width*0.93f,
          screenSize.height*0.11f);
        attackButtonPosition = ccp(
          screenSize.width*0.93f,
          screenSize.height*0.35f);
      }

      SneakyJoystickSkinnedBase *joystickBase = 
        [[[SneakyJoystickSkinnedBase alloc] init] autorelease];
      joystickBase.position = joystickBasePosition;
      joystickBase.backgroundSprite = [CCSprite spriteWithFile:@"dpadDown.png"];
      joystickBase.thumbSprite = [CCSprite spriteWithFile:@"joystickDown.png"];
      joystickBase.joystick =
        [[SneakyJoystick alloc] initWithRect:joystickBaseDimensions];
      leftJoystick = [joystickBase.joystick retain];
      [self addChild:joystickBase];

      SneakyButtonSkinnedBase *jumpButtonBase =
        [[[SneakyButtonSkinnedBase alloc] init] autorelease]; 
      jumpButtonBase.position = jumpButtonPosition; 
      jumpButtonBase.defaultSprite = [CCSprite spriteWithFile:@"jumpUp.png"]; 
      jumpButtonBase.activatedSprite = [CCSprite spriteWithFile:@"jumpDown.png"]; 
      jumpButtonBase.pressSprite = [CCSprite spriteWithFile:@"jumpDown.png"]; 
      jumpButtonBase.button = [[SneakyButton alloc] initWithRect:jumpButtonDimensions]; 
      jumpButton = [jumpButtonBase.button retain]; 
      jumpButton.isToggleable = NO; 
      [self addChild:jumpButtonBase]; 

      SneakyButtonSkinnedBase *attackButtonBase =
        [[[SneakyButtonSkinnedBase alloc] init] autorelease]; 
      attackButtonBase.position = attackButtonPosition; 
      attackButtonBase.defaultSprite = [CCSprite spriteWithFile:@"handUp.png"]; 
      attackButtonBase.activatedSprite = [CCSprite spriteWithFile:@"handDown.png"]; 
      attackButtonBase.pressSprite = [CCSprite spriteWithFile:@"handDown.png"]; 
      attackButtonBase.button = [[SneakyButton alloc] initWithRect:attackButtonDimensions]; 
      attackButton = [attackButtonBase.button retain]; 
      attackButton.isToggleable = NO; 
      [self addChild:attackButtonBase]; 
    }

Add an `applyJoystick` method which will be called everytime the viking position gets updated for
the joystick movement:

    - (void) applyJoystick:(SneakyJoystick *)aJoystick 
                    toNode:(CCNode *)tempNode 
              forTimeDelta:(float)deltaTime { 
      CGPoint scaledVelocity = ccpMult(aJoystick.velocity, 1024.0f); 
      CGPoint newPosition = ccp(
        tempNode.position.x + scaledVelocity.x * deltaTime, 
        tempNode.position.y + scaledVelocity.y * deltaTime); 
      [tempNode setPosition:newPosition]; 
      if (jumpButton.active == YES) { 
        CCLOG(@"Jump button is pressed."); 
      } 
      if (attackButton.active == YES) { 
        CCLOG(@"Attack button is pressed."); 
      } 
    } 

Cocos2D automatically calls an update method before each time the viking is rendered. At 60fps,
that's 60 times per second:

    - (void) update:(ccTime)deltaTime { 
      [self applyJoystick:leftJoystick 
                   toNode:vikingSprite
             forTimeDelta:deltaTime];
    }

We'll need to schedule the update method to be called along with initializing the joystick/buttons.
Do this inside the init method:

    [self initJoystickAndButtons];
    [self scheduleUpdate];

A quick note about performance. If you have too many sprites and textures, your game will slow down.
Batch them with `CCSpriteBatchNode`. It will reduce the number of calls to OpenGL ES. This uses a
**texture atlas or sprite sheet**.

Images are best stored in power-of-two increments, otherwise you're wasting space. Instead of a
129x129 image, try to pack images together and sprite them in 256x256. It's another advantage of
using a texture atlas.

Two tools for creating texture atlas are:

* Zwoptex <http://zwoptexapp.com>
* TexturePacker <http://texturepacker.com>

Use any of the two tools to create a packed PNG image and corresponding plist file. Add the PNG and
plist files to your project, there should be an additional one for retina display with an extra
"-hd". Here's example code:

    CCSpriteBatchNode *chapter2SpriteBatchNode;
    if (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad) {
      [[CCSpriteFrameCache sharedSpriteFrameCache] 
        addSpriteFramesWithFile:@"scene1atlas.plist"];
      chapter2SpriteBatchNode =
        [CCSpriteBatchNode batchNodeWithFile:@"scene1atlas.png"];
    } else { 
      [[CCSpriteFrameCache sharedSpriteFrameCache]
        addSpriteFramesWithFile:@"scene1atlasiPhone.plist"];
      chapter2SpriteBatchNode =
        [CCSpriteBatchNode batchNodeWithFile:@"scene1atlasiPhone.png"];
    } 
    vikingSprite = [CCSprite spriteWithSpriteFrameName:@"sv_anim_1.png"];
    [chapter2SpriteBatchNode addChild:vikingSprite];
    [self addChild:chapter2SpriteBatchNode];
    [vikingSprite
      setPosition:CGPointMake(screenSize.width/2, screenSize.height*0.17f)];

Make sure GAME_AUTOROTATION is defined in GameConfig.h to perform better on iPhone 3G and older
devices:

    #define GAME_AUTOROTATION kGameAutorotationCCDirector

# Introduction to Cocos2D Animation and Actions

All animations are single image frames being switched in/out. The two steps:

1. Create a CCAnimation to specify frames (images/textures)
2. Create a CCAnimate action and run it on a sprite

    // Animation example with a Sprite (not a CCSpriteBatchNode)
    CCSprite *animatingRobot = [CCSprite spriteWithFile:@"an1_anim1.png"];
    [animatingRobot setPosition:
      ccp([vikingSprite position].x + 50.0f, [vikingSprite position].y)];
    [self addChild:animatingRobot];
    CCAnimation *robotAnim = [CCAnimation animation];
    [robotAnim addFrameWithFilename:@"an1_anim2.png"]; 
    [robotAnim addFrameWithFilename:@"an1_anim3.png"];
    [robotAnim addFrameWithFilename:@"an1_anim4.png"];
    id robotAnimationAction = [CCAnimate actionWithDuration:0.5f
                                                  animation:robotAnim
                                       restoreOriginalFrame:YES];
    id repeatRobotAnimation =
      [CCRepeatForever actionWithAction:robotAnimationAction];
    [animatingRobot runAction:repeatRobotAnimation]; 

Animating with a CCSpriteBatchNode is a bit different for retrieving the sprites:

    CCAnimation *exampleAnim = [CCAnimation animation];
    [exampleAnim addFrame:[[CCSpriteFrameCache sharedSpriteFrameCache]
        spriteFrameByName:@"sv_anim_2.png"]];
    [exampleAnim addFrame:[[CCSpriteFrameCache sharedSpriteFrameCache]
        spriteFrameByName:@"sv_anim_3.png"]];
    [exampleAnim addFrame:[[CCSpriteFrameCache sharedSpriteFrameCache]
        spriteFrameByName:@"sv_anim_4.png"]];

CCAnimationCache lets you store/retrieve sprite animations as needed which is very useful for games
with a lot of similar animations. It's a cache, so you'll need to check if your animation is present
or not:

    CCAnimationCache cache = [CCAnimationCache sharedAnimationCache];
    [cache addAnimation:animation name:@"AnimationName"];
    [cache animationByName:@"AnimationName"];

CCAction lets you move, transform, transition your nodes:

    CCAction *moveAction =
      [CCMoveBy actionWithDuration:2.0f position:ccp(200.0f, 0.0f)];
    [vikingSprite runAction:moveAction];  // all CCNodes have this method

Animations are a special type of actions. Here are common ones:

* CCAnimate
* CCJumpBy
* CCRepeatForever
* CCSequence - combine two or more actions together
* CCSpawn - two or more starting at the same time

Animations get cumbersome if you wrote all this code. Cocos2d lets you store animation in property
list files along with sprite frames.

The authors suggest organizing your code around a GameObject, the root of all objects in your game.
It will inherit from CCSprite. GameCharacter will be characters in your game and include methods for
dealing with bounding boxes, health, and states.

In addition to the root classes, the authors setup a "Constants.h" and "CommonProtocols.h" that
include all of the constants, enums, and common protocols of the game.

GameObject will be our root class for all objects in the game. It inherits from CCSprite:

    // GameObject.h
    @interface GameObject : CCSprite {
      BOOL isActive;
      BOOL reactsToScreenBoundaries;
      CGSize screenSize;
      GameObjectType gameObjectType;
    }
    @property (readwrite) BOOL isActive;
    @property (readwrite) BOOL reactsToScreenBoundaries;
    @property (readwrite) CGSize screenSize;
    @property (readwrite) GameObjectType gameObjectType;
    - (void) changeState:(CharacterStates)newState;
    - (void) updateStateWithDeltaTime:(ccTime)deltaTime
                 andListOfGameObjects:(CCArray*)listOfGameObjects;
    - (CGRect) adjustedBoundingBox;
    - (CCAnimation*) loadPlistForAnimationWithName:(NSString*)animationName
                                      andClassName:(NSString*)className;
    @end

    // GameObject.m
    - (id) init {
      if((self=[super init])){
        CCLOG(@"GameObject init");
        screenSize = [CCDirector sharedDirector].winSize;
        isActive = TRUE;
        gameObjectType = kObjectTypeNone;
      }
      return self;
    }
    // ... other methods do CCLog(@"Should have inherited...") ...

`adjustedBoundingBox` takes into account transparent pixels for collisions, so you'll be able to
override the sprite's default bounding box. In Cocos2D, bounding boxes are called **axis-aligned
bounding boxes or AABB**.

The GameCharacter class provides a state machine brain, health, a check to make sure it's on screen,
and more:

    // GameCharacter.h
    @interface GameCharacter : GameObject {
      int characterHealth;
      CharacterStates characterState;
    }
    - (void) checkAndClampSpritePosition;
    - (int) getWeaponDamage;
    @property (readwrite) int characterHealth;
    @property (readwrite) CharacterStates characterState;
    @end 

    // GameCharacter.m
    - (void) checkAndClampSpritePosition {
      CGPoint currentSpritePosition = [self position];
      if (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad) {
        // Clamp for the iPad
        if (currentSpritePosition.x < 30.0f) {
          [self setPosition:ccp(30.0f, currentSpritePosition.y)];
        } else if (currentSpritePosition.x > 1000.0f) {
          [self setPosition:ccp(1000.0f, currentSpritePosition.y)];
        }
      } else {
        // Clamp for iPhone, iPhone 4, or iPod touch
        if (currentSpritePosition.x < 24.0f) {
          [self setPosition:ccp(24.0f, currentSpritePosition.y)];
        } else if (currentSpritePosition.x > 456.0f) { 
          [self setPosition:ccp(456.0f, currentSpritePosition.y)];
        }
      }
    }
    @end 

The method `checkAndClampSpritePosition` makes sure the character stays on the screen. Cocos2D uses
a point system. On the retina display, 1 point = 2 pixels. On the non-retina, 1 point = 1 pixel.

# Simple Collision Detection and the First Enemy

Let's make an enemy for the viking and have it do battle. Make a RadarDish class with these
animation properties:

    // RadarDish.h, use @property (nonatomic, retain)
    CCAnimation *tiltingAnim;
    CCAnimation *transmittingAnim;
    CCAnimation *takingAHitAnim;
    CCAnimation *blowingUpAnim; 
    GameCharacter *vikingCharacter;

RadarDish should override the changeState method:

    - (void) changeState:(CharacterStates)newState {
      [self stopAllActions];
      id action = nil;
      [self setCharacterState:newState];
      switch (newState) {
        case kStateSpawning:
          CCLOG(@"RadarDish->Starting the Spawning Animation");
          action = [CCAnimate actionWithAnimation:tiltingAnim
                             restoreOriginalFrame:NO];
          break;
        case kStateIdle:
          CCLOG(@"RadarDish->Changing State to Idle"); 
          action = [CCAnimate actionWithAnimation:transmittingAnim
                             restoreOriginalFrame:NO];
          break;
        case kStateTakingDamage:
          CCLOG(@"RadarDish->Changing State to TakingDamage");
          characterHealth = characterHealth - [vikingCharacter getWeaponDamage];
          if (characterHealth <= 0.0f) {
            [self changeState:kStateDead];
          } else {
            action = [CCAnimate actionWithAnimation:takingAHitAnim
                               restoreOriginalFrame:NO];
          }
          break;
        case kStateDead:
          CCLOG(@"RadarDish->Changing State to Dead");
          action = [CCAnimate actionWithAnimation:blowingUpAnim
                             restoreOriginalFrame:NO];
          break;
        default:
          CCLOG(@"Unhandled state %d in RadarDish", newState);
          break;
      }
      if (action != nil) { [self runAction:action]; }
    } 

RadarDish can be shown as spawning, idle, taking damage, or dead. Each state has a different
animation. The method updateStateWithDeltaTime will change the RadarDish state.

    - (void) updateStateWithDeltaTime:(ccTime)deltaTime
                 andListOfGameObjects:(CCArray*)listOfGameObjects {
      if (characterState == kStateDead) return;
      vikingCharacter =
        (GameCharacter*)[[self parent] getChildByTag:kVikingSpriteTagValue];
      CGRect vikingBoudingBox = [vikingCharacter adjustedBoundingBox];
      CharacterStates vikingState = [vikingCharacter characterState];
      // Calculate if the Viking is attacking and nearby
      if ((vikingState == kStateAttacking) &&
          (CGRectIntersectsRect([self adjustedBoundingBox], vikingBoudingBox))) {
        if (characterState != kStateTakingDamage) {
          // If RadarDish is NOT already taking Damage
          [self changeState:kStateTakingDamage];
          return;
        }
      }
      if (([self numberOfRunningActions] == 0) && (characterState != kStateDead)) {
        CCLOG(@"Going to Idle");
        [self changeState:kStateIdle];
        return;
      }
    } 

This method determines which state the RadarDish is in. RadarDish should have an init method which
sets each animation along with health and other instance variables.

The Viking class will be similar. It will inherit from GameCharacter and have a standing, breathing,
and walking animation for both itself and the mallet. It will also have a crouching, standing up,
and jumping animation. Finally, it should have a punching, damage, and death animation. Each one can
be stored as a property.

An interesting part of the Viking class is joystick application:

    - (void) applyJoystick:(SneakyJoystick *)aJoystick
              forTimeDelta:(float) deltaTime {
      CGPoint scaledVelocity = ccpMult(aJoystick.velocity, 128.0f);
      CGPoint oldPosition = [self position];
      CGPoint newPosition =
        ccp(oldPosition.x + scaledVelocity.x * deltaTime, oldPosition.y);
      [self setPosition:newPosition];
      self.flipX = oldPosition.x > newPosition.x;
    }

Flipping the viking via a vertical access so that when he moves in a direction, he will look in that
same direction. Cocos2D includes function for flipping pixels (`flipX` and `flipY`) so you don't
have to create separate images for each version of an image.

The updateStateWithDeltaTime:andListOfGameObjects: is a bit more complicated:

    - (void) updateStateWithDeltaTime:(ccTime)deltaTime
                 andListOfGameObjects:(CCArray*)listOfGameObjects {
      if (self.characterState == kStateDead ||
         ((self.characterState == kStateTakingDamage) &&
          ([self numberOfRunningActions] > 0))) return; // dead or taking damage
      // Check for collisions
      // Change this to keep the object count from querying it each time
      CGRect myBoundingBox = [self adjustedBoundingBox];
      for (GameCharacter *character in listOfGameObjects) {
        // This is Ole the Viking himself
        // No need to check collision with one's self
        if ([character tag] == kVikingSpriteTagValue) continue;
        CGRect characterBox = [character adjustedBoundingBox];
        if (CGRectIntersectsRect(myBoundingBox, characterBox)) {
          // Remove the PhaserBullet from the scene
          if ([character gameObjectType] == kEnemyTypePhaser) {
            [self changeState:kStateTakingDamage];
            [character changeState:kStateDead];
          } else if ([character gameObjectType] == kPowerUpTypeMallet) {
            // Update the frame to indicate Viking is
            // carrying the mallet
            isCarryingMallet = YES;
            [self changeState:kStateIdle];
            // Remove the Mallet from the scene
            [character changeState:kStateDead];
          } else if ([character gameObjectType] == kPowerUpTypeHealth) {
            [self setCharacterHealth:100.0f];
            // Remove the health power-up from the scene
            [character changeState:kStateDead];
          }
        }
      }
      [self checkAndClampSpritePosition];
      if ((self.characterState == kStateIdle) ||
          (self.characterState == kStateWalking) ||
          (self.characterState == kStateCrouching) ||
          (self.characterState == kStateStandingUp) ||
          (self.characterState == kStateBreathing)) {
        if (jumpButton.active) {
          [self changeState:kStateJumping];
        } else if (attackButton.active) {
          [self changeState:kStateAttacking];
        } else if ((joystick.velocity.x == 0.0f) && (joystick.velocity.y == 0.0f)) {
          if (self.characterState == kStateCrouching) [self changeState:kStateStandingUp];
        } else if (joystick.velocity.y < -0.45f) {
          if (self.characterState != kStateCrouching) [self changeState:kStateCrouching];
        } else if (joystick.velocity.x != 0.0f) {
          // dpad moving
          if (self.characterState != kStateWalking)
            [self changeState:kStateWalking];
          [self applyJoystick:joystick forTimeDelta:deltaTime];
        }
      }
      if ([self numberOfRunningActions] == 0) {
        // Not playing an animation
        if (self.characterHealth <= 0.0f) {
          [self changeState:kStateDead];
        } else if (self.characterState == kStateIdle) {
          millisecondsStayingIdle = millisecondsStayingIdle + deltaTime;
          if (millisecondsStayingIdle > kVikingIdleTimer) {
            [self changeState:kStateBreathing];
          }
        } else if ((self.characterState != kStateCrouching) &&
                   (self.characterState != kStateIdle)){
          millisecondsStayingIdle = 0.0f;
          [self changeState:kStateIdle];
        }
      }
    }

The bounding box for the viking:

    -(CGRect)adjustedBoundingBox {
      // Adjust the bouding box to the size of the sprite
      // without the transparent space
      CGRect vikingBoundingBox = [self boundingBox]; 
      float xOffset;
      float xCropAmount = vikingBoundingBox.size.width * 0.5482f;
      float yCropAmount = vikingBoundingBox.size.height * 0.095f;
      if ([self flipX] == NO) {
        // Viking is facing to the rigth, back is on the left
        xOffset = vikingBoundingBox.size.width * 0.1566f;
      } else {
        // Viking is facing to the left; back is facing right
        xOffset = vikingBoundingBox.size.width * 0.4217f;
      }
      vikingBoundingBox = CGRectMake(
        vikingBoundingBox.origin.x + xOffset,
        vikingBoundingBox.origin.y,
        vikingBoundingBox.size.width - xCropAmount,
        vikingBoundingBox.size.height - yCropAmount);
      if (characterState == kStateCrouching) {
        // Shrink the bounding box to 56% of height
        // 88 pixels on top on iPad
        vikingBoundingBox = CGRectMake(
          vikingBoundingBox.origin.x,
          vikingBoundingBox.origin.y,
          vikingBoundingBox.size.width,
          vikingBoundingBox.size.height * 0.56f);
      }
      return vikingBoundingBox;
    } 

The updateStateWithDeltaTime method checks for collisions with other objects via intersection of
bounding boxes. It also checks the current state of the viking. Using this informations, it
determines the new state for the Viking.

The adjustedBoundingBox method takes into account transparent pixels.

The Viking class should also include an init method which initializes all of its animations and
stores them in instance variables.

Now GameplayLayer needs to load RadarDish and Viking onto itself. Add an instance variable:

    CCSpriteBatchNode *sceneSpriteBatchNode;

This will hold all of the game layer's nodes. We'll need to delegate the calls to update:

    - (void) update:(CCTime)deltaTime {
      CCArray *listOfGameObjects = [sceneSpriteBatchNode children];
      for (GameCharacter *tempChar in listOfGameObjects) {
        [tempChar updateStateWithDeltaTime:deltaTime
                      andListOfGameObjects:listOfGameObjects];
    }

You can move the creation code into GameplayerLayer's init method or use a helper method. Here's
what the initialization code looks like:

    [[CCSpriteFrameCache sharedSpriteFrameCache]
      addSpriteFramesWithFile:@"scene1atlasiPhone.plist"];
    sceneSpriteBatchNode =
      [CCSpriteBatchNode batchNodeWithFile:@"scene1atlasiPhone.png"];
    [self addChild:sceneSpriteBatchNode z:0];
    [self initJoystickAndButtons];
    
    Viking *viking = [[Viking alloc]
      initWithSpriteFrame:[[CCSpriteFrameCache sharedSpriteFrameCache]
        spriteFrameByName:@"sv_anim_1.png"]];
    [viking setJoystick:leftJoystick];
    [viking setJumpButton:jumpButton];
    [viking setAttackButton:attackButton];
    [viking setPosition:ccp(screenSize.width * 0.35f, screenSize.height * 0.14f)];
    [viking setCharacterHealth:100];
    [sceneSpriteBatchNode addChild:viking
                                 z:kVikingSpriteZValue
                               tag:kVikingSpriteTagValue];
    [self createObjectOfType:kEnemyTypeRadarDish
                  withHealth:100
                  atLocation:ccp(screenSize.width*0.878f, screenSize.height*0.13f)
                  withZValue:10];
    [self scheduleUpdate]; 

# More Actions, Effects, and Cocos2D Scheduler

Let's make a Mallet power-up. Make a Mallet class with one instance variable:

    @property (nonatomic, retain) CCAnimation *malletAnim;

It inherits from GameObject. The init method will setup the animation and other instance variables:

    - (id) init {
      if (!(self = [super init])) return;
      screenSize = [CCDirector sharedDirector].winSize;
      gameObjectType = kPowerUpTypeMallet;
      [self setMalletAnim:
        [self loadPlistForAnimationWithName:@"malletAnim"
                               andClassName:NSStringFromClass([self class])]];
      [self changeState:kStateSpawning];
      return self;
    }

The changeState: method is pretty simple, it will start animating on spawn or it will remove itself
when used up:

    - (void)changeState:(CharacterStates)newState {
      if (newState == kStateSpawning) {
        [self runAction:[CCRepeatForeveractionWithAction:
          [CCAnimate actionWithAnimation:malletAnim restoreOriginalFrame:NO]]];
      } else {
        [self setVisible:NO];
        [self removeFromParentAndCleanup:YES];
      }
    }

The updateStateWithDeltaTime: method will make sure the mallet is either on the ground or falling
towards the ground:

    - (void)updateStateWithDeltaTime:(ccTime)deltaTime
                andListOfGameObjects:(CCArray *)listOfGameObjects {
      float groundHeight = screenSize.height * 0.065f;
      if ([self position].y > groundHeight) {
        [self setPosition:ccp([self position].x, [self position].y - 5.0f)];
      }
    }

The health power-up is almost the exact same code. Except its gameObjectType is different and uses a
different sprite/animation (a sandwich!).

Now we'll add a SpaceCargoShip which goes back and forth. When it nears the Viking, it will drop a
power up. There are no animations, it'll use basic move actions. The delegate knows how to create
the power ups. It will have two instance variables:

    BOOL hasDroppedMallet;
    id <GameplayLayerDelegate> delegate;

The init method starts the action:

    - (id) init {
      if (!(self = [super init])) return;
      hasDroppedMallet = NO;
      float shipHeight = screenSize.height * 0.71f;
      CGPoint position1 = ccp(screenSize.width * -0.48f, shipHeight);
      CGPoint position2 = ccp(screenSize.width * 2.0f, shipHeight);
      CGPoint position3 = ccp(position2.x * -1.0f, shipHeight);
      CGPoint offScreen = ccp(screenSize.width * -1, screenSize.height * -1);
      id action = [CCRepeatForever actionWithAction:
        [CCSequence actions:
          [CCDelayTime actionWithDuration:2.0f], // otherwise appears too much
          [CCMoveTo actionWithDuration:0.01f position:position1],
          [CCScaleTo actionWithDuration:0.01f scale:0.5f],
          [CCFlipX actionWithFlipX:YES],
          [CCMoveTo actionWithDuration:0.01f position:position2],
          [CCScaleTo actionWithDuration:0.1f scale:1.0f],
          [CCFlipX actionWitihFlipX:NO],
          [CCMoveTo actionWithDuration:7.5 position:position3],
          [CCScaleTo actionWithDuration:0.1f scale:2.0f],
          [CCFlipX actionWithFlipX:YES],
          [CCMoveTo actionWithDuration:6.5f position:position2],
          [CCFlipX actionWithFlipX:NO],
          [CCScaleTo actionWithDuration:0.1f scale:2.0f],
          [CCMoveTo actionWithDuration:5.5 position:position3],
          [CCFlipX actionWithFlipX:YES],
          [CCScaleTo actionWithDuration:0.1f scale:4.0f],
          [CCMoveTo actionWithDuration:4.5f position:position2],
          [CCCallFunc actionWithTarget:self selector:@selector(dropCargo)],
          [CCMoveTo actionWithDuration:0.0f position:offScreen],
          nil];
      [self runAction:action];
      return self;
    }

This sequence of movements works really well for background objects in your games. The dropCargo
method does just what it says:

    - (void) dropCargo {
      [delegate createObjectOfType:(hasDroppedMallet ? kPowerUpTypeHealth : kPowerUpTypeMallet)
                        withHealth:0.0f
                        atLocation:ccp(screenSize.width/2, screenSize.height)
                        withZValue:50];
      hasDroppedMallet = YES;
    }

The EnemyRobot class has more animations: robotWalkingAnim, raisePhaserAnim, shootPhaserAnim,
lowerPhaserAnim, torsoHitAnim, headHitAnim, and robotDeathAnim. It also has a few states: spawning,
idle, walking, attacking, taking damage, and dead. It uses some special CCActions:

* CCCallFunc - wrap a method to work with CCAction
* CCCallFuncN - passes current node
* CCCallFuncND - passes current node and data pointer

Cocos2D has built in support for effects. They're packaged as normal actions. Effects act on the
OpenGL ES frame buffer object (FBO) first before it gets sent to the GPU for processing and onscreen
display. You can apply it to a single CCSprite, all of a CCSpriteBatchNode sprites, or to a CCLayer
(everything on that layer):

    id wavesAction = [CCWaves actionWithWaves:5
                                    amplitude:20
                                   horizontal:NO
                                     vertical:YES
                                         grid:ccg(15, 10)
                                     duration:20];
    [backgroundImage runAction:[CCRepeatForever actionWithAction:wavesAction]];
    // ...
    [backgroundImage runAction:[CCStopGrid action]];

# Text, Fonts, and the Written Word

CCLabelTTF lets you display text with minimal setup and code:

    CCLabelTTF *label = [CCLabelTTF labelWithString:@"Hello World"
                                           fontName:@"Market Felt"
                                           fontSize:64];

Under the hoods, CCLabelTTF uses CCTexture2D to make an image from text. You can use the CCLabelTTF
object like any other CCNode.

    [label setPosition:ccp(screenSize.width/2, screenSize.height/2)];
    [self addChild:label];
    [label runAction:[CCSpawn actions:
      [CCScaleBy actionWithDuration:2.0f scale:4],
      [CCFadeOut actionWithDuration:2.0f],
      nil]];

CCNodes have anchor points for positioning and alignment. The default anchor point is in the center.
The origin (0, 0) is the bottom left corner. Point (1, 1) is the top right corner. Anchoring uses
the range 0 to 1.

    [label setAnchorPoint:ccp(0, 0)]; // bottom left
    [label setAnchorPoint:ccp(0, 1)]; // top left
    [label setAnchorPoint:ccp(1, 0)]; // bottom right
    [label setAnchorPoint:ccp(1, 1)]; // top right

Anchor points are also used for rotations. If you change the anchor point for positioning, it also
affects rotations.

CCLabelBMFont (BM = bitmapped) can be used to render your own custom fonts. A bitmapped font atlas
is an image containing all characters you want to display. Cocos2D supports the `fnt` file format
for fonts. You can use the apps Hiero or Glyph Designer to create font files.

    CCLabelBMFont *label = [CCLabelBMFont labelWithString:@"Game Start"
                                                  fntFile:@"Font.fnt"];

Overlaying your game with text labels is very useful for debugging.

# Main Menu, Level Completed, Credits Screen

A game is made up of scenes. So far, we've made a GameScene. We'll also make:

* MainMenuScene
* LevelCompleteScene
* OptionsScene
* CreditsScene

We'll also make a GameManager singleton which tells the director which scene to display.

    @interface GameManager : NSObject {
      BOOL isMusicON;
      BOOL isSoundEffectsON;
      BOOL hasPlayerDied;
      SceneTypes currentScene;
    }
    @property (readwrite) BOOL isMusicON;
    @property (readwrite) BOOL isSoundEffectsON;
    @property (readwrite) BOOL hasPlayerDied;

    + (GameManager *) sharedGameManager;
    - (void) runSceneWithID:(SceneTypes)sceneID;
    - (void) openSiteWithLinkType:(LinkTypes)linkTypeToOpen;
    @end

There are two enums here: SceneTypes and LinkTypes (think URL links to the developer's website and
more). The sharedGameManager method just returns a singleton GameManager. alloc is overidden to
prevent more than one game manager being allocated (using NSAssert). init just sets all the initial
variables.

    static GameManager *_sharedGameManager;
    + (id) alloc {
      @synchronized([GameManager class]) {
        NSAssert( _sharedGameManager == nil,
          @"Attempted to allocate second GameManager.");
        _sharedGameManager = [[super alloc] init];
        return _sharedGameManager;
      }
    }

The runSceneWithID method checks the validity of the sceneID and then tells CCDirector to switch
scenes:

    switch (sceneID) {
      // ...
      case kIntroScene:
        sceneToRun = [IntroScene node];
        break;
      // ...
    }
    if ([[CCDirector sharedDirector] runningScene]) {
      [[CCDirector sharedDirector] replaceScene:sceneToRun];
    } else {
      [[CCDirector sharedDirector] runWithScene:sceneToRun];
    }

Cocos2D has a built in menu system:

* CCMenu has menu list items, buttons, and toggles. Gets added to CCLayer.
* CCMenuAtlasFont is a bitmapped font atlas class for text strings/buttons.
* CCMenuItemFont is a menu item that displays text.
* CCMenuItemImage for normal/hover/active images.
* CCMenuItemLabel uses CCLabelTTF.
* CCMenuItemSprite just like CCMenuItemImage except uses CCSprite.
* CCMenuItemToggle is a switch made of text or a label.

The MainMenuScene should just add MainMenuLayer as a child in its init method:

    mainMenuLayer = [MainMenuLayer node];
    [self addChild:mainMenuLayer];

And MainMenuLayer has two menus:

    CCMenu *mainMenu;
    CCMenu *sceneSelectMenu;

It also includes some private methods: buyBook, showOptions, and playScene:. playScene: takes a
CCMenuItemFont.

    - (void) playScene:(CCMenuItemFont *)itemPassedIn {
      if ([itemPassedIn tag] == 1) {
        [[GameManager sharedGameManager] runSceneWithID:kIntroScene];
      } else {
        CCLog("Placeholder for next chapters.");
      }
    }

The methods displayMainMenu and displaySceneSelection are used for rendering.

    - (void) displayMainMenu {
      CCSize screenSize = [CCDirector sharedDirector].winSize;
      if (sceneSelectMenu != nil) {
        [sceneSelectMenu removeFromParentAndCleanup:YES];
      }
      CCMenuItemImage *playGameButton =
        [CCMenuItemImage itemFromNormalImage:@"PlayGameButtonNormal.png"
                               disabledImage:nil
                                      target:self
                                    selector:@selector(displaySceneSelection)];
      CCMenuItemImage *buyBookButton =
        [CCMenuItemImage itemFromNormalImage:@"BuyBookButtonNormal.png"
                               selectedImage:@"BuyBookButtonSelected.png"
                               disabledImage:nil
                                      target:self
                                    selector:@selector(buyBook)];
      mainMenu = [CCMenu menuWithItems:playGameButton, buyBookButton, nil];
      [mainMenu alignItemsVerticallyWithPadding:screenSize.height * 0.059f];
      [mainMenu setPosition:ccp(screenSize.width * 2, screenSize.height / 2)];
      id moveAction = [CCMoveTo actionWithDuration:1.0f
        position:ccp(screenSize.width * 0.85, screenSize.height / 2)];
      id moveEffect = [CCEaseIn actionWithAction:moveAction rate:1.0f];
      [mainMenu runAction:moveEffect];
      [self addChild:mainMenu z:0 tag:kMainMenuTagValue];
    }

Buttons use a target/selector for their action on click, just like AppKit. The method
displaySceneSelection does the same thing, it constructs a menu and shows it. The cleanup and
addChild is similar.

    - (void) displaySceneSelection {
      if (mainMenu != nil) {
        [mainMenu removeFromParentAndCleanup:YES];
        // ...
        [self addChild:sceneSelectMenu z:1 tag:kSceneMenuTagValue];
      }
    }

MainMenuLayer should initialize with an image background:

    CCSprite *background = [CCSprite spriteWithFile:@"MainMenuBackground.png"];
    [background setPosition:ccp(screenSize.width/2, screenSize.height/2)];
    [self addChild:background];
    [self displayMainMenu];

The intro, credits, level complete, and options menu are setup the same way. Layers have a property
called `isTouchEnabled`, if it's set to `YES` then they will receive `ccTouchesBegan:withEvent:`
messages.

    self.isTouchEnabled = YES;
    // ...
    - (void) ccTouchesBegan:(NSSet *)touches withEvent:(UIEvent *)event {
      CCLOG(@"Touches received, skipping intro");
      [[GameManager sharedGameManager] runSceneWithID:kGameLevel1];
    }

# Pump Up the Volume!

Apple provides AVAudioPlayer and OpenAL. AVAudioPlayer is quick and simple while OpenAL is low-level
but provides greater control. Cocos2D comes with CocosDenshion, a wrapper around both frameworks.
CocosDenshion uses the `CD` namespace. You'll be using CocosDenshion's SimpleAudioEngine API.

Be sure to copy sound files into your project.

The Space Viking game has a few constants and macros related to sound.

    #define AUDIO_MAX_WAITTIME 150
    typedef enum {
      kAudioManagerUninitialized=0, 
      kAudioManagerInitializing=2,
      kAudioManagerInitialized=100,
      kAudioManagerLoading=200,
      kAudioManagerReady=300
    } GameManagerSoundState;
    // Audio Constants
    #define SFX_NOTLOADED NO
    #define SFX_LOADED YES
    #define PLAYSOUNDEFFECT(...) \
    [[GameManager sharedGameManager] playSoundEffect:@#__VA_ARGS__]
    #define STOPSOUNDEFFECT(...) \
    [[GameManager sharedGameManager] stopSoundEffect:__VA_ARGS__]
    // Background Music
    // Menu Scenes
    #define BACKGROUND_TRACK_MAIN_MENU @"VikingPreludeV1.mp3"
    // GameLevel1 (Ole Awakens)
    #define BACKGROUND_TRACK_OLE_AWAKES @"SpaceDesertV2.mp3" 
    // Physics Puzzle Level
    #define BACKGROUND_TRACK_PUZZLE @"VikingPreludeV1.mp3"
    // Physics MineCart Level
    #define BACKGROUND_TRACK_MINECART @"DrillBitV2.mp3"
    // Physics Escape Level
    #define BACKGROUND_TRACK_ESCAPE @"EscapeTheFutureV3.mp3" 

The authors keep their sound effect filenames in a plist file. Music tends to be the second biggest
asset to deal with in games. You don't want to tie up the UI thread while loading music into memory.
Loading it asynchronously helps.

    // GameplayLayer.h
    #import "SimpleAudioEngine.h"
    // ... instance variables ...
    SimpleAudioEngine *soundEngine;

    // GameplayLayer.m
    - (void) loadAudio {
      // Loading Synchronously
      [CDSoundEngine setMixerSampleRate:CD_SAMPLE_RATE_MID];
      [[CDAudioManager sharedManager] setResignBehavior:kAMRBStopPlay
                                             autoHandle:YES];
      soundEngine = [SimpleAudioEngine sharedEngine];
      [soundEngine preloadBackgroundMusic:BACKGROUND_TRACK_OLE_AWAKES];
      [soundEngine playBackgroundMusic:BACKGROUND_TRACK_OLE_AWAKES]; 
    }

    // in GameplayLayer's init
    [self loadAudio];

To load a sound effect, play it, then unload it:

    [soundEngine preloadEffect:@"soundname.wav"];
    [soundEngine playEffect:@"soundname.wav"];
    [soundEngine stopEffect:@"soundname.wav"];
    [soundEngine unloadEffect:@"soundname.wav"];

Use NSOperationQueue to initialize audio in background threads. CocosDenshion is not designed to be
thread safe, so don't attempt to load and play audio at the same time.

    - (void) setupAudioEngine {
      if (hasAudioBeenInitialized) return;
      hasAudioBeenInitialized = YES;
      NSOperationQueue *queue = [[NSOperationQueue new] autorelease];
      NSInvocationOperation *asyncSetupOperation = 
        [[NSInvocationOperation alloc] initWithTarget:self
                                             selector:@selector(initAudioAsync)
                                               object:nil];
      [queue addOperation:asyncSetupOperation];
      [asyncSetupOperation autorelease];
    }

    - (void) initAudioAsync {
      managerSoundState = kAudioManagerInitializing;
      [CDSoundEngine setMixerSampleRate:CD_SAMPLE_RATE_MID];
      // only play if there's no background music
      [CDAudioManager initAsynchronously:kAMM_FxPlusMusicIfNoOtherAudio];
      while ([CDAudioManager sharedManagerState] != kAMStateInitialised) {
        [NSThread sleepForTimeInterval:0.1];
      }
      CDAudioManager *audioManager = [CDAudioManager sharedManager];
      if (!audioManager.soundEngine || !audioManager.soundEngine.functioning) {
        CCLOG(@"CocosDenshion failed to init.");
        managerSoundState = kAudioManagerFailed;
      } else {
        [audioManager setResignBehavior:kAMRBStopPlay autoHandle:YES];
        soundEngine = [SimpleAudioEngine sharedEngine];
        managerSoundState = kAudioManagerReady;
        CCLOG(@"CocosDenshion is ready.");
      }
    }

Whenever you change scenes, be sure the preload the sounds for that scene. Then use the
`playEffect:` method to actually play the sound. When you change out of the scene, use
`unloadEffect:`.

There are equivalents for background music. Just stopping the background music will release the
resource.

    [soundEngine preloadBackgroundMusic:@"music.wav"];
    [soundEngine playBackgroundMusic:@"music.wav"];
    [soundEngine stopBackgroundMusic];

A useful method for chaining sounds with actions is using CCCallFunc.

    [CCCallFunc actionWithTarget:self selector:@selector(playSound)];

For easy background threads, use performSelectorInBackground.

    [self performSelectorInBackground:@selector(playSound) withObject:self];

For more control, use SimpleAudioEngine's `playEffect:pitch:pan:gain:`.

# When the World Gets Bigger: Adding Scrolling

Add a getDimensionsOfCurrentScene method to GameManager.

    - (CGSize) getDimensionsOfCurrentScene {
      CGSize screenSize = [[CCDirector sharedDirector] winSize];
      if (currentScene == kGameLevel2) {
        return CGSizeMake(screenSize.width*2, screenSize.height*2);
      } else {
        return screenSize;
      }
    }

We'll be making the second level larger than the rest. You'll need to update
checkAndClampSpritePosition methods.

Without scrolling, your character will just move offscreen. We'll need to scroll the world as your
character moves through it. The SpaceViking projects includes a directory called
ParallaxBackgrounds. Import it. Parallax scrolling just scrolls a background at a different rate
than the foreground - causing an illusion of depth.

Create a GameScene2 class that subclsses CCScene. We'll also split the layers. There's a
GameControlLayer for the joystick and buttons, since these will never move. The
GameplayScrollingLayer is where all the action will be. Finally, the StaticBackgroundLayer will just
be a static background that doens't move for depth.

    @interface GameScene2 : CCScene {
      GameControlLayer *controlLayer;
    }
    @end

    @implementation GameScene2
    - (id) init {
      if (!(self = [super init])) {
        StaticBackgroundLayer *backgroundLayer = [StaticBackgroundLayer node];
        [self addChild:backgroundLayer z:0];
        controlLayer = [GameControlLayer node];
        [self addChild:controlLayer z:2];
        GameplayScrollingLayer *scrollingLayer = [GameplayScrollingLayer node];
        [scrollingLayer connectControlsWithJoystick:[controlLayer leftJoystick]
                                      andJumpButton:[controlLayer jumpButton]
                                    andAttackButton:[controlLayer attackButton]];
        [self addChild:scrollingLayer z:1];
      }
      return self;
    }
    @end

The method `connectControlsWithJoystick:andJumpButton:andAttackButton` is used so the scrolling
layer has access to the joystick/buttons. It needs this information for scrolling.

The StaticBackgroundLayer just renders a simple static image as the background. The GameControlLayer
should initialize the joystick and buttons as we've done previously.

First, let's create a simple scrolling layer with a background that's twice as long as the screen.
Then we'll add a parallax node and scroll with a TileMap layer.

    @interface GameplayScrollingLayer : CCLayer {
      CCSpriteBatchNode *sceneSpriteBatchNode;
      CCTMXTiledMap *tileMapNode;
      CCParallaxNode *parallaxNode;
    }
    - (void) connectControlsWithJoystick:(SneakyJoystick *)leftJoystick
                           andJumpButton:(SneakyButton *)jumpButton
                         andAttackButton:(SneakyButton *)attackButon;

The connection method just connects the various buttons to our viking. We'll add the method
addScrollingBackground which adds the long background.

    - (void)addScrollingBackground {
      CGSize screenSize = [[CCDirector sharedDirector] winSize];
      CGSize levelSize = [[GameManager sharedGameManager] getDmensionsOfCurrentScene];
      CCSprite *scrollingBackground;
      [CCSprite spriteWithFile:(UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad ?
          @"FlatScrollingLayer.png",
          @"FlatScrollingLayeriPhone.png")];
      [scrollingBackground setPosition:ccp(levelSize.width/2, levelSize.height/2)];
      [self addChild:scrollingBackground];
    }

The method was pretty simple, just adding a new sprite as a background. The init method will add a
sprite to the cache and allocate a new viking.

    - (id) init {
      if (!(self = [super init])) return;
      CGSize screenSize = [[CCDirector sharedDirector] winSize];
      BOOL isIpad = UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad ;
      [[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:
        (isIpad ? @"scene1atlas.plist", @"scene1atlasiPhone.plist")];
      sceneSpriteBatchNode = [CCSpriteBatchNode batchNodeWithFile:
        (isIpad ? @"scene1atlas.png" : @"scene1atlasiPhone.png"];
      [self addChild:sceneSpriteBatchNode];

      Viking *viking = [[Viking alloc] initWithSpriteFrame:
        [[CCSpriteFrameCache sharedSpriteFromCache] spriteFrameByName:@"sv_anim_1.png"]];
      [viking setJoystick:nil];
      [viking setJumpButton:nil];
      [viking setAttackButton:nil];
      [viking setPosition:ccp(screenSize.width*0.35f, screenSize.height*0.14f)];
      [viking setCharacterHealth:100];
      [sceneSpriteBatchNode addChild:viking z:1000 tag:kVikingSpriteTagValue];

      [self addScrollingBackground];
      [self scheduleUpdate];
      return self;
    }

The adjustLayer method will move the background layer appropriately whenever the viking moves.

    - (void) adjustLayer {
      Viking *viking = (Viking *) [sceneSpriteBatchNode getChildByTag:kVikingSpriteTagValue];
      float vikingXPosition = viking.position.x;
      CGSize screenSize = [[CCDirector sharedDirector] winSize];
      float halfOfTheScreen = screenSize.width / 2.0f;
      CGSize levelSize = [[GameManager sharedGameManager] getDimensionsOfCurrentScene];
      if (vikingXPosition > halfOfTheScreen &&
          vikingXPosition < (levelSize.width - halfOfTheScreen)) {
        float newXPosition = halfOfTheScreen - vikingXPosition;
        [self setPosition:ccp(newXPosition, self.position.y)];
      }
    }

If the viking is more than halfway across the screen and less than half a screen from the end of the
level, the layer gets scrolled. The update: method for this layer should call adjustLayer.

Cocos2D has a built in action called CCFollow which can follow any CCNode and can be used for layer
scrolling. Unfortunately, it works in both the X and Y axes, so we couldn't use it.

    id followAction = [CCFollow actionWithTarget:playerCharacter];
    [layer runAction:followAction];

To give more depth to the game, you can have multiple background layers scrolling at different rates
(known as Parallax Layers). Backgrounds that are closer to the player will scroll faster.

    - (void) addScrollingBackgroundWithParallax {
      CGSize screenSize = [[CCDirector sharedDirector] winSize];
      CGSize levelSize = [[GameManager sharedGameManager] getDimensionsOfCurrentScene];
      CCSprite *BGLayer1 = [CCSprite spriteWithFile:@"chap9_scrolling4iPhone.png"];
      CCSprite *BGLayer2 = [CCSprite spriteWithFile:@"chap9_scrolling2iPhone.png"];
      CCSprite *BGLayer3 = [CCSprite spriteWithFile:@"chap9_scrolling3iPhone.png"];
      parallaxNode = [CCParallaxNode node];
      [parallaxNode setPosition:ccp(levelSize.width/2.0f, screenSize.height/2.0f)];
      float xOffset = 0;

      [parallaxNode addChild:BGLayer1
                           z:40
               parallaxRatio:ccp(1.0f, 1.0f)
              positionOffset:ccp(0.0f, 0.0f)];
      xOffset = (levelSize.width/2) * 0.3f;
      [parallaxNode addChild:BGLayer2
                           z:20
               parallaxRatio:ccp(0.2f, 1.0f)
             positionOffset:ccp(xOffset, 0)];
      xOffset = (levelSize.width/2) * 0.8f;
      [parallaxNode addChild:BGLayer3
                           z:30
               parallaxRatio:ccp(0.7f, 1.0f)
             positionOffset:ccp(xOffset, 0)];
      [self addChild:parallaxNode z:10];
    }

Now switch addScrollingBackground with our new parallax background method. It works by using ratios
and offsets for each background.

Now we're going to make a cut scene with an infinite scrolling background of clouds. We'll have 25
clouds moving right to left at random speeds. When they go offscreen on the left, we'll reposition
them on the right side.

    @interface PlatformScrollingLayer : CCLayer {
      CCSpriteBatchNode *scrollingBatchNode;
    }
    @end

There will be 6 different clouds in the same texture atlas. CCSpriteBatchNode will include all 25
clouds, the viking, and the background layer.

    @interface PlatformScrollingLayer (Private)
    - (void) resetCloudWithNode:(id)node;
    - (void) createCloud;
    - (void) createVikingAndPlatform;
    - (void) createStaticBackground;
    @end

The init method initializes the batch node and calls other methods.

    - (id) init {
      if (!(self = [super init])) return nil;
      srandom(time(NULL));
      self.isTouchEnabled = YES;
      [self createStaticBackground];
      [CCSpriteFrameCache sharedSpriteFrameCache] 
        addSpriteFramesWithFile:@"ScrollingCloudsTextureAtlasiPhone.plist"];
      scrollingBatchNode =
        [CCSpriteBatchNode batchNodeWithFile:@"ScrollingCloudsTextureAtlasiPhone.png"];
      [self addChild:scrollingBatchNode];
      for (int x=0; x<25; x++) {
        [self createCloud];
      }
      [self createVikingAndPlatform];
      return self;
    }

The createStaticBackground method is simple and just adds a background node to the screen.

    - (void) createStaticBackground {
      CGSize screenSize = [CCDirector sharedDirector].winSize;
      CCSprite *background = [CCSprite spriteWithFile:@"tiles_grad_bkgrndiPhone.png"];
      [background setPosition:ccp(screenSize.width/2, screenSize.height/2)];
      [self addChild:background];
    }

The createCloud method creates a cloud using a random tile from our sprite.

    - (void) createCloud {
      int cloudToDraw = random() % 6;
      NSString *cloudFileName =
        [NSString stringWithFormat:@"tiles_cloud%d.png", cloudToDraw];
      CCSprite *cloudSprite = [CCSprite spriteWithSpriteFrameName:cloudFileName];
      [scrollingBatchNode addChild:cloudSprite];
      [self resetCloudWithNode:cloudSprite];
    }

resetCloudWithNode is used to reset the cloud's position to the right and use a CCMove action to
move it left.

    - (void) resetCloudWitihNode:(id)node {
      CGSize screenSize = [CCDirector sharedDirector].winSize;
      CCNode *cloud = (CCNode *) node;
      float xOffset = [cloud boundingBox].size.width / 2;
      int xPosition = screenSize.width + 1 + xOffset;
      int yPosition = random() % (int) screenSize.height;
      [cloud setPosition:ccp(xPosition, yPosition)];
      int moveDuration = random() % kMaxCloudMoveDuration;
      if (moveDuration < kMinCloudMoveDuration) {
        moveDuration = kMinCloudMoveDuration;
      }
      float offScreenXPosition = (xOffset * -1) - 1;
      id moveAction = [CCMoveTo actionWithDuration:moveDuration
                       position:ccp(offScreenXPosition, [cloud position].y)];
      id resetAction = [CCCallFuncNactionWithTarget:self selector:@selector(resetCloudWithNode:)];
      id sequenceAction = [CCSequence actions:moveAction, resetAction, nil];
      [cloud runAction:sequenceAction];

      int newZOrder = kMaxCloudMoveDuration - moveDuration;
      [scrollingBatchNode reorderChild:cloud z:newZOrder];
    }

Finally, the createVikingAndPlatform method is used to add the viking and his platform to the
screen.

    - (void) createVikingAndPlatform {
      CGSize screenSize = [CCDirector sharedDirector].winSize;
      int nextZValue = [scrollingBatchNode children].count + 1;
      CCSprite *platform = [CCSprite spriteWithSpriteFrameName:@"platform.png"];
      [platform setPosition:ccp(screenSize.width/2, screenSize.height * 0.09f)];
      [scrollingBatchNode addChild:platform z:nextZValue];
      nextZValue = nextZValue + 1;
      CCSprite *viking = [CCSprite sepriteWithSpriteFrameName:@"sv_anim_1.png"];
      [viking setPosition:ccp(screenSize.width/2, screenSize.height*0.23f)];
      [scrollingBatchNode addChild:viking z:nextZValue];
    }

# Basic Game Physics: Adding Realism with Box2D

Game physics lets you add more realism to your game for collisions, bouncing, collapsing, or
falling. Box2D is a physics library integrated with Cocos2D. You tell Box2D where to initially place
your objects and it does the rest.

For this example, we're going to add a see-saw to the game as a puzzle.

    @interface PuzzleLayer : CCLayer {
    }
    + (id) scene;
    @end

    @implementation PuzzleLayer
    + (id) scene {
      CCScene *scene = [CCScene node];
      PuzzleLayer *layer = [self node];
      [scene addChild:layer];
      return scene;
    }

    - (id) init {
      if (!(self = [super init])) return;
      CGSize winSize = [CCDirector sharedDirector].winSize;
      CCLabelTTF *label = [CCLabelTTF
        labelWithString:@"Hello, Mad Dreams of the Dead!"];
               fontName:@"Helvetica"
               fontSize:24.0];
      label.position = ccp(winSize.width/2, winSize.height/2);
      [self addChild:label];
      return self;
    }
    @end

When you created your project, you can choose the Cocos2D Application template with Box2D. We
didn't, so we'll have to manually add them. Just download Box2D from the website and add them to the
libs folder of your project. Be sure to copy items into destination folder. Next, click on your
project settings. Go to Build Settings for All/Combined projects. Look for Search Paths > Header
Search Paths. Add a new entry and add the libs directory.

Box2D uses C++, so you'll need to use Objective-C++ instead. Just rename your file extensions to
`.mm` instead of `.m` and Xcode will know how to handle it.

Box2D is optimized to work with meters, kilograms, and seconds. Objects of length between 0.1 and 10
meters are optimized for. A good conversion between Cocos2D coordinate system and Box2D is 100px = 1
meter for our viking game. Each game will have its own good ratio value (it depends on the size of
your sprites!)

    #define PTM_RATIO 100.0

That's for the iPad. What about iPhone?

    #define PTM_RATIO ((UI_USER_INTERFACE_IDIOM() == \
                        UIUserInterfaceIdiomPad) ? 100.0 : 50.0)

To get access to Box2D's functions and classes:

    #import "GLES-Render.h"

Now add this to PuzzleLayer:

    // instance variables
    b2World *world;
    GLESDebugDraw *debugDraw;

    // implementation
    - (void) setupWorld {
      b2Vec2 gravity = b2Vec2(0.0f, -10.0f); // x-axis and y-axis gravity
      bool doSleep = true;
      world = new b2World(gravity, doSleep);
    }

`-10.0f` is a downwards 10 meters/second^2 gravity which is close the the actual 9.8 m/s^2
acceleration of the real world.

Since we're using C++, we have to be sure to deallocate our initialized world when we're done with
it.

    - (void) dealloc {
      if (world) {
        delete world;
        world = NULL;
      }
      [super dealloc];
    }

Box2D's jargon:

* body - each individual object in Box2D world. It's a rigid world, so bodies don't squish when they
  collide.
* fixture - the pieces that make up a body.
* body definition - specification for properties of a body
* dynamic body - Box2D handles the movement
* kinematic body - game code handles the movement
* static body - the body doesn't move at all

Let's create a box in PuzzleLayer.

    - (void) createBoxAtLocation:(CGPointlocation)location withSize:(CGSize)size {
      b2BodyDef bodyDef;
      bodyDef.type = b2_dynamicBody;
      bodyDef.position = b2Vec2(location.x/PTM_RATIO, location.y/PTM_RATIO);
      b2Body *body = world->CreateBody(&bodyDef);

      b2PolygonShape shape;
      shape.SetAsBox(size.width/2/PTM_RATIO, size.height/2/PTM_RATIO);

      b2FixtureDef fixtureDef;
      fixtureDef.shape = &shape;
      fixtureDef.density = 1.0;  // higher the density, heavier it is
      body->CreateFixture(&fixtureDef);
    }

The Box2D body is there, but nothing actually gets rendered. Use Box2D's debugging capabilities to
draw something quickly.

    - (void) setupDebugDraw {
      debugDraw = new GLESDebugDraw(
        PTM_RATIO * [[CCDirector sharedDirector] contentScaleFactor]);
      world->SetDebugDraw(debugDraw);
      debugDraw->SetFlags(b2DebugDraw::e_shapeBit);
    }

    - (void) draw {
      glDisable(GL_TEXTURE_2D);
      glDisableClientState(GL_COLOR_ARRAY);
      glDisableClientState(GL_TEXTURE_COORD_ARRAY);

      world->DrawDebugData();

      glEnable(GL_TEXTURE_2D);
      glEnableClientState(GL_COLOR_ARRAY);
      glEnableClientState(GL_TEXTURE_COORD_ARRAY);
    }

    - (void) dealloc {
      [super dealloc];
      //...
      if (debugDraw) {
        delete debugDraw;
        debugDraw = nil;
      }
    }