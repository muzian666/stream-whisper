
# 使用 Faster-whisper 模拟实时语音转写

<figure style="text-align: center; radius:10pt">
    <img src="docs/flow.gif" width=689pt radius=10pt>
    <figcaption style="text-align:center"> faster-whiper 模拟实时语音转写流程 </figcaption>
</figure>



# 使用方法
## 服务端 
- (目前仅在Linux上得到了验证)
### 需要额外安装的内容
#### Linux
```bash
apt -y install libcublas11
```
- `libcublas11` 是 NVIDIA CUDA Toolkit 的依赖，如果需要使用 CUDA Toolkit，需要安装。

### 启动服务端
```bash
git clone https://github.com/ultrasev/stream-whisper
cd stream-whisper
pip3 install -r requirements.txt
python3 -m src.server
```

注：

- 经 [@muzian666](https://github.com/muzian666) 提示，aioredis 包目前仍然不支持 Python3.11，Python 版本建议 3.8 ~ 3.10

首次运行时会提示自动创建 `.env` 文件并要求输入 `REDIS_SERVER`，将以 `redis://` 开头的链接输入其中即可

第一次执行时，可以选择从本地读取或从网络下载，如果选择本地读取则会从 `./src/model` 中加载模型，如果选择网络下载则会从huggingface下载对应模型。鉴于目前 Huggingface 已经被防火墙特别对待了，下载速度很慢，建议使用代理。


## 客户端
```bash
git clone https://github.com/ultrasev/stream-whisper
apt -y install portaudio19-dev
cd stream-whisper
pip3 install -r requirements.txt
```

注：
- `portaudio19-dev` 是 pyaudio 的依赖，如果系统已安装，可以忽略。

同样需要把 `.env` 文件中的 `REDIS_SERVER` 改成自己的 Redis 地址，在本地机器上运行 `python3 -m src.client`，客户端就启动了。运行前先测试一下麦克风是否正常工作，确认能够正常录音。 

# 可优化方向
1. 缩短静音间隔，提高实时性。默认静音间隔是 0.5 秒，可以根据自己的需求在 `client.py` 中调整。
2. 使用更好的语音识别模型，提高识别准确率。

# Q&A
## Redis 地址怎么搞？
1. 自己有带有公网 IP 的服务器的话， 使用 docker 可以很方便的创建一个；
2. 或者通过 [redislabs](https://app.redislabs.com/#/) 注册账号，创建一个免费实例，获取连接信息。免费实例有 30M 内存，足够使用。建议选择日本 AWS 区域，延迟低。

## 为什么要用 Redis？
Redis 不是必须的，从 client 端往 server 端传输数据，有很多种方法，可以根据自己的需求选择。


