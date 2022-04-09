
from utils.kdtree  import tree
from utils.algeria import fromTupleToCity
def getCommuneWilayaLine(lat,lang):

    p = tree.closest_point((float(lat),float(lang)))
    city=fromTupleToCity(p)
    print(p)
    return city["nom"]+", "+city["wilaya"]




# def main():
#     print(getCommuneWilayaLine(36.7323769,3.9575154))

# if __name__=="__main__":
#     main()