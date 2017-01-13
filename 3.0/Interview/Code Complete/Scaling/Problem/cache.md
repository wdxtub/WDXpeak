# Cache

出处

Imagine a web server for a simplified search engine. This system has 100 machines to respond to search queries, which may then call out using processSearch(string query) to another cluster of machines to actually get the result. The machine which responds to a given query is chosen at random, so you cannot guarantee that the same machine will always respond to the same request. The method processSearch is very expensive. Design a caching mechanism for the most recent queries. Be sure to explain how you would update the cache when data changes.

## Solution

Start from designing it for a single machine.

linkedlist + hashtable

Then expand to many machines

+ Option1: Each machine has its own cache
+ Option2: Each machine has a copy of the cache
+ Option3: Each machine stores a segment of the cache

LRU, LFU

