/**
 * Observer Design Pattern
 *
 * Intent: Lets you define a subscription mechanism to notify multiple objects
 * about any events that happen to the object they're observing.
 *
 * Note that there's a lot of different terms with similar meaning associated
 * with this pattern. Just remember that the Subject is also called the
 * Publisher and the Observer is often called the Subscriber and vice versa.
 * Also the verbs "observe", "listen" or "track" usually mean the same thing.
 */
class Observer {
public:
    virtual ~Observer() {}
    virtual void Update() = 0;
};

/**
 * The Subject owns some important state and notifies observers when the state
 * changes.
 */
class Subject {
private:
    list<Observer*> observers;

public:
    virtual ~Subject() {}
    void Attach(Observer* observer) {
        observers.push_back(observer);
    }
    void Detach(Observer* observer) {
        observers.remove(observer);
    }
    void Notify() {
        for (auto observer = observers.begin(); observer != observers.end(); observer++) {
            (*observer)->Update();
        }
    }
};

class ConcreteSubject : public Subject {
private:
    string subject_state;

public:
    string GetState() {
        return subject_state;
    }
    void SetState(string state) {
        subject_state = state;
    }
};

class ConcreteObserver : public Observer {
private:
    string name;
    ConcreteSubject* subject;
    string observer_state;

public:
    ConcreteObserver(ConcreteSubject* s, string n) {
        subject = s;
        name = n;
    }
    void Update() override {
        observer_state = subject->GetState();
        cout << "observer: " << name << ", its new state is: " << observer_state << endl;
    }
    string GetState() {
        return observer_state;
    }
    void SetState(string state) {
        observer_state = state;
    }
};
