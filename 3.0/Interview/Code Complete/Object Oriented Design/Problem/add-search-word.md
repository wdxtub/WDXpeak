# Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

    void addWord(word)
    bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true

Note:

You may assume that all words are consist of lowercase letters a-z.


You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.

## Solution

```java
public class WordDictionary {
    static class TrieNode {
        // Initialize your data structure here.
        TrieNode[] children = new TrieNode[26];
        int count = 0;
        public TrieNode() {
        }

        TrieNode safe(int i){
            if(children[i] == null){
                children[i] = new TrieNode();
            }
            return children[i];
        }

        int index(char c){
            return (int)(c - 'a');
        }

        void insert(char[] word, int st, int len){
            if(len == 0){
                this.count++;
                return;
            }
            TrieNode t = safe(index(word[st]));
            t.insert(word, st + 1, len - 1);
        }

        boolean search(char[] word, int st, int len){
            if(len == 0){
                return this.count > 0;
            }
            if(word[st] == '.'){
                for(TrieNode t : children){
                    if(t != null){
                        if(t.search(word, st + 1, len - 1)){
                            return true;
                        }
                    }
                }
                return false;
            }
            TrieNode t = children[index(word[st])];
            if(t == null){
                return false;
            }
            return t.search(word, st + 1, len - 1);
        }
    }
    TrieNode root = new TrieNode();

    // Adds a word into the data structure.
    public void addWord(String word) {
        root.insert(word.toCharArray(), 0, word.length());
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        return root.search(word.toCharArray(), 0, word.length());
    }
}

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary = new WordDictionary();
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");
```

