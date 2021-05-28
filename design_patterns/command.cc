/**
 * The Receiver classes contain some important business logic. They know how to
 * perform all kinds of operations, associated with carrying out a request. In
 * fact, any class may serve as a Receiver.
 */
class Receiver {
public:
    void Action() {
        cout << "Receiver" << endl;
    }
};

/**
 * The Command interface declares a method for executing a command.
 */
class Command {
public:
    virtual ~Command() {}
    virtual void SetReceiver(Receiver* r) const = 0;
    virtual void Execute() const = 0;
};

/**
 * Some commands can delegate more complex operations to other objects called
 * "receivers".
 */
class ConcreteCommand : public Command {
private:
    Receiver* receiver;

public:
    void SetReceiver(Receiver* r) const override {
        receiver = r;
    }
    void Excute() const override {
        receiver->Action();
    }
};

/**
 * The Invoker is associated with one or several commands. It sends a request to
 * the command.
 */
class Invoker {
private:
    list<Command*> commands;

public:
    void SetCommand(Command* c) {
        commands.push_back(c);
    }
    void Notify() {
        for (auto c = commands.begin(); c != commands.end(); c++) {
            (*c)->Excute();
        }
    }
};
