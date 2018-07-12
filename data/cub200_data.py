from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import pickle
from PIL import Image
import numpy as np
import os
import random
from data.dataset import dataset

birds_classes = []

all_models_file = "/data/fgvc-aircraft-2013b/data/variants.txt"


cub200_classes = ["Black_footed_Albatross", "Laysan_Albatross", "Sooty_Albatross", "Groove_billed_Ani", "Crested_Auklet", "Least_Auklet", "Parakeet_Auklet", "Rhinoceros_Auklet", "Brewer_Blackbird", "Red_winged_Blackbird", "Rusty_Blackbird", "Yellow_headed_Blackbird", "Bobolink", "Indigo_Bunting", "Lazuli_Bunting", "Painted_Bunting", "Cardinal", "Spotted_Catbird", "Gray_Catbird", "Yellow_breasted_Chat", "Eastern_Towhee", "Chuck_will_Widow", "Brandt_Cormorant", "Red_faced_Cormorant", "Pelagic_Cormorant", "Bronzed_Cowbird", "Shiny_Cowbird", "Brown_Creeper", "American_Crow", "Fish_Crow", "Black_billed_Cuckoo", "Mangrove_Cuckoo", "Yellow_billed_Cuckoo", "Gray_crowned_Rosy_Finch", "Purple_Finch", "Northern_Flicker", "Acadian_Flycatcher", "Great_Crested_Flycatcher", "Least_Flycatcher", "Olive_sided_Flycatcher", "Scissor_tailed_Flycatcher", "Vermilion_Flycatcher", "Yellow_bellied_Flycatcher", "Frigatebird", "Northern_Fulmar", "Gadwall", "American_Goldfinch", "European_Goldfinch", "Boat_tailed_Grackle", "Eared_Grebe", "Horned_Grebe", "Pied_billed_Grebe", "Western_Grebe", "Blue_Grosbeak", "Evening_Grosbeak", "Pine_Grosbeak", "Rose_breasted_Grosbeak", "Pigeon_Guillemot", "California_Gull", "Glaucous_winged_Gull", "Heermann_Gull", "Herring_Gull", "Ivory_Gull", "Ring_billed_Gull", "Slaty_backed_Gull", "Western_Gull", "Anna_Hummingbird", "Ruby_throated_Hummingbird", "Rufous_Hummingbird", "Green_Violetear", "Long_tailed_Jaeger", "Pomarine_Jaeger", "Blue_Jay", "Florida_Jay", "Green_Jay", "Dark_eyed_Junco", "Tropical_Kingbird", "Gray_Kingbird", "Belted_Kingfisher", "Green_Kingfisher", "Pied_Kingfisher", "Ringed_Kingfisher", "White_breasted_Kingfisher", "Red_legged_Kittiwake", "Horned_Lark", "Pacific_Loon", "Mallard", "Western_Meadowlark", "Hooded_Merganser", "Red_breasted_Merganser", "Mockingbird", "Nighthawk", "Clark_Nutcracker", "White_breasted_Nuthatch", "Baltimore_Oriole", "Hooded_Oriole", "Orchard_Oriole", "Scott_Oriole", "Ovenbird", "Brown_Pelican", "White_Pelican", "Western_Wood_Pewee", "Sayornis", "American_Pipit", "Whip_poor_Will", "Horned_Puffin", "Common_Raven", "White_necked_Raven", "American_Redstart", "Geococcyx", "Loggerhead_Shrike", "Great_Grey_Shrike", "Baird_Sparrow", "Black_throated_Sparrow", "Brewer_Sparrow", "Chipping_Sparrow", "Clay_colored_Sparrow", "House_Sparrow", "Field_Sparrow", "Fox_Sparrow", "Grasshopper_Sparrow", "Harris_Sparrow", "Henslow_Sparrow", "Le_Conte_Sparrow", "Lincoln_Sparrow", "Nelson_Sharp_tailed_Sparrow", "Savannah_Sparrow", "Seaside_Sparrow", "Song_Sparrow", "Tree_Sparrow", "Vesper_Sparrow", "White_crowned_Sparrow", "White_throated_Sparrow", "Cape_Glossy_Starling", "Bank_Swallow", "Barn_Swallow", "Cliff_Swallow", "Tree_Swallow", "Scarlet_Tanager", "Summer_Tanager", "Artic_Tern", "Black_Tern", "Caspian_Tern", "Common_Tern", "Elegant_Tern", "Forsters_Tern", "Least_Tern", "Green_tailed_Towhee", "Brown_Thrasher", "Sage_Thrasher", "Black_capped_Vireo", "Blue_headed_Vireo", "Philadelphia_Vireo", "Red_eyed_Vireo", "Warbling_Vireo", "White_eyed_Vireo", "Yellow_throated_Vireo", "Bay_breasted_Warbler", "Black_and_white_Warbler", "Black_throated_Blue_Warbler", "Blue_winged_Warbler", "Canada_Warbler", "Cape_May_Warbler", "Cerulean_Warbler", "Chestnut_sided_Warbler", "Golden_winged_Warbler", "Hooded_Warbler", "Kentucky_Warbler", "Magnolia_Warbler", "Mourning_Warbler", "Myrtle_Warbler", "Nashville_Warbler", "Orange_crowned_Warbler", "Palm_Warbler", "Pine_Warbler", "Prairie_Warbler", "Prothonotary_Warbler", "Swainson_Warbler", "Tennessee_Warbler", "Wilson_Warbler", "Worm_eating_Warbler", "Yellow_Warbler", "Northern_Waterthrush", "Louisiana_Waterthrush", "Bohemian_Waxwing", "Cedar_Waxwing", "American_Three_toed_Woodpecker", "Pileated_Woodpecker", "Red_bellied_Woodpecker", "Red_cockaded_Woodpecker", "Red_headed_Woodpecker", "Downy_Woodpecker", "Bewick_Wren", "Cactus_Wren", "Carolina_Wren", "House_Wren", "Marsh_Wren", "Rock_Wren", "Winter_Wren", "Common_Yellowthroat",]

imgs_annot_for_train = "/data/CUB_200_2011/CUB_200_2011/train.pkl"
imgs_annot_for_test = "/data/CUB_200_2011/CUB_200_2011/test.pkl"
img_dir = "/data/CUB_200_2011/CUB_200_2011/images"

class cub200_dataset(dataset):
    def __init__(self, mode="TRAIN"):
        if mode == "TRAIN":
            dataset.__init__(self, annot_file=imgs_annot_for_train, img_dir=img_dir, name='cub200')
        else:
            dataset.__init__(self, annot_file=imgs_annot_for_test, img_dir=img_dir, name='cub200')

    def process_img(self, img_full_path):
        imgobj = Image.open(img_full_path)
        img_resized = imgobj.resize((448,448), Image.ANTIALIAS)
        imgnd = np.array(img_resized)
        if len(imgnd.shape) == 2: # grayscale image
            imgnd = np.stack((imgnd,) * 3, -1)
        elif imgnd.shape[2] == 4:
            imgnd = imgnd[...,:3] # rgba
        return imgnd

        
        
# class cub200_data_layer():
#     def __init__(self, rand_seed=42, pkl_path="/data/CUB_200_2011/CUB_200_2011/train.pkl", img_dir="/data/CUB_200_2011/CUB_200_2011/images", batch_size=32):
        
#         assert os.path.exists(pkl_path), "pickle path not exist"
#         assert os.path.exists(img_dir), "image dir not exist"

#         self.img_dir = img_dir
#         self.batch_size = batch_size
#         self.img_and_cls = pickle.load(open(pkl_path ,"r"))
        
#         random.seed(rand_seed)

#         random.shuffle(self.img_and_cls)
#         self.total_ct = len(self.img_and_cls)
#         self.iter = 0

#     def get_next_batch(self):
#         items = []

#         img_batch = []
#         cls_batch = []

#         if self.batch_size + self.iter > self.total_ct:

#             items = self.img_and_cls[self.iter:] + self.img_and_cls[:self.iter+self.batch_size-self.total_ct]
#         else:
#             items = self.img_and_cls[self.iter:self.iter+self.batch_size]

#         self.iter = (self.iter + self.batch_size) % self.total_ct            

#         for item in items:
#             img_name = item["img_name"]
#             cls = item["cls"]
            
#             imgobj = Image.open(os.path.join(self.img_dir, img_name))
 
#             imgresized = imgobj.resize((448, 448), Image.ANTIALIAS)

#             imgnd = np.array(imgresized)

#             if len(imgnd.shape) == 2:
#                 imgnd = np.stack((imgnd,)*3, -1)
#             elif imgnd.shape[2] == 4:
#                 imgnd = imgnd[...,:3]

#             img_batch.append(imgnd)

#             cls_batch.append(cls)

#         img_batch = np.array(img_batch)
#         cls_batch = np.array(cls_batch)
        
#         return {"img":img_batch, "cls":cls_batch}
    
#     def data_iterator(self, num_epochs=10):
#         iter_time =  int(self.total_ct / self.batch_size * num_epochs)
#         print ("total iter time:"+str(iter_time))
#         for _ in range(iter_time):
#             yield self.get_next_batch()