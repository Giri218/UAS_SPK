from settings import MEREK_SCALE,DEV_SCALE_kamera,DEV_SCALE_ram,DEV_SCALE_storage,DEV_SCALE_baterai,DEV_SCALE_harga

class BaseMethod():

    def __init__(self, data_dict, **setWeight):

        self.dataDict = data_dict

        # 1-7 (Kriteria)
        self.raw_weight = {
            'Merk': 5, 
            'Kamera': 3, 
            'Memori_Internal': 4, 
            'RAM': 3, 
            'Baterai': 4, 
            'Harga': 3, 
        }

        if setWeight:
            for item in setWeight.items():
                temp1 = setWeight[item[0]] # value int
                temp2 = {v: k for k, v in setWeight.items()}[item[1]] # key str

                setWeight[item[0]] = item[1]
                setWeight[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'id': smartphone['id'],
            'Merk': MEREK_SCALE[smartphone['Merk']],
            'Kamera': DEV_SCALE_kamera[smartphone['Kamera']],
            'Memori_Internal': DEV_SCALE_storage[smartphone['Memori_Internal']],
            'RAM': DEV_SCALE_ram[smartphone['RAM']],
            'Baterai': DEV_SCALE_baterai[smartphone['Baterai']],
            'Harga': DEV_SCALE_harga[smartphone['Harga']],
        } for smartphone in self.dataDict]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        Merk = [] # max
        Kamera = [] # max
        Memori_Internal = [] # max
        RAM = [] # max
        baterai = [] # max
        ukuran_layar = [] # max
        harga = [] # min
        for data in self.data:
            Merk.append(data['Merk'])
            Kamera.append(data['Kamera'])
            Memori_Internal.append(data['Memori_Internal'])
            RAM.append(data['RAM'])
            baterai.append(data['Baterai'])
            harga.append(data['Harga'])

        max_Merk = max(Merk)
        max_Kamera = max(Kamera)
        max_Memori_Internal = max(Memori_Internal)
        max_RAM = max(RAM)
        max_baterai = max(baterai)
        min_harga = min(harga)

        return [
            {   'id': data['id'],
                'Merk': data['Merk']/max_Merk, # benefit
                'Kamera': data['Kamera']/max_Kamera, # benefit
                'Memori_Internal': data['Memori_Internal']/max_Memori_Internal, # benefit
                'RAM': data['RAM']/max_RAM, # benefit
                'Baterai': data['Baterai']/max_baterai, # benefit
                'Harga': min_harga/data['Harga'] # cost
                }
            for data in self.data
        ]
 

class WeightedProduct(BaseMethod):
    def __init__(self, dataDict, setWeight:dict):
        super().__init__(data_dict=dataDict, **setWeight)
    @property
    def calculate(self):
        weight = self.weight
        result = {row['id']:
    round(
        row['Merk'] ** weight['Merk'] *
        row['Kamera'] ** weight['Kamera'] *
        row['Memori_Internal'] ** weight['Memori_Internal'] *
        row['RAM'] ** weight['RAM'] *
        row['Baterai'] ** weight['Baterai'] *
        row['Harga'] ** weight['Harga']
        , 2
    )
    for row in self.normalized_data}

        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))