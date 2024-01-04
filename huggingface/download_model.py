from huggingface_hub import snapshot_download
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model_name", 
                    type=str, 
                    help = "Huggingface Repo Id",
                    default="THUDM/chatglm2-6b-32k")

args = parser.parse_args()
model_name = args.model_name

# parse command line arguments


downloaded_model_path = snapshot_download(repo_id=model_name,
                                        resume_download=True,
                                        max_workers=1,
                                        use_auth_token=True) 
print(downloaded_model_path)