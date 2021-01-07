import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

files = ['/tmp/test-systemd-unit-file.service',
         '/tmp/test-systemd-unit-file-with-handler.service']
user = 'root'
group = 'root'
mode = '0o444'
content = """# Ansible managed: Do NOT edit this file manually!

[Unit]
Description=A dummy service for testing

[Service]
ExecStart=/bin/true
Type=oneshot
"""

cases = [
        ('/tmp/test-systemd-unit-file.service', user, group, mode, content),
        ('/tmp/test-systemd-unit-file-with-handler.service', user, group,
            mode, content)
        ]


@pytest.mark.parametrize('file, user, group, mode, content', cases)
def test_systemd_unit_file_content(host, file, user, group, mode, content):
    file = host.file(file)

    assert file.exists
    assert file.user == user
    assert file.group == group
    assert oct(file.mode) == mode
    assert file.content_string == content
