import os

import testinfra.utils.ansible_runner

testinfra_runner = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
)
testinfra_hosts = testinfra_runner.get_hosts('all')
testinfra_variables = testinfra_runner.get_variables('all')


lgsm_user: str = 'lgsm'
lgsm_group: str = 'lgsm'
lgsm_version: str = '19.12.0'


def test_dependencies(host):
    dependencies: list = [
        "mailutils",
        "postfix",
        "curl",
        "wget",
        "file",
        "tar",
        "bzip2",
        "gzip",
        "unzip",
        "bsdmainutils",
        "python",
        "util-linux",
        "ca-certificates",
        "binutils",
        "bc",
        "jq",
        "tmux",
        "default-jre"
    ]
    for dependencie in dependencies:
        package = host.package(dependencie)
        assert package.is_installed


def test_user_exist(host):
    assert host.user(lgsm_user).exists
    assert host.group(lgsm_group).exists


def test_lgsm_is_enabled(host):
    f_bin = host.file('/usr/local/bin/linuxgsm.sh')
    assert f_bin.exists

    f_opt = host.file('/opt/LinuxGSM-{}/linuxgsm.sh'
                      .format(lgsm_version))
    assert f_opt.exists
    assert f_opt.user == lgsm_user
    assert f_opt.group == lgsm_group
    assert f_opt.mode == 0o550
