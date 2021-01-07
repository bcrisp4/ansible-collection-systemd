# bcrisp4.systemd.dropin

Generates systemd dropins for exisitng units.

## Role Variables

| Variable                  | Default             | Description                                                                          |
|---------------------------|---------------------|--------------------------------------------------------------------------------------|
| systemd_dropins           | []                  | A list of dictionaries describing the Systemd dropins to be generated (see examples) |
| systemd_dropin_system_dir | /etc/systemd/system | The directory that system unit dropins should be saved in                            |
| systemd_dropin_user_dir   | /etc/systemd/user   | The directory that user unit dropins should be saved in                              |
| systemd_dropin_file_owner | root                | The user that should own the dropin files                                            |
| systemd_dropin_file_group | root                | The group that should own the dropin files                                           |
| systemd_dropin_file_mode  | ugo=r               | The permissions of the dropin files                                                  |
| systemd_dropin_dir_owner  | root                | The user that should own the dropin directories                                      |
| systemd_dropin_dir_group  | root                | The group that should own the dropin directories                                     |
| systemd_dropin_dir_mode   | u=rwx,go=rx         | The permissions of the dropin directories                                            |

## Dependencies

- bcrisp4.systemd.file

## Examples

### Add a dropin that overrides RestartSecs for foo.service

```yaml
- hosts: 127.0.0.1
  variables:
    systemd_dropins:
      - name: 50-restart-secs # name of the dropin file (gets suffixed with .conf)
        unit: foo.service # the name of the unit the dropin is for
        sections: # the content of the dropin file
          Service:
            RestartSecs: 10
  tasks:
    - import_role:
        name: bcrisp4.systemd.dropin
```

## License

MIT

## Author Information

Ben Crisp <ben@thecrisp.io>
