# Nebby analysis result

The measurement was performed using the `iPerf3` client as in the `clients.sh`:
```bash
iperf3 -c $URL -p 8081 -R -C $cca -t 60 -M 100
```
The server was just a simple `iPerf3` server:
```bash
iperf3 -s -p 8081
```
Each CCA was measured with 5 BDPs:
1. 2
2. 4
3. 8
4. 12
5. 16
And each measurement was repeated 10 times.
