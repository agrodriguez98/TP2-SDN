# TP2-SDN

## Controlador POX
Asumiendo que firewall.py se encuentra en /pox/pox/misc/firewall.py
```
pox/pox.py log.level --DEBUG forwarding.l2_learning misc.firewall
```
## Mininet
Asumiendo que topologia.py se encuentra en el directorio TP2-SDN
```
sudo mn --custom ./TP2-SDN/topologia.py --topo customtopo,n=6 --mac --arp --switch ovsk --controller remote --xterm
```

## Probar con iperf
En la terminal de un host (por ejemplo h1 10.0.0.1) crear un servidor TCP escuchando en el puerto 80
```
iperf -s -p 80
```
Luego en otro host (por ejemplo h4 10.0.0.4) crear un cliente que se conecte al servidor anterior
```
iperf -c 10.0.0.1 -p 80
```
