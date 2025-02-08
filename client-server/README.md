# Nebby analysis result

The folders are named after the following schema: 
```
<PRE>-<POST>-<BANDWIDTH>-<BUFFER>-<HOST>
```
Where `<PRE>`, `<POST>`, `<BANDWIDTH>` and `<BUFFER>` are the parameters for Nebby.
`<HOST>` is either `pi` or `server` depending on which hardware did the measurment as the client.

## 5-45-200-1
This measurement was only done once on an Raspberry Pi 4b.

| CCA       | Analysis result (Pi)        |
|-----------|-----------------------------|
| bbr       | TOO MUCH MSE ERROR          |
| cubic     | HTCP                        |
| dctcp     | Outlier with degree fit = 1 |
| highspeed | WESTWOOD                    |
| htcp      | Outlier with degree fit = 1 |
| lp        | VENO                        |
| nv        | BIC                         |
| reno      | HIGHSPEED                   |
| scalable  | VENO                        |
| vegas     | Outlier with degree fit = 3 |
| veno      | VENO                        |
| westwood  | HIGHSPEED                   |
| yeah      | VENO                        |


## 5-45-200-2
The measurement was repeated on an Raspberry Pi 4b and a DELL Optiplex 7020.

| CCA       | Analysis result (Pi)        | Analysis result (Server)    |
|-----------|-----------------------------|-----------------------------|
| bbr       | BBR                         | BBR                         |
| bic       | TOO MUCH MSE ERROR          | CUBIC                       |
| cdg       |                             | TOO MUCH MSE ERROR          |
| cubic     | CUBIC                       | CUBIC                       |
| dctcp     | Outlier with degree fit = 1 | Outlier with degree fit = 1 |
| highspeed | HIGHSPEED                   | Outlier with degree fit = 1 |
| htcp      | CUBIC                       | CUBIC                       |
| hybla     |                             | NAN - NO FEATURES           |
| illinois  |                             | NAN - NO FEATURES           |
| lp        | Outlier with degree fit = 3 | VENO                        |
| nv        | VENO                        | Outlier with degree fit = 1 |
| reno      | Outlier with degree fit = 1 | Outlier with degree fit = 1 |
| scalable  |                             | NAN - NO FEATURES           |
| vegas     | BBR                         | BBR                         |
| veno      | VENO                        | VENO                        |
| westwood  | WESTWOOD                    | Outlier with degree fit = 1 |
| yeah      | Outlier with degree fit = 1 | HTCP                        |

## 5-95-200-2
The measurement was repeated on an Raspberry Pi 4b and a DELL Optiplex 7020.

| CCA       | Analysis result (Pi)        | Analysis result (Server)    |
|-----------|-----------------------------|-----------------------------|
| bbr       | BBR                         | BBR(Maybe)                  |
| bic       | CUBIC                       | CUBIC                       |
| cdg       |                             | NAN - NO FEATURES           |
| cubic     | HTCP                        | HTCP                        |
| dctcp     | HIGHSPEED                   | HIGHSPEED                   |
| highspeed | Outlier with degree fit = 1 | Outlier with degree fit = 1 |
| htcp      | Outlier with degree fit = 2 | Outlier with degree fit = 2 |
| hybla     |                             | NAN - NO FEATURES           |
| illinois  |                             | NAN - NO FEATURES           |
| lp        | HIGHSPEED                   | HIGHSPEED                   |
| nv        | Outlier with degree fit = 3 | WESTWOOD                    |
| reno      | HIGHSPEED                   | WESTWOOD                    |
| scalable  |                             | NAN - NO FEATURES           |
| vegas     | TOO MUCH MSE ERROR          | TOO MUCH MSE ERROR          |
| veno      | WESTWOOD                    | HIGHSPEED                   |
| westwood  | WESTWOOD                    | WESTWOOD                    |
| yeah      |                             | NAN - NO FEATURES           |
