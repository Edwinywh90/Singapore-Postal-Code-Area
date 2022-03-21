ONE_MAP_API = 'https://developers.onemap.sg/commonapi/search?searchVal={ searchVal }&returnGeom=Y&getAddrDetails=N'
URA_API = 'https://www.ura.gov.sg/arcgis/rest/services/MP19/Updated_Landuse_gaz/MapServer/45/query?returnGeometry=true&where=1%3D1&outSr=4326&outFields=lu_desc%2Cgpr_num%2Cregion_n%2Cpln_area_n%2Csubzone_n&inSr=4326&geometry=%7B%22x%22%3A{ lng }%2C%22y%22%3A{ lat }%2C%22spatialReference%22%3A%7B%22wkid%22%3A4326%7D%7D&geometryType=esriGeometryPoint&spatialRel=esriSpatialRelWithin&f=json'
POSTAL_CODE_PREFIX_URL = 'https://www.ura.gov.sg/realEstateIIWeb/resources/misc/list_of_postal_districts.htm'
POSTAL_CODE_SUFFIX_RANGE = range(3009, 3011) # from 0000 to 9999
POSTAL_CODE_SUFFIX_LEADING_ZERO = 4
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}