/**
 * The base Component interface defines operations that can be altered by
 * decorators.
 */
class Component{
public:
    virtual ~Component() {}
    virtual void Operation() const = 0;
};
/**
 * Concrete Components provide default implementations of the operations. There
 * might be several variations of these classes.
 */
class ConcreteComponent : public Component {
public:
    void Operation() const override {
        cout << "ConcreteComponent" << endl;
    }
};
/**
 * The base Decorator class follows the same interface as the other components.
 * The primary purpose of this class is to define the wrapping interface for all
 * concrete decorators. The default implementation of the wrapping code might
 * include a field for storing a wrapped component and the means to initialize
 * it.
 */
class Decorator : public Component {
private:
    Component* component;

public:
    Decorator(Component* c) : component(c) {}
    void Operation() const override {
        return this->component->Operation();
    }
};
/**
 * Concrete Decorators call the wrapped object and alter its result in some way.
 */
class ConcreteDecoratorA : public Decorator {
private:
    string addedState;

public:
    void Operation() const override {
        Decorator::Operation();
        addedState = "New State";
        cout << "ConcreteDecoratorA: " << addedState << endl;
    }
};
/**
 * Decorators can execute their behavior either before or after the call to a
 * wrapped object.
 */
class ConcreteDecoratorB : public Decorator {
private:
    void AddedBehavior() {
        cout << "ConcreteDecoratorB: New Behavior" << endl;
    }

public:
    void Operation() const override {
        Decorator::Operation();
        AddedBehavior();
    }
};
