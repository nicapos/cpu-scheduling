# CPU Scheduling Algorithm Simulator

A programming exercise that simulates the basic CPU scheduling algorithms:

- First-Come-First-Serve (FCFS)
- Shortest-Job First (SJF)
- Shortest-Remaining-Time-First (SRTF)
- Round-Robin (RR)

## Instructions

### Input

The program reads the following from standard input:
The first line contains three integers separated by space, $X\hspace{.1cm}Y\hspace{.1cm}Z$.

- $X$ denotes the CPU scheduling algorithm.
- $Y$ denotes the number of processes where $3 \leq Y \leq 100$
- $Z$ denotes a time slice value (applicable for Round-Robin algorithm only), where $1 \leq Z \leq 100$. If the CPU scheduling algorithm indicated by the value of $X$ is not the Round-Robin algorithm, this value must be set to 1 but ignored.

See the table below for the CPU scheduling algorithm and the corresponding value of $X$.

| CPU Scheduling Algorithm | Value of $X$ |
| ------------------------ | ------------ |
| FCFS                     | 0            |
| SJF                      | 1            |
| SRTF                     | 2            |
| RR                       | 3            |

There will be $Y$ lines of space-separated integers $A\hspace{.1cm}B\hspace{.1cm}C$ where $A$ is the process ID, $B$ is the arrival time, and $C$ is the burst time.

### Output

The output includes the following:

- $Y$ lines of processes with the start time, end time, and total waiting time. If there are multiple start and end times for each process, display them in order. (where $S_1 ... S_N, \hspace{.1cm} E_1 ... E_N, \hspace{.1cm} \text{WT} \geq 0 $)

- An additional last line, where 𝐴𝑊𝑇 indicates the average waiting time of the processes. The output should be sorted according to the process ID $A$.

```bash
Average waiting time: <AWT>
```

## Usage

To run the simulator with manual input, run:

```bash
python main.py
```

To run the simulator with an input file, run:

```bash
# On Windows
type ./path/to/input.txt | python main.py
```

```bash
# On Mac/Linux
cat ./path/to/input.txt | python main.py
```

To run the simulator with an input and output file, run:

```bash
# On Windows
type ./path/to/input.txt | python main.py > ./path/to/output.txt
```

```bash
# On Mac/Linux
cat ./path/to/input.txt | python main.py > ./path/to/output.txt
```

### Test

To run the test cases for all algorithms, run:

```bash
python test.py
```

To run all the test cases for a certain algorithm, run:

```bash
python test.py --algo algorithm_name
```

To run a certain test case for a certain algorithm, run:

```bash
python test.py --algo algorithm_name --case n
```

```bash
# To use ./test/RR/input02.txt as a test case, run:
python test.py --algo rr --case 02
```

To run a single test case, run:

```bash
python test.py --input input.txt --output expected_output.txt
```

or using the shorthand:

```bash
python test.py -i input.txt -o expected_output.txt
```
