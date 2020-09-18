import pandas as pd
import json


ffhq_fn = "ffhq-dataset-v2.json"

with open(ffhq_fn) as f:
    ffhq_dict = json.load(f)

df = pd.DataFrame.from_dict(ffhq_dict, orient="index")

ffhq_list = []
for index, row in df.iterrows():

    a = dict()
    idx = dict(index=index)
    category = dict(category=row['category'])
    metadata = row['metadata']
    image = row['image']
    del image['face_landmarks']

    a.update(idx)
    a.update(category)
    a.update(metadata)
    a.update(image)

    ffhq_list.append(a)

    # if int(index) == 5:
    #     break

df_ffhq = pd.DataFrame(ffhq_list)

