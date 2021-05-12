/**
 * The Product interface declares the operations that all concrete products must
 * implement.
 */
class Product {
public:
    virtual ~Product() {}
    virtual void Operation() const = 0;
};
/**
 * Concrete Products provide various implementations of the Product interface.
 */
class ConcreteProductA : public Product {
public:
    void Operation() const override {
        cout << "ConcreteProductA" << endl;
    }
};

class ConcreteProductB : public Product {
public:
    void Operation() const override {
        cout << "ConcreteProductB" << endl;
    }
};
/**
 * The Creator class declares the factory method that is supposed to return an
 * object of a Product class. The Creator's subclasses usually provide the
 * implementation of this method.
 */
class Creator {
public:
    virtual ~Creator() {};
    virtual Product* FactoryMethod() const = 0;
};
/**
 * Concrete Creators override the factory method in order to change the
 * resulting product's type.
 */
class ConcreteCreatorA : public Creator {
public:
    Product* FactoryMethod() const override {
        return new ConcreteProductA();
    }
};

class ConcreteCreatorB : public Creator {
public:
    Product* FactoryMethod() const override {
        return new ConcreteProductB();
    }
};
