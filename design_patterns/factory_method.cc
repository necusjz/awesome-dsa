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
class ConcreteProduct1 : public Product {
public:
    void Operation() {
        cout << "ConcreteProduct1" << endl;
    }
};
class ConcreteProduct2 : public Product {
public:
    void Operation() {
        cout << "ConcreteProduct2" << endl;
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
class ConcreteCreator1 : public Creator {
public:
    Product* FactoryMethod() {
        return new ConcreteProduct1();
    }
};
class ConcreteCreator2 : public Creator {
public:
    Product* FactoryMethod() {
        return new ConcreteProduct2();
    }
};
