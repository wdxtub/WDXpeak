# Pastebin

Design a system like Pastebin, where a user can enter a piece of text and get a randomly generated URL to access it.

## Solution

+ The system does not support user accounts or editing documents
+ The system tracks analytics of how many times each page is accessed
+ Old documents get deleted after not being accessed for a sufficiently long period of time
+ While there isnot true authentication on accessing documents, users should not be able to "guess" document URLs easily
+ The system has a frontend as well as an API
+ The analytics for each URL can be accessed through a stats link on each page.
+ Generate randome GUID
+ hashtable - mongodb

