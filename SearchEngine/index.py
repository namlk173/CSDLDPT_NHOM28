from colordescriptor import ColorDescriptor

import os
import imageio.v2 as imageio

path_dir_data = r'ImageSimilar/static/Data/DataSet'
cd = ColorDescriptor((8, 12, 3))

output = open("SearchEngine/index.csv", "w")

for imageFoler in os.listdir(path_dir_data):
    for imageName in os.listdir(path_dir_data + "/" + imageFoler):
        imageID  = imageFoler + "/" + imageName
        image = imageio.imread(path_dir_data + "/" + imageID)

        features = cd.describe(image)
        features = [str(f) for f in features]
        output.write("%s,%s\n" % ('Data/DataSet/' + imageID, ",".join(features)))
output.close()
