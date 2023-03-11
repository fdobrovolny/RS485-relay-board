from minimalmodbus import Instrument


class RelayBoard:
    """
    Class for interaction with relay boards over modbus.

    By default, the relay is in state "closed" / LOW.
    "Closed" state means that COM is connected to NC and not to NO.
    "Open" state means that COM is connected to NO and not to NC and is indicated by LED.
    For this library state `True` means "open" state.

    e.g. Open = HIGH to relay, Closed = LOW to relay

    """

    board: Instrument
    channels: int

    def __init__(
        self,
        port: str,
        slaveaddress: int,
        channels: int = 16,
        baudrate: int = 9600,
        read_timeout: float = 0.2,
        close_port_after_each_call: bool = False,
        debug: bool = False,
    ):
        """
        Setup relay board.

        :param port: The serial port name, for example `/dev/ttyUSB0` (Linux),
                     `/dev/tty.usbserial` (OS X) or `COM4` (Windows).
        :param slaveaddress: Slave address in the range 0 to 247 (use decimal numbers, not hex).
        :param channels: Number of channels of the relay board.
        :param baudrate: Baudrate to use.
        :param read_timeout: Read timeout after each command.
        :param close_port_after_each_call: If the serial port should be closed after each call to the board.
        :param debug: Set this to `True` to print the communication details
        """

        self.board = Instrument(
            port=port,
            slaveaddress=slaveaddress,
            close_port_after_each_call=close_port_after_each_call,
            debug=debug,
        )
        self.board.serial.baudrate = baudrate
        self.board.serial.timeout = read_timeout

        self.channels = channels

    def check_channel_number(self, channel: int):
        """
        Check if channel number is between 1 and `self.channels`.

        :param channel:
        :raise ValueError:
        """
        if not (1 <= channel <= self.channels):
            raise ValueError("Invalid number of channel.")

    def check_seconds(self, seconds: int):
        """
        Check if seconds is between 0 and 255.

        :param seconds:
        :return:
        """
        if not (0 <= seconds <= 255):
            raise ValueError("Delay can be only in range 0-255 seconds")

    def open_relay(self, channel: int):
        """
        Open relay

        :param channel: channel channel
        """
        self.check_channel_number(channel)
        self.board.write_register(channel, value=0x0100, functioncode=6)

    def close_relay(self, channel: int):
        """
        Close relay

        :param channel: channel channel
        """
        self.check_channel_number(channel)
        self.board.write_register(channel, value=0x0200, functioncode=6)

    def set_relay(self, channel: int, state: bool):
        if state:
            self.open_relay(channel)
        else:
            self.close_relay(channel)

    def toggle(self, channel: int):
        """
        Toggle (Self-locking) relay

        :param channel: channel channel
        """
        self.check_channel_number(channel)
        self.board.write_register(channel, value=0x0300, functioncode=6)

    def latch(self, channel: int):
        """
        Latch (Inter-locking) relay

        :note: No idea what this does? This behaves like open.

        :param channel: channel channel
        """
        self.check_channel_number(channel)
        self.board.write_register(channel, value=0x0400, functioncode=6)

    def momentary(self, channel: int):
        """
        Momentary (Non-locking).

        Close relay for 1s.

        :param channel: channel channel
        """
        self.check_channel_number(channel)
        self.board.write_register(channel, value=0x0500, functioncode=6)

    def delay(self, channel: int, seconds: int):
        """
        Delay

        Open relay for <seconds>s.

        Works even if relay is currently opened.

        :param channel: channel channel
        :param seconds: channel of seconds to close the relay for
        """
        self.check_channel_number(channel)
        self.check_seconds(seconds)
        self.board.write_register(channel, value=(0x06 << 8) + seconds, functioncode=6)

    def open_all(self):
        """
        Open all relays.

        :param channel: channel channel
        """
        self.board.write_register(0, value=0x0700, functioncode=6)

    def close_all(self):
        """
        Close all relays.


        :param channel: channel channel
        """
        self.board.write_register(0, value=0x0800, functioncode=6)

    def read_relay(self, channel: int):
        self.check_channel_number(channel)
        return 1 == self.board.read_register(channel)

    def read_relays(self, start_channel: int, length: int):
        self.check_channel_number(start_channel)
        if self.channels - start_channel + 1 < length:
            raise ValueError("Invalid length.")
        return tuple(
            1 == x
            for x in self.board.read_registers(
                start_channel, number_of_registers=length
            )
        )

    def read_all_relays(self):
        return self.read_relays(1, self.channels)
