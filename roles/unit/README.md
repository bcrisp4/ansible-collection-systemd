# bcrisp4.systemd.unit

Generates Systemd units (services, timers etc.)

## Role Variables

| Variable                     | Default             | Description                                                                                 |
|------------------------------|---------------------|---------------------------------------------------------------------------------------------|
| systemd_units                | []                  | A list of dictionaries describing the Systemd units to be generated (see examples)          |
| systemd_unit_system_dir      | /etc/systemd/system | The directory that system unit files should be saved in                                     |
| systemd_unit_user_dir        | /etc/systemd/user   | The directory that user unit files should be saved in                                       |
| systemd_unit_file_owner      | root                | The user that should own the unit files                                                     |
| systemd_unit_file_group      | root                | The group that should own the unit files                                                    |
| systemd_unit_file_mode       | ugo=r               | The permissions of the unit files                                                           |
| systemd_unit_manage_service  | false               | Determines if the role should manage the unit state by default (can be overridden per unit) |
| systemd_unit_service_state   | started             | Default state of created units (can be overridden per unit)                                 |
| systemd_unit_service_enabled | true                | Determines if the role should enable the unit by default (can be overridden per unit)       |

## Examples

### Create a system service, but do not manage service state

```yaml
- hosts: 127.0.0.1
  vars:
    systemd_units:
      - name: foo.service
        sections:
          Unit:
            Description: Foo Bar
          Service:
            ExecStart: /usr/bin/foo --bar
  tasks:
    - import_role:
        name: bcrisp4.systemd.unit
```

### Create a user service, ensure the service is started and enabled

```yaml
- hosts: 127.0.0.1
  vars:
    systemd_units:
      - name: foo.service
        user_unit: true
        manage: true
        sections:
          Unit:
            Description: Foo Bar
          Service:
            ExecStart: /usr/bin/foo --bar
  tasks:
    - import_role:
        name: bcrisp4.systemd.unit
```

### Create a system service and a timer to start it, but ensure the timer is stopped and disabled

```yaml
- hosts: 127.0.0.1
  vars:
    systemd_units:
      - name: foo.service
        sections:
          Unit:
            Description: Foo Bar
          Service:
            ExecStart: /usr/bin/foo --bar
      - name: foo.timer
        manage: yes
        state: stopped
        enabled: false
        sections:
          Unit:
            Description: Run Foo Bar every day at 04:00:00
          Timer:
            OnCalendar: *-*-* 04:00:00
          Install:
            WantedBy: timers.target
  tasks:
    - import_role:
        name: bcrisp4.systemd.unit
```

## License

MIT

## Author Information

Ben Crisp <ben@thecrisp.io>
