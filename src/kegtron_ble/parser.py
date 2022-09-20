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
from sensor_state_data import SensorLibrary

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

        self.address = service_info.address
        self.manufacturer = "Kegtron"

        (port,) = unpack(">B", data[6:7])

        if port & (1 << 6) == 0:
            self.model = "KT-100"
            self.port_count = "Single port device"
            self.device_id = None
            self.port_id = ""
        elif port & (1 << 6) == 64:
            self.model = "KT-200"
            self.port_count = "Dual port device"
            if port & (1 << 4) == 0:
                self.device_id = "port 1"
                self.port_id = "_port_1"
            elif port & (1 << 4) == 16:
                self.device_id = "port 2"
                self.port_id = "_port_2"
            else:
                return None

        else:
            return

        self.set_title(
            f"{self.manufacturer} {self.model} {short_address(self.address)}"
        )
        self.set_device_name(
            f"{self.manufacturer} {self.model} {short_address(self.address)}"
        )
        self.set_device_type(self.model)
        self.set_device_manufacturer(self.manufacturer)

        if self.model == "KT-200":
            self.set_device_name(
                f"{self.manufacturer} {self.model} {short_address(self.address)}",
                self.device_id
            )
            self.set_device_type(self.model, self.device_id)
            self.set_device_manufacturer(self.manufacturer, self.device_id)

        self._process_update(data)

    def _process_update(self, data: bytes) -> None:
        """Update from BLE advertisement data."""
        _LOGGER.debug("Parsing Kegtron BLE advertisement data: %s", data)

        (keg_size, vol_start, vol_disp, port, port_name) = unpack(">HHHB20s", data)

        if port & (1 << 0) == 0:
            port_state = "Unconfigured (new device)"
        elif port & (1 << 0) == 1:
            port_state = "Configured"
        else:
            return None

        if keg_size in KEGTRON_SIZE_DICT:
            keg_type = KEGTRON_SIZE_DICT[keg_size]
        else:
            keg_type = "Other (" + str(keg_size / 1000) + " L)"

        port_name = str(port_name.decode("utf-8").rstrip("\x00"))

        self.update_sensor(
            key="port_count",
            native_unit_of_measurement=SensorLibrary.PORT_COUNT__NONE.native_unit_of_measurement,
            native_value=self.port_count,
            device_class=SensorLibrary.PORT_COUNT__NONE.device_class,
        )
        self.update_sensor(
            key=f"keg_size{self.port_id}",
            native_unit_of_measurement=(
                SensorLibrary.KEG_SIZE__VOLUME_LITERS.native_unit_of_measurement
            ),
            native_value=keg_size / 1000,
            device_class=SensorLibrary.KEG_SIZE__VOLUME_LITERS.device_class,
            device_id=self.device_id,
        )
        self.update_sensor(
            key=f"keg_type{self.port_id}",
            native_unit_of_measurement=(
                SensorLibrary.KEG_TYPE__NONE.native_unit_of_measurement
            ),
            native_value=keg_type,
            device_class=SensorLibrary.KEG_TYPE__NONE.device_class,
            device_id=self.device_id,
        )
        self.update_sensor(
            key=f"volume_start{self.port_id}",
            native_unit_of_measurement=(
                SensorLibrary.VOLUME_START__VOLUME_LITERS.native_unit_of_measurement)
            ,
            native_value=vol_start / 1000,
            device_class=SensorLibrary.VOLUME_START__VOLUME_LITERS.device_class,
            device_id=self.device_id,
        )
        self.update_sensor(
            key=f"volume_dispensed{self.port_id}",
            native_unit_of_measurement=SensorLibrary.VOLUME_DISPENSED__VOLUME_LITERS.native_unit_of_measurement,
            native_value=vol_disp / 1000,
            device_class=SensorLibrary.VOLUME_DISPENSED__VOLUME_LITERS.device_class,
            device_id=self.device_id,
        )
        self.update_sensor(
            key=f"port_state{self.port_id}",
            native_unit_of_measurement=SensorLibrary.PORT_STATE__NONE.native_unit_of_measurement,
            native_value=port_state,
            device_class=SensorLibrary.PORT_STATE__NONE.device_class,
            device_id=self.device_id,
        )
        self.update_sensor(
            key=f"port_name{self.port_id}",
            native_unit_of_measurement=SensorLibrary.PORT_NAME__NONE.native_unit_of_measurement,
            native_value=port_name,
            device_class=SensorLibrary.PORT_NAME__NONE.device_class,
            device_id=self.device_id,
        )
