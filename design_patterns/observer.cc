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
class IObserver {
public:
    virtual ~IObserver() {}
    virtual void Update() = 0;
};

class ISubject {
private:
    list<IObserver*> observers;

public:
    virtual ~ISubject() {}
    void Attach(IObserver* observer) {
        observers.push_back(observer);
    }
    void Detach(IObserver* observer) {
        observers.remove(observer);
    }
    void Notify() {
        for (auto observer = observers.begin(); observer != observers.end(); observer++) {
            (*observer)->Update();
        }
    }
};

/**
 * The Subject owns some important state and notifies observers when the state
 * changes.
 */
class Subject : public ISubject {
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

class Observer : public IObserver {
private:
    string name;
    Subject* subject;
    string observer_state;

public:
    Observer(Subject* s, string n) {
        subject = s;
        name = n;
    }
    void Update() {
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
