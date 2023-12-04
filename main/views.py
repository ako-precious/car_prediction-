
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Item
from .serializers import ItemSerializer,CarModelSerializer
from pyspark.ml.pipeline import PipelineModel   
from rest_framework import status
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType
from pyspark.sql import SparkSession

@api_view(['GET'])
def ItemView(request):
    data = Item.objects.all()
    ser = ItemSerializer(data, many=True)
    return Response(ser.data)


@api_view(['POST','GET'])
def PredictionView(request):
    if request.method == "GET":
        read = {
                "example": {
                    "Condition": 21,
                    "Vehicle_brand": 102,
                    "Production_year": 2001,
                    "Mileage_km": 4000,
                    "Power_HP": 100,
                    "Displacement_cm3": 1500,
                    "Fuel_type": 32,
                    "Transmission":11,
                    "Type":64,
                    "Doors_number":3,
                    "Colour": 54,
                    "First_owner":51,
                    "FT": 30,
                    },


                
                "Condition": {"Used":21,"New":22},
                "Vehicle_brand": {
                                'Abarth': 101, 'Acura': 102, 'Aixam': 103, 'Alfa Romeo': 104, 'Alpine': 105, 'Aston Martin': 106, 'Audi': 107,
                                'Austin': 108, 'Baic': 109, 'Bentley': 110, 'BMW': 111, 'Buick': 112, 'Cadillac': 113, 'Casalini': 114, 'Chatenet': 115,
                                'Chevrolet': 116, 'Chrysler': 117, 'Citroën': 118, 'Cupra': 119, 'Dacia': 120, 'Daewoo': 121, 'Daihatsu': 122,
                                'DFSK': 123, 'Dodge': 124, 'DS Automobiles': 125, 'Ferrari': 126, 'Fiat': 127, 'Ford': 128, 'GMC': 129, 'Honda': 130,
                                'Hummer': 131, 'Hyundai': 132, 'Infiniti': 133, 'Isuzu': 134, 'Iveco': 135, 'Jaguar': 136, 'Jeep': 137, 'Kia': 138,
                                'Lada': 139, 'Lamborghini': 140, 'Lancia': 141, 'Land Rover': 142, 'Lexus': 143, 'Ligier': 144, 'Lincoln': 145,
                                'Lotus': 146, 'MAN': 147, 'Maserati': 148, 'Maybach': 149, 'Mazda': 150, 'McLaren': 151, 'Mercedes-Benz': 152,
                                'Mercury': 153, 'MG': 154, 'Microcar': 155, 'MINI': 156, 'Mitsubishi': 157, 'Moskwicz': 158, 'Nissan': 159,
                                'Oldsmobile': 160, 'Opel': 161, 'Tata': 162, 'Uaz': 163, 'Suzuki': 164, 'Inny': 165, 'Volkswagen': 166, 'Subaru': 167,
                                'Toyota': 168, 'Trabant': 169, 'Rolls-Royce': 170, 'RAM': 171, 'Peugeot': 172, 'Renault': 173, 'Triumph': 174,
                                'Porsche': 175, 'Volvo': 176, 'Plymouth': 177, 'Polonez': 178, 'Pontiac': 179, 'Rover': 180, 'Saab': 181, 'Santana': 182,
                                'Saturn': 183, 'Scion': 184, 'Seat': 185, 'Škoda': 186, 'Smart': 187, 'SsangYong': 188, 'Tarpan': 189, 'Tesla': 190,
                                'Vanderhall': 191, 'Wartburg': 192, 'Wołga': 193
                                },
                "Production_year": "1960-present",
                "Mileage_km": "2000+",
                "Power_HP": "80+",
                "Displacement_cm3": "900+",
                "Fuel_type": {
                            'Gasoline': 31, 'Diesel': 32, 'Gasoline + LPG': 33, 'Hybrid': 34, 'Gasoline + CNG': 35,'Electric':36,'Hydrogen':37
                            },
                "Transmission": {'Manual':11, 'Automatic':12},
                "Type": {
                    'small_cars': 61, 'city_cars': 62, 'sedan': 63, 'compact': 64, 'station_wagon': 65,
                    'coupe': 66, 'SUV': 67, 'convertible': 68, 'minivan': 69
                    },
                
                "Doors_number": "1-5",
   
                "Colour": {
                    'gray': 41, 'white': 42, 'yellow': 43, 'black': 44, 'red': 45, 'other': 46, 'blue': 47,
                    'silver': 48, 'brown': 49, 'burgundy': 50, 'green': 51, 'beige': 52, 'golden': 53,
                    'violet': 54
                    },
                "First_owner": {51:"No",52:"Yes"},
                "FT":"no of features: 1-60"
    
                
            }
        return Response(read)
    
    if request.method == "POST":

        Model = PipelineModel.load("GB_car_model3")
        print(request.data)
        if len(request.data)==13:
            dt = request.data
            data = [(dt["Condition"],dt["Vehicle_brand"],dt["Production_year"],dt["Mileage_km"],dt["Power_HP"],dt["Displacement_cm3"],dt["Fuel_type"],dt["Transmission"],dt["Type"],dt["Doors_number"],dt["Colour"],dt["First_owner"],dt["FT"])]
           
            # Define the schema
            schema = StructType([
                StructField("Condition", IntegerType(), True),
                StructField("Vehicle_brand", IntegerType(), True),
                StructField("Production_year", IntegerType(), True),
                StructField("Mileage_km", IntegerType(), True),
                StructField("Power_HP", IntegerType(), True),
                StructField("Displacement_cm3", IntegerType(), True),
                StructField("Fuel_type", IntegerType(), True),
                StructField("Transmission", IntegerType(), True),
                StructField("Type", IntegerType(), True),
                StructField("Doors_number", IntegerType(), True),
                StructField("Colour", IntegerType(), True),
                StructField("First_owner", IntegerType(), True),
                StructField("FT", IntegerType(), True)
            ])
            spark = SparkSession.builder.appName('car_price_prediction').getOrCreate()

            df = spark.createDataFrame(data, schema=schema)
            prd = Model.transform(df)
            cell_value = prd.select("prediction").collect()[0][0]
            val = {"Predicted_price in dollars":cell_value}
            return Response(val)
        else:
            return Response("err")
            