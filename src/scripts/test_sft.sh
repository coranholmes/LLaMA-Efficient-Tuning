CUDA_VISIBLE_DEVICES=3 python src/cli_demo.py \
    --model_name_or_path /data2/models/llama2-13b-hf \
    --template llama2 \
    --finetuning_type lora \
    --checkpoint_dir output/llama2_13b_newT_ds