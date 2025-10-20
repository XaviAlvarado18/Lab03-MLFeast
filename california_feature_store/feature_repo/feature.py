from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float64, Int64
from datetime import timedelta

# ============================================
# 1. Definir la entidad (house)
# ============================================
house = Entity(
    name="house_id",
    description="Identificador único para cada casa en el dataset"
)

# ============================================
# 2. Definir el source (archivo parquet)
# ============================================
# Usa ruta absoluta o relativa desde donde ejecutas 'feast apply'
california_housing_source = FileSource(
    path="data/california_data.parquet",  # Relativa desde feature_repo/
    timestamp_field="event_timestamp",
)

# ============================================
# 3. Crear FeatureView con las features principales
# ============================================
california_housing_features = FeatureView(
    name="california_housing_features",
    entities=[house],
    ttl=timedelta(days=365),  # Time to live: cuánto tiempo mantener las features
    schema=[
        Field(name="MedInc", dtype=Float64),
        Field(name="HouseAge", dtype=Float64),
        Field(name="AveRooms", dtype=Float64),
        Field(name="AveBedrms", dtype=Float64),
        Field(name="Population", dtype=Float64),
        Field(name="AveOccup", dtype=Float64),
        Field(name="Latitude", dtype=Float64),
        Field(name="Longitude", dtype=Float64),
        Field(name="MedHouseVal", dtype=Float64),  # Target variable
    ],
    online=True,
    source=california_housing_source,
    tags={"team": "ml_engineering", "dataset": "california_housing"},
)