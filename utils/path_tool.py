#路径工具
#统一管理项目中的文件路径
import os
#获取工程根目录
def get_project_root() -> str:   #-> 用于标注函数的返回值类型
    current_file=os.path.abspath(__file__)
    current_dir=os.path.dirname(current_file)
    project_root=os.path.dirname(current_dir)
    return project_root

def get_abs_path(relative_path:str) ->str:
    project_root=get_project_root()
    return os.path.join(project_root,relative_path)

if __name__ == '__main__':
    print(get_abs_path('data/test.txt'))