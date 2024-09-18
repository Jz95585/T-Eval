echo "evaluating retrieve ..."
python test.py --model_type api --model_path $1  --resume --out_name retrieve.json --out_dir out_dirs1/$1/ --dataset_path data1/agent_final数据/retrieve_checked_zh.json --eval rru --prompt_type json --model_display_name  $1
# python test.py --model_type api --model_path $1  --resume --out_name retrieve.json --out_dir out_dirs1/$1/ --dataset_path data1/agent_final数据/retrieve_checked_zh.json --eval retrieve --prompt_type str --model_display_name  $1

# echo "evaluating reason ..."
# python test.py --model_type api --model_path $1  --resume --out_name resaon.json --out_dir out_dirs/$1/ --dataset_path data1/agent_final数据/reason_checked_zh.json --eval reason --prompt_type str --model_display_name  $1
# echo "evaluating understand ..."
# python test.py --model_type api --model_path $1  --resume --out_name understand.json --out_dir out_dirs/$1/ --dataset_path data1/agent_final数据/understand_checked_zh.json --eval understand --prompt_type str --model_display_name  $1
