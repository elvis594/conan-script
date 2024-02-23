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

# set up environment
def set_conan_environment():
    # 示例：添加Conan远程仓库
    subprocess.run(["conan", "remote", "add", REMOTE_REPO_NAME, REMOTE_REPO], check=True)
    print("Added Conan remote repository.")



if __name__ == "__main__":
    if not check_conan_installed():
        install_conan()
    
    if check_conan_installed():
        set_conan_environment()
        detect_conan_profile()
    else:
        sys.exit(1)