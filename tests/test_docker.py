from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_docker_service(Service):
    service = Service('docker')
    assert service.is_running
    assert service.is_enabled


def test_docker_cli(Command, Sudo):
    with Sudo():
        assert Command('docker ps').rc == 0


def test_docker_socket(File):
    socket = File('/var/run/docker.sock')
    assert socket.is_socket
    assert socket.mode == 0o0660
    assert socket.user == 'root'
    assert socket.group == 'docker'
