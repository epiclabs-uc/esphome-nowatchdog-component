# esphome-nowatchdog-component

Component to disable watchdog in ESPHome for QEMU debugging

To use, add this to your configuration:

```yaml
external_components:
    - source: github://epiclabs-uc/esphome-nowatchdog-component@master
      refresh: 60s
      components:
        - no_watchdog
```

Then, add to the top of your configuration:

```yaml
no_watchdog:
```

Adding it to the top ensures the watchdog is disabled as soon as possible.
