# Nebby analysis result

The measurement was performed using the `iPerf3` client on the University Server as in the `clients.sh`:
```bash
iperf3 -c $URL -p 8081 -R -C $cca -t 60 -M 100
```
Measured using
```bash
./test_repeatedly.sh $URL
```
twice with 25 iterations each.

The server was just a simple `iPerf3` server running on the Optiplex:
```bash
iperf3 -s -p 8081
```
