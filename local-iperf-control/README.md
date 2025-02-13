# Nebby analysis result

The measurement was performed using the `iPerf3` client on the Optiplex as in the `clients.sh`:
```bash
iperf3 -c $URL -p 8081 -R -C $cca -t 60 -M 100
```
The server was just a simple `iPerf3` server running on a Raspberry Pi 4b:
```bash
iperf3 -s -p 8081
```
Booth devices were connected on the same network.
