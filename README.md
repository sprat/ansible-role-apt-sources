Ansible Role: apt_sources
=========================

[![Build Status][build_badge]][build_link]
[![Ansible Galaxy][galaxy_badge]][galaxy_link]

Configure the APT sources list on Ubuntu or Debian

Requirements
------------

None.

Role Variables
--------------

See [defaults/main.yml](defaults/main.yml).

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: server
  roles:
    - role: sprat.apt_sources
```

License
-------

MIT

Author Information
------------------

This role was created in 2020 by [Sylvain Prat](https://github.com/sprat).


[build_badge]:  https://img.shields.io/github/workflow/status/sprat/ansible-role-apt-sources/CI
[build_link]:   https://github.com/sprat/ansible-role-apt-sources/actions?query=workflow:CI
[galaxy_badge]: https://img.shields.io/ansible/role/47754
[galaxy_link]:  https://galaxy.ansible.com/sprat/apt_sources
