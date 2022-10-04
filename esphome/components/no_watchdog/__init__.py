import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ADDRESS, CONF_ID


no_watchdog_ns = cg.esphome_ns.namespace("no_watchdog")
no_watchdogComponent = no_watchdog_ns.class_("NoWatchdog", cg.Component)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(no_watchdogComponent),
    }
).extend(cv.COMPONENT_SCHEMA)

MULTI_CONF = True
CODEOWNERS = ["@jpeletier"]


async def to_code(config):

    id = config[CONF_ID]
    server = cg.new_Pvariable(id)

    await cg.register_component(server, config)

    return
