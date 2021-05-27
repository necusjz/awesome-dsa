/**
 * It makes sense to use the Builder pattern only when your products are quite
 * complex and require extensive configuration.
 *
 * Unlike in other creational patterns, different concrete builders can produce
 * unrelated products. In other words, results of various builders may not
 * always follow the same interface.
 */
class Product {
private:
    list<string> parts;

public:
    void Add(string part) {
        parts.push_back(part);
    }
    void Show() {
        for (auto node = parts.begin(); node != parts.end(); node++) {
            cout << (*node) << " ";
        }
        cout << endl;
    }
};

/**
 * The Builder interface specifies methods for creating the different parts of
 * the Product objects.
 */
class Builder {
public:
    virtual ~Builder() {}
    virtual void BuildPartA() const = 0;
    virtual void BuildPartB() const = 0;
    virtual Product* GetResult() const = 0;
};

/**
 * The Concrete Builder classes follow the Builder interface and provide
 * specific implementations of the building steps. Your program may have several
 * variations of Builders, implemented differently.
 */
class ConcreteBuilder1 : public Builder {
private:
    Product* product;

public:
    ConcreteBuilder1() {
        product = new Product();
    }
    ~ConcreteBuilder1() {
        delete product;
    }
    void BuildPartA() const override {
        product->Add("ConcreteBuilder1: PartA");
    }
    void BuildPartB() const override {
        product->Add("ConcreteBuilder1: PartB");
    }
    Product* GetResult const override {
        return product;
    }
};

class ConcreteBuilder2 : public Builder {
private:
    Product* product;

public:
    ConcreteBuilder2() {
        product = new Product();
    }
    ~ConcreteBuilder2() {
        delete product;
    }
    void BuildPartA() const override {
        product->Add("ConcreteBuilder2: PartA");
    }
    void BuildPartB() const override {
        product->Add("ConcreteBuilder2: PartB");
    }
    Product* GetResult const override {
        return product;
    }
};

/**
 * The Director is only responsible for executing the building steps in a
 * particular sequence. It is helpful when producing products according to a
 * specific order or configuration. Strictly speaking, the Director class is
 * optional, since the client can control builders directly.
 */
class Director {
public:
    void Construct(Builder* builder) {
        builder->BuildPartA();
        builder->BuildPartB();
    }
};
