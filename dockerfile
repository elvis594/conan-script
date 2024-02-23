# 使用官方Python镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制脚本到容器中
COPY set_up_environment.py /app

# 运行脚本
CMD ["python", "./set_up_environment.py"]
