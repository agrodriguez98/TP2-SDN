# TP2-SDN

## Controlador POX
```
pox/pox.py log.level --DEBUG firewall
```
## Mininet
```
mn --custom ./TP2-SDN/topologia.py --topo customtopo,n=6 --mac --arp --switch ovsk --controller remote --xterm
```

## Preguntas

1. ¿Cuál es la diferencia entre un Switch y un router? ¿Qué tienen en común?
- El switch opera en la capa de enlace y utiliza las direcciones MAC para realizar el direccionamiento de paquetes en la red local. El router opera en la capa de red y se sustenta de las direcciones IP para redirigir los paquetes entre las distintas redes.
Tienen en común que ambos pueden tener múltiples interfaces y toman el tráfico del puerto de entrada para dirigirlo hacia el destino.


2. ¿Cuál es la diferencia entre un Switch convencional y un Switch OpenFlow?
- La diferencia es que en el switch convencional, el plano de datos y de control está en el mismo dispositivo definido por hardware. En cambio, en el switch OpenFlow se separa el plano de control. De esta forma el controlador y las reglas de direccionamiento se pueden definir por software. 

3. ¿Se pueden reemplazar todos los routers de la Intenet por Switches OpenFlow? Piense en el escenario interASes para
elaborar su respuesta
- 
