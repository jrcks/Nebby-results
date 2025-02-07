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

## BBR

| CCA         | Analysis result             |
|-------------|-----------------------------|
| bbr1        | BBR                         |
| bbr2        | BBR                         |
| bbr3        | BBR                         |
| bbr4        | BBR                         |
| bbr5        | BBR(Maybe)                  |
| bbr6        | BBR                         |
| bbr7        | BBR                         |
| bbr8        | BBR                         |
| bbr9        | BBR                         |
| bbr10       | BBR                         |
| bbr11       | BBR                         |
| bbr12       | BBR                         |
| bbr13       | NAN - NO FEATURES           |
| bbr14       | BBR                         |
| bbr15       | BBR                         |
| bbr16       | BBR                         |
| bbr17       | BBR                         |
| bbr18       | BBR                         |
| bbr19       | NAN - NO FEATURES           |
| bbr20       | BBR                         |
| bbr21       | BBR                         |
| bbr22       | BBR                         |
| bbr23       | BBR                         |
| bbr24       | BBR                         |
| bbr25       | BBR                         |

## BIC

| CCA         | Analysis result             |
|-------------|-----------------------------|
| bic1        | BBR(Maybe)                  |
| bic2        | NAN - NO FEATURES           |
| bic3        | CUBIC                       |
| bic4        | NAN - NO FEATURES           |
| bic5        | NAN - NO FEATURES           |
| bic6        | NAN - NO FEATURES           |
| bic7        | NAN - NO FEATURES           |
| bic8        | CUBIC                       |
| bic9        | CUBIC                       |
| bic10       | CUBIC                       |
| bic11       | BBR(Maybe)                  |
| bic12       | CUBIC                       |
| bic13       | CUBIC                       |
| bic14       | CUBIC                       |
| bic15       | CUBIC                       |
| bic16       | CUBIC                       |
| bic17       | CUBIC                       |
| bic18       | CUBIC                       |
| bic19       | CUBIC                       |
| bic20       | NAN - NO FEATURES           |
| bic21       | CUBIC                       |
| bic22       | NAN - NO FEATURES           |
| bic23       | NAN - NO FEATURES           |
| bic24       | CUBIC                       |
| bic25       | CUBIC                       |

## Cubic

| CCA         | Analysis result             |
|-------------|-----------------------------|
| cubic1      | CUBIC                       |
| cubic2      | CUBIC                       |
| cubic3      | Outlier with degree fit = 3 |
| cubic4      | CUBIC                       |
| cubic5      | Outlier with degree fit = 3 |
| cubic6      | Outlier with degree fit = 3 |
| cubic7      | CUBIC                       |
| cubic8      | CUBIC                       |
| cubic9      | CUBIC                       |
| cubic10     | CUBIC                       |
| cubic11     | Outlier with degree fit = 3 |
| cubic12     | Outlier with degree fit = 3 |
| cubic13     | CUBIC                       |
| cubic14     | Outlier with degree fit = 3 |
| cubic15     | CUBIC                       |
| cubic16     | Outlier with degree fit = 3 |
| cubic17     | Outlier with degree fit = 3 |
| cubic18     | Outlier with degree fit = 3 |
| cubic19     | CUBIC                       |
| cubic20     | CUBIC                       |
| cubic21     | CUBIC                       |
| cubic22     | CUBIC                       |
| cubic23     | CUBIC                       |
| cubic24     | CUBIC                       |
| cubic25     | Outlier with degree fit = 3 |

## DCTCP

| CCA         | Analysis result             |
|-------------|-----------------------------|
| dctcp1      | LP                          |
| dctcp2      | RENO                        |
| dctcp3      | LP                          |
| dctcp4      | RENO                        |
| dctcp5      | HIGHSPEED                   |
| dctcp6      | HIGHSPEED                   |
| dctcp7      | RENO                        |
| dctcp8      | LP                          |
| dctcp9      | LP                          |
| dctcp10     | HIGHSPEED                   |
| dctcp11     | HIGHSPEED                   |
| dctcp12     | RENO                        |
| dctcp13     | LP                          |
| dctcp14     | HIGHSPEED                   |
| dctcp15     | LP                          |
| dctcp16     | HIGHSPEED                   |
| dctcp17     | LP                          |
| dctcp18     | HIGHSPEED                   |
| dctcp19     | RENO                        |
| dctcp20     | LP                          |
| dctcp21     | RENO                        |
| dctcp22     | RENO                        |
| dctcp23     | RENO                        |
| dctcp24     | RENO                        |
| dctcp25     | LP                          |

## Highspeed

| CCA         | Analysis result             |
|-------------|-----------------------------|
| highspeed1  | Outlier with degree fit = 3 |
| highspeed2  | Outlier with degree fit = 1 |
| highspeed3  | Outlier with degree fit = 3 |
| highspeed4  | Outlier with degree fit = 3 |
| highspeed5  | Outlier with degree fit = 3 |
| highspeed6  | BIC                         |
| highspeed7  | BIC                         |
| highspeed8  | Outlier with degree fit = 3 |
| highspeed9  | Outlier with degree fit = 3 |
| highspeed10 | Outlier with degree fit = 3 |
| highspeed11 | WESTWOOD                    |
| highspeed12 | BIC                         |
| highspeed13 | Outlier with degree fit = 3 |
| highspeed14 | BIC                         |
| highspeed15 | Outlier with degree fit = 3 |
| highspeed16 | BIC                         |
| highspeed17 | Outlier with degree fit = 3 |
| highspeed18 | Outlier with degree fit = 3 |
| highspeed19 | BIC                         |
| highspeed20 | BIC                         |
| highspeed21 | Outlier with degree fit = 3 |
| highspeed22 | Outlier with degree fit = 3 |
| highspeed23 | Outlier with degree fit = 3 |
| highspeed24 | Outlier with degree fit = 3 |
| highspeed25 | Outlier with degree fit = 3 |

## HTCP

| CCA         | Analysis result             |
|-------------|-----------------------------|
| htcp1       | BBR(Maybe)                  |
| htcp2       | BBR(Maybe)                  |
| htcp3       | BBR(Maybe)                  |
| htcp4       | BBR(Maybe)                  |
| htcp5       | BBR(Maybe)                  |
| htcp6       | BBR(Maybe)                  |
| htcp7       | BBR(Maybe)                  |
| htcp8       | BBR(Maybe)                  |
| htcp9       | BBR(Maybe)                  |
| htcp10      | BBR(Maybe)                  |
| htcp11      | BBR(Maybe)                  |
| htcp12      | BBR(Maybe)                  |
| htcp13      | BBR(Maybe)                  |
| htcp14      | BBR(Maybe)                  |
| htcp15      | BBR(Maybe)                  |
| htcp16      | BBR(Maybe)                  |
| htcp17      | BBR(Maybe)                  |
| htcp18      | BBR(Maybe)                  |
| htcp19      | BBR(Maybe)                  |
| htcp20      | BBR(Maybe)                  |
| htcp21      | BBR(Maybe)                  |
| htcp22      | BBR(Maybe)                  |
| htcp23      | BBR(Maybe)                  |
| htcp24      | BBR(Maybe)                  |
| htcp25      | BBR(Maybe)                  |

## LP

| CCA         | Analysis result             |
|-------------|-----------------------------|
| lp1         | HIGHSPEED                   |
| lp2         | RENO                        |
| lp3         | LP                          |
| lp4         | LP                          |
| lp5         | LP                          |
| lp6         | RENO                        |
| lp7         | RENO                        |
| lp8         | VENO                        |
| lp9         | HIGHSPEED                   |
| lp10        | HIGHSPEED                   |
| lp11        | HIGHSPEED                   |
| lp12        | HIGHSPEED                   |
| lp13        | RENO                        |
| lp14        | LP                          |
| lp15        | RENO                        |
| lp16        | LP                          |
| lp17        | LP                          |
| lp18        | LP                          |
| lp19        | HIGHSPEED                   |
| lp20        | HIGHSPEED                   |
| lp21        | LP                          |
| lp22        | LP                          |
| lp23        | LP                          |
| lp24        | LP                          |
| lp25        | RENO                        |

## Reno

| CCA         | Analysis result             |
|-------------|-----------------------------|
| reno1       | HIGHSPEED                   |
| reno2       | HIGHSPEED                   |
| reno3       | LP                          |
| reno4       | LP                          |
| reno5       | LP                          |
| reno6       | RENO                        |
| reno7       | RENO                        |
| reno8       | HIGHSPEED                   |
| reno9       | LP                          |
| reno10      | LP                          |
| reno11      | HIGHSPEED                   |
| reno12      | HIGHSPEED                   |
| reno13      | HIGHSPEED                   |
| reno14      | RENO                        |
| reno15      | LP                          |
| reno16      | LP                          |
| reno17      | HIGHSPEED                   |
| reno18      | LP                          |
| reno19      | LP                          |
| reno20      | HIGHSPEED                   |
| reno21      | RENO                        |
| reno22      | LP                          |
| reno23      | LP                          |
| reno24      | HIGHSPEED                   |
| reno25      | RENO                        |

## Scalable

| CCA         | Analysis result             |
|-------------|-----------------------------|
| scalable1   | CUBICQ                      |
| scalable2   | VENO                        |
| scalable3   | WESTWOOD                    |
| scalable4   | BIC                         |
| scalable5   | Outlier with degree fit = 1 |
| scalable6   | Outlier with degree fit = 1 |
| scalable7   | VENO                        |
| scalable8   | BIC                         |
| scalable9   | CUBICQ                      |
| scalable10  | BIC                         |
| scalable11  | VENO                        |
| scalable12  | BIC                         |
| scalable13  | Outlier with degree fit = 1 |
| scalable14  | BIC                         |
| scalable15  | Outlier with degree fit = 1 |
| scalable16  | WESTWOOD                    |
| scalable17  | BIC                         |
| scalable18  | VENO                        |
| scalable19  | YEAH                        |
| scalable20  | Outlier with degree fit = 1 |
| scalable21  | BIC                         |
| scalable22  | VENO                        |
| scalable23  | CUBICQ                      |
| scalable24  | YEAH                        |
| scalable25  | Outlier with degree fit = 1 |

## Vegas

| CCA         | Analysis result             |
|-------------|-----------------------------|
| vegas1      | TOO MUCH MSE ERROR          |
| vegas2      | TOO MUCH MSE ERROR          |
| vegas3      | TOO MUCH MSE ERROR          |
| vegas4      | TOO MUCH MSE ERROR          |
| vegas5      | TOO MUCH MSE ERROR          |
| vegas6      | TOO MUCH MSE ERROR          |
| vegas7      | TOO MUCH MSE ERROR          |
| vegas8      | Outlier with degree fit = 3 |
| vegas9      | TOO MUCH MSE ERROR          |
| vegas10     | TOO MUCH MSE ERROR          |
| vegas11     | TOO MUCH MSE ERROR          |
| vegas12     | TOO MUCH MSE ERROR          |
| vegas13     | TOO MUCH MSE ERROR          |
| vegas14     | TOO MUCH MSE ERROR          |
| vegas15     | Outlier with degree fit = 3 |
| vegas16     | TOO MUCH MSE ERROR          |
| vegas17     | TOO MUCH MSE ERROR          |
| vegas18     | TOO MUCH MSE ERROR          |
| vegas19     | TOO MUCH MSE ERROR          |
| vegas20     | TOO MUCH MSE ERROR          |
| vegas21     | Outlier with degree fit = 3 |
| vegas22     | TOO MUCH MSE ERROR          |
| vegas23     | TOO MUCH MSE ERROR          |
| vegas24     | TOO MUCH MSE ERROR          |
| vegas25     | TOO MUCH MSE ERROR          |

## Veno

| CCA         | Analysis result             |
|-------------|-----------------------------|
| veno1       | CUBICQ                      |
| veno2       | VENO                        |
| veno3       | CUBICQ                      |
| veno4       | CUBICQ                      |
| veno5       | HIGHSPEED                   |
| veno6       | VENO                        |
| veno7       | VENO                        |
| veno8       | WESTWOOD                    |
| veno9       | VENO                        |
| veno10      | VENO                        |
| veno11      | WESTWOOD                    |
| veno12      | WESTWOOD                    |
| veno13      | VENO                        |
| veno14      | VENO                        |
| veno15      | CUBICQ                      |
| veno16      | CUBICQ                      |
| veno17      | CUBICQ                      |
| veno18      | WESTWOOD                    |
| veno19      | WESTWOOD                    |
| veno20      | VENO                        |
| veno21      | VENO                        |
| veno22      | WESTWOOD                    |
| veno23      | WESTWOOD                    |
| veno24      | WESTWOOD                    |
| veno25      | VENO                        |

## Westwood

| CCA         | Analysis result             |
|-------------|-----------------------------|
| westwood1   | RENO                        |
| westwood2   | HIGHSPEED                   |
| westwood3   | LP                          |
| westwood4   | RENO                        |
| westwood5   | HIGHSPEED                   |
| westwood6   | RENO                        |
| westwood7   | RENO                        |
| westwood8   | HIGHSPEED                   |
| westwood9   | HIGHSPEED                   |
| westwood10  | HIGHSPEED                   |
| westwood11  | RENO                        |
| westwood12  | HIGHSPEED                   |
| westwood13  | RENO                        |
| westwood14  | RENO                        |
| westwood15  | HIGHSPEED                   |
| westwood16  | RENO                        |
| westwood17  | RENO                        |
| westwood18  | DCTCP                       |
| westwood19  | HIGHSPEED                   |
| westwood20  | RENO                        |
| westwood21  | RENO                        |
| westwood22  | BIC                         |
| westwood23  | RENO                        |
| westwood24  | RENO                        |
| westwood25  | RENO                        |

## YeAH

| CCA         | Analysis result             |
|-------------|-----------------------------|
| yeah1       | CUBICQ                      |
| yeah2       | YEAH                        |
| yeah3       | BIC                         |
| yeah4       | HIGHSPEED                   |
| yeah5       | CUBICQ                      |
| yeah6       | Outlier with degree fit = 1 |
| yeah7       | WESTWOOD                    |
| yeah8       | BIC                         |
| yeah9       | Outlier with degree fit = 1 |
| yeah10      | HIGHSPEED                   |
| yeah11      | NAN - NO FEATURES           |
| yeah12      | VENO                        |
| yeah13      | Outlier with degree fit = 1 |
| yeah14      | HIGHSPEED                   |
| yeah15      | Outlier with degree fit = 1 |
| yeah16      | HIGHSPEED                   |
| yeah17      | HIGHSPEED                   |
| yeah18      | CUBICQ                      |
| yeah19      | HIGHSPEED                   |
| yeah20      | YEAH                        |
| yeah21      | VENO                        |
| yeah22      | Outlier with degree fit = 1 |
| yeah23      | HIGHSPEED                   |
| yeah24      | VENO                        |
| yeah25      | HIGHSPEED                   |
