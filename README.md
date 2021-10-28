# Vexp

Open these files in Spyder (or another editor).

Find Spyder via the Anaconda3 Start Menu item.

* `make_runs.py`
* `deliver_runs.py`

You should also go to the Anaconda3 Start Menu, and choose Anaconda Powershell Prompt (or Anaconda Prompt).

Then, at that prompt, change directory to this directory.

```
cd c:\repos\vexp
```

All the Ready, Set etc wav files last for 750 ms (see the file
`make_clipped.py`).

Have a look at `make_runs.py`.  Change any parameters you want to.  If in Spyder, click Run button.  Otherwise, from the shell you've just opened.

```
python make_runs.py
```

This rebuilds the `.csv` files that define the runs.

To deliver the stimuli:

```
python deliver_runs.py run_001.csv
```

(where `run_001.csv` is your chosen stimulus file).

To run a training session:

```
python deliver_runs.py train_001.csv
```

(where `train_001.csv` is your chosen stimulus file).

Press Ctrl-C to abort the run.  Otherwise it will continue for the default 50 trials.

At the beginning of the 25th trial, the program will pause and ask you to press Space to continue.
