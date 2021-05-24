/**
 * The base State class declares methods that all Concrete State should
 * implement and also provides a backreference to the Context object, associated
 * with the State. This backreference can be used by States to transition the
 * Context to another State.
 */
class Context;

class State {
public:
    virtual ~State() {}
    virtual void Handle(Context* c) = 0;
};

/**
 * The Context defines the interface of interest to clients. It also maintains a
 * reference to an instance of a State subclass, which represents the current
 * state of the Context.
 */
class Context {
private:
    State* state;

public:
    Context(State* s) : state(s) {}
    ~Context() {
        if (state != nullptr) {
            delete state;
            state = nullptr;
        }
    }
    void Request() {
        if (state == nullptr) {
            return;
        }
        state->Handle(this);
    }
    void SetState(State* s) {
        state = s;
    }
};

/**
 * Concrete States implement various behaviors, associated with a state of the
 * Context.
 */
class ConcreteStateA : public State {
public:
    void Handle(Context* c) override;
};

class ConcreteStateB : public State {
public:
    void Handle(Context* c) override {
        cout << "ConcreteStateB" << endl; 
        c->SetState(new ConcreteStateA());
    }
};

void ConcreteStateA::Handle(Context* c) { 
    cout << "ConcreteStateA" << endl; 
    c->SetState(new ConcreteStateB());
}
