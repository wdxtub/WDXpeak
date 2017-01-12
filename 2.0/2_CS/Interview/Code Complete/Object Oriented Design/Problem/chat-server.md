# Chat Server

Explain hwo you would design a chat server. In particular, provide details about the various backend components, classes, and methods. What would be the hardest problems to solve?

## Solution

Some ideas:

+ Signing online and offline
+ Add requests (sending, accepting, and rejecting)
+ Updating a status message
+ Creating private and group chats
+ Adding new messages to private and group chats

We must have a concept of users, add request status, online status, and messages.

Other keywords: database, XML

+ class UserManager
+ class User
+ class Conversation
+ class GroupChat extends Conversation
+ class PrivateChat extends Conversation
+ class Message
+ class AddRequest
+ class UserStatus
+ enum UserStatusType
+ enum RequestStatus

