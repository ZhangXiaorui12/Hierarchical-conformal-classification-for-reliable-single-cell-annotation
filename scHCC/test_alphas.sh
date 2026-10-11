#!/bin/bash

probability_matrix_path='output/Lung_Cell_Atlas/probability_matrix'
output_path='output/Lung_Cell_Atlas/hcc_result/'

keys=('popv_celltypist_prediction')
alphas=(0.2 0.1 0.05 0.005 0.001)
betas=(0.25)

for key in "${keys[@]}"; do
    echo "=== Running: $key ==="
    for alpha in "${alphas[@]}"; do
        for beta in "${betas[@]}"; do
            python hierarchical-conformal-classification.py \
                "$probability_matrix_path/$key.csv" \
                LCA-en \
                "data/Lung_Cell_Atlas/LCA_id_to_label.json" \
                "$output_path/${key}_${alpha}_${beta}_output.csv" \
                True False $alpha $beta 42 False "hierarchical" True "first" "lac"
        done
    done
done