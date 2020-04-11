from charms.reactive import Endpoint


class HostPortProvides(Endpoint):

    def configure(self, host, port):
        """
        Configure the host and port
            - host
            - port
        """

        for relation in self.relations:
            relation.to_publish.update({
                'host': host,
                'port': port,
            })
