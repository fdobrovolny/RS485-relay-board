# RS485 relay board

Lightweight python library for interaction with R4D8B08 and R4D3B16

## Example

```python
from rs485_relay_board import RelayBoard


SLAVE_ADDR = 1
board = RelayBoard("/dev/ttyUSB0", SLAVE_ADDR)

board.open_all()
```

# RelayBoard API

* [RelayBoard](#rs485_relay_board.base.RelayBoard)
  * [\_\_init\_\_](#rs485_relay_board.base.RelayBoard.__init__)
  * [check\_channel\_number](#rs485_relay_board.base.RelayBoard.check_channel_number)
  * [check\_seconds](#rs485_relay_board.base.RelayBoard.check_seconds)
  * [open\_relay](#rs485_relay_board.base.RelayBoard.open_relay)
  * [close\_relay](#rs485_relay_board.base.RelayBoard.close_relay)
  * [set\_relay](#rs485_relay_board.base.RelayBoard.set_relay)
  * [toggle](#rs485_relay_board.base.RelayBoard.toggle)
  * [latch](#rs485_relay_board.base.RelayBoard.latch)
  * [momentary](#rs485_relay_board.base.RelayBoard.momentary)
  * [delay](#rs485_relay_board.base.RelayBoard.delay)
  * [open\_all](#rs485_relay_board.base.RelayBoard.open_all)
  * [close\_all](#rs485_relay_board.base.RelayBoard.close_all)
  * [read\_relay](#rs485_relay_board.base.RelayBoard.read_relay)
  * [read\_relays](#rs485_relay_board.base.RelayBoard.read_relays)
  * [read\_all\_relays](#rs485_relay_board.base.RelayBoard.read_all_relays)


<a id="rs485_relay_board.base.RelayBoard"></a>

## RelayBoard

```python
class RelayBoard()
```

Class for interaction with relay boards over modbus.

By default, the relay is in state "closed" / LOW.
"Closed" state means that COM is connected to NC and not to NO.
"Open" state means that COM is connected to NO and not to NC and is indicated by LED.
For this library state `True` means "open" state.

e.g. Open = HIGH to relay, Closed = LOW to relay

<a id="rs485_relay_board.base.RelayBoard.__init__"></a>

#### \_\_init\_\_

```python
def __init__(port: str,
             slaveaddress: int,
             channels: int = 16,
             baudrate: int = 9600,
             read_timeout: float = 0.2,
             close_port_after_each_call: bool = False,
             debug: bool = False)
```

Setup relay board.

**Arguments**:

- `port`: The serial port name, for example `/dev/ttyUSB0` (Linux),
`/dev/tty.usbserial` (OS X) or `COM4` (Windows).
- `slaveaddress`: Slave address in the range 0 to 247 (use decimal numbers, not hex).
- `channels`: Number of channels of the relay board.
- `baudrate`: Baudrate to use.
- `read_timeout`: Read timeout after each command.
- `close_port_after_each_call`: If the serial port should be closed after each call to the board.
- `debug`: Set this to `True` to print the communication details

<a id="rs485_relay_board.base.RelayBoard.check_channel_number"></a>

#### check\_channel\_number

```python
def check_channel_number(channel: int)
```

Check if channel number is between 1 and `self.channels`.

**Arguments**:

- `channel`: Number of channel.

**Raises**:

- `ValueError`: 

<a id="rs485_relay_board.base.RelayBoard.check_seconds"></a>

#### check\_seconds

```python
def check_seconds(seconds: int)
```

Check if seconds is between 0 and 255.

**Arguments**:

- `seconds`: Whole number of seconds

<a id="rs485_relay_board.base.RelayBoard.open_relay"></a>

#### open\_relay

```python
def open_relay(channel: int)
```

Open relay.

**Arguments**:

- `channel`: Number of channel.

<a id="rs485_relay_board.base.RelayBoard.close_relay"></a>

#### close\_relay

```python
def close_relay(channel: int)
```

Close relay

**Arguments**:

- `channel`: Number of channel.

<a id="rs485_relay_board.base.RelayBoard.set_relay"></a>

#### set\_relay

```python
def set_relay(channel: int, state: bool)
```

Set state of given relay.

True means "Open" / High to relay state.

**Arguments**:

- `channel`: Number of channel.
- `state`: Bool state

<a id="rs485_relay_board.base.RelayBoard.toggle"></a>

#### toggle

```python
def toggle(channel: int)
```

Toggle (Self-locking) relay

**Arguments**:

- `channel`: Number of channel.

<a id="rs485_relay_board.base.RelayBoard.latch"></a>

#### latch

```python
def latch(channel: int)
```

Latch (Inter-locking) relay

**Arguments**:

- `channel`: Number of channel.

<a id="rs485_relay_board.base.RelayBoard.momentary"></a>

#### momentary

```python
def momentary(channel: int)
```

Momentary (Non-locking).

Close relay for 1s.

**Arguments**:

- `channel`: Number of channel.

<a id="rs485_relay_board.base.RelayBoard.delay"></a>

#### delay

```python
def delay(channel: int, seconds: int)
```

Delay

Open relay for <seconds>s.

Works even if relay is currently opened.

**Arguments**:

- `channel`: Number of channel.
- `seconds`: Number of seconds to close the relay for

<a id="rs485_relay_board.base.RelayBoard.open_all"></a>

#### open\_all

```python
def open_all()
```

Open all relays.

<a id="rs485_relay_board.base.RelayBoard.close_all"></a>

#### close\_all

```python
def close_all()
```

Close all relays.

<a id="rs485_relay_board.base.RelayBoard.read_relay"></a>

#### read\_relay

```python
def read_relay(channel: int) -> bool
```

Read state of a relay.

True means "Open" / High to relay state.

**Arguments**:

- `channel`: Number of channel.

**Returns**:

Bool

<a id="rs485_relay_board.base.RelayBoard.read_relays"></a>

#### read\_relays

```python
def read_relays(start_channel: int, length: int) -> Tuple[bool]
```

Read state of n relays.

**Arguments**:

- `start_channel`: Number of channel to start reading from.
- `length`: Number of relays to read.

**Returns**:

Tuple of booleans of length n(length).

<a id="rs485_relay_board.base.RelayBoard.read_all_relays"></a>

#### read\_all\_relays

```python
def read_all_relays() -> Tuple[bool]
```

Read state of all relays.

**Returns**:

Tuple of booleans of length `self.channels`.



## License

MIT