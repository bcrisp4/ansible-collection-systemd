# Ansible Collection - bcrisp4.systemd

**WIP**

A collection of roles for Systemd related things

## Roles

_See individual role README files for more information._

### [bcrisp4.systemd.file](https://github.com/bcrisp4/ansible-collection-systemd/tree/main/roles/file) ![bcrisp4.systemd.file](https://github.com/bcrisp4/ansible-collection-systemd/workflows/bcrisp4.systemd.file/badge.svg)

Generates Systemd-style (ini-like) configuration files

### [bcrisp4.systemd.unit](https://github.com/bcrisp4/ansible-collection-systemd/tree/main/roles/unit)

Generates Systemd units (services, timers, etc.), and can optionally manage the unit state (start/stop/enable etc.)

### [bcrisp4.systemd.dropin](https://github.com/bcrisp4/ansible-collection-systemd/tree/main/roles/dropin)

Generates Systemd dropins to augment existing units

## Todo
- [ ] test suite (in progress)
- [ ] CI (in progress)
- [ ] resolved role
- [ ] timesyncd role
- [ ] networkd role
- [ ] systemd system config role
