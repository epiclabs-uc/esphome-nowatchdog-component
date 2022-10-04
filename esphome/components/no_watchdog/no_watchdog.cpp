#include "esphome/core/log.h"
#include "no_watchdog.h"
#include <esp_task_wdt.h>

namespace esphome {

namespace no_watchdog {

static const char *TAG = "no_watchdog";

void NoWatchdog::setup() {
  ESP_LOGW(TAG, "No Watchdog enabled! no_watchdog should only be enabled for emulator testing");
  esp_task_wdt_init(30, false);
}
void NoWatchdog::loop() {}

}  // namespace no_watchdog
}  // namespace esphome