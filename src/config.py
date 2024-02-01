import os
from dotenv import load_dotenv

# 检查 .env 文件是否存在
env_file = '.env'
if not os.path.exists(env_file):
    redis_server = input("请输入 REDIS_SERVER 的值: ")
    with open(env_file, 'w') as f:
        f.write(f"REDIS_SERVER={redis_server}\n")
    print(f"已将 REDIS_SERVER 的值记录在 {env_file} 中。")

load_dotenv(env_file)

REDIS_SERVER = os.getenv('REDIS_SERVER')

if REDIS_SERVER is None:
    raise EnvironmentError(
        "The REDIS_SERVER environment variable is not set. "
        "Please set it in your .env file or as an environment variable.")
