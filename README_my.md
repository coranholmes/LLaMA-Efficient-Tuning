## 运行流程
1. 训练`./scripts/train_sft.sh`或者使用`./scripts/deepspeed_train.sh`（注意重新设置模型输出位置）
2. 测试`./scripts/test_sft.sh`（注意重新设置训练好的模型位置）
3. （可选）合并adapter到base model`./scripts/merge_model.sh`（注意重新设置训练好的模型位置）
4. 使用训练好的模型用20个预设的profile进行大五人格测试`./scripts/eval_persona.sh`（注意重新设置训练好的模型位置）

其他信息参考README_orig.md