python src/export_model.py \
    --model_name_or_path /data2/models/llama2-13b-hf \
    --template llama2 \
    --finetuning_type lora \
    --checkpoint_dir output_llama2_v2 \
    --output_dir llama2_13b_lora_1000_v2