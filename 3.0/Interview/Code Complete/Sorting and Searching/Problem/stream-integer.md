# Stream Integer

出处

Having a stream of integers, design a data structure to support easy look up the number of values less than or equal to a given value.

## Solution

需要一个动态的数据结构，支持快速检索，并且满足一定的有序性，这样才能维护这个特殊属性(给定值在这个有序结构中的相对位置)，使用二叉搜索树。(注意堆没有其他数据结构例如哈希表的辅助，无法支持给定key的快速检索。)

## Complexity

与 BST 复杂度一致

## Code

```cpp
class Node{
    private:
        Node* trackhelp(Node*rt,int x);
    public:
        Node *left;
        Node *right;
        int key;
        int left_cnt;
        void track(int x);
        int getRank(int x);
        Node(int key,Node*l = NULL,Node*r =NULL,int cnt = 0):key(key),left(l),right(r),left_cnt(cnt){};
};

Node *Node::trackhelp(Node*rt, int x){
    if( rt == NULL) return new Node(x);
    if( x <= rt->key ){
        rt->left = trackhelp(rt->left,x);
        rt->left_cnt++;
    } else {
        rt->right = trackhelp(rt->right,x);
    }
    return rt;
}

void Node::track( int x){
     trackhelp(this,x);
}

int Node::getRank(int x){
    if(this == NULL) return -1;
    if(x == key)
       return left_cnt;
    if(x < key)
      return left->getRank(x);
    if(x > key){
        if(right->getRank(x) == -1) return -1;
        return left_cnt + 1 + right->getRank(x);
    }
}
```

