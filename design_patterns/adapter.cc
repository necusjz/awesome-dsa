/**
 * The Target defines the domain-specific interface used by the client code.
 */
class Target {
public:
    virtual ~Target() {}
    virtual void Request() const = 0;
};

/**
 * The Adaptee contains some useful behavior, but its interface is incompatible
 * with the existing client code. The Adaptee needs some adaptation before the
 * client code can use it.
 */
class Adaptee {
public:
    void SpecificRequest() {
        cout << "Adaptee" << endl;
    }
};

/**
 * The Adapter makes the Adaptee's interface compatible with the Target's
 * interface.
 */
class Adapter : public Target {
private:
    Adaptee* adaptee;

public:
    Adapter() {
        adaptee = new Adaptee();
    }
    ~Adapter() {
        delete adaptee;
    }
    void Request() const override {
        adaptee->SpecificRequest();
    }
};
