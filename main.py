from typing import List

from fastapi import FastAPI, File, UploadFile
#
app = FastAPI()
# 使用Form表单上传文件，fastapi使用File获取上传的文件。
#
# 指定了参数类型是bytes：file: bytes = File(),此时会将文件内容全部读取到内存，比较适合小文件。
#
# 使用File需要提前安装 python-multipart
#只要在路径操作函数中声明了变量的类型是bytes且使用了File,则fastapi会将上传文件的内容全部去读到参数中。




@app.post("/files/")
async def create_files( files: List [ bytes ] = File() ):
    return {"file_sizes": [ len(file) for file in files ]}


@app.post("/uploadfiles/")
async def create_upload_files( files: List [ UploadFile ] ):
    return {"filenames": [ file.filename for file in files ]}