/**
 * Each distinct product of a product family should have a base interface. All
 * variants of the product must implement this interface.
 */
class AbstractProductA {
public:
    virtual ~AbstractProductA() {}
    virtual void Operation() const = 0;
};

/**
 * Concrete Products are created by corresponding Concrete Factories.
 */
class ConcreteProductA1 : public AbstractProductA {
public:
    void Operation() const override {
        cout << "ConcreteProductA1" << endl;
    }
};

class ConcreteProductA2 : public AbstractProductA {
public:
    void Operation() const override {
        cout << "CConcreteProductA2" << endl;
    }
};

/**
 * Here's the the base interface of another product. All products can interact
 * with each other, but proper interaction is possible only between products of
 * the same concrete variant.
 */
class AbstractProductB {
public:
    virtual ~AbstractProductB() {}
    virtual void Operation() const = 0;
};

/**
 * Concrete Products are created by corresponding Concrete Factories.
 */
class ConcreteProductB1 : public AbstractProductB {
public:
    void Operation() const override {
        cout << "ConcreteProductB1" << endl;
    }
};

class ConcreteProductB2 : public AbstractProductB {
public:
    void Operation() const override {
        cout << "ConcreteProductB2" << endl;
    }
};

/**
 * The Abstract Factory interface declares a set of methods that return
 * different abstract products. These products are called a family and are
 * related by a high-level theme or concept. Products of one family are usually
 * able to collaborate among themselves. A family of products may have several
 * variants, but the products of one variant are incompatible with products of
 * another.
 */
class AbstractFactory {
public:
    virtual ~AbstractFactory() {}
    virtual AbstractProductA* CreateProductA() const = 0;
    virtual AbstractProductB* CreateProductB() const = 0;
};

/**
 * Concrete Factories produce a family of products that belong to a single
 * variant. The factory guarantees that resulting products are compatible. Note
 * that signatures of the Concrete Factory's methods return an abstract product,
 * while inside the method a concrete product is instantiated.
 */
class ConcreteFactory1 : public AbstractFactory {
public:
    AbstractProductA* CreateProductA() const override {
        return new ConcreteProductA1();
    }
    AbstractProductB* CreateProductB() const override {
        return new ConcreteProductB1();
    }
};

class ConcreteFactory2 : public AbstractFactory {
public:
    AbstractProductA* CreateProductA() const override {
        return new ConcreteProductA2();
    }
    AbstractProductB* CreateProductB() const override {
        return new ConcreteProductB2();
    }
};
