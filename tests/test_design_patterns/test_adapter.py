from src.design_patterns.adapter import UsbCable, UsbPort, MicroUsbCable, MicroToUsbAdapter


def test_adapter():
    usb_cable = UsbCable()
    usb_port = UsbPort()

    assert usb_cable.is_plugged is False
    assert usb_port.is_available is True

    usb_port.plug(usb_cable)

    assert usb_cable.is_plugged is True
    assert usb_port.is_available is False

    adapter = MicroToUsbAdapter(MicroUsbCable())
    usb_port = UsbPort()

    assert adapter.is_plugged is False
    assert usb_port.is_available is True

    usb_port.plug(adapter)

    assert adapter.is_plugged is True
    assert usb_port.is_available is False
