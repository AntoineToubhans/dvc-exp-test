DVC Experiment Management
===

Veille technique AntoineT


- run une exp: `dvc exp run -S seed=XXX`
- run avec queue:
  - `dvc exp run --queue -S seed=XX1`
  - `dvc exp run --queue -S seed=XX2`
  - `dvc exp run --queue -S seed=XX3`
  - `dvc exp run --run-all --jobs 2`
- checkout sur une exp donnée
- persist d'une exp
- voir toutes les exp: `dvc exp show -A`

- partage d'exp
  - `dvc exp push origin EXP_ID`
  - `dvc exp pull origin EXP_ID`
