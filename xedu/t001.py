from XEdu.hub import Workflow as wf 

wf.support_task()

body = wf(task="pose_body17")

img = "images/pose001.jpg"
result, new_img = body.inference(data=img, img_type="cv2", show=True)
