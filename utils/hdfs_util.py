import requests
import os

def _download_file(download_hdfs_api, remote_path, local_path):
    resp = requests.get(download_hdfs_api % remote_path)
    if resp.status_code == 200:
        with open(local_path, 'wb') as local_file:
            local_file.write(resp.content)
    if not os.path.exists(local_path):
        print('download from hdfs failed %s' % remote_path)
    return os.path.exists(local_path)

def _upload_file(local_path, hdfs_path):
    data = open(local_path).read()
    resp = requests.put(
        url = upload_hdfs_api % (hdfs_path),
        data = data,
        headers = {'Content-Type': 'application/octet-stream'}
    )
    return resp.status_code ==  201

def _is_exist_file(download_hdfs_api, remote_path):
    resp = requests.get(download_hdfs_api % remote_path)
    return resp.status_code == 200

