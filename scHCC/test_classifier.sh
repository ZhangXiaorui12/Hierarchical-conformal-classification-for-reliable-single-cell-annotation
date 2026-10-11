#!/bin/bash

probability_matrix_path='output/LCA/probability_matrix'
output_path='output/LCA/hcc_result/'
#
keys=('popv_celltypist_prediction' 'popv_scanvi_prediction' 'popv_knn_on_scvi_prediction' 'popv_xgboost_prediction' 'popv_knn_bbknn_prediction' 'popv_rf_prediction' 'popv_svm_prediction')
alphas=(0.01)
betas=(0.25)

for key in "${keys[@]}"; do
    echo "=== Running: $key ==="
    for alpha in "${alphas[@]}"; do
        for beta in "${betas[@]}"; do
            python hierarchical-conformal-classification.py \
                "$probability_matrix_path/$key.csv" \
                LCA_TS-en \
                "data/LCA_TS/LCA_TS_id_to_label.json" \
                "$output_path/${key}_${alpha}_${beta}_leaf_output.csv" \
                True False $alpha $beta 42 True "hierarchical" True "first" "lac"
        done
    done
done