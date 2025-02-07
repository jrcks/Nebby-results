# Nebby analysis result

The measurement was performed using the `iPerf3` client as in the `clients.sh`:
```bash
iperf3 -c $URL -p 8081 -R -C $cca -t 60 -M 100
```
The server was just a simple `iPerf3` server:
```bash
iperf3 -s -p 8081
```

# Tables

The following tables summarize the results of the analysis:

| #  | BBR               | BIC               | Cubic                       | DCTCP     | Highspeed                   | HTCP       | LP          | Reno       | Scalable                    | Vegas                       | Veno        | Westwood  | YeAH                        |
|----|-------------------|-------------------|-----------------------------|-----------|-----------------------------|------------|-------------|------------|-----------------------------|-----------------------------|-------------|-----------|-----------------------------|
| 1  | BBR               | BBR(Maybe)        | CUBIC                       | LP        | Outlier with degree fit = 3 | BBR(Maybe) | HIGHSPEED   | HIGHSPEED  | CUBICQ                      | TOO MUCH MSE ERROR          | CUBICQ      | RENO      | CUBICQ                      |
| 2  | BBR               | NAN - NO FEATURES | CUBIC                       | RENO      | Outlier with degree fit = 3 | BBR(Maybe) | RENO        | HIGHSPEED  | VENO                        | TOO MUCH MSE ERROR          | VENO        | HIGHSPEED | YEAH                        |
| 3  | BBR               | CUBIC             | Outlier with degree fit = 3 | LP        | Outlier with degree fit = 3 | BBR(Maybe) | LP          | LP         | WESTWOOD                    | TOO MUCH MSE ERROR          | CUBICQ      | LP        | BIC                         |
| 4  | BBR               | NAN - NO FEATURES | CUBIC                       | RENO      | Outlier with degree fit = 3 | BBR(Maybe) | LP          | LP         | BIC                         | TOO MUCH MSE ERROR          | CUBICQ      | RENO      | HIGHSPEED                   |
| 5  | BBR(Maybe)        | NAN - NO FEATURES | Outlier with degree fit = 3 | HIGHSPEED | Outlier with degree fit = 3 | BBR(Maybe) | LP          | LP         | Outlier with degree fit = 1 | TOO MUCH MSE ERROR          | HIGHSPEED   | HIGHSPEED | CUBICQ                      |
| 6  | BBR               | NAN - NO FEATURES | Outlier with degree fit = 3 | HIGHSPEED | BIC                         | BBR(Maybe) | RENO        | RENO       | Outlier with degree fit = 1 | TOO MUCH MSE ERROR          | VENO        | RENO      | Outlier with degree fit = 1 |
| 7  | BBR               | NAN - NO FEATURES | CUBIC                       | RENO      | BIC                         | BBR(Maybe) | RENO        | RENO       | VENO                        | TOO MUCH MSE ERROR          | VENO        | RENO      | WESTWOOD                    |
| 8  | BBR               | CUBIC             | CUBIC                       | LP        | Outlier with degree fit = 3 | BBR(Maybe) | VENO        | HIGHSPEED  | BIC                         | Outlier with degree fit = 3 | WESTWOOD    | HIGHSPEED | BIC                         |
| 9  | BBR               | CUBIC             | CUBIC                       | LP        | Outlier with degree fit = 3 | BBR(Maybe) | HIGHSPEED   | LP         | CUBICQ                      | TOO MUCH MSE ERROR          | VENO        | HIGHSPEED | Outlier with degree fit = 1 |
| 10 | BBR               | CUBIC             | CUBIC                       | HIGHSPEED | Outlier with degree fit = 3 | BBR(Maybe) | HIGHSPEED   | LP         | BIC                         | TOO MUCH MSE ERROR          | VENO        | HIGHSPEED | HIGHSPEED                   |
| 11 | BBR               | BBR(Maybe)        | Outlier with degree fit = 3 | HIGHSPEED | WESTWOOD                    | BBR(Maybe) | HIGHSPEED   | HIGHSPEED  | VENO                        | TOO MUCH MSE ERROR          | WESTWOOD    | RENO      | NAN - NO FEATURES           |
| 12 | BBR               | CUBIC             | Outlier with degree fit = 3 | RENO      | BIC                         | BBR(Maybe) | HIGHSPEED   | HIGHSPEED  | BIC                         | TOO MUCH MSE ERROR          | WESTWOOD    | HIGHSPEED | VENO                        |
| 13 | NAN - NO FEATURES | CUBIC             | CUBIC                       | LP        | Outlier with degree fit = 3 | BBR(Maybe) | RENO        | HIGHSPEED  | Outlier with degree fit = 1 | TOO MUCH MSE ERROR          | VENO        | RENO      | Outlier with degree fit = 1 |
| 14 | BBR               | CUBIC             | Outlier with degree fit = 3 | HIGHSPEED | BIC                         | BBR(Maybe) | LP          | RENO       | BIC                         | TOO MUCH MSE ERROR          | VENO        | RENO      | HIGHSPEED                   |
| 15 | BBR               | CUBIC             | CUBIC                       | LP        | Outlier with degree fit = 3 | BBR(Maybe) | RENO        | LP         | Outlier with degree fit = 1 | Outlier with degree fit = 3 | CUBICQ      | HIGHSPEED | Outlier with degree fit = 1 |
| 16 | BBR               | CUBIC             | Outlier with degree fit = 3 | HIGHSPEED | BIC                         | BBR(Maybe) | LP          | LP         | WESTWOOD                    | TOO MUCH MSE ERROR          | CUBICQ      | RENO      | HIGHSPEED                   |
| 17 | BBR               | CUBIC             | Outlier with degree fit = 3 | LP        | Outlier with degree fit = 3 | BBR(Maybe) | LP          | HIGHSPEED  | BIC                         | TOO MUCH MSE ERROR          | CUBICQ      | RENO      | HIGHSPEED                   |
| 18 | BBR               | CUBIC             | Outlier with degree fit = 3 | HIGHSPEED | Outlier with degree fit = 3 | BBR(Maybe) | LP          | LP         | VENO                        | TOO MUCH MSE ERROR          | WESTWOOD    | DCTCP     | CUBICQ                      |
| 19 | NAN - NO FEATURES | CUBIC             | CUBIC                       | RENO      | BIC                         | BBR(Maybe) | HIGHSPEED   | LP         | YEAH                        | TOO MUCH MSE ERROR          | WESTWOOD    | HIGHSPEED | HIGHSPEED                   |
| 20 | BBR               | NAN - NO FEATURES | CUBIC                       | LP        | BIC                         | BBR(Maybe) | HIGHSPEED   | HIGHSPEED  | Outlier with degree fit = 1 | TOO MUCH MSE ERROR          | VENO        | RENO      | YEAH                        |
| 21 | BBR               | CUBIC             | CUBIC                       | RENO      | Outlier with degree fit = 3 | BBR(Maybe) | LP          | RENO       | BIC                         | Outlier with degree fit = 3 | VENO        | RENO      | VENO                        |
| 22 | BBR               | NAN - NO FEATURES | CUBIC                       | RENO      | Outlier with degree fit = 3 | BBR(Maybe) | LP          | LP         | VENO                        | TOO MUCH MSE ERROR          | WESTWOOD    | BIC       | Outlier with degree fit =   |
| 23 | BBR               | NAN - NO FEATURES | CUBIC                       | RENO      | Outlier with degree fit = 3 | BBR(Maybe) | LP          | LP         | CUBICQ                      | TOO MUCH MSE ERROR          | WESTWOOD    | RENO      | HIGHSPEED                   |
| 24 | BBR               | CUBIC             | CUBIC                       | RENO      | Outlier with degree fit = 3 | BBR(Maybe) | LP          | HIGHSPEED  | YEAH                        | TOO MUCH MSE ERROR          | WESTWOOD    | RENO      | VENO                        |
| 25 | BBR               | CUBIC             | Outlier with degree fit = 3 | LP        | Outlier with degree fit = 3 | BBR(Maybe) | RENO        | RENO       | Outlier with degree fit = 1 | TOO MUCH MSE ERROR          | VENO        | RENO      | HIGHSPEED                   |
| ✓ | 23/25 = 92%       | 0/25 = 0%         | 15/25 = 60%                 | 0/25 = 0% | 0/25 = 0%                   | 0/25 = 0%  | 14/25 = 56% | 5/25 = 20% | 0/25 = 0%                   | 0/25 = 0%                   | 10/25 = 40% | 0/25 = 0% | 2/25 = 8%                   |
