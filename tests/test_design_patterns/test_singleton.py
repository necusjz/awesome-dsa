from src.design_patterns.singleton import ApplicationState


def test_singleton():
    state1 = ApplicationState.get_app_state()

    assert state1.is_login is False

    state2 = ApplicationState.get_app_state()
    state1.is_login = True

    assert state1.is_login is True
    assert state2.is_login is True
