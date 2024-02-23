import sys
import subprocess


REMOTE_REPO = "https://center.conan.io"
REMOTE_REPO_NAME = "conancenter"

# check conan version
def check_conan_installed():
    try:
        subprocess.run(["conan", "--version"], check=True)
        print("Conan installed")
        return True
    except subprocess.CalledProcessError:
        print("Conan not installed. Please install conan first.")
        return False
    except FileNotFoundError:
        print("Conan not found. Please install conan first.")
        return False

# install conan
def install_conan():
    """通过pip安装Conan"""
    try:
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run(["python", "-m", "pip", "install", "conan"], check=True)
        print("Conan has been successfully installed.")
    except subprocess.CalledProcessError as e:
        print("Failed to install Conan.")
        print(e)

def detect_conan_profile():
    """运行conan profile detect --force命令"""
    try:
        subprocess.run(["conan", "profile", "detect", "--force"], check=True)
        print("Conan profile detected and set successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to detect and set Conan profile.")
        print(e)

def check_conan_remote_exists(remote_name):
    try:
        result = subprocess.run(["conan", "remote", "list"], capture_output=True, text=True, check=True)
        return remote_name in result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error checking Conan remotes: {e}")
        return False

# set up environment
def set_conan_environment():
    # 检查远程仓库是否存在
    if not check_conan_remote_exists(REMOTE_REPO_NAME):
        # 远程仓库不存在，添加它
        subprocess.run(["conan", "remote", "add", REMOTE_REPO_NAME, REMOTE_REPO], check=True)
    else:
        # 远程仓库已存在，选择更新它或者跳过
        print(f"Remote '{REMOTE_REPO_NAME}' already exists. Skipping addition.")


if __name__ == "__main__":
    if not check_conan_installed():
        install_conan()
    
    if check_conan_installed():
        set_conan_environment()
        detect_conan_profile()
    else:
        sys.exit(1)