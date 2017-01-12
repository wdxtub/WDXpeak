# Database Doc V0.2

Basically there will be 3 tables in the database: `User`, `Note` and `Comment`. Here is the detail description of these three tables.

## User Table

Name | Type | Comment
:--: | :--: | :--:
userid | INT | `AUTO_INCREMENT` `PRIMARY_KEY`
username | VARCHAR(30) | no longer than 30 chars
password | VARCHAR(30) | no longer than 30 chars
gender | BIT | male / female
avatar | VARCHAR(128) | url address
info | TEXT | json description content

The content store in the `info` part includes:

+ age: int
+ birthday: date
+ what's up: string
+ region: place

(this part is for extenstion)

## Note Table

Name | Type | Comment
:--: | :--: | :--:
noteid | INT | `AUTO_INCREMENT` `PRIMARY_KEY`
longitude | VARCHAR(16) | longitude
latitude | VARCHAR(16) | Latitude
date | DATE | date of the post
content | VARCHAR(256) | content of the post
type | SMALLINT | different type of post
userid | INT | `FOREIGN_KEY`
info | TEXT | json description content

type detail

+ 0: Text
+ 1: Image
+ 2: Sound
+ 3: Video
+ 4: Lost&Found
+ 5: Poster/Activity
+ 6: Emotion
+ 7: Gossip

The content store in the `infor` part includes:

+ image:
+ sound:
+ video:

(this part is for extenstion)

## Comment Table

Name | Type | Comment
:--: | :--: | :--:
commentid | INT | `AUTO_INCREMENT` `PRIMARY_KEY`
date | DATE | date of the post
content | VARCHAR(256) | content of the post
userid | INT | `FOREIGN_KEY` (this is the user who posts the comment)
noteid | INT | `FOREIGN_KEY`

