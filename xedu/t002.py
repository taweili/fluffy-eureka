from XEdu.hub import Workflow as wf

face = wf(task='pose_face') # 数字可省略，当省略时，默认为pose_face106

keypoints,img_with_keypoints = face.inference(data='images/face002.jpg',img_type='pil') # 进行模型推理

format_result = face.format_output(lang='zh')# 将推理结果进行格式化输出
face.show(img_with_keypoints)# 展示推理图片
# face.save(img_with_keypoints,'img_with_keypoints.jpg')# 保存推理图片
