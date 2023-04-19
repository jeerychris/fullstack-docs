# overview

[深入浅出数据结构](https://www.bilibili.com/video/BV1Fv4y1f7T1?p=1&vd_source=0e72036c3cb260d7bb95074abdf9cc2f)

ADT, abstract data type

store and manipulate data in computer

- 逻辑结构
    - 线性 1:1 (前驱 ：后继)
        - list
        - stack
        - queue
    - 树 1:n
    - 图 m:n

- 存储结构
    - 顺序
    - 链表
    - 索引
    - 散列

- operation

非数值计算

effecient operation, algorithms

2 aspect:
- Mathmetical/Logical models
- Implementaion

# sequence

## primitive 数组

- 连续内存 (phisical)
- 读改, O(1) 
- insert, invalid, size 固定

### usage

### stl 

1. array
2. vecor, dynamic size

## list

单链表
双链表
循环链表

- logical 连续，but phisical
- 读取 O(n)
- insert, O(1)
- 无序，可重复

头节点: unify 空表 & normal

### impl

```cpp
// .h
template <typename Data>
struct Node {
    Data data;
    Node *pNext;
};

class MyForwardList {
    struct MyForwardListInfo *pImpl{};
public:
    MyForwardList();
    ~MyForwardList();

    bool isEmpty();
    int size();
    void clear();
    // insert place?
    // void insert();

    // pos range in [0, size()]
    Node *insert_after(int pos, Data data)

    Node *push_back(Data data) { return insert_after(size(), data); }
}
```

```cpp
struct MyForwardListInfo {
    Node *list{};
    MyForwardListInfo() : list(new Node){}
}

// list (x, node1) -> (x1, node2) -> (x2, nullptr)
// to
// list (x, nullptr)

MyForwardList::MyForwardList() :pImpl(new MyForwardListInfo){}
MyForwardList::~MyForwardList() {
    while (pImpl->list->next) {
        auto *tmp = pImpl->list->next;
        pImpl->list->next = tmp->next;
        delete tmp;
    }

    delete pImpl->list;
    delete pImpl;
    pImpl = nullptr;
}

bool MyForwardList::isEmpty() { return pImpl->list->next == nullptr; }

int MyForwardList::size() {
    int count = 0;
    auto *node = pImpl->list->next;
    while (node) {
        count += 1;
        node = node->next;
    }
}

Node *MyForwardList::insert_after(int pos, Data data) {
    if (pos < 0 || pos > size())  {
        assert(0)
        return nullptr;
    }

    Node *node = new Node{.data = data};

    Node *cur = pImpl->list;
    for (int i=0; i<pos; i++) {
        cur = cur->next;
    }

    node->next = cur->next;
    cur->next = node;

    return node;
}
```

### stl imp

1. forward_list

2. list


## 字符串 子串

### Backtrace

n * m

### KMS

滑动窗口, n + m