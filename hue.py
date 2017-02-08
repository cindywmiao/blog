import utils.hdfs_util as hdfs_util
import xml.etree.ElementTree as ET

from models.workflow import EmailItem


path = "/user/mercury/oozie/workspaces/"
workspace = "work_dir/"

download_hdfs_api = 'http://10.10.129.142:14000/webhdfs/v1%s?user.name=mercury&op=OPEN'
upload_hdfs_api = 'http://10.10.129.142:14000/webhdfs/v1%s?user.name=mercury&op=CREATE&data=true&overwrite=true'


def _get_workflow(workflow_id, name):
    workflow_path = path + workflow_id + '/' + name
    if hdfs_util._is_exist_file(download_hdfs_api, workflow_path):
        hdfs_util._download_file(download_hdfs_api, workflow_path, workspace + name)

def _read_workflow(name):
    tree = ET.parse(workspace + name)
    return tree

def


def main():
    # print('Main')
    # workflow_id = "hue-oozie-1486536630.54"
    # name = "workflow.xml"
    # #_get_workflow(workflow_id, name)
    # root = _read_workflow("country_data.xml")
    # print(root.tag)

    tree = ET.parse('work_dir/workflow.xml')
    root = tree.getroot()

    for child in root:
        if 'action' in child.tag:
            for item in child:
                if 'email' in item.tag:
                    emailItem = EmailItem(item)
                    emailItem.__display__()


if __name__ == '__main__':
    main()