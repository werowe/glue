import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *

from awsglue.transforms import Join


glueContext = GlueContext(SparkContext.getOrCreate())


titles = glueContext.create_dynamic_frame.from_catalog(database="moviesandratings", table_name="movieswalker")
 

ratings = glueContext.create_dynamic_frame.from_catalog(database="moviesandratings", table_name="walkerimdbratings")
 
ratingsTitles =   Join.apply(titles, ratings, 'tconst','tconst')
 ratingsTitles.toDF().select(['originalTitle','averageRating']).show()

