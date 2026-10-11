#!/bin/bash

probability_matrix_path='output/LCA/probability_matrix'
output_path='output/LCA/hcc_result/'

#
keys=('popv_scanvi_prediction' 'popv_knn_on_scvi_prediction' 'popv_celltypist_prediction')
alphas=(0.05 0.01 0.005)
betas=(0.25)

for key in "${keys[@]}"; do
    echo "=== Running: $key ==="
    for alpha in "${alphas[@]}"; do
        for beta in "${betas[@]}"; do
            python hierarchical-conformal-classification.py \
                "$probability_matrix_path/$key.csv" \
                LCA_TS-en \
                "data/LCA_TS/LCA_TS_id_to_label.json" \
                "$output_path/${key}_${alpha}_${beta}_nobc_output.csv" \
                True False $alpha $beta 42 False "hierarchical" nobc "first" "lac"
            python hierarchical-conformal-classification.py \
                "$probability_matrix_path/$key.csv" \
                LCA_TS-en \
                "data/LCA_TS/LCA_TS_id_to_label.json" \
                "$output_path/${key}_${alpha}_${beta}_ml_output.csv" \
                False False $alpha $beta 42 False "multi-label"
        done
    done
done