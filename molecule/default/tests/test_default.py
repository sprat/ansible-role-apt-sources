import os

import testinfra.utils.ansible_runner

here = os.path.dirname(__file__)
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def read_reference_file(system_info):
    filename = '%s_%s.list' % (system_info.distribution, system_info.codename)
    with open(os.path.join(here, 'references', filename)) as reference_file:
        return reference_file.read()


def test(host):
    reference = read_reference_file(host.system_info)
    sources_list = host.file("/etc/apt/sources.list").content_string
    assert sources_list == reference
