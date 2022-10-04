#pragma once
#include "esphome/core/component.h"
namespace esphome {
namespace no_watchdog {
using namespace std;

class NoWatchdog : public Component {
  void setup() override;
  void loop() override;
};

}  // namespace no_watchdog
}  // namespace esphome