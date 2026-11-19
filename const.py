"""Constants for the Huawei Solar integration."""

from datetime import timedelta

DOMAIN = "huawei_solar"
DEFAULT_PORT = 502
DEFAULT_SLAVE_ID = 0
DEFAULT_SERIAL_SLAVE_ID = 1
DEFAULT_USERNAME = "installer"
DEFAULT_PASSWORD = "00000a"
DEFAULT_BAUDRATE = 9600

CONF_SLAVE_IDS = "slave_ids"
CONF_ENABLE_PARAMETER_CONFIGURATION = "enable_parameter_configuration"
CONF_BAUDRATE = "baudrate"

# Option keys (entry.options). All polling intervals are expressed in seconds.
CONF_EMMA_POWER_INTERVAL = "emma_power_interval"
CONF_EMMA_ENERGY_INTERVAL = "emma_energy_interval"
CONF_INVERTER_INTERVAL = "inverter_interval"
CONF_POWER_METER_INTERVAL = "power_meter_interval"
CONF_ENERGY_STORAGE_INTERVAL = "energy_storage_interval"
CONF_CONFIGURATION_INTERVAL = "configuration_interval"

MIN_UPDATE_INTERVAL_SECONDS = 2
MIN_CONFIGURATION_INTERVAL_SECONDS = 60
MAX_UPDATE_INTERVAL_SECONDS = 86400

DATA_DEVICE_DATAS = "device_datas"
DATA_UPDATE_COORDINATORS = "update_coordinators"

INVERTER_UPDATE_INTERVAL = timedelta(seconds=30)
POWER_METER_UPDATE_INTERVAL = timedelta(seconds=30)
ENERGY_STORAGE_UPDATE_INTERVAL = timedelta(seconds=30)
# configuration can only change when edited through FusionSolar web or app
CONFIGURATION_UPDATE_INTERVAL = timedelta(minutes=15)
# The EMMA power/SOC registers are polled on a separate coordinator. The default
# is identical to the regular EMMA interval, so behaviour only changes when the
# user configures a faster interval in the options.
EMMA_POWER_UPDATE_INTERVAL = INVERTER_UPDATE_INTERVAL
# optimizer data is only refreshed every 5 minutes by the inverter.
OPTIMIZER_UPDATE_INTERVAL = timedelta(minutes=5)

SERVICE_FORCIBLE_CHARGE = "forcible_charge"
SERVICE_FORCIBLE_DISCHARGE = "forcible_discharge"
SERVICE_FORCIBLE_CHARGE_SOC = "forcible_charge_soc"
SERVICE_FORCIBLE_DISCHARGE_SOC = "forcible_discharge_soc"
SERVICE_STOP_FORCIBLE_CHARGE = "stop_forcible_charge"

SERVICE_RESET_MAXIMUM_FEED_GRID_POWER = "reset_maximum_feed_grid_power"
SERVICE_SET_DI_ACTIVE_POWER_SCHEDULING = "set_di_active_power_scheduling"
SERVICE_SET_ZERO_POWER_GRID_CONNECTION = "set_zero_power_grid_connection"
SERVICE_SET_MAXIMUM_FEED_GRID_POWER = "set_maximum_feed_grid_power"
SERVICE_SET_MAXIMUM_FEED_GRID_POWER_PERCENT = "set_maximum_feed_grid_power_percent"
SERVICE_SET_TOU_PERIODS = "set_tou_periods"
SERVICE_SET_CAPACITY_CONTROL_PERIODS = "set_capacity_control_periods"
SERVICE_SET_FIXED_CHARGE_PERIODS = "set_fixed_charge_periods"

SERVICES = (
    SERVICE_FORCIBLE_CHARGE,
    SERVICE_FORCIBLE_DISCHARGE,
    SERVICE_FORCIBLE_CHARGE_SOC,
    SERVICE_FORCIBLE_DISCHARGE_SOC,
    SERVICE_STOP_FORCIBLE_CHARGE,
    SERVICE_RESET_MAXIMUM_FEED_GRID_POWER,
    SERVICE_SET_DI_ACTIVE_POWER_SCHEDULING,
    SERVICE_SET_ZERO_POWER_GRID_CONNECTION,
    SERVICE_SET_MAXIMUM_FEED_GRID_POWER,
    SERVICE_SET_TOU_PERIODS,
    SERVICE_SET_CAPACITY_CONTROL_PERIODS,
    SERVICE_SET_FIXED_CHARGE_PERIODS,
)
