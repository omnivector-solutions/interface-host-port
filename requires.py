from charms.reactive import when
from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint


class HostPortRequires(Endpoint):

    @when('endpoint.{endpoint_name}.joined')
    def joined(self):
        if any(unit.received['port'] for unit in self.all_joined_units):
            set_flag(self.expand_name('available'))

    @when('endpoint.{endpoint_name}.changed')
    def changed(self):
        if any(unit.received['port'] for unit in self.all_joined_units):
            set_flag(self.expand_name('available'))

    def list_unit_data(self):
        """
        Get the list of the relation info for each unit.

        The host (address) and the port (as a string).
        For example::
            [
                {
                    'host': '10.1.1.1',
                    'port': '80',
                },
            ]
        """
        units_data = []
        for relation in self.relations:
            for unit in relation.joined_units:
                host = unit.received['host']
                port = unit.received['port']
                if not (host and port):
                    continue
                units_data.append({
                    'host': host,
                    'port': port,
                })
        return units_data
