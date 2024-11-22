from mininet.topo import Topo

class CustomTopo(Topo):
    def build(self, n=2):
        # Crear hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        
        if n < 1:
            raise ValueError("La cantidad de switches debe ser al menos 1")

        # Crear switches en cadena
        prev_switch = None
        for i in range(n):
            switch = self.addSwitch(f's{i+1}')
            if prev_switch:
                self.addLink(prev_switch, switch)
            prev_switch = switch

        # Conectar hosts a los extremos
        self.addLink(h1, 's1')
        self.addLink(h2, 's1')
        self.addLink(h3, f's{n}')
        self.addLink(h4, f's{n}')

topos = {'customtopo': CustomTopo}
