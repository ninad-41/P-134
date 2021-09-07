import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

bool =[]
gravity_bool = []

df = pd.read_csv("star_with_gravity.csv")
df.head()

for i in df.distance:
    if  i <= 100:
        bool.append(True)
    else:
        bool.append(False)


is_dist = pd.Series(bool)
is_dist.head()
star_dist=df[is_dist]


star_dist.reset_index(inplace=True,drop=True)
star_dist.head()

star_dist.shape

for g in star_dist.Gravity:
    if g<=350 and g>=150:
        gravity_bool.append(True)
    else :
        gravity_bool.append(False)

is_gravity = pd.Series(gravity_bool)

final_stars = star_dist[is_gravity]
final_stars.head()
final_stars.shape
final_stars.reset_index(inplace=True,drop=True)
final_stars.head()

final_stars.to_csv("filtered.csv")
