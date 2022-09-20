from bluetooth_sensor_state_data import BluetoothServiceInfo, DeviceClass, SensorUpdate
from sensor_state_data import (
    DeviceKey,
    SensorDescription,
    SensorDeviceClass,
    SensorDeviceInfo,
    SensorValue,
    Units,
)

from kegtron_ble.parser import KegtronBluetoothDeviceData

KEY_PORT_COUNT = "port_count"
KEY_PORT_NAME = "port_name"
KEY_PORT_STATE = "port_state"
KEY_VOLUME_DISPENSED = "volume_dispensed"
KEY_VOLUME_START = "volume_start"
KEY_KEG_TYPE = "keg_type"
KEY_KEG_SIZE = "keg_size"
KEY_SIGNAL_STRENGTH = "signal_strength"


def test_can_create():
    KegtronBluetoothDeviceData()


def test_kegtron_kt100():
    parser = KegtronBluetoothDeviceData()
    service_info = BluetoothServiceInfo(
        name="D0:CF:5E:5C:9B:75",
        manufacturer_data={
            65535: b"I\xef\x13\x88\x02\xe2\x01Single Port\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        },
        address="D0:CF:5E:5C:9B:75",
        rssi=-82,
        service_uuids=[],
        service_data={},
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title="Kegtron KT-100 9B75",
        devices={
            None: SensorDeviceInfo(
                name="Kegtron KT-100 9B75",
                model="KT-100",
                manufacturer="Kegtron",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key=KEY_PORT_COUNT, device_id=None): SensorDescription(
                device_key=DeviceKey(key=KEY_PORT_COUNT, device_id=None),
                device_class=SensorDeviceClass.PORT_COUNT,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key=KEY_KEG_SIZE, device_id=None): SensorDescription(
                device_key=DeviceKey(key=KEY_KEG_SIZE, device_id=None),
                device_class=SensorDeviceClass.KEG_SIZE,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key=KEY_KEG_TYPE, device_id=None): SensorDescription(
                device_key=DeviceKey(key=KEY_KEG_TYPE, device_id=None),
                device_class=SensorDeviceClass.KEG_TYPE,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key=KEY_VOLUME_START, device_id=None): SensorDescription(
                device_key=DeviceKey(key=KEY_VOLUME_START, device_id=None),
                device_class=SensorDeviceClass.VOLUME_START,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key=KEY_PORT_STATE, device_id=None): SensorDescription(
                device_key=DeviceKey(key=KEY_PORT_STATE, device_id=None),
                device_class=SensorDeviceClass.PORT_STATE,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key=KEY_PORT_NAME, device_id=None): SensorDescription(
                device_key=DeviceKey(key=KEY_PORT_NAME, device_id=None),
                device_class=SensorDeviceClass.PORT_NAME,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key=KEY_VOLUME_DISPENSED, device_id=None): SensorDescription(
                device_key=DeviceKey(key=KEY_VOLUME_DISPENSED, device_id=None),
                device_class=SensorDeviceClass.VOLUME_DISPENSED,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id=None): SensorDescription(
                device_key=DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id=None),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key=KEY_PORT_COUNT, device_id=None): SensorValue(
                device_key=DeviceKey(key=KEY_PORT_COUNT, device_id=None),
                name="Port Count",
                native_value="Single port device",
            ),
            DeviceKey(key=KEY_KEG_SIZE, device_id=None): SensorValue(
                device_key=DeviceKey(key=KEY_KEG_SIZE, device_id=None),
                name="Keg Size",
                native_value=18.927,
            ),
            DeviceKey(key=KEY_KEG_TYPE, device_id=None): SensorValue(
                device_key=DeviceKey(key=KEY_KEG_TYPE, device_id=None),
                name="Keg Type",
                native_value="Corny (5.0 gal)",
            ),
            DeviceKey(key=KEY_VOLUME_START, device_id=None): SensorValue(
                device_key=DeviceKey(key=KEY_VOLUME_START, device_id=None),
                name="Volume Start",
                native_value=5.0,
            ),
            DeviceKey(key=KEY_PORT_STATE, device_id=None): SensorValue(
                device_key=DeviceKey(key=KEY_PORT_STATE, device_id=None),
                name="Port State",
                native_value="Configured",
            ),
            DeviceKey(key=KEY_PORT_NAME, device_id=None): SensorValue(
                device_key=DeviceKey(key=KEY_PORT_NAME, device_id=None),
                name="Port Name",
                native_value="Single Port",
            ),
            DeviceKey(key=KEY_VOLUME_DISPENSED, device_id=None): SensorValue(
                device_key=DeviceKey(key=KEY_VOLUME_DISPENSED, device_id=None),
                name="Volume Dispensed",
                native_value=0.738,
            ),
            DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id=None): SensorValue(
                device_key=DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id=None),
                name="Signal Strength",
                native_value=-82,
            ),
        },
    )


def test_kegtron_kt200():
    parser = KegtronBluetoothDeviceData()
    service_info = BluetoothServiceInfo(
        name="D0:CF:5E:5C:9B:75",
        manufacturer_data={
            65535: b"\xe62:\x98\x02\xe2Q2nd Port\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        },
        address="D0:CF:5E:5C:9B:75",
        rssi=-82,
        service_uuids=[],
        service_data={},
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title="Kegtron KT-200 9B75",
        devices={
            None: SensorDeviceInfo(
                name="Kegtron KT-200 9B75",
                model="KT-200",
                manufacturer="Kegtron",
                sw_version=None,
                hw_version=None,
            ),
            'port 2': SensorDeviceInfo(
                name='Kegtron KT-200 9B75',
                model='KT-200',
                manufacturer='Kegtron',
                sw_version=None,
                hw_version=None
            )
        },
        entity_descriptions={
            DeviceKey(key=KEY_PORT_COUNT, device_id=None): SensorDescription(
                device_key=DeviceKey(key=KEY_PORT_COUNT, device_id=None),
                device_class=SensorDeviceClass.PORT_COUNT,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key=f"{KEY_KEG_SIZE}_port_2", device_id="port 2"): SensorDescription(
                device_key=DeviceKey(key=f"{KEY_KEG_SIZE}_port_2", device_id="port 2"),
                device_class=SensorDeviceClass.KEG_SIZE,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key=f"{KEY_KEG_TYPE}_port_2", device_id="port 2"): SensorDescription(
                device_key=DeviceKey(key=f"{KEY_KEG_TYPE}_port_2", device_id="port 2"),
                device_class=SensorDeviceClass.KEG_TYPE,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key=f"{KEY_VOLUME_START}_port_2", device_id="port 2"): SensorDescription(
                device_key=DeviceKey(key=f"{KEY_VOLUME_START}_port_2", device_id="port 2"),
                device_class=SensorDeviceClass.VOLUME_START,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key=f"{KEY_PORT_STATE}_port_2", device_id="port 2"): SensorDescription(
                device_key=DeviceKey(key=f"{KEY_PORT_STATE}_port_2", device_id="port 2"),
                device_class=SensorDeviceClass.PORT_STATE,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key=f"{KEY_PORT_NAME}_port_2", device_id="port 2"): SensorDescription(
                device_key=DeviceKey(key=f"{KEY_PORT_NAME}_port_2", device_id="port 2"),
                device_class=SensorDeviceClass.PORT_NAME,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key=f"{KEY_VOLUME_DISPENSED}_port_2", device_id="port 2"): SensorDescription(
                device_key=DeviceKey(key=f"{KEY_VOLUME_DISPENSED}_port_2", device_id="port 2"),
                device_class=SensorDeviceClass.VOLUME_DISPENSED,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id=None): SensorDescription(
                device_key=DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id=None),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id="port 2"): SensorDescription(
                device_key=DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id="port 2"),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id=None): SensorDescription(
                device_key=DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id=None),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key=KEY_PORT_COUNT, device_id=None): SensorValue(
                device_key=DeviceKey(key=KEY_PORT_COUNT, device_id=None),
                name="Port Count",
                native_value="Dual port device",
            ),
            DeviceKey(key=f"{KEY_KEG_SIZE}_port_2", device_id="port 2"): SensorValue(
                device_key=DeviceKey(key=f"{KEY_KEG_SIZE}_port_2", device_id="port 2"),
                name="Keg Size Port 2",
                native_value=58.93,
            ),
            DeviceKey(key=f"{KEY_KEG_TYPE}_port_2", device_id="port 2"): SensorValue(
                device_key=DeviceKey(key=f"{KEY_KEG_TYPE}_port_2", device_id="port 2"),
                name="Keg Type Port 2",
                native_value="Other (58.93 L)",
            ),
            DeviceKey(key=f"{KEY_VOLUME_START}_port_2", device_id="port 2"): SensorValue(
                device_key=DeviceKey(key=f"{KEY_VOLUME_START}_port_2", device_id="port 2"),
                name="Volume Start Port 2",
                native_value=15.0,
            ),
            DeviceKey(key=f"{KEY_PORT_STATE}_port_2", device_id="port 2"): SensorValue(
                device_key=DeviceKey(key=f"{KEY_PORT_STATE}_port_2", device_id="port 2"),
                name="Port State Port 2",
                native_value="Configured",
            ),
            DeviceKey(key=f"{KEY_PORT_NAME}_port_2", device_id="port 2"): SensorValue(
                device_key=DeviceKey(key=f"{KEY_PORT_NAME}_port_2", device_id="port 2"),
                name="Port Name Port 2",
                native_value="2nd Port",
            ),
            DeviceKey(key=f"{KEY_VOLUME_DISPENSED}_port_2", device_id="port 2"): SensorValue(
                device_key=DeviceKey(key=f"{KEY_VOLUME_DISPENSED}_port_2", device_id="port 2"),
                name="Volume Dispensed Port 2",
                native_value=0.738,
            ),
            DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id=None): SensorValue(
                device_key=DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id=None),
                name="Signal Strength",
                native_value=-82,
            ),
            DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id="port 2"): SensorValue(
                device_key=DeviceKey(key=KEY_SIGNAL_STRENGTH, device_id="port 2"),
                name="Signal Strength",
                native_value=-82,
            ),
        },
    )
