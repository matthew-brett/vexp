# Vexp

Open these files in Spyder (or another editor):

* `make_runs.py`
* `deliver_runs.py`

All the Ready, Set etc wav files last for 750 ms (see the file
`make_clipped.py`).

Have a look at `make_runs.py`.  Change any parameters you want to.  If in Spyder, click Run button.  Otherwise, from a Cmd or Powershell shell:

```
python make_runs.py
```

This rebuilds the `.csv` files that define the runs.

To deliver the stimuli:

```
python deliver_runs.py run_001.csv
```

(where `run_001.csv` is your chosen stimulus file).

Press Ctrl-C to stop the run.
