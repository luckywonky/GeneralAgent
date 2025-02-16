<h1 align="center">GeneralAgent: From LLM to Agent</h1>
<p align="center">
<a href="README.md"><img src="https://img.shields.io/badge/document-English-blue.svg" alt="EN doc"></a>
<a href="README_CN.md"><img src="https://img.shields.io/badge/文档-中文版-blue.svg" alt="CN doc"></a>
<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=white&style=flat" alt="License"/>
</p>
<p align='center'>
A simple, general, customizable Agent framework
</p>


## Features

* Simple、Fast、Stable: **stable with GPT3.5**.
* GeneralAgent support **serialization**, include **python state**.
* Build-in interpreters: Python, AppleScript, Shell, File, Plan, Retrieve Embedding etc.
* **Dynamic UI**: Agent can create dynamic ui to user who can use.
* **WebUI with agent builder**. You can use natural language to create agent without coding.
* [AthenaAgent](https://github.com/sigworld/AthenaAgent) is a TypeScript port of GeneralAgent.



## Architecture

**GeneralAgent**

![Architecture](./docs/images/Architecture_2023.11.15.png)

**WebUI**

<p align="center">
<img src="./docs/images/webui_2023.11.15.png" alt="WebUI" width=600/>
</p>


## Demo

**Version 0.03**

![webui](./docs/images/2023.11.15.jpg)



**Version 0.0.2**



https://github.com/CosmosShadow/GeneralAgent/assets/13933465/9d9b4d6b-0c9c-404d-87d8-7f8e03f3772b



## Usage

### docker

```bash
# pull docker
docker pull cosmosshadow/general-agent

# make .env
cp .env.example .env
vim .env
# Configure environment variables in the .env file, such as OPENAI_API_KEY, etc.

# run
docker run \
-p 3000:3000 \
-p 7777:7777 \
-v `pwd`/.env:/workspace/.env \
-v `pwd`/data:/workspace/data \
--name=agent \
--privileged=true \
-d cosmosshadow/general-agent

# open web with localhost:3000
```



### Local installation and usage

#### Installation

```bash
pip install GeneralAgent
```

#### Set environment variables

```bash
cp .env.example .env
vim .env
# Configure environment variables in the .env file, such as OPENAI_API_KEY, etc.
export $(grep -v '^#' .env | sed 's/^export //g' | xargs)
```

#### Command line tool

```shell
GeneralAgent
# or
GeneralAgent --workspace ./test --new --auto_run
# worksapce: Set workspace directory, default ./general_agent
# new: if workspace exists, create a new workspace, like ./general_agent_2023xxx
# auto_run: if auto_run, the agent will run the code automatically, default no
```

#### WebUI

```bash
git clone https://github.com/CosmosShadow/GeneralAgent
cd GeneralAgent
# Preparation
cd webui/web/ && npm install && cd ../../
cd webui/server/server/ts_builder && npm install && cd ../../../../
# Start the server
cd webui/server/server/
uvicorn app:app --host 0.0.0.0 --port 7777
# Start the web service
cd webui/web
npm run start
```

#### Python usage

Please refer to the code for usage

* [examples](examples)
* [webui/server/server/applications](webui/server/server/applications)



## Others

* GeneralAgent uses [litellm](https://docs.litellm.ai/docs/) to access various platforms of large models.




## Join us

Scan the QR code below with WeChat

<p align="center">
<img src="./docs/images/wechat.jpg" alt="wechat" width=400/>
</p>

discord is comming soon.