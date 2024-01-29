class ApplicationState:
    instance = None

    def __init__(self):
        self.is_login = False

    @staticmethod
    def get_app_state():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()

        return ApplicationState.instance
