Ansible Role: apt_sources
=========================

[![Build Status](https://api.travis-ci.com/sprat/ansible-role-apt-sources.svg?branch=master)](https://travis-ci.com/sprat/ansible-role-apt-sources)

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
