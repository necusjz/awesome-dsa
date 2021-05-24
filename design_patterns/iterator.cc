/**
 * Iterator Design Pattern
 *
 * Intent: Lets you traverse elements of a collection without exposing its
 * underlying representation (list, stack, tree, etc.).
 */
class Iterator {
public:
    virtual ~Iterator() {}
    virtual string First() = 0;
    virtual string Next() = 0;
    virtual bool IsDone() = 0;
    virtual string Current() = 0;
};

class Aggregate {
public:
    virtual Iterator* CreateIterator() = 0;
    virtual int Count() = 0;
    virtual void Push(string s) = 0;
    virtual string Pop(int idx) = 0;
};

class ConcreteIterator : public Iterator {
private:
    Aggregate* aggregate;
    int idx;

public:
    ConcreteIterator(Aggregate* a) {
        idx = 0;
        aggregate = a;
    }
    string First() override {
        return aggregate->Pop(0);
    }
    string Next() override {
        string s;
        idx++;
        if (idx < aggregate->Count()) {
            s = aggregate->Pop(idx);
        }
        return s;
    }
    bool IsDone() override {
        return idx >= aggregate->Count();
    }
    string Current() override {
        return aggregate->Pop(idx);
    }
};

class ConcreteAggregate : public Aggregate {
private:
    vector<string> elements;
    Iterator* iterator;

public:
    ConcreteAggregate() {
        iterator = nullptr;
        elements.clear();
    }
    ~ConcreteAggregate() {
        if (iterator) {
            delete iterator;
            iterator = nullptr;
        }
    }
    Iterator* CreateIterator() override {
        if (iterator == nullptr) {
            iterator = new ConcreteIterator(this);
        }
        return iterator;
    }
    int Count() override {
        return elements.size();
    }
    void Push(string s) override {
        elements.push_back(s);
    }
    string Pop(int idx) override {
        string s;
        if (idx < Count()) {
            s = elements[idx];
        }
        return s;
    }
};
