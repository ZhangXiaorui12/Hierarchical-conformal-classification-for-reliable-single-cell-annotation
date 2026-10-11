# Hierarchical conformal classification for reliable single-cell annotation

## Installation and setup

```
conda env create -f environment.yml
conda activate scHCC
```

## Usage

The pipeline can be executed as follows:

1. Train a base classifier from scratch following `Base classifier.ipynb`, or load a pretrained model if available.
2. (Optional) For cross‑dataset validation, train the OOD detector using `OOD_detector.ipynb`.
3. Load the ontology lexicon:
   ```python
   import wn
   wn.add("data/LCA_TS/LCA_TS_tree.xml")

4. Run the hierarchical conformal classification pipeline via `HCC_process.ipynb`.

5. Evaluate the performance of scHCC with `Evaluation.ipynb`.

## Files

'hierarchical-conformal-classification.py' ——main entrypoint for hierarchical conformal classification

'classifiers/' ——codes for base classifiers

'hcc/'——codes for hierarchical conformal classification process

'ood_detector'——codes for OOD detection process

