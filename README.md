# RS485 relay board

Lightweight python library for interaction with R4D8B08 and R4D3B16

## Example

```python
from rs485_relay_board import RelayBoard


SLAVE_ADDR = 1
board = RelayBoard("/dev/ttyUSB0", SLAVE_ADDR)

board.open_all()
```
