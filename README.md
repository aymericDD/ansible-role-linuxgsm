Ansible Role: LinuxGSM
=========

[![Build Status](https://travis-ci.com/aymericDD/ansible-role-linuxgsm.svg?branch=master)](https://travis-ci.com/aymericDD/ansible-role-linuxgsm)
[![test-suite](https://img.shields.io/badge/ansible--roles--linuxgsm-tests-ansible--role--linuxgsm.svg?style=flat)](https://github.com/aymericDD/ansible-role-linuxgsm/tree/master/molecule/default)
[![Ansible
Galaxy](https://img.shields.io/badge/galaxy-aymericdd.linuxgsm-660198.svg?style=flat)](https://galaxy.ansible.com/aymericdd/linuxgsm)

Installs LinuxGSM server for Debian.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

``` yaml
---
lgsm_dependencies:
  - mailutils 
  - postfix 
  - curl 
  - wget 
  - file 
  - tar 
  - bzip2 
  - gzip 
  - unzip 
  - bsdmainutils 
  - python 
  - util-linux 
  - ca-certificates 
  - binutils 
  - bc 
  - jq 
  - tmux 
  - default-jre

lgsm_user: "lgsm"
lgsm_group: "lgsm"

```

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: aymericdd.linuxgsm }

License
-------

BSD

Author Information
------------------

This role is based on samba role written by Jeff Geerling, author of Ansible for DevOps.

This role was created in 2019 by [AymericDD](https://github.com/aymericDD).