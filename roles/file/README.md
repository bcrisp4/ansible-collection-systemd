# bcrisp4.systemd.file

Generates Systemd (ini-like) configuration files.

This role mostly exists as a helper for the other roles in `bcrisp4.systemd` that need to generate Systemd config files.

## Role Variables

| Variable      | Default | Description                                                                        |
|---------------|---------|------------------------------------------------------------------------------------|
| systemd_files | []      | A list of dictionaries describing the Systemd files to be generated (see examples) |

## Examples

```yaml
- hosts: 127.0.0.1
  vars:
    systemd_files:
      - path: /etc/systemd/system/foo.service # Full path the file, including the extension
        owner: root # The user that should own the file
        group: root # The group that should own the file
        mode: ugo=r # The permissions of the file
        handlers: # An (optional) list of handlers to notify if the file has changed
          - reload systemd
        sections: # A dict describing the sections and parameters in the file
          Unit:
            Description: Foo Bar
          Service:
            ExecStart: /usr/bin/foo --bar
  handlers:
    - name: reload systemd
      ansible.builtin.systemd:
        daemon_reload: true
  tasks:
    - import_role:
        name: bcrisp4.systemd.file
```

The above produces:
```ini
~ /etc/systemd/system/foo.service
# Ansible managed

[Unit]
Description=Foo Bar

[Service]
ExecStart=/usr/bin/foo --bar
```

## License

MIT

## Author Information

Ben Crisp <ben@thecrisp.io>
