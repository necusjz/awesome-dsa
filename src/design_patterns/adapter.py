class UsbCable:
    def __init__(self):
        self.is_plugged = False

    def plug_usb(self):
        self.is_plugged = True


class UsbPort:
    def __init__(self):
        self.is_available = True

    def plug(self, usb):
        if self.is_available:
            usb.plug_usb()

            self.is_available = False


class MicroUsbCable:
    def __init__(self):
        self.is_plugged = False

    def plug_micro_usb(self):
        self.is_plugged = True


class MicroToUsbAdapter(UsbCable):
    def __init__(self, micro_usb_cable):
        super().__init__()

        self.micro_usb_cable = micro_usb_cable
        self.micro_usb_cable.plug_micro_usb()

    # override UsbCable.plug_usb() if needed
