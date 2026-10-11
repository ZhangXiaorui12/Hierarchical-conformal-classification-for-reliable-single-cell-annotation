#!/bin/bash

probability_matrix_path='output/LCA_wo_capillary/probability_matrix'
output_path='output/LCA_wo_capillary/hcc_result/'

#'popv_scanvi_prediction' 'popv_knn_on_scvi_prediction' 
keys=('popv_celltypist_prediction')
alphas=(0.05 0.01 0.005)
betas=(0.25)

for key in "${keys[@]}"; do
    echo "=== Running: $key ==="
    for alpha in "${alphas[@]}"; do
        for beta in "${betas[@]}"; do
            python hierarchical-conformal-classification.py \
                "$probability_matrix_path/$key.csv" \
                LCA_wo_capillary-en \
                "data/LCA/LCA_wo_capillary_id_to_label.json" \
                "$output_path/${key}_${alpha}_${beta}_output.csv" \
                True False $alpha $beta 42 False "hierarchical" True "first" "lac"
            python hierarchical-conformal-classification.py \
                "$probability_matrix_path/$key.csv" \
                LCA_wo_capillary-en \
                "data/LCA/LCA_wo_capillary_id_to_label.json" \
                "$output_path/${key}_${alpha}_${beta}_leaf_output.csv" \
                True False $alpha $beta 42 True "hierarchical" True "first" "lac"
        done
    done
done