from bluetooth_sensor_state_data import BluetoothServiceInfo, DeviceClass, SensorUpdate
from sensor_state_data import (
    DeviceKey,
    SensorDescription,
    SensorDeviceInfo,
    SensorValue,
    Units,
)

from kegtron_ble.parser import KegtronBluetoothDeviceData


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
            DeviceKey(key="port_count", device_id=None): SensorDescription(
                device_key=DeviceKey(key="port_count", device_id=None),
                device_class=None,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="keg_size", device_id=None): SensorDescription(
                device_key=DeviceKey(key="keg_size", device_id=None),
                device_class=None,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key="keg_type", device_id=None): SensorDescription(
                device_key=DeviceKey(key="keg_type", device_id=None),
                device_class=None,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="volume_start", device_id=None): SensorDescription(
                device_key=DeviceKey(key="volume_start", device_id=None),
                device_class=None,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key="port_state", device_id=None): SensorDescription(
                device_key=DeviceKey(key="port_state", device_id=None),
                device_class=None,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="volume_dispensed", device_id=None): SensorDescription(
                device_key=DeviceKey(key="volume_dispensed", device_id=None),
                device_class=None,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="port_count", device_id=None): SensorValue(
                device_key=DeviceKey(key="port_count", device_id=None),
                name="Port Count",
                native_value="Single port device",
            ),
            DeviceKey(key="keg_size", device_id=None): SensorValue(
                device_key=DeviceKey(key="keg_size", device_id=None),
                name="Keg Size",
                native_value=18.927,
            ),
            DeviceKey(key="keg_type", device_id=None): SensorValue(
                device_key=DeviceKey(key="keg_type", device_id=None),
                name="Keg Type",
                native_value="Corny (5.0 gal)",
            ),
            DeviceKey(key="volume_start", device_id=None): SensorValue(
                device_key=DeviceKey(key="volume_start", device_id=None),
                name="Volume Start",
                native_value=5.0,
            ),
            DeviceKey(key="port_state", device_id=None): SensorValue(
                device_key=DeviceKey(key="port_state", device_id=None),
                name="Port State",
                native_value="Configured",
            ),
            DeviceKey(key="volume_dispensed", device_id=None): SensorValue(
                device_key=DeviceKey(key="volume_dispensed", device_id=None),
                name="Volume Dispensed",
                native_value=0.738,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
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
            )
        },
        entity_descriptions={
            DeviceKey(key="port_count", device_id=None): SensorDescription(
                device_key=DeviceKey(key="port_count", device_id=None),
                device_class=None,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="keg_size_port_2", device_id=None): SensorDescription(
                device_key=DeviceKey(key="keg_size_port_2", device_id=None),
                device_class=None,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key="keg_type_port_2", device_id=None): SensorDescription(
                device_key=DeviceKey(key="keg_type_port_2", device_id=None),
                device_class=None,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="volume_start_port_2", device_id=None): SensorDescription(
                device_key=DeviceKey(key="volume_start_port_2", device_id=None),
                device_class=None,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key="port_state_port_2", device_id=None): SensorDescription(
                device_key=DeviceKey(key="port_state_port_2", device_id=None),
                device_class=None,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="volume_dispensed_port_2", device_id=None): SensorDescription(
                device_key=DeviceKey(key="volume_dispensed_port_2", device_id=None),
                device_class=None,
                native_unit_of_measurement=Units.VOLUME_LITERS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="port_count", device_id=None): SensorValue(
                device_key=DeviceKey(key="port_count", device_id=None),
                name="Port Count",
                native_value="Dual port device",
            ),
            DeviceKey(key="keg_size_port_2", device_id=None): SensorValue(
                device_key=DeviceKey(key="keg_size_port_2", device_id=None),
                name="Keg Size 2nd Port",
                native_value=58.93,
            ),
            DeviceKey(key="keg_type_port_2", device_id=None): SensorValue(
                device_key=DeviceKey(key="keg_type_port_2", device_id=None),
                name="Keg Type 2nd Port",
                native_value="Other (58.93 L)",
            ),
            DeviceKey(key="volume_start_port_2", device_id=None): SensorValue(
                device_key=DeviceKey(key="volume_start_port_2", device_id=None),
                name="Volume Start 2nd Port",
                native_value=15.0,
            ),
            DeviceKey(key="port_state_port_2", device_id=None): SensorValue(
                device_key=DeviceKey(key="port_state_port_2", device_id=None),
                name="Port State 2nd Port",
                native_value="Configured",
            ),
            DeviceKey(key="volume_dispensed_port_2", device_id=None): SensorValue(
                device_key=DeviceKey(key="volume_dispensed_port_2", device_id=None),
                name="Volume Dispensed 2nd Port",
                native_value=0.738,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal Strength",
                native_value=-82,
            ),
        },
    )
