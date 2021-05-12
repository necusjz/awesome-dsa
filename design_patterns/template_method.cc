/**
 * The Abstract Class defines a template method that contains a skeleton of some
 * algorithm, composed of calls to (usually) abstract primitive operations.
 *
 * Concrete subclasses should implement these operations, but leave the template
 * method itself intact.
 */
class AbstractClass {
public:
    virtual ~AbstractClass() {}
    virtual void PrimitiveOperation1() const = 0;
    virtual void PrimitiveOperation2() const = 0;
    void TemplateMethod() {
        PrimitiveOperation1();
        PrimitiveOperation2();
    }
};
/**
 * Concrete classes have to implement all abstract operations of the base class.
 * They can also override some operations with a default implementation.
 */
class ConcreteClassA : public AbstractClass {
public:
    void PrimitiveOperation1() const override {
        cout << "ConcreteClassA: PrimitiveOperation1 & ";
    }
    void PrimitiveOperation2() const override {
        cout << "PrimitiveOperation2" << endl;
    }
};

class ConcreteClassB : public AbstractClass {
public:
    void PrimitiveOperation1() {
        cout << "ConcreteClassB: PrimitiveOperation1 & ";
    }
    void PrimitiveOperation2() {
        cout << "PrimitiveOperation2" << endl;
    }
};
