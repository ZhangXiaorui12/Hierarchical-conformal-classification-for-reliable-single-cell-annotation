#!/bin/bash

probability_matrix_path='output/LCA/probability_matrix'
output_path='output/LCA/hcc_result/'

#'popv_scanvi_prediction' 'popv_knn_on_scvi_prediction' 
keys=('popv_celltypist_prediction')
alphas=(0.01 0.005)
betas=(1 0.9 0.8 0.7 0.6 0.5 0.4 0.3 0.2 0.1 0)

for key in "${keys[@]}"; do
    echo "=== Running: $key ==="
    for alpha in "${alphas[@]}"; do
        for beta in "${betas[@]}"; do
            python hierarchical-conformal-classification.py \
                "$probability_matrix_path/$key.csv" \
                LCA_TS-en \
                "data/LCA_TS/LCA_TS_id_to_label.json" \
                "$output_path/${key}_${alpha}_${beta}_output.csv" \
                True False $alpha $beta 42 False "hierarchical" True "first" "lac"
        done
    done
done