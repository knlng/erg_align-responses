# README

The two scripts should speed up evaluations of ERG measurements. They align the responses from the ERG results to the flashpoint (here: -0.5 ms).

The data obtained after ERG measurement with the HMsERG / ERG system (Ocuscience LLC, USA) can be exported as CSV file. This CSV file consists of two columns, the first is the time [ms], the second is the response [µV]. To be able to compare ERG curves, these scripts shift the response values so that the response is zero where time is -0.5 (this is the flashpoint). They add an additional column to the CSV file with the aligned response values.

To run the scripts,
1) create "output" folder if not already created (e.g. in "\\path\to\data\3cd\output")
2) copy the scripts to a folder, e.g. "\\path\to\erg\scripts"
3) edit "erg_subscripts.py" by changing paths details: "path_csvdata" and "path_output"
4) run the following command using "Anaconda Prompt" on Windows
python \\path\to\erg\scripts\erg_evaluation.py
(path must be adjusted respectively)

