"""Parser for Kegtron BLE advertisements.

This file is shamelessly copied from the following repository:
https://github.com/Ernst79/bleparser/blob/ac8757ad64f1fc17674dcd22111e547cdf2f205b/package/bleparser/kegtron.py

MIT License applies.
"""
from __future__ import annotations

import logging
from struct import unpack

from bluetooth_data_tools import short_address
from bluetooth_sensor_state_data import BluetoothData
from home_assistant_bluetooth import BluetoothServiceInfo
from sensor_state_data import Units

_LOGGER = logging.getLogger(__name__)


MFR_ID = 0xFFFF


KEGTRON_SIZE_DICT = {
    9464: "Half Corny (2.5 gal)",
    18927: "Corny (5.0 gal)",
    19711: "1/6 Barrel (5.167 gal)",
    19550: "1/6 Barrel (5.167 gal)",
    20000: "20L (5.283 gal)",
    20457: "Pin (5.404 gal)",
    29337: "1/4 Barrel (7.75 gal)",
    40915: "Firkin (10.809 gal)",
    50000: "50L (13.209 gal)",
    58674: "1/2 Barrel (15.5 gal)",
}


class KegtronBluetoothDeviceData(BluetoothData):
    """Date update for Kegtron Bluetooth devices."""

    def _start_update(self, service_info: BluetoothServiceInfo) -> None:
        """Update from BLE advertisement data."""
        _LOGGER.debug("Parsing Kegtron BLE advertisement data: %s", service_info)
        if MFR_ID not in service_info.manufacturer_data:
            return
        manufacturer_data = service_info.manufacturer_data
        last_id = list(manufacturer_data)[-1]
        data = manufacturer_data[last_id]
        msg_length = len(data)
        if msg_length != 27:
            return

        address = service_info.address
        manufacturer = "Kegtron"

        (device_id,) = unpack(">B", data[6:7])

        if device_id & (1 << 6):
            model = "KT-200"
        else:
            model = "KT-100"

        self.set_device_type(model)
        self.set_title(f"{manufacturer} {model} {short_address(address)}")
        self.set_device_name(f"{manufacturer} {model} {short_address(address)}")
        self.set_device_manufacturer(manufacturer)
        self._process_update(data)

    def _process_update(self, data: bytes) -> None:
        """Update from BLE advertisement data."""
        _LOGGER.debug("Parsing Kegtron BLE advertisement data: %s", data)

        (keg_size, vol_start, vol_disp, port, port_name) = unpack(">HHHB20s", data)

        if keg_size in KEGTRON_SIZE_DICT:
            keg_type = KEGTRON_SIZE_DICT[keg_size]
        else:
            keg_type = "Other (" + str(keg_size / 1000) + " L)"

        if port & (1 << 0):
            port_state = "Configured"
        else:
            port_state = "Unconfigured (new device)"

        if port & (1 << 4):
            port_index = 2
        else:
            port_index = 1

        if port & (1 << 6):
            port_count = "Dual port device"
        else:
            port_count = "Single port device"

        port_name = str(port_name.decode("utf-8").rstrip("\x00"))

        self.update_sensor(
            key="keg_size",
            native_unit_of_measurement=Units.VOLUME_LITERS,
            native_value=keg_size / 1000,
        )
        self.update_sensor(
            key="keg_type",
            native_unit_of_measurement=None,
            native_value=keg_type,
        )
        self.update_sensor(
            key="volume_start",
            native_unit_of_measurement=Units.VOLUME_LITERS,
            native_value=vol_start / 1000,
        )
        self.update_sensor(
            key="port_count",
            native_unit_of_measurement=None,
            native_value=port_count,
        )
        self.update_sensor(
            key="port_index",
            native_unit_of_measurement=None,
            native_value=port_index,
        )
        self.update_sensor(
            key="port_state",
            native_unit_of_measurement=None,
            native_value=port_state,
        )
        if port_index == 1:
            self.update_sensor(
                key="volume_dispensed_port_1",
                native_unit_of_measurement=Units.VOLUME_LITERS,
                native_value=vol_disp / 1000,
                name=port_name,
            )
        elif port_index == 2:
            self.update_sensor(
                key="volume_dispensed_port_2",
                native_unit_of_measurement=Units.VOLUME_LITERS,
                native_value=vol_disp / 1000,
                name=port_name,
            )
        else:
            return None
