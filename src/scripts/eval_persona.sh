CUDA_VISIBLE_DEVICES=0 python src/big5_evaluator.py \
    --model_name_or_path /data2/models/llama2-13b-hf \
    --template llama2 \
    --finetuning_type lora \
    --checkpoint_dir output/llama2_new_template